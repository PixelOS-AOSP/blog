import os
import xml.etree.ElementTree as ET
from datetime import datetime, timezone

import requests
from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport

BRANCH = os.environ["BRANCH"]
GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]
INPUT_DATE = os.environ["START_DATE"]

ORG = "PixelOS-AOSP"
GITHUB_GRAPHQL_URL = "https://api.github.com/graphql"


def get_projects(file) -> list[str]:
    contents = requests.get(
        f"https://raw.githubusercontent.com/PixelOS-AOSP/android_manifest/{BRANCH}/snippets/{file}.xml"
    ).content
    root = ET.fromstring(contents)

    projects = root.findall(".//project")
    project_names = [
        project.get("name", "").split("/")[1]
        for project in projects
        if project.get("remote", "") == "github"
    ]

    return project_names


transport = RequestsHTTPTransport(
    url=GITHUB_GRAPHQL_URL,
    headers={"Authorization": f"Bearer {GITHUB_TOKEN}"},
    verify=True,
    retries=3,
)
client = Client(transport=transport, fetch_schema_from_transport=True)

# query template
query_template = """
query ($org: String!, $repo: String!, $branch: String!, $cursor: String) {
  repository(owner: $org, name: $repo) {
    ref(qualifiedName: $branch) {
      target {
        ... on Commit {
          history(first: 100, after: $cursor) {
            pageInfo {
              hasNextPage
              endCursor
            }
            edges {
              node {
                oid
                messageHeadline
                committedDate
                author {
                  name
                }
                url
              }
            }
          }
        }
      }
    }
  }
}
"""


def fetch_commits(repo, start_date, end_date):
    commits = []
    has_next_page = True
    cursor = None

    while has_next_page:
        query = gql(query_template)
        variables = {"org": ORG, "repo": repo, "branch": BRANCH, "cursor": cursor}
        try:
            result = client.execute(query, variable_values=variables)
            repository = result["repository"]

            if not repository or not repository["ref"]:
                print(
                    f"Warning: Branch 'main' not found in repository {repo}. Skipping..."
                )
                break

            history = repository["ref"]["target"]["history"]
            edges = history["edges"]

            if not edges:
                print(f"No commits found in repository {repo}.")
                break

            for edge in edges:
                node = edge["node"]
                commit_date = datetime.strptime(
                    node["committedDate"], "%Y-%m-%dT%H:%M:%SZ"
                ).replace(tzinfo=timezone.utc)

                # check if more data has to be fetched
                if commit_date < start_date:
                    print(
                        f"Reached commits older than start date in repository {repo}. Stopping..."
                    )
                    return commits

                if start_date <= commit_date <= end_date:
                    commit = {
                        "hash": node["oid"],
                        "link": node["url"],
                        "title": node["messageHeadline"],
                        "author": node["author"]["name"],
                        "date": node["committedDate"],
                    }
                    commits.append(commit)

            # update cursor position
            has_next_page = history["pageInfo"]["hasNextPage"]
            cursor = history["pageInfo"]["endCursor"]

            print(
                f"Fetched {len(edges)} commits from {repo}. Has next page: {has_next_page}"
            )

        except Exception as e:
            print(f"Error fetching commits from {repo}: {e}")
            break

    return commits


end_date = datetime.now(timezone.utc)
start_date = datetime.strptime(INPUT_DATE, "%Y-%m-%d").replace(tzinfo=timezone.utc)


all_commits = []
for repo in get_projects("pixelos"):
    print(f"Fetching commits from {repo}...")
    commits = fetch_commits(repo, start_date, end_date)
    all_commits.extend(commits)

all_commits.sort(key=lambda x: x["date"], reverse=True)

# formatting
output = ""
current_date = None
for commit in all_commits:
    date = datetime.strptime(commit["date"], "%Y-%m-%dT%H:%M:%SZ").strftime("%Y-%m-%d")
    if date != current_date:
        output += f"\n## {date}\n"
        current_date = date
    output += f"[{commit['hash'][:7]}]({commit['link']}) {commit['title']} _(by {commit['author']})_  \n"

with open("index.md", "w") as f:
    f.write(
        """---
pageClass: changelogSection
---

# Changelogs\n"""
    )
    f.write(output)
