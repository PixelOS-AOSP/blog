# Bypassing FRP Lock

In this guide, we will see how to bypass the Factory Reset Protection (FRP) lock on Android devices.

## Important Notes

- This method **ONLY** works on userdebug builds

::: info

For builds after [this commit](https://github.com/PixelOS-AOSP/vendor_aosp/commit/ee3e2d2110385f6f6da418bccd3cd14b85b94c9c) (February 22, 2025), the `wipe-frp.sh` script is included in the ROM itself. You do **not** need to download or push the script.

:::

Before starting, ensure you have your device in **recovery mode**, and platform-tools installed.

## Steps

### 1. Verify ADB connection and gain root access

First, check if your device is detected:

```sh
adb devices
adb root
```

Expected output:

```sh
List of devices attached
XYZ123456789    recovery

restarting adbd as root
```

### 2. Run the Script

::: details For newer builds
If you’re using a build that includes the script, simply run the script directly:

```sh
adb shell wipe-frp
```

:::

::: details For older builds
If your build does not include the script, you will need to:

1. [Download the `wipe-frp.sh` script](https://raw.githubusercontent.com/PixelOS-AOSP/vendor_aosp/refs/heads/fifteen/prebuilt/common/bin/wipe-frp.sh).

2. Push the script to your device:

   ```sh
   adb push wipe-frp.sh /sdcard/
   ```

   Expected output:

   ```sh
   wipe-frp.sh: 1 file pushed, 0 skipped. 0.1 MB/s (1686 bytes in 0.015s)
   ```

3. Make the script executable:

   ```sh
   adb shell chmod +x /sdcard/wipe-frp.sh
   adb shell /sdcard/wipe-frp.sh
   ```

:::

It should display similar output:

```log
device:/ # ./sdcard/wipe-frp.sh
32+0 records in
32+0 records out
32 bytes (32 B) copied, 0.004 s, 7.8 K/s
1000+0 records in
1000+0 records out
1000 bytes (0.9 K) copied, 0.004 s, 244 K/s
32+0 records in
32+0 records out
32 bytes (32 B) copied, 0.001 s, 31 K/s
8+0 records in
8+0 records out
8 bytes (8 B) copied, 0.001 s, 7.8 K/s
32+0 records in
32+0 records out
32 bytes (32 B) copied, 0.004 s, 7.8 K/s
device:/ #
```

### 3. Finally reboot your device

```sh
adb reboot
```

Your device should now be free from the FRP lock.

## Troubleshooting

If you encounter any issues, feel free to ask in our [community chat](https://t.me/pixeloschat).
