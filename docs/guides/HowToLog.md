# Guide to taking logs

Occasionally when using a custom ROM or kernel, you may experience an issue. The developer may want something called a logcat or dmesg to look into this but you may not know how to do that. This is valid for themers, ROM developers, and kernel developers.

A logcat is useful for debugging crashes or other weird behaviors with apps or themes. A radio logcat details what's going on in the phone's actual phone functionality. It tells you any errors that occured while trying to call. A dmesg is a kernel log, detailing what each subsystem is doing. A ramoops is the previous dmesg, which will detail why a phone force restarted. A ramoops is also known as last-kmsg or pstore, and can be retrieved from a custom recovery as well as from a booted device.

::: warning Asking for bug fixes

Reporting bugs should not morph into harrasing or pressuring the maintainers or developers to fix your issue.

Any instances of bullying maintainers will not be tolerated and action will be taken

:::

## 1. Using an app

### 1. Getting a logcat

1. Download a logcat app from the Play Store (I will be using Matlog for the rest of this tutorial).
2. Open the app and grant it root permissions (if you are not rooted and do not want to be, you will need to use ADB below).
3. Clear the buffer but clicking the three dot menu and hitting clear.
4. Click on the three dot menu, choose Settings, then Log Buffer(s).
5. Tick either radio, main or both depending on the type of bug.
6. Click on the three dot menu, choose File, then Record.
7. Duplicate your crash/issue.
8. Go back into Matlog and hit the stop button in the lower righthand corner.
9. Send the generated file to your developer/themer following the etiquette below.

### 2. Getting a dmesg

1. Either download a dmesg app and follow similar steps as above OR download a terminal emulator and continue on.
2. Open your terminal emulator and type su to enter as the root user.
3. Type dmesg > /sdcard/test.log
4. Send the generated file (located in the head folder of your internal storage partition) to your developer, following the etiquette below.

### 3(a). Getting a ramoops via system

1. Open a file manager and navigate to /sys/fs/pstore and copy the file named console-ramoops or console-ramoops1 to your sdcard folder.
2. Send that file to your kernel developer following the etiquette below.

### 3(b). Getting a ramoops via recovery

1. Ensure your device has TWRP installed from fastboot, search XDA for help
2. Immediately after the device reboots, force it to recovery by holding volume buttons.
3. Click [Advanced] and then [File Manager]. Navigate to /sys/fs/pstore and copy the file named console-ramoops or console-ramoops1 to /sdcard. Send that file to your kernel developer or whoever caused the bug following the etiquette below

## 2. Using ADB

1. Install ADB with your package manager, or download the latest tools from Google:

   - Windows: Download from Google, or install via CLI:

     [Download for Windows](https://dl.google.com/android/repository/platform-tools-latest-windows.zip)

     ```powershell
     winget install -e --id Google.PlatformTools
     ```

   - macOS: Download from Google, or install via CLI:

     [Download for Darwin](https://dl.google.com/android/repository/platform-tools-latest-darwin.zip)

     ```bash
     brew install android-platform-tools
     ```

   - Linux: Download from Google:

     [Download for Linux](https://dl.google.com/android/repository/platform-tools-latest-linux.zip)

2. Extract those to a folder and move into that folder:

   ```bash
   cd <folder_location>
   ```

3. Plug in your device and accept the debugging prompt (turn on ADB in
   Settings > Developer Options if you don't see it).

4. Verify your device is recognized.

   `adb devices` or `./adb devices`

5. Clear the logcat buffer.

   `adb logcat -c` or `./adb logcat -c`

6. Take your log:

   logcat: `adb logcat -d > test.log` or `./adb logcat -d > test.log`  
   dmesg: `adb shell dmesg > test.log` or `./adb shell dmesg > test.log`

7. Give that log to the appropriate party with a proper report, following the etiquette below.

## Bug Reporting Etiquette

1. First and foremost, understand that for the vast majority of people, this is a hobby, not a job. It may take some time for your issue to be resolved. Being a jerk or bossy is likely to get you banned or at the least have your issue dismissed.
2. Write in clear, concise manner what the issue is with steps to reproduce
   ::: tip Explaining your issue

   Bad: My phone is broken, help!

   Good: Whenever I open YouTube after a clean flash, it force closes.
   :::

3. Explain what you have done. A developer should not have to ask what has already been attempted.
4. Provide any scenarios/ROMs where it did work (was it working in a previous update, etc.)
5. If you are technically inclined, provide commits that are either the issue or will resolve the issue. Developers love having a solution presented for them.

```text
Copyright (C) 2016-2017 Nathan Chancellor

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>
```
