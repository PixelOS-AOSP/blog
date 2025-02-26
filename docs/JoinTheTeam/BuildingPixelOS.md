# Guide to Building PixelOS

This guide provides a step-by-step tutorial on setting up a build environment for building PixelOS on Ubuntu 24.10/24.04.2 LTS and syncing the ROM from the manifest.

## Step 1: Install Necessary Tools and Dependencies

Ensure you have the necessary tools and dependencies installed on your system, including the Java Development Kit (JDK), the Android SDK, Git, and Repo. Open a terminal and run the following command:

```bash
sudo apt-get update && sudo apt install bc bison build-essential ccache curl flex g++-multilib gcc-multilib git git-lfs gnupg gperf imagemagick lib32readline-dev lib32z1-dev libelf-dev liblz4-tool lz4 libsdl1.2-dev libssl-dev libxml2 libxml2-utils lzop pngcrush rsync schedtool squashfs-tools xsltproc zip zlib1g-dev
```

Alternatively, for a simpler method, run:

```bash
wget https://raw.githubusercontent.com/akhilnarang/scripts/master/setup/android_build_env.sh && sudo bash android_build_env.sh
```

## Step 2: Setup Git Lfs

You need Git Lfs to download some larger repositories, to do that run:

```bash
git lfs install
```

## Step 3: Sync PixelOS ROM Using Repo

Once your build environment is set up, use Repo to sync the PixelOS ROM from the manifest. Create a directory to store the PixelOS source code and run the following commands:

```bash
mkdir pixelos
cd pixelos
repo init -u https://github.com/PixelOS-AOSP/manifest.git -b fifteen --git-lfs
repo sync
```

This initializes the Repo tool and syncs the `fifteen` version of the PixelOS ROM from the manifest. The process may take some time, depending on your disk and internet connection speed.

## Step 3: Download Device-Specific Source Code

To download the device-specific source code for the PixelOS ROM, use the `git clone` command and sync the device sources to their respective folders.

## Step 4: Build the ROM

After downloading the device-specific source code, use the `lunch` and `make` commands to build the ROM. For example, to build PixelOS with the build type set to `user`:

```bash
lunch aosp_$device-ap4a-user
mka bacon -j$(nproc --all)
```

## Step 5: Locate the Built ROM

After the build process is complete, you should have a working zip file of the PixelOS ROM. You can find it at `./out/target/product/$device/PixelOS_*.zip`.

You can flash this zip to your device using the appropriate tools, such as PixelOS Recovery or TWRP.
