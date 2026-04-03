# Guide to Building PixelOS

This guide provides a step-by-step tutorial on setting up a build environment for building PixelOS on Ubuntu and syncing the ROM from the manifest.

## Step 1: Install Necessary Tools and Dependencies

Ensure you have the necessary tools and dependencies installed on your system, including the Java Development Kit (JDK), the Android SDK, Git, and Repo. Open a terminal and run the following command:

```bash
sudo apt-get update && sudo apt-get install bc bison build-essential curl flex g++-multilib gcc-multilib git git-lfs gnupg gperf lib32ncurses-dev lib32readline-dev lib32z1-dev libelf-dev liblz4-tool libncurses-dev libssl-dev libxml2 libxml2-utils lzop openjdk-21-jdk pngcrush protobuf-compiler python3 repo unzip xsltproc zip zlib1g-dev
```

Alternatively, for a simpler method, run:

```bash
wget https://raw.githubusercontent.com/akhilnarang/scripts/master/setup/android_build_env.sh && sudo bash android_build_env.sh
```

If you run into the `Build sandboxing disabled due to nsjail error` message during builds, run:

```bash
sudo sysctl -w kernel.apparmor_restrict_unprivileged_userns=0
```

This fixes the `07:37:33 Build sandboxing disabled due to nsjail error` issue on systems where AppArmor blocks unprivileged user namespaces.

## Step 2: Sync PixelOS ROM Using Repo

Once your build environment is set up, use Repo to sync the PixelOS ROM from the manifest. Create a directory to store the PixelOS source code and run the following commands:

```bash
mkdir pixelos
cd pixelos
repo init -u https://github.com/PixelOS-AOSP/android_manifest.git -b sixteen-qpr2 --git-lfs
repo sync
```

This initializes the Repo tool and syncs the `sixteen` version of the PixelOS ROM from the manifest. The process may take some time, depending on your disk and internet connection speed.

## Step 3: Download Device-Specific Source Code

To download the device-specific source code for the PixelOS ROM, use the `git clone` command and sync the device sources to their respective folders.

## Step 4: Build the ROM

After downloading the device-specific source code, use the `breakfast` and `m` commands to build the ROM. For example, to build PixelOS for the device codenamed `xaga` with the build type set to `user`:

```bash
breakfast xaga user
m pixelos -j$(nproc --all)
```

Change `user` to `userdebug` or `eng` if you want to build a debug or engineering build.

## Step 5: Locate the Built ROM

After the build process is complete, you should have a working zip file of the PixelOS ROM. You can find it at `./out/target/product/xaga/PixelOS_*.zip` (replace `xaga` with the codename for your device).

You can flash this zip to your device using the appropriate tools, such as PixelOS Recovery or TWRP.
