import { defineConfig } from "vitepress";

import { getSidebarBlog } from "./blogUtil";
import tailwindcss from "@tailwindcss/vite";

const blogItems = await getSidebarBlog();

export default defineConfig({
  title: "PixelOS Docs",
  head: [["link", { rel: "icon", href: "/favicon.ico" }]],
  description: "Documentation for PixelOS",
  cleanUrls: true,
  lastUpdated: true,

  vite: {
    plugins: [tailwindcss()],
  },

  themeConfig: {
    logo: "/favicon.ico",
    nav: [
      {
        text: "Blog",
        link: `/blog/${blogItems[0].name}`,
        activeMatch: "^/blog/",
      },
      {
        text: "Changelogs",
        link: "/changelogs",
        activeMatch: "^/changelogs/",
      },
      {
        text: "For Users",
        link: "/docs/ForUsers/faq",
        activeMatch: "^/docs/ForUsers/",
      },
      {
        text: "For Maintainers",
        link: "/docs/JoinTheTeam",
        activeMatch: "^/docs/JoinTheTeam/",
      },
      {
        text: "Resources",
        link: "/docs/resources/ImportantLinks",
        activeMatch: "^/docs/resources/",
      },
      {
        text: "Donate",
        link: "/docs/donate",
      },
    ],

    search: {
      provider: "local",
    },

    sidebar: {
      "/blog/": blogItems.map((item) => ({
        text: item.year,
        items: [
          {
            text: item.title,
            link: `/blog/${item.name}`,
          },
        ],
      })),
      "/docs/ForUsers/": [
        {
          base: "/docs/ForUsers/",
          items: [
            {
              text: "Frequently Asked Questions",
              link: "faq",
            },
            {
              text: "Community Guidelines",
              link: "CommunityGuidelines",
            },
          ],
        },
        {
          text: "Guides",
          collapsed: false,
          base: "/docs/guides/",
          items: [
            { text: "Reporting Bugs", link: "BugReport" },
            { text: "Taking Logs", link: "HowToLog" },
            { text: "Rooting and SafetyNet", link: "HowToRoot" },
          ],
        },
      ],
      "/docs/guides/": [
        {
          base: "/docs/ForUsers/",
          items: [
            {
              text: "Frequently Asked Questions",
              link: "faq",
            },
            {
              text: "Community Guidelines",
              link: "CommunityGuidelines",
            },
          ],
        },
        {
          text: "Guides",
          collapsed: false,
          base: "/docs/guides/",
          items: [
            { text: "Reporting Bugs", link: "BugReport" },
            { text: "Taking Logs", link: "HowToLog" },
            { text: "Rooting and SafetyNet", link: "HowToRoot" },
          ],
        },
      ],
      "/docs/JoinTheTeam/": [
        {
          text: "Join The Team",
          base: "/docs/JoinTheTeam/",
          items: [
            {
              text: "Maintainers Requirements",
              link: "MaintainersRequirements",
            },
            {
              text: "Device Requirements",
              link: "DeviceRequirements",
            },
          ],
        },
        {
          text: "Building PixelOS",
          base: "/docs/JoinTheTeam/",
          items: [
            {
              text: "Build Guide",
              link: "BuildingPixelOS",
            },
          ],
        },
      ],
      "/docs/resources/": [
        {
          text: "Resources",
          items: [
            {
              text: "Important Links",
              link: "/docs/resources/ImportantLinks",
            },
            {
              text: "Banners Archive",
              link: "/docs/resources/BannerArchives",
            },
            {
              text: "Wallpapers",
              link: "/docs/resources/wallpapers",
            },
          ],
        },
      ],
    },

    socialLinks: [
      { icon: "github", link: "https://github.com/PixelOS-AOSP" },
      { icon: "telegram", link: "https://t.me/PixelOSOfficial" },
      { icon: "twitter", link: "https://twitter.com/PixelOSROM" },
    ],
  },
});
