---
pageClass: changelogSection
---

# Changelogs

## 2026-03-11
[a66ad43](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/a66ad43d8a96e5440a788f42c4eb7c6dd50c0a06) fixup! [PM] Check unknown sources for intent installation _(by Ivan Chiang)_  
[4342512](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/4342512e1c1d4f9af05a1de52dcfd72e585161b3) fixup! Reapply "[PM] Check unknown sources user restriction for inten… _(by Ivan Chiang)_  
[44abba0](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/44abba04276107463d2d76afea9f4c1504eac572) RESTRICT AUTOMERGE Ignore pinned Windows (Consolidated fix) _(by Achim Thesmann)_  
[f661314](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/f661314774ef56353ee093b7dc75853a1d84e3f3) Revert "Ignore pinned Windows" _(by Achim Thesmann)_  
[d146070](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/d1460708bc4a16c5fd255af28903f751c3a5accc) Apps clearing self data shouldn't get permissions restored _(by Nate Myren)_  
[ed14954](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/ed14954e89267244068cbc29b0960a3ce5df2f0e) fixup! Prevent long press on profile notifs when locked _(by Julia Reynolds)_  

## 2026-03-08
[274a478](https://github.com/PixelOS-AOSP/android_hardware_interfaces/commit/274a478d86e42b29694df6cae09a3aa364a579ba) fixup! audio: Allow opting out of speaker_layout_channel_mask field _(by Yuan Tong)_  
[de6dc46](https://github.com/PixelOS-AOSP/android_vendor_lineage/commit/de6dc4672bed513c9f0f0921d4499fbbd1a54752) release: Bump Security String to 2026-03-01 _(by Michael Bestas)_  
[9201094](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/9201094089d559288a497c4fdbb3cba5958c2666) Enforce permission and debuggability for `am dumpbitmaps` _(by Eric Miao)_  

## 2026-03-07
[bf3d9ff](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/bf3d9ff36f001b87f83e3be417648efa13b4382c) Settings: Implement localepicker from SettingsGoogle _(by ralph950412)_  

## 2026-03-06
[e492d73](https://github.com/PixelOS-AOSP/android_packages_modules_Virtualization/commit/e492d736eabfba591e4e98e5cb7859f0d954f925) vmbase,pvmfw: aarch64: Clean dcache to PoC not PoU _(by Pierre-Clément Tosi)_  
[ae2c35a](https://github.com/PixelOS-AOSP/android_external_dng_sdk/commit/ae2c35ac47d23ce7a14ad968db595dfc02a9ec41) Update to DNG SDK 1.7.1 2410 _(by John Reck)_  
[7c4d94f](https://github.com/PixelOS-AOSP/android_hardware_st_nfc/commit/7c4d94fa58ad266c41a41bdd4db08cdbb4c8615f) Fix use-after-free in eventCallback _(by Kyle Hsiao)_  
[84c3557](https://github.com/PixelOS-AOSP/android_frameworks_av/commit/84c35576b5f7a12e383f51db5c12daacf46edfb7) Fix vulnerability in drmserver _(by Kyle Zhang)_  
[fb17c8f](https://github.com/PixelOS-AOSP/android_frameworks_native/commit/fb17c8f51d386717b0b934c5f823490eb840f8cc) Clip to layer bounds when drawing blur regions _(by Alec Mouri)_  
[e25e735](https://github.com/PixelOS-AOSP/android_frameworks_native/commit/e25e7356b6300b28cc2d1ae4f78e28c874357333) Truncate WindowInfo.name during parcelling. _(by Anton Ivanov)_  
[c3df39e](https://github.com/PixelOS-AOSP/android_packages_apps_DocumentsUI/commit/c3df39e6dd24ce159243ea92e376a7a31c53262a) Prevent a malicious selector from launching an arbitrary activity. _(by Himanshu Arora)_  
[50e507a](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/50e507a4ba34e1dda3391f59c7ed679a12f4d3d9) Fixed "Unlock your phone" unexpectedlly turned ON after OTA _(by Shawn Lin)_  
[b4ee6e8](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/b4ee6e8ff6d64cb15a7ba8715641912ff17fe0ec) Check permission of the calling package in multi-pane devices _(by Mill Chen)_  
[2490990](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/24909909d3643a671bf75de0acb085ae03711f07) Ignore enrollAfterFace in FaceEnroll from ext pkg _(by Milton)_  
[650d92f](https://github.com/PixelOS-AOSP/android_packages_modules_Permission/commit/650d92fc7987e1b818504bf2ee8e0f01fc83c74f) Update RuntimePermissionsUpgradeController to accept null PermGroups _(by Nate Myren)_  
[028269a](https://github.com/PixelOS-AOSP/android_packages_modules_Permission/commit/028269abb5f2d5b99641a089c943bf97a16e4aff) V2 Merge all permissions in a shared UID for every package in that UID _(by Nate Myren)_  
[6e5d7d8](https://github.com/PixelOS-AOSP/android_packages_providers_MediaProvider/commit/6e5d7d8664e4b27cdd2ac52f84d226f1ca27b376) Throw exception on MediaStore createRequest for non-existent uri _(by Garvita Jain)_  
[fd7d0d0](https://github.com/PixelOS-AOSP/android_packages_providers_MediaProvider/commit/fd7d0d07498eaf3d7f4fb3cce194329e8e84203b) Fix ACCESS_MEDIA_LOCATION bypass via SAF picker _(by Himanshu Arora)_  
[63e0173](https://github.com/PixelOS-AOSP/android_packages_services_Telephony/commit/63e0173470d5cc281b744f8fc44a64102e7ec526) Block overriding satellite carrier config keys on user builds _(by Jayachandran C)_  
[568a20e](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/568a20ea482da9eb1061e4ba08cf2fbeee80b619) [UidMigration] fix update uninstallation with sharedUserMaxSdkVersion _(by Song Chun Fan)_  
[9272f7c](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/9272f7cad794c59e6747522b490acf23d56357b6) Limit the number of services (NLSes, etc) that can be approved per user _(by Matías Hernández)_  
[a87653d](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/a87653d94137b80b45a4858db4cac7576c7e1ee3) Block overriding satellite carrier config keys on user builds _(by Jayachandran C)_  
[c0bcd0b](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/c0bcd0bf5938d9be840e1fb7526f34a6230bfbf7) Remove any revoked associations after reboot _(by Evan Chen)_  
[97eda68](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/97eda6869dd14e83e0e46d7ed99cf5e45b041d51) MediaSession: Enforce max name length on broadcast receivers too _(by Ian Baker)_  
[9ee5a0d](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/9ee5a0d38e096315858471e1c781b21768da60a5) Be more strict about content types for message array _(by Julia Reynolds)_  
[14e471a](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/14e471a6d0b83e4ce43f59975e70dfdc8ca39ea5) Prevent long press on profile notifs when locked _(by Julia Reynolds)_  
[997d237](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/997d237305fcf724be446b482c90f5a7d80507e6) [PM] Check unknown sources for intent installation _(by Ivan Chiang)_  
[3439dc5](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/3439dc5827f66d815a340dc88785c79d154db6fa) Reapply "[PM] Check unknown sources user restriction for intent insta… _(by Ivan Chiang)_  
[ed26de9](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/ed26de9944ec05d0197861755843cf81304bd158) Explicitly unset INSTALL_FROM_MANAGED_USER_OR_PROFILE flag _(by Sanjana Sunil)_  
[336c08d](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/336c08dda3317e05dadd27874fb52048e95311d3) Prevent launchedFromPackage spoofing via FLAG_ACTIVITY_FORWARD_RESULT. _(by Annie Lin)_  
[495fe70](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/495fe705a5ce3230d5a913a9c2086a10964bfa24) Handle loadDescription OutOfMemoryError in DeviceAdminInfo _(by Iustin Ventaniuc)_  
[b3955a9](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/b3955a9db671fc37164849e2caacb0f3679b7b53) Introduce InputMethodSubtypeSafeList _(by Hiroki Sato)_  
[c94614d](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/c94614ddf341287c05201e714d1d7a6005c5500b) Harden InputMethodInfo parsing against large metadata _(by Hiroki Sato)_  
[44effeb](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/44effebdb529878796b08b72a84aed45d256bcac) Fixed "Unlock your phone" unexpectedlly turned ON after OTA _(by Shawn Lin)_  
[9245fa7](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/9245fa79a41e9f9e18417f5ce0f867aa8002e11c) Sanitize a11y qs shortcut tile service name before using it _(by Chun-Ku Lin)_  
[111f595](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/111f595e6e3d1764a82288d1b54e87216024c8ff) Trim permission, permission group names _(by Nate Myren)_  
[a756d43](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/a756d43ce178d4111ae4e09d8cb4e3515626ba53) Prohibit untrusted proxys from specifying proxied attribution tags _(by Nate Myren)_  
[5f104ac](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/5f104ac39035925c9f783176b4c712a28a6a09d3) Ensure sandboxed UIDs are treated as untrusted in Appops _(by Nate Myren)_  
[70bd77b](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/70bd77b1f5b1882510867320851006219bd0ea1f) [RESTRICT AUTOMERGE] Stay in app pinned mode upon SystemUI crash _(by Brad Hinegardner)_  

## 2026-02-28
[8538a4e](https://github.com/PixelOS-AOSP/android_vendor_lineage/commit/8538a4e9b04862bc14fede69b8d4955d1d119456) Revert "lineage: branded adb icon" _(by charcoal4494)_  

## 2026-02-27
[50f4567](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/50f45673bdb5eb7b5a76612c2157cd17a5b1866b) base: Never show the pseudo locales _(by Ido Ben-Hur)_  

## 2026-02-25
[daa6b3f](https://github.com/PixelOS-AOSP/android_vendor_lineage/commit/daa6b3fc80a994b8667253ccef24266815650881) config: Do not include Lineage-specific configuration _(by charcoal4494)_  

## 2026-02-24
[27a6c12](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/27a6c126ecea34bca6e1212d6d20a409ed4c1b58) SystemUI: Dismiss screenshot window on touch outside _(by LibXZR)_  
[5b292fd](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/5b292fdb899aa5a7a42003dc609cecbbc2dbe46d) screenrecord: Set entire screenrecord as the default option _(by Sourajit Karmakar)_  
[4046dc4](https://github.com/PixelOS-AOSP/android_build_soong/commit/4046dc4ce4886e9a1967097a8e587e8c3e25ac40) check_boot_jars: Add MTK packages to whitelist _(by Nolen Johnson)_  
[c888969](https://github.com/PixelOS-AOSP/android_frameworks_av/commit/c8889698e6296da70604dee016948cff511c710b) MediaCodec: Use proper surface when creating PersistentSurface _(by Luca Stefani)_  

## 2026-02-22
[ab19e64](https://github.com/PixelOS-AOSP/android_system_memory_libmeminfo/commit/ab19e64baa7a4d6c65262f03e5b16d204de703c6) sysmeminfo: Skip per process GPU memory usage trace if disabled in ke… _(by Tashfin Shakeer Rhythm)_  
[b7f34ff](https://github.com/PixelOS-AOSP/android_system_core/commit/b7f34ff6798a98be61743ae3dc781c64e51689af) Revert "libprocessgroup: CgroupSetup should fail if a required contro… _(by Yumi Yukimura)_  

## 2026-02-21
[bd020a5](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/bd020a5773790c49c33f7e4b0a3edc75a24d3011) Revert "SystemUI: Enable landscape lockscreen flag" _(by lemezohaib)_  
[fa29ea1](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/fa29ea185087f987209591e9c3cafbcdc682ae6d) KeyGestureController: Fallback to fullscreen screenshot on null data _(by inferno0230)_  

## 2026-02-17
[da4dcc6](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/da4dcc66b3acb712a77c655a8b7654daff0b62f2) Settings: BackgroundCheckSummary: use InstrumentedFragment to avoid NPE _(by inferno0230)_  

## 2026-02-15
[0132132](https://github.com/PixelOS-AOSP/android_packages_apps_Updater/commit/013213267b779b48b49837233d438b7588154b91) Updater: introduce stream OTA _(by Ashwin Devi Srinivasan)_  
[23ce6af](https://github.com/PixelOS-AOSP/android_vendor_lineage/commit/23ce6af3726be32e874c86be9be15ab7a4dc8f5c) Revert "config: tablet: Disable desktop windowing mode on internal di… _(by inferno0230)_  
[a6069e4](https://github.com/PixelOS-AOSP/android_packages_modules_Permission/commit/a6069e49446f3c6912ff8e2ef841aaffbf521aaa) PermissionController: Add missing permission groups _(by Pranav Vashi)_  
[98db2cb](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/98db2cb45906735e4767e59b20e9a40d4069b21a) fixup! SystemUI: Network Traffic _(by Sam Mortimer)_  

## 2026-02-14
[f28f76f](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/f28f76f79b69499c5328cd58ea1e31b2dc1bb71f) wm: Allow disabling window blurs by default _(by basamaryan)_  
[59d8825](https://github.com/PixelOS-AOSP/android_frameworks_av/commit/59d8825ffaa4c9afee96034756d1a7973bdff299) CAMX: CHI: Added support for handling jpeg debug data. _(by Abhinav sohane)_  
[b13e6d1](https://github.com/PixelOS-AOSP/android_system_core/commit/b13e6d17d3b0abf7621e00cc7492f02eb5bf089f) Merge "Revert "init.rc: remove 4.9/4.14 support"" into sixteen-qpr2 _(by Hridaya Prajapati)_  
[e405b34](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/e405b3473745ce19f1a694a2b39b307f35c416cb) fixup! SystemUI: Add double tap to sleep gesture _(by Pranav Vashi)_  
[79c5401](https://github.com/PixelOS-AOSP/android_system_core/commit/79c540150cad99c2212ea4c6beb9f29eeb8fb999) Revert "init.rc: remove 4.9/4.14 support" _(by Ido Ben-Hur)_  
[46ad4fe](https://github.com/PixelOS-AOSP/android_system_update_engine/commit/46ad4fe2747d599a9da3dcabe08c051885a22429) Use ro.build.type in HardwareAndroid::AllowDowngrade() _(by LuK1337)_  
[b69fc13](https://github.com/PixelOS-AOSP/android_system_bpf/commit/b69fc133eaa201f25ba1eda4b66157b35ade2979) bpfloader: Allow overriding kernel version _(by kyasu)_  
[2972fc7](https://github.com/PixelOS-AOSP/android_bootable_recovery/commit/2972fc7f906586bca19917f685080bddc43d34af) recovery: Make recovery usable on user builds _(by Christian Oder)_  
[4d2a0d6](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/4d2a0d6edddc67f5de9c8a012c4b265df9a6d929) s2ss: Remove property usage _(by LibXZR)_  
[ae8f6c1](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/ae8f6c1953bdac4dff0b5087241d2c65f5a6e32d) Settings: Network Traffic [2/2] _(by Jon Haus)_  
[6e1b0ad](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/6e1b0adb10d7c42146dda6e4dca207749d62595e) Settings: Add lineagehealth IFastCharge interface support _(by LuK1337)_  
[8381254](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/838125403cfc8a3a7a3a95f97330f6899c332677) Settings: Blend advanced reboot with new UI _(by Bruno Martins)_  
[10ee062](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/10ee06247ad2549f5b715bd90b56fa23c97d0088) Settings: Add three-fingers-swipe to screenshot [2/2] _(by ghbhaha)_  
[0599023](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/059902365432ae9f7e45f596f2a2d105452d85e1) Settings: DevicePicker: Adapt to S style _(by ReallySnow)_  
[b963a8d](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/b963a8dbfa6d97e2e71123696017097969f63cbc) Settings: Add Face Unlock with ParanoidSense _(by Chris Crump)_  
[d86ed90](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/d86ed90538571099f22d07600d3f8b3736ace651) Settings: Allow devices to provide remote gesture preferences _(by Bruno Martins)_  
[8b5bd8a](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/8b5bd8ad8fa7f59cdbc55f91a778a01f9c13a567) Settings: Add a RemotePreference for device-specific doze settings _(by Steve Kondik)_  
[8d3f3b0](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/8d3f3b02225c14a3f529b7f464fb2feafe0d932c) Settings: Add advanced restart with global actions _(by Adin Kwok)_  
[90a7880](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/90a7880a1bcfb07d1ba294e229b723d403177765) Settings: allow disable of screenshot shutter sound [2/2] _(by maxwen)_  
[e7fb2cc](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/e7fb2cc4cb9c09170d53cacf1824a95a4670b002) Settings: Allow devices to opt-out of advanced refresh rate page _(by hridaya)_  
[f14b14c](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/f14b14c444fbf8122082af413643d7815c78d706) Settings: Move configurable PIF and keybox to Developer options _(by hridaya)_  
[efe98e3](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/efe98e38ba5aa07c5ec5cf601e4a6d522565d9af) Settings: Kill play store too when applying new PIF data _(by Abhay Singh Gill)_  
[1d23d82](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/1d23d82d96b859f5779a913936435e4f367b8263) KeyboxDataPreference: Accept N >= 1 certs per key [2/2] _(by Ido Ben-Hur)_  
[5b72e17](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/5b72e17994fae5b270d6f4b6b5a2d7b7a7aea6ba) Settings:  Make PIF user configurable [2/2] _(by Abhay Singh Gill)_  
[111e1b8](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/111e1b88ba30a7f6b3020367673fea6d218faec2) Settings: Add key generation for keybox spoofing [2/2] _(by Abhay Singh Gill)_  
[e52e1ee](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/e52e1ee4b8566813f88a7ba5b2ecfa86f31e6c7b) Settings: Append custom version on build display id _(by jhenrique09)_  
[7ba1a3e](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/7ba1a3e3849aaca71500f5a051c36af748c64d37) Settings: Abstract away app check list fragment _(by Adithya R)_  
[c5da592](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/c5da5925102f5945a8dec9c59dfe45e8a75995ed) Settings: Implement cutout force full screen [3/3] _(by jhenrique09)_  
[03d70ce](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/03d70ce92d5ccb4dc5ddd21ce48ed5420591f172) Settings: Use ActionPrimaryButton style for face buttons _(by Jyotiraditya Panda)_  
[ae238ef](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/ae238efab7d819f7f34bde223c50e41b53b3bdd1) Settings: Add option to launch statusbar tuner [2/2] _(by Jyotiraditya)_  
[5adc336](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/5adc3369cf5a0d236c1874aaebccd92ac6a1dcc8) Hide the "Show the vibrate icon in the Status Bar" setting _(by Chirayu Desai)_  
[c0125ee](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/c0125ee63f237f2c3ae04c236c7e5e7f877ad508) SoftAp: add client manager _(by cjybyjk)_  
[4053d2c](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/4053d2c1410dea83e28b56c856ce8fdd28e84e37) Settings: add TextView for summary into SeekBarDialogPreference _(by cjybyjk)_  
[148a6db](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/148a6db5e5b501fdf0a543dca1a096a641ff91d2) SoftAp: add Hidden SSID preference _(by cjybyjk)_  
[d15521a](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/d15521a3ea5ad75e0cd0abda70c004266a6b1bd4) Settings: Pull screen off UDFPS toggle out _(by Ido Ben-Hur)_  
[cba5f06](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/cba5f06dc21a32e0f0e48dfc0c98f67ac27d5dcd) Settings: gestures: Add page for Screen-Off UDFPS _(by Cosmin Tanislav)_  
[e665859](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/e665859fd7473640e51b13bb76d791af079f3bb5) Settings: Add toggle for 60Hz refresh rate on battery saver _(by Adithya R)_  
[001c5eb](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/001c5ebdab16adc4c8b46709931b7679477d8341) Settings: Add QS tile for refresh rate indicator _(by Adithya R)_  
[2d6db91](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/2d6db911c9a786c722b05bb557313b3770b13bc8) Settings: Introduce new refresh rate selector page _(by Adithya R)_  
[bb917d1](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/bb917d1cb7c0d90df6315c6208d30573ee8d2dfa) Settings: Make Ambient Display toggle show on single tap sensor _(by Cyber Knight)_  
[49e5af6](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/49e5af6edfed7004c9774e86d703cd2701bb86b2) Settings: Allow setting wake for notification separately from doze [2/2] _(by Ido Ben-Hur)_  
[856ae1f](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/856ae1f3958796864f04445e5a4f25f4d57b94d1) Settings: Allow showing Ambient instead of fully waking [2/2] _(by Ido Ben-Hur)_  
[53d64d1](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/53d64d13ad588ff6ff5646d1274ac093fa9d7206) Settings: Add missing icon for media output _(by ReallySnow)_  
[ed7a4e9](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/ed7a4e91a97879b862d5d3aa13911eb5c7c277ac) Settings: Add Private DNS icons _(by penglezos)_  
[8ac54fa](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/8ac54fa862a051bb09809ceefbd31ab3d225e010) Settings: Add incall vibration options [3/3] _(by beanstown106)_  
[3626b59](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/3626b59c77a31b8ef5bd6218aa2deb8e03370581) Settings: Use List Preference for NightLight settings _(by Akash)_  
[6eb4d05](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/6eb4d05f1aebe30edadd70f40f6b47791fd0ca8c) Settings: Use List Preference for DarkMode _(by Pranav Vashi)_  
[945dd0b](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/945dd0b1a60177de34295a4ad6633ac908f4273e) Settings: Move window ignore secure to global settings _(by someone5678)_  
[8b9f31f](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/8b9f31f13b3703849248d8dc40b6545fee0057b7) Settings: Add window ignore secure feature [2/2] _(by LibXZR)_  
[6d4d28d](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/6d4d28d9b7b156c708827193c8c53826301a09e1) Settings: display: Add wake on plug switch _(by Jon Evans)_  
[29ba70f](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/29ba70fff4648d8fc85e3c851f873bc581ec78fe) Settings: Add option to cycle through ringer modes [2/2] _(by rituj)_  
[f89e431](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/f89e431b1299de21e6e9fe4fceab784870dfa477) Settings: Forward Port Volume Long Press Skip Tracks [2/2] _(by Chris Crump)_  
[f3111b7](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/f3111b7e138f324dabc6621c989d67d9afe4ac7a) Settings: Long press power button to toggle flashlight [2/2] _(by Chris Crump)_  
[2b04308](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/2b04308263e81500b68f3c5e1fca4091c0a5090d) Settings: Hide power menu on secure lockscreen [2/2] _(by Altaf-Mahdi)_  
[252f5f0](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/252f5f0b2bb15befd1620a621aaaa50e81fd0ab7) Settings: Add toggle for Smart 5G [2/2] _(by Adithya R)_  
[220ccef](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/220ccef9ada81cac51b073901a5c4d5ec338d311) Settings: Add preference for one shot auto-brightness _(by Cédric Bellegarde)_  
[a3cd7c8](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/a3cd7c84e97f9aa3b10b95d7c50bbc989c851efb) Settings: Display auto rotate settings instead of toggle _(by Adithya R)_  
[55b0d74](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/55b0d74a2b7594e5d4f08b89ac8787251dcdd651) Settings: Configurable 0, 90, 180 and 270 degree rotation [2/2] _(by kufikugel)_  
[c7b67ca](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/c7b67ca7ead8ffac15265162f5110928851495ad) Settings: Forward port pattern visibility settings (2/2) _(by Michael Bestas)_  
[6f78908](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/6f7890878ed831ff604fd30eece9af04cafe7ca1) Settings: Forward port lock pattern grid size (2/2) _(by Michael Bestas)_  
[38627ca](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/38627caa1e6d784e22ccedcc0eb340e3ac81004d) base: Add three-fingers-swipe to screenshot [1/2] _(by ghbhaha)_  
[db83ffa](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/db83ffaea9c19e5dc7c16911325f79d101fc073d) camera: Add backwards-compatible CaptureResultExtras constructor _(by Adithya R)_  
[949eb91](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/949eb914025f786a3a27669337013423f5ec10e7) core: camera2: StreamConfigurationMap: add constructor for MIUI camera _(by Pulkit077)_  
[805bdfc](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/805bdfc09a44a8fede54b06c28540ced75151473) camera2: Add methods for backward compatibility _(by Ihor Ivanov)_  
[3c536fc](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/3c536fc2d00c0a928b226fdaebc237c2785bd6b2) base: Update some icons to MD2 _(by Anushek Prasal)_  
[77fb9c5](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/77fb9c599d5ebe9785279f974ffbeeb941bb1572) SettingsLib: Update 5G+ icon to Silk design _(by Adithya R)_  
[e15d7fa](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/e15d7fa1d2f9a76e29bdc78d2074554022ae0544) SettingsLib: Update 4G+ icon to Silk design as well _(by TH779)_  
[c644684](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/c644684a8b678ced2467232010605df9d5eecb06) SettingsLib: Update LTE+ icon as per new Silk design _(by Adithya)_  
[cc22f49](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/cc22f49f679baeda6b033cd1b2f8b016761f409e) SystemUI: Adapt screenshot sound to ringer modes _(by Ashwin R C)_  
[751c52d](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/751c52de270a8b1fac2690e46e6543211b9490d0) display: Don't spam log when display state changes _(by Adithya R)_  
[4220dc2](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/4220dc28383bacd9bbb4356efe327c9ae743fa11) display: Consider peak refresh rate in BrightnessObserver _(by Adithya R)_  
[711079a](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/711079ad26b7176790a9467f9f6bc7ae2990ca18) SystemUI: Update SystemUI icon for advanced reboot _(by hridaya)_  
[5d5275a](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/5d5275a8d21e3d03ed8e5b0e32847fc386152dd6) core: Remove fastbootd option from Advanced reboot _(by hridaya)_  
[468a7f1](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/468a7f14fae65206245c3b93bdcbe58d5420e144) SystemUI: Add restart SystemUI in Advanced Reboot _(by Phạm Tiên Sinh)_  
[813c721](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/813c721c76b06f5a1f3f3bd4f6bb0ded66f40dd6) frameworks: Add support for advanced restart options _(by Michael Bestas)_  
[049fe6f](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/049fe6f4a2de34dc11ddfed2846a1017e8138883) BatteryService: Add support for oem fast charger detection _(by Alexander Martinz)_  
[c263b15](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/c263b15a01d82ad1f9d47db420208f61fc973815) SystemUI: Network Traffic [1/2] _(by Jon Haus)_  
[e65c68d](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/e65c68d2e6f92f6221d9284e14bb07b9807e7749) SystemUI: Add custom statusbar item holder _(by Sam Mortimer)_  
[a6ceb99](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/a6ceb9992ecc5f9a42726af9ca80dd0d8a6c0790) SystemUI: Disable smartspace default view _(by aswin7469)_  
[116c894](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/116c89423e50196bf8a4fd94704cb582723d3a0b) SystemUI: Implement the newly reverse-engineered smartspace _(by ralph950412)_  
[8a3f8f0](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/8a3f8f09738b82abc201588108aaa89409e99944) SystemUI: Implement face unlock recognition text _(by minaripenguin)_  
[d9aa49b](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/d9aa49bed839ad7cb184d648a37c652977bc2fdb) KeyguardBouncer: Don't delay showing if face auth running _(by jhenrique09)_  
[c17b42c](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/c17b42cdb373c424cdbbb82e15a8dd9b21555d17) SystemUI: biometrics: Follow user setting to confirm face unlock _(by Pranav Vashi)_  
[fafb452](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/fafb452f01baad6d31523ce1ceed0f7d006acb8c) SystemUI: Disable FaceUnlock Lockouts _(by minaripenguin)_  
[762fc14](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/762fc141807ce806e04e7526de95a3640874fc8b) services: Force load FaceSense providers _(by Pranav Vashi)_  
[dabac5d](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/dabac5db0dcd2045cd5d220131866a6da2af7b67) FaceSense: Vibrate on successful authentication _(by Adithya R)_  
[3c2f92e](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/3c2f92e27af4d8ec2af1550abcbab7bffb85698d) FaceService: Conditionally add ParanoidSense _(by someone5678)_  
[6c0e4ad](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/6c0e4ad5294246ba9e1395f9b6be7a1acca3fdec) base: Initial SenseProvider for FaceSense service _(by Chris Crump)_  
[ca9d1b5](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/ca9d1b54ccfa848922152c9f4b7a0b343d0efc04) SystemUI: Introduce Data Switch QS Tile _(by Christian Oder)_  
[25a5afc](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/25a5afcc97b2191eeb985261fbc029f06622d418) SystemUI: Add Autobrightness tile _(by Dil3mm4)_  
[6dbca4d](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/6dbca4dc6f1cc739a548e539c53b3916771334a3) Quick Settings power menu uses keyguard show state _(by Tommy Webb)_  
[45d17f9](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/45d17f93866e8c3115d26268c8224900894e1ea3) JobScheduler: Respect allow-in-power-save perm _(by Tommy Webb)_  
[dc67980](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/dc679802a1e5e1cb6c81efea6d98b541545315d9) Enable Binder Proxy Tracking by Uid only on eng builds _(by dianlujitao)_  
[37c341d](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/37c341d589dc92057fa88d2c4d5b11f7cb2d0a42) SystemServer: only enable fd leak tracker on eng _(by Simao Gomes Viana)_  
[5fae1af](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/5fae1afb5c600d8e42b7d770bf41c4ec12a7822a) AutofillManager: Make userdebug default to NO_LOGGING _(by LuK1337)_  
[529df3c](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/529df3c23e285e7cc2d4482023204ca82f21dcc4) webkit: SystemImpl: Make systemIsDebuggable() check IS_ENG _(by LuK1337)_  
[c65dcc1](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/c65dcc1619d775c5be328d70aeafd920019f00e0) base: Implement cutout force full screen [1/2] _(by jhenrique09)_  
[f823eee](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/f823eee6120a2ba68816dff1eebcffe79851f6d0) aapt2: add freeze IDs for ContextualSearch _(by Matt Filetto)_  
[02ca1c1](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/02ca1c15edb283f61eb80c492ba194fc7234c13e) aapt2: support freezing private resource IDs _(by nift4)_  
[25acb44](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/25acb44148ce5f4731b81d7e828fd8be59f27cd5) SystemUI: Add double tap to sleep gesture _(by Rashed Abdel-Tawab)_  
[df6cb71](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/df6cb71b7d3763afb1708a6147771ebb56fed762) base: Allow setting wake for notifications separately from doze [1/2] _(by Ido Ben-Hur)_  
[f4ac5d1](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/f4ac5d118b687f1bd1f3e2a9d639104ec46eeece) base: Allow showing Ambient instead of fully waking [1/2] _(by ezio84)_  
[1f0a7b4](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/1f0a7b4995d91bd2757063304fec76df95af4a3b) SystemUI: Add DOUBLE_TAP_TO_WAKE to tuner service reset exceptions _(by LuK1337)_  
[4431a24](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/4431a24d63237a8e5152699e7d422327f346d9fc) SystemUI: use DOUBLE_TAP_TO_WAKE setting also for wake from aod _(by maxwen)_  
[8da25d9](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/8da25d94b8838dcc716e367c37a5dde2e64c3821) PowerManagerService: Wake on plug (1/2) _(by Jon Evans)_  
[d5146e0](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/d5146e00d1a5749bfc6bc7daac9ec0a03fff049d) base: Allow disabling refresh rate lowering in battery saver _(by Adithya R)_  
[dff5ff8](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/dff5ff88b61e504b35e80518a0d0cc40a209410f) base: Incall vibration options [1/3] _(by beanstown106)_  
[1d0e9b9](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/1d0e9b98e079404a1a746f0d41da313b86a423b1) base: Add support for window ignore secure [1/2] _(by LibXZR)_  
[425260e](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/425260e5cd59fa8eb541dd6de4a74f31d5953f76) [SQUASH] base: Add option to cycle through ringer modes [1/2] _(by rituj)_  
[bb0c7cc](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/bb0c7ccc14eef3bf0cbbc0bb8610df93a64bc178) base: Forward Port Volume Long Press Skip Tracks [1/2] _(by Austin T. Conn)_  
[a9e0b67](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/a9e0b6796ab5da7f1a0d6397f8cf1464f1929f25) base: Long press power button to toggle flashlight [1/2] _(by ezio84)_  
[77ff56e](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/77ff56ef714d951d2ef3655d111fae089e8217d0) SystemUI: Launch power menu from QS only if enabled _(by DarkJoker360)_  
[75f5c0f](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/75f5c0fbe8b6c83f2269555b1f35da0283b0bcf2) base: Fix disabling power menu completely on secured lockscreen _(by Pranav Vashi)_  
[c60a333](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/c60a333d280c16d4ebcc9201a53ea1e36e8619d7) base: Hide power menu on secure lockscreen [1/2] _(by Altaf-Mahdi)_  
[8164482](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/81644824b283b413cda8b29a906f22a687844423) Configurable 0, 90, 180 and 270 degree rotation _(by Ricardo Cerqueira)_  
[f338609](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/f33860911ee38c6f020e8205ad4059d5cecdd730) Increase maximum password length to 64 _(by Oliver Scott)_  
[6835d72](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/6835d72257ddbdab2eb3914157370e884f30a5dc) Forward port CM Screen Security settings (1/2) _(by Michael Bestas)_  
[121d5a5](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/121d5a5115500e467ed654e5b5854c7df0d07dc5) Keyguard: Add option to scramble pin layout when unlocking (2/2). _(by Adnan)_  
[80b388a](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/80b388aedd9e64942f87da3858765011b45d5636) AutoBrightness: Add support for one shot auto-brightness _(by Cédric Bellegarde)_  
[f444ea7](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/f444ea73194a6b18fc34566cfef1994851e2799e) SystemUI: Fix burn-in translations not applying to keyguard slices _(by Andy CrossGate Yan)_  
[5e63b0c](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/5e63b0c30d8ca64b738e44765d5980f94799fb72) SystemUI: Update buildNumber flow to return null _(by NurKeinNeid)_  
[d178764](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/d1787645ff48eba8da47b4a4417c2b5b9be6c818) AudioService: Remove Analog Dock from fixed-volume devices _(by Vachounet)_  
[add394f](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/add394ff76ec80c58e0f93a583ea87f9fa737f60) SystemUI: Remove screenshot action chip labels _(by Dhina17)_  
[0f9d318](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/0f9d318b72256bc7195de537f3dbcbb7b11c448c) SystemUI: Reduce screenshot dismiss delay to 3 seconds _(by Danny Lin)_  
[c6f26dd](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/c6f26dd0e39d19a9f4fd0ea4dc7eb847d900d905) SystemUI: screenshot: Add delete action chip intent _(by ganeshi4u)_  
[a5fce17](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/a5fce17dc73f7864a07c3e12f178f04f5118311e) SystemUI: screenshot: disable magnification for partial screenshots _(by Cosmin Tanislav)_  
[2d6b860](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/2d6b86014db5b1c89821489c3420b18bd97c6acf) SystemUI: screenshot: close QS after launching long screenshot activity _(by LuK1337)_  
[dc8aea7](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/dc8aea7efeb252642a2d649740d0f06e73812940) SystemUI: screenshot: open long screenshot activity for partial scree… _(by Cosmin Tanislav)_  
[7060a4f](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/7060a4f83033887dd6d985f77e823a692f7e9585) SystemUI: screenshot: add extra crop boundaries _(by Cosmin Tanislav)_  
[5aff7e0](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/5aff7e0c5a5cf3fc5c12ef3c180efa7da898c4f0) SystemUI: screenshot: remove duplicate clamping on move action _(by Cosmin Tanislav)_  
[6ce842c](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/6ce842cdb86ead3aacaa26c28d3a44f5545e81e0) Implement click to take partial screenshot [1/3] _(by Jesse Chan)_  
[9615bad](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/9615bad54031428edb624be75cad84e230283177) Put bare minimum metadata in screenshots _(by Chirayu Desai)_  
[9bd1b60](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/9bd1b60de3d8ce90b38387954c7054f591f80eb5) Screenshot: Append app name to filename _(by ezio84)_  
[3f04fdf](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/3f04fdf30fb9a66847f603b1edf0e7c79318478a) base: ChooserActivity: Don't show image edit button on multiple targets _(by Aayush Gupta)_  
[df6e157](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/df6e157dad9410bac696a3093a7f88f41cbe09d2) SystemUI: screen_record_options: Switch to common textAppearance style _(by hridaya)_  
[941ea60](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/941ea60ae7e9483161f4eefd8c85d50a29da6f5c) Screenrecord: Save preferences for permission dialog _(by Pranav Vashi)_  
[3929803](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/39298035fe305ec035489d7776a6b8887351a6ae) Screenrecord: Hide HEVC option when no HW codec is available _(by Ido Ben-Hur)_  
[c967515](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/c9675154a0c31f5a9e21dd919b78bb95f7eb0aeb) Screenrecord: Add an option to use HEVC _(by Ido Ben-Hur)_  
[8e92ac3](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/8e92ac3685e7a2811aa88445ee6580920b141e59) Screenrecord: Allow to reduce 3 second screen record timer _(by maitreya29)_  
[25bf02a](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/25bf02a728541a2c0df8f4ff6222552b8640b4d6) Screenrecord: Add an option to record for longer _(by Ido Ben-Hur)_  
[31e5cd2](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/31e5cd2ec5b173e55a931aa66965649a9e83d4d0) Screenrecord: Make low quality bitrate scalable per device _(by Ido Ben-Hur)_  
[8753f85](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/8753f8568838c236eedb346b8c0ec510e2c7a0b8) Screenrecord: add low quality option _(by ezio84)_  
[c5ce07c](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/c5ce07cdf6ca41d0b8e1edba3f63c38009693400) Screenrecord: Allow to select AVC codec profile level _(by iusmac)_  
[a3d551a](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/a3d551a7aa8ba3f5e8319c517453a85b8c4ba120) Screenrecord: Allow limiting the max framerate _(by Kuba Wojciechowski)_  
[36836db](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/36836db09ae78bb9e4f4028348e07bcc2528a80a) Screenrecord: Use AVCProfileMain _(by Arne Coucheron)_  
[87e5426](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/87e5426607f7d03c48556a1bddb6b5500498d951) Add some fwb stubs from Oplus _(by DennySPb)_  
[af2ea22](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/af2ea2280085ea395e1ade851a59c4d91603e999) BatteryService: Expose [maximum|design] capacity API _(by Jyotiraditya Panda)_  
[da5a73a](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/da5a73a4cf9ac5f1c152ea44002d5d84a83fa5c5) BrightnessUtils: Conditionally disable gamma conversion for brightnes… _(by SagarMakhar)_  
[44393dd](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/44393dd025ffda17595cdbde79014dbaeb2063e4) Keyguard: Hide battery indication on battery-less devices _(by Bruno Martins)_  
[5f1f1c3](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/5f1f1c383ebe5a7f3f3590790dc8b0b3f034155a) Fallback BUTTON_SELECT to BACK _(by Aaron Kling)_  
[483d98c](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/483d98c6091557e96dc8045807527cc038dff87c) Fallback ESC to BACK _(by Aaron Kling)_  
[1685175](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/1685175beba425c0bce9988996adf61da0bf9e1a) [SQUASH] Implement DeviceConfigUtils and service _(by jhenrique09)_  
[d90fd85](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/d90fd8511ff307f8f15f0ded4a0e58df1602e33d) Add config to exempt telephony-related app from location indicators _(by Danny Lin)_  
[34b50ca](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/34b50ca5d85107a9cc2d59ced5653e910195b1a3) Smart5gService: Avoid early return with multiple subs _(by Adithya R)_  
[b220eea](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/b220eea225547a7b79598e7255b563716bb9f12c) base: Introduce Smart 5G service [1/2] _(by Adithya R)_  
[78f66fc](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/78f66fc14d21c53859cec671b37a9366eeb13e74) PowerOffAlarmService: Guard until boot is completed _(by Ido Ben-Hur)_  
[5e92f5d](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/5e92f5dbe443578c65b8122fb3ce69eb2e32f96a) PowerOffAlarmService: Handle NPE with shared preferences _(by Adithya R)_  
[c22c1d9](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/c22c1d92bad84b5dd41e467b2f5964975e4c3cfd) base: Introduce PowerOffAlarmService _(by Ido Ben-Hur)_  
[2c9e0c8](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/2c9e0c8036f3e486d1cd24d350230cbc7ff59686) SystemUI: Remove alarm from statusbar icon blocklist _(by Adithya R)_  
[5a0628d](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/5a0628dd09970c19204bff1b85c946b226088b31) fw/b: Add setting to allow tethering to use VPN upstreams _(by Oliver Scott)_  
[d954608](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/d95460879c6c2a33a9a81e8b6edb0c76252d30e5) core: Overlay the PIF JSON update URL _(by hridaya)_  
[91add03](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/91add036ec304fed76c57e760c1067e9daf9113e) PropImitationHooks: Block key attestation for play integrity _(by Abhay Singh Gill)_  
[2208536](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/2208536aa04a15d9eeee291e746756badd897117) PropImitationHooks: Skip play Integrity props in isolated processes _(by Akash Srivastava)_  
[ca53b9b](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/ca53b9b5b931795fe6abcff4b2fa866f90aeb5d7) KeyProviderManager: Accept N >= 1 certs per key [1/2] _(by Ido Ben-Hur)_  
[ba4e0f4](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/ba4e0f4214c0ec8738ec1e7087deca326435376c) PropImitationHooks: Spoof certified props to finsky as well _(by Ghosuto)_  
[d42100d](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/d42100d1d14af734c7a7b0f2802da2d3bc8bbfe7) core: Make PIF user configurable [1/2] _(by Abhay Singh Gill)_  
[a085e0e](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/a085e0e82c3eeccef027b57490bca7556462f532) PIHooks: Dynamically spoof props for GMS _(by SamarV-121)_  
[25fa495](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/25fa4953ef34293cea6372ca558ae1b19779faed) base: Add key generation for keybox spoofing [1/2] _(by Abhay Singh Gill)_  
[8cc0a48](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/8cc0a48232ce752ee281902306e9c5ee0f1980da) Initial implementation of KeyboxImitationHooks _(by Jyotiraditya Panda)_  
[9e0a61b](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/9e0a61bad32073e48a1288de607fcee0f65bfdcc) PIHooks: Spoof Google Photos _(by Adithya R)_  
[07ec304](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/07ec3041c8d8bcf28f37b5507704da0fc07dcc49) PropImitationHooks: Make it a hidden API _(by Adithya R)_  
[5ce0886](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/5ce08865f72851d367176207ed7073922f0aefe2) PropImitationHooks: Allow user to disable prop imitation _(by Jyotiraditya Panda)_  
[4615abd](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/4615abd8800b0da75433a622286a1d594eb84983) PIHooks: Get resources from context _(by Adithya R)_  
[908dd17](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/908dd17df4e3c500095a6c2cdbad8f3302f8a770) PIHooks: Allow setting any field in certified build props _(by Adithya R)_  
[5bf0e17](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/5bf0e17c3ac30a2c1388ce0086c7c3e287d8fd8c) Introduce PropImitationHooks _(by Omkar Chandorkar)_  
[07e1709](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/07e170900c0c29a65e125f2f459d3e334d1da814) health: Catch all exceptions in fastcharge handleSettingChange _(by Michael Bestas)_  
[13d549e](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/13d549efee52d42092f8549c1fa5bb44a553b23d) base: Add lineagehealth IFastCharge interface support _(by LuK1337)_  
[ccb6dac](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/ccb6dac2362a11b2423bc382b4fe591430fcb9f0) sdk: Export receiver for health service _(by Nick Reuter)_  
[bb20d66](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/bb20d66d95c9dfecb87a31390f0368b4683514c0) sdk: Remove LiveDisplay HIDL support _(by Bruno Martins)_  
[4be7411](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/4be7411e7a21d071713ec9a0588ad967dfe64de0) lineage-sdk: sdk: Try getting LineageHardwareService again before che… _(by Andy CrossGate Yan)_  
[b850aa3](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/b850aa35eb9d34e6d9189ce8c84009b4b42d1811) lineage: Wire up AIDL LiveDisplay HAL _(by LuK1337)_  
[bbb4d09](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/bbb4d090741645a02ae84c0b793073297eb68552) health: Fix limit notification _(by Luofan Chen)_  
[b3e96a2](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/b3e96a24644a449f9e4544ec2f8f5722a09fa164) health: Implement new charging control battery listener _(by Luofan Chen)_  
[c8124d5](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/c8124d543f7336ab6b821c5c33c5c82be03d6d30) TwilightService: Use temporary TwilightState when location is not ava… _(by rituj)_  
[d752d10](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/d752d10683a7db8f44b2336b29ca21128c994410) services: TwilightTracker: create an attribution context and use it i… _(by jhonboy121)_  
[01e8aa6](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/01e8aa6f616dc9f6a08de44bd056e083132df18a) lineage-sdk: Fix UserContentObserver build _(by Michael Bestas)_  
[ea3e8e5](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/ea3e8e5b74fafea98a3699064ee2d3a169678ac3) lineage: Remove touch HIDL support _(by Bruno Martins)_  
[7568c8f](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/7568c8f19057339ab4693a9c04c5850810eb5a1c) lineage: Wire up AIDL touch HAL _(by Luca Stefani)_  
[a88a864](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/a88a8644275fb1a7dfa8bbada538f66f4feb304f) fixup! Add high touch sensitivity and hovering to InputService _(by Oliver Scott)_  
[4843a58](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/4843a5839666a582800e952fd9ce398d39dac557) fixup! Introduce high touch polling rate feature control _(by Michael Bestas)_  
[303490b](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/303490bfd298e4bfdd8a3c17d6f0d2ea3e5e9a8c) utils: Import PackageManagerUtils _(by Michael W)_  
[7ec287b](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/7ec287bc51d6d0d7044bd9d6e758d220dba29189) utils: Introduce FileUtils class _(by Michael Bestas)_  
[1edf72d](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/1edf72dfe239dff296772316e129074fff0fc88c) health: Update charging control if next alarm is changed _(by Trogel)_  
[5f4d71b](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/5f4d71bac1ce941444811b92ecf5964b6f73f5b8) health: Don't turn on charging control if not plugged in _(by Trogel)_  
[fb75039](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/fb75039483763ec0ce44ae17d041444c4a7fc016) health: Allow Limit/Toggle providers for MODE_AUTO/MODE_MANUAL _(by LuK1337)_  
[d50a003](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/d50a0039421db58c182a2c2e16366db1b6e0046e) health: Select correct provider on init _(by LuK1337)_  
[279b153](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/279b153f8cb55d3bee44516ed54d28bb58782e61) health: Implement charge limit mode _(by Oliver Scott)_  
[540459b](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/540459bd0b58f0cfb35ed01f67a52f1d6e9ef1dc) ChargingControl: Prevent crash against very frequent power toggle _(by Oliver Scott)_  
[1a48a21](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/1a48a210a72ab091d6796c552cafda66dfb89fe3) health: Catch all setCharging*() exceptions _(by LuK1337)_  
[cf8b3df](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/cf8b3df1a86e635ffb390f36e04376bb981c2a67) health: Rename msToUTCString to msToHMSString _(by Luofan Chen)_  
[9852e5f](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/9852e5fb60922c12f7cf9470b9259b5213f3600c) health: Format notification's target time according to locale _(by наб)_  
[703ab02](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/703ab02745953d496f311fd088413636e212f837) base: Decouple charging control and main logic _(by Luofan Chen)_  
[f8568d5](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/f8568d5186a247647b47a2d0031cffba0018947e) Introduce high touch polling rate feature control _(by Ramii Ahmed)_  
[2afe27e](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/2afe27e29e6b0e03905665b69eac719c76e2f852) base: Add Touch HIDL support _(by Anushek Prasal)_  
[93f1d37](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/93f1d376b1ebefd58c93dd0579458a2c8d176403) Introduce anti flicker mode in LiveDisplay _(by Arian)_  
[06038ff](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/06038ff86849a14bd46dd97c8fcb36c7636da4c9) Introduce LiveDisplay from Lineage _(by Henrique Silva)_  
[15af49d](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/15af49dd8c2b79803f3c92814d8de21a4ac512d0) Initial import of lineagehw _(by jhenrique09)_  
[95bafe1](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/95bafe168528eb2579a3cd6759bec02cb43bc3b7) base: Implement Lineage Health Service _(by Luofan Chen)_  
[55ed663](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/55ed6630e92b9dbbf80065d78698b0c7662bb7c0) policy: Add support for device alert sliders. _(by thecrazyskull)_  
[ae53194](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/ae531942a4bb16e0e7b5d500f6ef9e7d9850eb79) SystemUI: Allow skipping mirroring confirmation dialog _(by Sebastiano Barezzi)_  
[0a8730e](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/0a8730ef9542bc5b82cd87e36202bd4f2378f36d) power: Respect global vibration setting for charging sounds _(by Michael Bestas)_  
[0e21870](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/0e2187027ef4eca03af08bced77b2e19bb5429c4) power: Explicitly check for silent ringtone _(by Sam Mortimer)_  
[0986108](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/098610834e149952d34c934629a522935be08dbd) Sharesheet: Display two rows of max ranked targets _(by LuK1337)_  
[cc638e9](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/cc638e976a5791d82898b879d2606cf5985efb98) Settings.Global: Add UIDS_ALLOWED_ON_RESTRICTED_NETWORKS _(by Chirayu Desai)_  
[8ef75fa](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/8ef75fae67788e16e603fb68c27e398c347c33e4) SystemUI: Support black theme for dark mode _(by althafvly)_  
[52b154c](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/52b154c58db7c74984c40bc5a924b2b54fcf201f) Don't skip theme application if it's already current _(by Michael Bestas)_  
[54488e9](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/54488e9721023f2adbf5087d5a057dfc3ab33e2c) Fix bug Device that can't support adoptable storage cannot read the s… _(by sangho.yoon)_  
[70ee2e4](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/70ee2e48ed6574c80e91c5d315387e64dd68cedd) base: Add button to upload crash log to mkrbin _(by Till Kottmann)_  
[6de4467](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/6de4467081f7168bd87070a9d9c33330319e0f4c) Add deep sleep info to uptime preference _(by maxwen)_  
[4b97e38](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/4b97e38c60b2e8501dbe0c8084f4adc33593a581) webkit: SystemImpl: Filter out unavailable providers _(by LuK1337)_  
[79bd14b](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/79bd14bb0082263f19d5c90c2f2a8d39dc90156f) Fix ever-growing AppOpItem string representation _(by Tommy Webb)_  
[482b30e](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/482b30ef118c5d6fa3c171ac22f920cd7edd46d3) PhoneWindowManager: Restore haptic feedback for physical nav keys _(by LuK1337)_  
[249afe9](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/249afe9a77162a08f0ca16a5d54be013413cab53) Allow BAL for usb debugging notifications _(by Christian Hoffmann)_  
[e722eb9](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/e722eb9ef245fe0fad1c165bd32a818c8d50c75c) core: convertVelocityToFrameRate should use MAX frame rate at any vel… _(by John Galt)_  
[4381772](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/43817721a6c67856412fc2f56955c930f09fd7fd) services: core: wfd: extend check for qualcomm wfd jar _(by Alexander Martinz)_  
[2f64a02](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/2f64a02f516d83cab399030883ef2b1a317a4b39) SystemUI: Grant android.permission.ACCESS_FINE_LOCATION _(by LuK1337)_  
[8ea53a7](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/8ea53a75694e2c63bb84c829e031b9564ddd0a68) Don't strub mac addresses in getWifiDisplayStatus() for SYSTEM_UID _(by LuK1337)_  
[5458514](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/54585142ae2d76bdc41d17c5eeb7347a2ed17e67) WifiDisplayController: handle preexisting p2p connection status _(by Li Sun)_  
[543a0e9](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/543a0e9a6d506eacded3369d774929065f9e19e7) SystemUI: Check whether the selected WFD route is available _(by Weijie Wang)_  
[4bb9cfb](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/4bb9cfb1dcb10fe9f49faf1d2a2a7de848633290) Merge changes for launching wifidisplay from system settings _(by Indranil Chakraborty)_  
[eb74b9d](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/eb74b9d07341a2c5d2df89fc69e18c731096f1d1) Fix HDMI CEC volume control setting being ignored _(by João Oliveira)_  
[aebca84](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/aebca84ccce345a13b09774c7eb1ff12da84c6c6) Grant CAPTURE_AUDIO_OUTPUT permission for media uid _(by LuK1337)_  
[02646e3](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/02646e3383ff3f7161b6abcef1a35a595899dd6c) UdfpsHelper: Track brightness mirror to hide/show dim layer _(by pjgowtham)_  
[83dadee](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/83dadeec07b2bedba5c478c8c41b44667eca2806) Biometrics: Allow disabling of fingerprint cleanups _(by Quallenauge)_  
[ad79ae5](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/ad79ae53ca1e23321fe737755e09aa25333bfd20) FingerprintUtils: Migrate old fp config xml to new one on HIDL/AIDL s… _(by Luofan Chen)_  
[e12873d](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/e12873d0e7b825f3739e21460689559e46f99464) HidlFingerprintSensorConfig: UNKNOWN -> UNDER_DISPLAY_OPTICAL _(by LuK1337)_  
[6fc6bd3](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/6fc6bd341753ca1daf3117bd372c7d1263dfb961) HidlFingerprintSensorConfig: Add support for HIDL workaround props _(by LuK1337)_  
[8d3b6e7](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/8d3b6e7e1138675089e03763f7b6f6ddf5f3067e) fixup! SystemUI: Add support for udfps dim layer _(by ExtremeXT)_  
[01f1b84](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/01f1b84bb4bb3844902c42f64524d21b31a78da9) SystemUI: Add support for udfps dim layer _(by pjgowtham)_  
[a4291cc](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/a4291cc1fbeafc8bf41828e1169aedd60d4009f7) udfps: Make pressed udfps view configurable _(by TheScarastic)_  
[f46641f](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/f46641f17eb7ef08ba13475c1867e26c8faabd3b) udfps: Restore illumination dot for global hbm _(by Arian)_  
[b3905cb](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/b3905cb2d26a221d620b84b571de9b5e2f978379) Biometrics: Hook up support for halHandlesDisplayTouches prop _(by Bruno Martins)_  
[2ecb033](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/2ecb033ef33569221b4526c3b0d510192d2d7981) SystemUI: SideFpsEventHandler: Don't crash without FingerprintManager _(by Michael W)_  
[58b3574](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/58b357462a96f02fae0bab44204d773ba72fa160) SystemUI: Restore 14 QPR1 FingerprintInteractiveToAuth handling _(by LuK1337)_  
[f059f53](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/f059f53c99fd42a2d47222393784f5cfde54497f) SystemUI: Add FingerprintInteractiveToAuthProvider implementation _(by Adithya R)_  
[74f2578](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/74f257800c2924ec99b7ef233bdd91fedefa8913) Apply monet to fingerprint authentication ripple animation _(by SagarMakhar)_  
[aea3a1c](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/aea3a1cee9f2b47e4e3dcfae764e170360be0e55) core: pm: Allow wildcard in RRO system property value checks _(by Luca Stefani)_  
[a65bb37](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/a65bb37ea77b77dc7ae65ff1c14261a3e875c0e5) core: pm: Use checkRequiredSystemProperties from FrameworkParsingPack… _(by Luca Stefani)_  
[5ff5ab3](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/5ff5ab3b761d375f43f496b47b93c2ae0628156e) Download: Add support to manually pause/resume download _(by qqzhou)_  
[96753e6](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/96753e68d7189d09671c48d44ba780d787a5fac2) base: Allow disabling turbulence noise after clicking the play button _(by Ido Ben-Hur)_  
[556a9ad](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/556a9adc799a1c0512a7536ef8f7b29eb5720838) DozeSensors: only use proximity sensor if supported _(by Demon000)_  
[abff283](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/abff283194f2b3d1cbeb0620622cce7fd593d715) SystemUI: doze: add config for long press sensors that need a proximi… _(by Cosmin Tanislav)_  
[9483a24](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/9483a24b94df571d46df3678371c5724bd5b39c1) SystemUI: doze: add config for double tap sensors that need a proximi… _(by Cosmin Tanislav)_  
[8bb110a](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/8bb110ad2a1f1c9af110e84e8d40ffde2490713c) Partially revert "Assume sensors perform prox check" _(by Cosmin Tanislav)_  
[067a67b](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/067a67b48af76b90cfcb0b5e9043abb63933f9d2) SystemUI: Make isLargeScreen() use correct API for getting window met… _(by LuK1337)_  
[4a13089](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/4a130897aa5e3753fc0ba8916976aaf3e7c300fe) SystemUI: ToastUI: Fixup toast theme again _(by Ido Ben-Hur)_  
[ab96baa](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/ab96baa87dbff363c1bf5c796b53c3d6b2050fd5) toast: fix bg color not changing with theme change _(by SuperDroidBond)_  
[7b0f713](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/7b0f7138d55d5a756a456b9511c7cac157812fe7) aconfig: Use old storage if /metadata is not available _(by LuK1337)_  
[3723508](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/3723508322ac2cb8293d16a5b235296456859352) usb: Show charging notification only if power brick is disconnected _(by Adithya R)_  
[8f47ccd](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/8f47ccd84703668c2c0821c6a0c729697ddd9664) Correction in logic of roundend size calculation of SD card _(by Chetan Gurjar)_  
[04cfa0d](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/04cfa0d7227d9ee4358e4bc1ee06b0aff72bbe90) SettingsLib: Use framework resource for headline font _(by Adithya R)_  
[8922a72](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/8922a72a1679de04b13b0b4d017489c8472a9551) DisplayCutout: fully animate camera protection _(by Cosmin Tanislav)_  
[fff578c](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/fff578c2b94ea58678cfe1b059f3d477e383dc4f) fixup! Update the cutout side override doc to encourage all side over… _(by Aaron Kling)_  
[b383a13](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/b383a130e2dbda20efa9d7513c5853ad47578598) camera2: allow access to CaptureRequest.mLogicalCameraSettings _(by Cosmin Tanislav)_  
[9a410ae](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/9a410ae50ef5807de691a967b8c642bfd9e5cca3) camera: Skip HFR checks for privileged apps. _(by Sai Kumar Sanagavarapu)_  
[4bbb7f0](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/4bbb7f05c01b836c28964081b5059a65668a37ec) Camera: Skip stream size check for whitelisted apps. _(by Gaoxiang Chen)_  
[88242fc](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/88242fc3443509c06505c887f672921fdf1b63ac) camera: Support exposing aux camera to apps _(by Sauhard Pande)_  
[7ce89d2](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/7ce89d29372b780e56d96917747da3d49a418dbc) Exempt location packages from location indicators _(by Chirayu Desai)_  
[bdd313c](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/bdd313ca22ff1f0a86b8dc0a78378bf5dc82b6d7) SystemUI: Fix system animation disable checks _(by Dhina17)_  
[e4c2e5c](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/e4c2e5c945d2d3c99033690bd040b1a13e1c4c13) SystemUI: Fix the unlock sound played repeatedly _(by Shufeng Hou)_  
[a8d1cd6](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/a8d1cd6cd4ac646c8e8bddc466cbc415e7a0f27f) SystemUI: Make battery clickable again _(by Ido Ben-Hur)_  
[c06d6d2](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/c06d6d224a3195dd2e1e7deb4735b716e4512f99) QSLongPressEffect: Provide a fallback for devices with no primitives _(by Ido Ben-Hur)_  
[cda3b23](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/cda3b230fa7cf554199f3c7760e37da6140a6ab2) SystemUI: Check if primitive vibrations are supported in new quick af… _(by Fabian Leutenegger)_  
[5380307](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/53803074bf9ad75cd9e3900e577e9112e4c0e8f4) InternetDialog: Add missing setOnClickListener for data toggle _(by Pranav Vashi)_  
[13648a2](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/13648a27aefe0627739a36910010798863189fc6) SystemUI: Allow disabling QS tiles long click effect for specific tiles _(by Ido Ben-Hur)_  
[6631855](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/6631855a052072dc72ad66e8693018d0ca79b769) SystemUI: Internet tile: Allow long-pressing on mobile network _(by Michael W)_  
[b5c123d](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/b5c123d00ecfec7d67170c942079cbf5c905bd8f) SystemUI: tiles: Preload icon drawable for Modes tile _(by Pranav Vashi)_  
[2db5643](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/2db56434f1e2d51607994da9be5a8f89175a2f4e) SystemUI: Enable cast tile without Wi-Fi connection _(by nift4)_  
[2067300](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/2067300e0dce8e15f0970d25cb45f8a82f0b19ad) SystemUI: DreamTile: Enable for everyone _(by Ido Ben-Hur)_  
[2ab5762](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/2ab576243187b51864991922df6af1961fa3d18b) SystemUI: Add wifi/cell tiles _(by Pranav Vashi)_  
[a5c430e](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/a5c430efbb6bed7daa960324290ddd3173616736) SystemUI: Add VPN tile _(by Danny Baumann)_  
[261f23c](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/261f23c957c0253e6795acb1881c102fe8dec25f) SystemUI: Enable NFC tile _(by Tim Schumacher)_  
[711b525](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/711b5254b78617c0da350419bb8c8860004b47e3) SystemUI: Add reading mode tile _(by Joey)_  
[22fec7d](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/22fec7d4de737c42eb5c3f4784ef0fd582f11792) SystemUI: Add powershare QS tile _(by Linux4)_  
[9e02887](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/9e028871fce951827fafe4bf62bc380e61dc1a3e) SystemUI: Add AOD QS tile _(by Marko Man)_  
[3fa4cb7](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/3fa4cb7dde75a9b60fb85d33596a96fa88bfc6e7) SystemUI: Add USB Tether tile _(by BestPig)_  
[26d3cee](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/26d3cee29472fb9cb40da63580c7bced49d00754) SystemUI: Add AmbientDisplay tile _(by Adnan Begovic)_  
[079de49](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/079de49af4a11dc8f4d667ade12e0543d2e7f1ff) SystemUI: Add Sync tile _(by Altaf-Mahdi)_  
[afdce9f](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/afdce9f636d18b670dcbd47e6cfb311ce4ac6e7b) SystemUI: Add heads up tile _(by Michael Bestas)_  
[2ba2f45](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/2ba2f4518ca26738a3cc027ee2e1ad38d7a702c6) SystemUI: Add caffeine QS tile _(by Keith Mok)_  
[fe2060a](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/fe2060a350fccfaac4e82a7dfbf03d8f773a8b1f) SystemUI: Enable landscape lockscreen flag _(by Michael Bestas)_  
[9d11694](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/9d116944350524b1d634ac3bcdc0580bee1a0cae) SystemUI: Expose VPN icon to allow toggling _(by Bruno Martins)_  
[76c5fe3](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/76c5fe346c88a0ae933b2a8c3f549d6636fb5922) SystemUI: Bring in drawables for statusbar icon toggles _(by althafvly)_  
[2451a0a](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/2451a0aa43774110f38f4d21c1461f3d5a44cd39) SystemUI: Split status bar icon controls for vibrate and mute _(by althafvly)_  
[9c7e295](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/9c7e2955ba1b99613c5289fe274911b08832a07a) SystemUI: Status bar tuner improvements _(by Rashed Abdel-Tawab)_  
[30fd56c](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/30fd56c944cc74f28d19efa62ebf577c6f19fc27) base: Add CUSTOM metrics const. _(by Bauuuuu)_  
[d33806f](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/d33806fea7d52b5ec0a1d4329b6fba87528cd534) SystemUI: Show bluetooth battery level _(by LuK1337)_  
[d257652](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/d25765287a397afc889ba5f55905be902df79e39) core: Implement ADBRootService _(by LuK1337)_  
[1580e75](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/1580e752f907742656d8c69f37f2ea483b00f898) Fallback to global actions if assistant is not available _(by LuK1337)_  
[429edb6](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/429edb6798112158e8e23673ca0902a235044e52) SystemUI: Add support for persistent usb drive notification. _(by Adnan Begovic)_  
[c135cb8](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/c135cb8f67bc7ed21307c7e05e63bfe7bbb2738d) SystemUI: Allow snoozing SD card notification unconditionally _(by LuK1337)_  
[df61c3f](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/df61c3fccf2e331ff8bee82ac65bdf20eb1ad130) SystemUI: Allow privileged system apps to access screenshot service _(by Danny Lin)_  
[d110a76](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/d110a760c4c414ce059927b888913bd83e516d5e) core: Expose method to start assistant through Binder _(by Danny Lin)_  
[67db351](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/67db35168a5e27d98f306091e62341cdf5784967) SystemUI: handle camera launch gesture from keyhandler _(by Roman Birg)_  

## 2026-02-09
[7dacdc9](https://github.com/PixelOS-AOSP/android_vendor_custom/commit/7dacdc98a1728d9a6c5e1dc138a15e5fa84b2d76) config/version: Bump CUSTOM_PLATFORM_VERSION to 16.2 _(by inferno0230)_  

## 2026-02-08
[87bd6ab](https://github.com/PixelOS-AOSP/android_external_zstd/commit/87bd6abe8e4582a2c97f854ee80b519eb1c081d4) zstd: Android.bp: Allow rsync to add zstd compression support _(by DroidFreak32)_  
[9f0389e](https://github.com/PixelOS-AOSP/android_external_zstd/commit/9f0389ee8c43d4a7cea63e1e7717d7eb804556fb) zstd: Allow to build zstd cmdline tools _(by DroidFreak32)_  
[da0c175](https://github.com/PixelOS-AOSP/android_vendor_lineage/commit/da0c175fdd38d508adc10736921a8d4583aa6063) Merge branch 'lineage-23.2' of https://github.com/LineageOS/android_v… _(by hridaya)_  
[3ccfea1](https://github.com/PixelOS-AOSP/android_packages_services_Telephony/commit/3ccfea1ee1bee943e399522a68c7e81bece16b4b) Telephony: Migrate RadioInfo from ScrollView to NestedScrollView _(by ReallySnow)_  
[b7be3b2](https://github.com/PixelOS-AOSP/android_packages_services_Telephony/commit/b7be3b233a8f861dff356e62b0218c2c43422727) Telephony: Add ERI configuration for U.S. Cellular _(by Arne Coucheron)_  
[7ae43f0](https://github.com/PixelOS-AOSP/android_external_dng_sdk/commit/7ae43f025808d9ded31de94ad81e2818381edae1) dng_area_task: Provide backwards compatibility with legacy blobs _(by Bruno Martins)_  
[d01ed4a](https://github.com/PixelOS-AOSP/android_external_dng_sdk/commit/d01ed4a8b982ad98ae2e4c7be2fe1e42825822c2) libbng_sdk: Make it available to vendor again _(by Bruno Martins)_  
[e160982](https://github.com/PixelOS-AOSP/android_external_libjxl/commit/e160982d3890c0b2acc06f953eb23b5b4a164d3f) libjxl: Make it available to vendor _(by imranpopz)_  
[7e697f5](https://github.com/PixelOS-AOSP/android_vendor_lineage/commit/7e697f5bc94d66b8684d62125c362eae591a891b) overlay: Bring in BlackTheme overlay _(by hridaya)_  
[dfff491](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/dfff491ec6818e37d3d10a727557836fe4440279) Hide fingerprint settings help if URL is empty _(by Michael Bestas)_  
[35c5083](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/35c5083761b68ebfda96d6b05911ecd1e3ea4e1a) Settings: Show single-touch wakeup setting on rear & front fps devices _(by Terminator-J)_  
[22a48c6](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/22a48c619933795bc6104bf08777d15abe433410) Hide SFPS wakeup setting when it's not supported _(by Michael Bestas)_  
[be6c7e2](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/be6c7e2154988e35c6ce66f338d38d0f02d853df) fingerprint: Rework enrollment screen _(by Bruno Martins)_  
[31564a7](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/31564a719b7134227f8cd50a69ba13980eaff8a5) ChargingControl: Respect 24 hour locales in TimePicker _(by Georg Veichtlbauer)_  
[6446e44](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/6446e44097b79a4441b7e8a37eb1ded48d48ecea) Settings: Add charging control preferences _(by Danny Trunk)_  
[6499c91](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/6499c91ff9524282fba4ee6c4a070c247f1f4ecb) Settings: Display: Add High Touch Polling Rate Support _(by Ramii Ahmed)_  
[ba407cd](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/ba407cd92f76c1c11c569dcf522d9a8c353fa599) Settings: Add high touch sensitivity and touchscreen hovering toggles _(by LuK1337)_  
[a1e801e](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/a1e801e80c7631b7dcd2c42914273182f3440f38) Settings: Changes for LiveDisplay _(by jhenrique09)_  
[131fbdd](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/131fbdd418175c33ec5c0cb6f0b65131030ebd1b) Remove the "About phone" avatar. _(by Alex Cruz)_  
[4bf0ae5](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/4bf0ae5a1e77b61e1ed621e61b454b604e205040) Settings: Hide|disable "Phone number" from About phone information _(by kubersharma001)_  
[bf65d88](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/bf65d8883745ebe03f9c1cca90324ed0a73de2d3) Settings: Hide Flashlight _(by Michael W)_  
[cff2c05](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/cff2c05d6577fdf69108aea7f328e991dc07c270) Settings: Add toggle for heads up notifications _(by Michael Bestas)_  
[cd6bd8e](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/cd6bd8e50e132fe7170ace7f5c377f0403d9c818) Settings: Expose radio info (*#*#4636#*#*) _(by xyyx)_  
[d98a72b](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/d98a72b7d2036ad06cf5df9157f476a90d68b678) Settings: Long press to copy wifi password _(by Ido Ben-Hur)_  
[10f4da9](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/10f4da938e4a157426f30f05e27bb486bab2e1a2) Settings: Set the default account provider to Google _(by jhenrique09)_  
[18591e9](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/18591e95dfab01d7e6e2d24136fcece86211477a) Settings: make sure Wifi exists before adding controllers _(by Timi Rautamäki)_  
[37c363f](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/37c363fc01de198ca640ece0c556c5451900e899) KeyboardSettings: Add a RemotePreference for device-specific panel _(by Bruno Martins)_  
[0e72878](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/0e728789578ac6ec06faba8046910dbcee39ffd8) Settings: Good news, `encryptable=footer` is broken _(by Michael W)_  
[eb803e5](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/eb803e5d073516dd85faf728da69ee5eb752d9c0) Hide unavailable battery info _(by Michael Bestas)_  
[4f15d33](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/4f15d33565944f79f0475bb9f44b6d788133a616) Make battery cycle count configurable and enable it by default _(by Michael Bestas)_  
[2b7e366](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/2b7e366bbf6f06a5638d054f63cd206349c073bf) Settings: deviceinfo: Extend Battery info page _(by Jyotiraditya Panda)_  
[6c460ac](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/6c460ac48635f34e3a09078ce57d129d989e0ec6) Make battery info configurable and enable it by default _(by Michael Bestas)_  
[6d3a3ed](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/6d3a3ed260d124335ea5d0fefdfbc56cacc176ae) Settings: Add switch preference for AGPS _(by juwei)_  
[1a362c5](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/1a362c554af285d761f5eaa96cad44979810965d) Settings: Add preference for TouchGestures _(by Anushek Prasal)_  
[baca1e9](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/baca1e9e6c71e3a58fcf4f65b1fe0805f11062ad) Settings: Build custom-preference library _(by jhenrique09)_  
[d54d5e4](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/d54d5e4297c5b4a3a9ff6b3bfb953d292d6aed44) Settings: support black theme for dark mode _(by Jesse Chan)_  
[1a260aa](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/1a260aada8d39e255f9009282f64f8fef4ec6d99) Reapply "Settings: Protect sensitive data on the about phone" _(by althafvly)_  
[3ab0db3](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/3ab0db384ceab6197da2126a759eace8f19305d2) Settings: Switch back to udfps_enroll_enrolling_non_scroll layout _(by LuK1337)_  
[3b7e981](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/3b7e981986f63d63210595c42c5fd48e3991af63) Settings: Disable clipping in biometrics_glif_content _(by LuK1337)_  
[b610e01](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/b610e0112cd24f9f3f4862ceed47c3ce3e353f87) SlicesDatabaseHelper: Use Build.VERSION.INCREMENTAL _(by jhenrique09)_  
[1906cc9](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/1906cc97e94952ad1c4b356ca58814a8353e8c2e) Settings: fix typo in settings namespace for qr scanner on ls _(by maxwen)_  
[5a48ebf](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/5a48ebf3dd35dfe913fbdef2666d2bd13b1ee5c3) Partially revert "[Settings] Start SettingsDumpService to dump the db… _(by ExactExampl)_  
[e393737](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/e3937372a4b7053d2234dea7c0d9c1c925f79459) Biometrics: Pass halHandlesDisplayTouches to FingerprintSensorPropert… _(by Bruno Martins)_  
[fda8313](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/fda831381a4b9ea75c4e6014d085a7eca95d495a) Settings: Make SIM toggle unchangable when not supported _(by LuK1337)_  
[1c6b823](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/1c6b82325014145576496c86a13796ec0d28f7bf) BatteryTip: Hide Learn more button if URL is empty _(by Michael Bestas)_  
[44bc158](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/44bc1588ba6dd749d900e539d4725632f2f8e78e) Settings: Add option to scramble pin layout when unlocking (1/2). _(by Adnan)_  
[26a3030](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/26a30309a7feedc7373a990e13738ddd35dfb5d9) Settings: Add hotspot setting to allow VPN upstreams _(by Sam Mortimer)_  
[29221c4](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/29221c4029282d8c000c951efbcdfc7263c56e78) Settings: Add double tap to sleep preference _(by Rashed Abdel-Tawab)_  
[7144621](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/71446211bafd9ed95a9508f965ad421de464d676) Remove useless USB page header _(by Michael Bestas)_  
[c8cad51](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/c8cad51ceb25dd24f858205daa4756398439a49a) get outer NFC preference to listen for changes _(by inthewaves)_  
[0f44016](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/0f440165ecad20dee1f46489e71d3b1ded46965b) Fix inconsistent USB preference screen title _(by Danny Lin)_  
[a681ed1](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/a681ed15fe9def0f8443a9d643bde1f503bb1264) Settings: use Glif themed button bar _(by Timi Rautamäki)_  
[4d85f0b](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/4d85f0b795ba18e474b8cbcc969195618ae5af43) Settings: Hide unsupported USB modes automatically _(by Wang Han)_  
[7ebcdb2](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/7ebcdb2cda880e5aaad90068efd513ad1b9d8d11) Settings: Check if we have any color modes declared in overlay _(by Luca Stefani)_  
[d6096c2](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/d6096c2b083135af6c34277d6634cf93d834f5a3) Settings: Fix the failing strings _(by Michael Bestas)_  
[967df32](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/967df32f90c090da176ef98319c612b0dd152d48) Don't reset A2DP offload when disabling developer settings _(by Michael Bestas)_  
[a873a17](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/a873a17ecec8ba19c247741a437303487ca2efec) Display: Assign a key to color preference category _(by Bruno Martins)_  
[10b574d](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/10b574dc9f7fcbf46e234425c314f465b3c12f49) One does not simply become a Developer _(by Chirayu Desai)_  
[2542fb9](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/2542fb9e6f8caa619d9a5c5ca793648eda4c923a) Settings: Reset tether offload developer setting correctly _(by Adithya R)_  
[fa1cf60](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/fa1cf60b4d5f484a1aa1eefeec76bda44f82ca86) Add toggle to enable ADB root _(by Luca Stefani)_  
[2f8f4a0](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/2f8f4a04e46d3373c62cd8e86d28eb3cf6a0e58a) BasebandVersionPreference: Trim baseband if needed _(by Bruno Martins)_  
[f436822](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/f436822a6cc9505940635f9882d08ca930863636) ImeiInfoPreferenceController: Fix NPE _(by ExtremeXT)_  
[4feb884](https://github.com/PixelOS-AOSP/android_packages_apps_Settings/commit/4feb8846092fdbdf7ff5607c5064a43b418761e1) MainlineModuleVersionPreference: Fully hide if intent is null _(by LuK1337)_  
[d54b888](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/d54b888d9008ac44f71060fcd274e32a0bf764f5) Support for device specific key handlers _(by Bruno Martins)_  
[3353698](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/335369896515b554f16bf7a1b49dfd7bf394bfb9) Check for null callerPackage in getStorageEncryptionStatus _(by Ethan Chen)_  
[a88c77c](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/a88c77c47f2016460bedf786a0093cca9bdbeea5) Fix default values for 5G Ultra Wideband icon carrier config keys _(by Vala Zadeh)_  
[2dddf05](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/2dddf05abc3c836963e28367cb104dd3f3ccfca4) Add 5G Ultra Wideband icon carrier config keys _(by Vala Zadeh)_  
[3bd37ba](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/3bd37bacc506366fd7531b7ae71ffcb23f1a820c) GnssLocationProvider: Implement xtra-daemon toggle _(by Michael Bestas)_  
[179e9f8](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/179e9f8987361e6d0003766bc83c12542c23eaf2) GnssLocationProvider: Implement PSDS periodic download toggle _(by Michael Bestas)_  
[30f12e2](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/30f12e29dc683a74b613b36fc6c2b495a5f3c5bd) GnssLocationProvider: Disable AGPS by default, it'll be enabled in Se… _(by Chirayu Desai)_  
[a5b6565](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/a5b65650588d5662c46b22fac3767c6340003e2e) Ignore AGPS toggle during user-initiated emergency calls _(by Chirayu Desai)_  
[0e9c09d](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/0e9c09d7a32741d7f2bbe50d9a19e02dd742d7b7) Remove sensitive info from SUPL requests _(by Tommy Webb)_  
[95aa675](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/95aa675fb36270d8229a6a535b16c98a474ee61b) fw/b: Use ro.build.version.incremental to signal OTA upgrades _(by dhacker29)_  
[5b18d64](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/5b18d64e5204586bb75db60a09a2b62c958d7171) UpdateEngine: Add perf mode binder interface _(by Luca Stefani)_  
[c58893e](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/c58893e88cad6d1bb06f140d0a0c22200f02b3e9) WiredAccessoryManager: replace every non digit character _(by Francesco "Dil3mm4" Manzo)_  
[eb87e36](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/eb87e36136db4e8b47121fa87aeb734e37a298ad) WiredAccessoryManager: support for DP/HDMI display on soc:qcom,msm-ex… _(by Sai Priyanka Thirukkovela)_  
[52aa618](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/52aa618b16eba92172fd7b7c656114618ae330a8) Force using WiredAccessoryObserver for DisplayPort _(by Harold Tan)_  
[a33cc2f](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/a33cc2fd1e30ea34dfab6514528420a3b76e13b9) WiredAccessoryManager: Update stream index assignment _(by Harold Tan)_  
[8ba0071](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/8ba0071b65e8dee0f5ba4047f64c1aa279e120c7) WiredAccessoryManager: use dev index from UEventInfo to form devPath _(by Harold Tan)_  
[3ab3663](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/3ab366317fd43105be0caa080082639fd36fbca0) WiredAccessoryManager: Update display port device index _(by Aniket Kumar Lata)_  
[679c3b7](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/679c3b794d145365dad854256bd12d2617dfbfc3) WiredAccessoryManager: support for multiple display ports _(by Vignesh Kulothungan)_  
[fbb4829](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/fbb4829283a79466b615a4061115d2ff2eb2489a) audio: update WiredAccessoryManager to use ExtconUEventObserver based… _(by Dhananjay Kumar)_  
[2b55f49](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/2b55f49ae91e287dd18e16ad9f698523ae3045b8) WiredAccessoryManager: Support for multiple extconn devices _(by Haynes Mathew George)_  
[250ba6e](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/250ba6ecf2f5af535b09c106bda249929ff2dc24) WiredAccessoryManager: update extcon file paths _(by Aalique Grahame)_  
[d164b07](https://github.com/PixelOS-AOSP/android_frameworks_base/commit/d164b072a6ada7c108e0f3c7d46fda38f8401d67) WiredAccessoryManager: Add support for DisplayPort Audio _(by Revathi Uddaraju)_  

## 2026-02-07
[31b8181](https://github.com/PixelOS-AOSP/android_vendor_lineage/commit/31b818191ac5d7f5c65c92b81a16950da1e66a39) vendor: Opt out of all the fonts stuff _(by AdarshGrewal)_  
[527a039](https://github.com/PixelOS-AOSP/android_vendor_lineage/commit/527a039e5e5575e72ff6ba45272b1684170a7523) Reapply "Include GoogleSansFlex font and friends" _(by AdarshGrewal)_  

## 2026-02-04
[a1cee09](https://github.com/PixelOS-AOSP/android_vendor_lineage/commit/a1cee09ee3d35038d64b46e3b6a017e216e72500) vars: February 2026 Pixel Update _(by Nolen Johnson)_  

## 2026-02-02
[bb34413](https://github.com/PixelOS-AOSP/android_vendor_lineage/commit/bb3441306c0d1d3fca18319035eaf3965ef47449) release: Bump Security String to 2026-02-01 _(by Nolen Johnson)_  
