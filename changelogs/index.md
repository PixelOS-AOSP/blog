---
pageClass: changelogSection
---

# Changelogs

## 2025-03-26
[05ecbdc](https://github.com/PixelOS-AOSP/build_soong/commit/05ecbdc923d8777647031a495eb37b828a68cb70) fsgen: Use prebuilt_{root,any} in case install_in_root is set _(by Luca Stefani)_  
[4fd7df9](https://github.com/PixelOS-AOSP/build_soong/commit/4fd7df9ae7979a16c20706b5eeea64451047cb0a) Expand the usages of prebuilt_any in prebuilt_etc module gen _(by Jihoon Kang)_  
[82e18ed](https://github.com/PixelOS-AOSP/build_soong/commit/82e18ede838cd2e62a42fa6338eea8760c7c81fa) Add Compress_apk property to android_app_import _(by Nelson Li)_  
[963a559](https://github.com/PixelOS-AOSP/build_soong/commit/963a55904b245373d936a04f874aeb87a373b3c9) Support extract_apk in soong _(by Herbert Xue)_  
[36828d6](https://github.com/PixelOS-AOSP/build_soong/commit/36828d6c6e4f41fe82a0128c0a5e69e1a53a844b) Disallow prebuilt_root module type from setting Dsts property _(by Jihoon Kang)_  
[9be3629](https://github.com/PixelOS-AOSP/build_soong/commit/9be36297af3c584c8e84d513a47f2892842f2588) Introduce prebuilt_any module type _(by Jihoon Kang)_  
[b48bc9f](https://github.com/PixelOS-AOSP/build_soong/commit/b48bc9f97599b5c75134f7d72cfaf36046cc6f2f) Add vendor_manifest.xml to createFsGenState _(by Jihoon Kang)_  

## 2025-03-22
[5752186](https://github.com/PixelOS-AOSP/device_lineage_sepolicy/commit/575218609ceff4cd27d2a3f6b3d74f80fe28ae9f) common: Drop deprecated vendor.lineage.camera.motor _(by Michael Bestas)_  
[32bd9b0](https://github.com/PixelOS-AOSP/vendor_aosp/commit/32bd9b08139c1b1229222598915f0ac8ad09dd18) config: Drop deprecated vendor.lineage.camera.motor _(by Michael Bestas)_  
[0d5a5b9](https://github.com/PixelOS-AOSP/build/commit/0d5a5b9b4b802fe8ddc061280e1dfc3ac1f7d341) Reapply "Add tradeinmode to the system image." _(by Hridaya Prajapati)_  

## 2025-03-21
[832ea9a](https://github.com/PixelOS-AOSP/packages_apps_Updater/commit/832ea9a621ef5723ed357a41b12a11c6dc14c4de) Updater: Update gradle-generateBp to 1.22 _(by Luca Stefani)_  

## 2025-03-17
[5026b0a](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/5026b0ab8c5614f9849b1b384acfa3144b3cc527) Settings: Hide|disable "Phone number" from About phone information _(by kubersharma001)_  
[d8785c7](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/d8785c798ca863ac272bd619c5be8c8cda06887f) Revert "[Sim UI enhancement] remove the "Tap to show info"" _(by althafvly)_  
[f62dace](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/f62dace359c597504bff5a23403623df2242aacd) Settings: Remove divider from Battery Manager _(by Akash Srivastava)_  
[ad58c1d](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/ad58c1db94ef48ac8880ee89aa5b4aa3bb54741a) Add setting to allow/disallow interacting with quick settings on secu… _(by Oliver Scott)_  
[84402a4](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/84402a4c3403c7ae7cebbdbe4933ccf90712b4a5) Settings: Make SIM toggle unchangable when not supported _(by LuK1337)_  
[285488b](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/285488bd982c22fc2900084e56c1c64cb3582a6c) AppVolumeSlice: Allow querying icon of apps installed by any user _(by cjybyjk)_  
[09a6ed5](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/09a6ed5f9c1aeed6c5da0d1dc535404c84654975) Settings: support per-app volume [3/3] _(by cjybyjk)_  
[5a780b9](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/5a780b953906f97b2e0968761e48717c0365963f) Settings: Pull screen off UDFPS toggle out _(by Ido Ben-Hur)_  
[8d799c7](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/8d799c7f7d1694b37d885c5778ea884f165f458b) Settings: gestures: Improve screen-off udfps phrasing _(by timocapa)_  
[e062b4c](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/e062b4cf0be61f80eeb7a9d99f4e7cf7cc69b476) Settings: gestures: Add page for Screen-Off UDFPS _(by Cosmin Tanislav)_  
[72bb698](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/72bb6987fd8fe8b42355bb0b9ec9ceda77d121a9) Make battery info configurable and enable it by default _(by Michael Bestas)_  
[dea2e13](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/dea2e1310988507c2691c91dff2e4d178901ab05) Settings: Add missing icon for media output _(by ReallySnow)_  
[885b411](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/885b411ba1447410b1fc6d7f0103c91dc05278df) Settings: Declare an activity for WirelessDebuggingFragment _(by Ido Ben-Hur)_  
[ca3c76b](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/ca3c76bed29c4fe6e4297dd71bccd8897f2a33a3) fingerprint: hide link icon when there's no link _(by Timi Rautamäki)_  
[9e0b9f0](https://github.com/PixelOS-AOSP/frameworks_base/commit/9e0b9f0c17362c66eb1707f994f9210c46e5b186) SystemUI: Nuke oriented navbar handle _(by Ido Ben-Hur)_  
[471ca1b](https://github.com/PixelOS-AOSP/frameworks_base/commit/471ca1bd0f6084fef60a40a68c1464bd58c27000) SystemUI: Update advanced reboot icons _(by Gustavo Mendes)_  
[eb67eb7](https://github.com/PixelOS-AOSP/frameworks_base/commit/eb67eb7a050838119f7fd7b0c9d25279d48d7e42) SystemUI: Hide advanced reboot options on keyguard _(by Adithya R)_  
[44ab700](https://github.com/PixelOS-AOSP/frameworks_base/commit/44ab700d8123b592368c0ec69e78d99ef140a606) SystemUI: Make advanced reboot optional _(by Adithya R)_  
[606db19](https://github.com/PixelOS-AOSP/frameworks_base/commit/606db191b40f2ab53f764f90d55e30ce44847aa0) base: PowerMenu advanced reboot options _(by Adithya R)_  
[a406235](https://github.com/PixelOS-AOSP/frameworks_base/commit/a406235be15adc59dcaea58ea25c9f5f3418c9c4) BatteryService: Add support for oem fast charger detection _(by Alexander Martinz)_  
[6c79200](https://github.com/PixelOS-AOSP/frameworks_base/commit/6c79200ff743dd1b4e0d0260a3aff496a96aebce) SystemUI: Bump dependencies _(by dependabot[bot])_  
[b3b9633](https://github.com/PixelOS-AOSP/frameworks_base/commit/b3b9633b4331cd66783a0857fe9bf556b6bdb731) PiHooks: Update fingerprints _(by Hridaya Prajapati)_  
[6b1d6d6](https://github.com/PixelOS-AOSP/frameworks_base/commit/6b1d6d6789f8df9b9126d6c3938adffd86aa6b10) PIHooks: Add a system prop to enable debug logs _(by Adithya R)_  
[4ac0f7b](https://github.com/PixelOS-AOSP/frameworks_base/commit/4ac0f7b3cb9a3deaeba47ba8856da4b7c30a525f) PIHooks: Allow user to disable prop imitation _(by Jyotiraditya Panda)_  
[edb39dd](https://github.com/PixelOS-AOSP/frameworks_base/commit/edb39dd355e9517002dfb15822ba37eab989db3c) PIHooks: Simplify tablet spoofing _(by bheatleyyy)_  
[ddfddc0](https://github.com/PixelOS-AOSP/frameworks_base/commit/ddfddc0e3e90e59437e4600339ac8f33e99a1234) PIHooks: Refactor _(by basamaryan)_  
[26fdcc9](https://github.com/PixelOS-AOSP/frameworks_base/commit/26fdcc999fbaa0677fb7786abeed40a908d5d85d) PIHooks: Set HARDWARE, ID values _(by someone5678)_  
[266eea0](https://github.com/PixelOS-AOSP/frameworks_base/commit/266eea08c9217746ad7849a3d585729663a2a995) PIHooks: Drop GBoard spoofing _(by basamaryan)_  
[2020e19](https://github.com/PixelOS-AOSP/frameworks_base/commit/2020e19cb6de6f4deed02ce3d96bc15bef2af24c) PIHooks: Spoof as Pixel Tab for tablets _(by saikiran2001)_  
[78758df](https://github.com/PixelOS-AOSP/frameworks_base/commit/78758df3c637b85cbb33fafd378b20332c53fcee) PIHooks: Spoof more Google apps _(by PainKiller3)_  
[80be872](https://github.com/PixelOS-AOSP/frameworks_base/commit/80be872a64e9bca90d9536e53d0a7a9a9cb88dda) PIHooks: Spoof Pixel 8 Pro to some Google apps _(by Adithya R)_  
[09acebd](https://github.com/PixelOS-AOSP/frameworks_base/commit/09acebd270eaf717a01591b4adba03b296ec32a9) PIHooks: Spoof more gapps and google photos _(by Adithya R)_  
[d480ba4](https://github.com/PixelOS-AOSP/frameworks_base/commit/d480ba4900628e9c59f2c6e7361c1945a29746c2) PIHooks: Make it a hidden API _(by Adithya R)_  
[826dcce](https://github.com/PixelOS-AOSP/frameworks_base/commit/826dcced49c9ef0706f034d8e271ae563131e0d3) PIHooks: Set system props for native hook _(by Adithya R)_  
[040565d](https://github.com/PixelOS-AOSP/frameworks_base/commit/040565d46600fb91d5c1bd0e8d18009597dc5baf) PIHooks: Get resources from context _(by Adithya R)_  
[afee27f](https://github.com/PixelOS-AOSP/frameworks_base/commit/afee27fe6070f191bb87e16bdb693aa8e7ee7c23) PIHooks: Allow setting any field in certified build props _(by Adithya R)_  
[01cc296](https://github.com/PixelOS-AOSP/frameworks_base/commit/01cc296182347a23d64919d1d91b3b9631061e87) Introduce PropImitationHooks _(by Omkar Chandorkar)_  
[fcbb668](https://github.com/PixelOS-AOSP/frameworks_base/commit/fcbb66837d3416069234af025d9bda79ef33c035) SystemUI: VolumeDialog: Fix per-app volume on secondary users _(by Dhina17)_  
[7b9e37a](https://github.com/PixelOS-AOSP/frameworks_base/commit/7b9e37a19510a6f1e7ff6cc37acad9bd87278770) SystemUI: Update per-app volume icon _(by yukiscape)_  
[1b14a0d](https://github.com/PixelOS-AOSP/frameworks_base/commit/1b14a0da3a905754fd4e770b944477ccf1a8a632) base: make per-app work with multi audio focus _(by El Dainosor)_  
[ed452bd](https://github.com/PixelOS-AOSP/frameworks_base/commit/ed452bd5f9aacf8fdc48b06e8089f7a558bacb6b) base: support per-app volume [2/3] _(by cjybyjk)_  
[a880265](https://github.com/PixelOS-AOSP/frameworks_base/commit/a880265a3bbffd3035abdfc3ff4246f49c855481) SystemUI: volume dialog: Align padding/margin for left and right _(by Arian)_  
[fa6a092](https://github.com/PixelOS-AOSP/frameworks_base/commit/fa6a0929c74b9b05c3aa83de561e3b4824ebfcaf) VolumeDialogImpl: Handle the outmost row with respect to left gravity _(by Arian)_  
[dfb7eb2](https://github.com/PixelOS-AOSP/frameworks_base/commit/dfb7eb27576ca5616f13161ef748ff35c1409a00) VolumeDialogImpl: Respect left gravity in ringer drawer _(by Arian)_  
[bc68787](https://github.com/PixelOS-AOSP/frameworks_base/commit/bc687876f54875078168e11f07dfddfa3b2a7864) VolumeDialogImpl: Set touchable region properly for left gravity _(by Arian)_  
[d2c4f77](https://github.com/PixelOS-AOSP/frameworks_base/commit/d2c4f77b54e11c519b0251fa7c9cc64953fad02b) VolumeDialogImpl: Drop unnecessary layout gravity defines and handle … _(by Arian)_  
[25556e4](https://github.com/PixelOS-AOSP/frameworks_base/commit/25556e4b617cbd4f928f9627b1cd8240e9323fe5) VolumeDialogImpl: Fix cut layout when on setup or lock task mode _(by jhenrique09)_  
[4160a1c](https://github.com/PixelOS-AOSP/frameworks_base/commit/4160a1c6557132beb5c8babc3a245672e2e44247) VolumeDialogImpl: Don't vibrate when volume dialog is not visible _(by LuK1337)_  
[d6b46f5](https://github.com/PixelOS-AOSP/frameworks_base/commit/d6b46f59160b4748e24a32c8fa3d583f87d21cf4) SystemUI: Fix up large clock top margin with pixel-fw _(by Pranav Vashi)_  
[bf9930c](https://github.com/PixelOS-AOSP/frameworks_base/commit/bf9930ccdcb4843b9570b434901cac452b6a9d2d) SystemUI: Fix smartspace layout _(by Pranav Vashi)_  
[ee1fa91](https://github.com/PixelOS-AOSP/frameworks_base/commit/ee1fa912b83d5aeafc5a0fe6bb3e40456e01373a) SystemUI: SmartspaceSection: Build decoupled views only when required _(by Pranav Vashi)_  
[b1f610d](https://github.com/PixelOS-AOSP/frameworks_base/commit/b1f610dd3d2459fa4e028f9179dcc827da3989b3) SystemUI: Grant additional permissions for smartspace _(by Andrzej Perczak)_  
[3659d9c](https://github.com/PixelOS-AOSP/frameworks_base/commit/3659d9c702b786278523b6a44e1b5d11ea0588f0) SystemUI: Adapt Smartspace A15-QPR1 _(by clarencelol)_  
[c57e3ca](https://github.com/PixelOS-AOSP/frameworks_base/commit/c57e3caf5ea6272c0a219a490bfabe9bb430f360) SystemUI: smartspace: Adapt for 14 QPR2 _(by aswin7469)_  
[97d9cef](https://github.com/PixelOS-AOSP/frameworks_base/commit/97d9cef15a84dac6fbac7e6efb0d483a60713179) SystemUI: Implement Reverse-engineered Smartspace _(by Daniel Jacob Chittoor)_  
[ab8aaa0](https://github.com/PixelOS-AOSP/frameworks_base/commit/ab8aaa0d7a276a595e65ea86269d8ff728ec54e8) BrightnessUtils: Conditionally disable gamma conversion for brightnes… _(by SagarMakhar)_  
[4acb6ab](https://github.com/PixelOS-AOSP/frameworks_base/commit/4acb6ab195b4f836babe11c0f90445cfe3331047) SystemUI: Turn on the display briefly when resuming AOD _(by Adithya R)_  
[5db6f6e](https://github.com/PixelOS-AOSP/frameworks_base/commit/5db6f6e35b5004394871b97fdfa47f78753722d3) SystemUI: Disable animations during biometric wake-and-unlock _(by Adithya R)_  
[1856ca4](https://github.com/PixelOS-AOSP/frameworks_base/commit/1856ca40cf1b7cbbbc4ef2dafd32761b52fc1aca) SystemUI: React to PrivacyConfig changes properly _(by Tommy Webb)_  
[eba53c4](https://github.com/PixelOS-AOSP/frameworks_base/commit/eba53c445be4f6a966ddeb6cfc292bf838e3f7a9) Catch BadParcelableException when checking extras _(by Luca Stefani)_  
[2835e7a](https://github.com/PixelOS-AOSP/frameworks_base/commit/2835e7a6cde91a677474560d3f1b2b62f1734db6) SettingsProvider: aconfig: do not error on missing flag files _(by Aaron Kling)_  
[0b22c98](https://github.com/PixelOS-AOSP/frameworks_base/commit/0b22c98e6828d37edf22cb55d26294fd2c70bb4a) pm: aconfig: do not error on missing flag files _(by Thomas Makin)_  
[a0e958b](https://github.com/PixelOS-AOSP/frameworks_base/commit/a0e958b1f304d0588c02c6ad036219fa63ac79ad) ExifInterface: do not spam stacktrace on invalid format _(by Thomas Makin)_  
[5dafdcd](https://github.com/PixelOS-AOSP/frameworks_base/commit/5dafdcd0cd8e42105719f9093299542a15b7c594) core: PinSet: Fixup and improve algorithms caching _(by jhonboy121)_  
[85e4b67](https://github.com/PixelOS-AOSP/frameworks_base/commit/85e4b67d8ac2283f3c271791af87d5aa3fd492be) Cache pin algorithms in PinSet _(by Till Kottmann)_  
[a0b2143](https://github.com/PixelOS-AOSP/frameworks_base/commit/a0b214379ea2d8a53acd30d96ceacde71c0d77fd) Cache KeyStoreService _(by Till Kottmann)_  
[7a4914e](https://github.com/PixelOS-AOSP/frameworks_base/commit/7a4914e62c8e9258e40ebc62bae6013e017c2667) (Point) Only calculate sin and cos once _(by Till Kottmann)_  
[3fa4b1d](https://github.com/PixelOS-AOSP/frameworks_base/commit/3fa4b1dcf07c4d980a27472e2cc8a11948eb2fbc) SystemUI: CastTile: Open cast settings on long click _(by Ido Ben-Hur)_  
[09851fe](https://github.com/PixelOS-AOSP/frameworks_base/commit/09851fe70d12c98e59f323c9d06a23450d497cba) FingerprintUtils: Migrate old fp config xml to new one on HIDL/AIDL s… _(by Luofan Chen)_  
[2c3f30b](https://github.com/PixelOS-AOSP/frameworks_base/commit/2c3f30b3c3d79208fb3a289adadc262c4d510955) JobScheduler: Respect allow-in-power-save perm _(by Tommy Webb)_  
[590648e](https://github.com/PixelOS-AOSP/frameworks_base/commit/590648e5819f18f6b817457a09fb6b6b0dc07307) SystemUI: Check whether the selected WFD route is available _(by Weijie Wang)_  
[2167c4e](https://github.com/PixelOS-AOSP/frameworks_base/commit/2167c4e29388b69fca48530dfdcdecb88b560d4f) camera2: allow access to CaptureRequest.mLogicalCameraSettings _(by Cosmin Tanislav)_  
[b6f416b](https://github.com/PixelOS-AOSP/frameworks_base/commit/b6f416b8488582d6d8edff8b9b09dc8c97b0a29c) base: Export bodyFontFamily and bodyFontFamilyMedium symbols _(by Pranav Vashi)_  
[474be30](https://github.com/PixelOS-AOSP/frameworks_base/commit/474be302b25672bcdfc3e7d4b01a6e0240295674) CachedAppOptimizer : Pageout File pages during system compaction _(by Divyanand Rangu)_  
[2bff28d](https://github.com/PixelOS-AOSP/frameworks_base/commit/2bff28ddaa0155b570b9e65323afba0454b2dfb7) webkit: SystemImpl: Make systemIsDebuggable() check IS_ENG as well _(by LuK1337)_  
[055ca84](https://github.com/PixelOS-AOSP/frameworks_base/commit/055ca84e6698d3b2f634f4d10577bed417be86da) SystemUI: Fix QS customizer corner radius _(by Pranav Vashi)_  
[5cbc8cc](https://github.com/PixelOS-AOSP/frameworks_base/commit/5cbc8ccb85e5418d91ce11671787e1a33c26663f) SystemUI: Fix burn-in translations not applying to keyguard slices _(by Andy CrossGate Yan)_  
[1a71429](https://github.com/PixelOS-AOSP/frameworks_base/commit/1a71429000470daf30252b58c80e9737b2d4fb8b) BluetoothControllerImpl: Optimize connected battery level scanning _(by minaripenguin)_  
[7a86e6c](https://github.com/PixelOS-AOSP/frameworks_base/commit/7a86e6cad613b9e82a0b9790f0a9383296c91c04) BluetoothControllerImpl: fetch battery level from any device _(by jhonboy121)_  
[6d7df3b](https://github.com/PixelOS-AOSP/frameworks_base/commit/6d7df3b41c66ffd47288d3c1482abceff34e0f0a) BluetoothControllerImpl: Synchronize mConnectedDevices access _(by jhonboy121)_  
[f359bb0](https://github.com/PixelOS-AOSP/frameworks_base/commit/f359bb094f80517dae674b640ea082d0aa39767d) Revert "AudioService: do not log sound effects in audio dumpsys" _(by jro1979oliver)_  
[0c0ab94](https://github.com/PixelOS-AOSP/frameworks_base/commit/0c0ab94c504a631f847de02b605867d0410e1fee) SystemUI: Fix Internet Tile showing no service _(by Tommy Webb)_  
[c01d54a](https://github.com/PixelOS-AOSP/frameworks_base/commit/c01d54a23d3993143ba4261e46aa1b2ad02357a4) SystemUI: require unlocking to use QS tiles _(by Dmitry Muhomor)_  
[43a53df](https://github.com/PixelOS-AOSP/frameworks_base/commit/43a53df177c0844681fd776dda9a9b2d8b73c838) SystemUI: Add DOUBLE_TAP_TO_WAKE to tuner service reset exceptions _(by LuK1337)_  
[3007e63](https://github.com/PixelOS-AOSP/frameworks_base/commit/3007e632e0a52878f5311d4323d5828e5a379cb4) SystemUI: Constrain keyguard indication area burn-in offset _(by Adithya R)_  
[a723fb8](https://github.com/PixelOS-AOSP/frameworks_base/commit/a723fb850ba72c57968d998af70239629b8177cb) fixup! Add setting to allow/disallow interacting with quick _(by Dhina17)_  
[7bf4590](https://github.com/PixelOS-AOSP/frameworks_base/commit/7bf4590ec5a402ea44f5e139c524bdd6722dda0a) Add setting to allow/disallow interacting with quick settings on secu… _(by Oliver Scott)_  
[32fe5a5](https://github.com/PixelOS-AOSP/frameworks_base/commit/32fe5a5e037e4ad3d45465405ab549a17d910916) SystemUI: Don't remove keyguard slice view _(by LuK1337)_  
[4d2c339](https://github.com/PixelOS-AOSP/frameworks_base/commit/4d2c33917e72cd6b1e11a23a7058fd324d49781f) SystemUI: Fix constraints for keyguard slice view _(by LuK1337)_  
[f9acafc](https://github.com/PixelOS-AOSP/frameworks_base/commit/f9acafc5be65d597370c37da30310a9e7d2963cb) FlashlightStrengthTile: Move torch strength percentage to description _(by Hridaya Prajapati)_  
[1e294e9](https://github.com/PixelOS-AOSP/frameworks_base/commit/1e294e912e8f1e253160023fe6bcdac975fd9db3) FlashlightStrengthTile: Update bg color only if supports flash streng… _(by Dhina17)_  
[c54a48f](https://github.com/PixelOS-AOSP/frameworks_base/commit/c54a48f9a727cd28d1e440620da860cfd397d400) SliderQSTileView: Pass the SlideableQSTile interface itself _(by Dhina17)_  
[77cca82](https://github.com/PixelOS-AOSP/frameworks_base/commit/77cca82df3d550f40759ba0d852a33b7cb0a7d88) FlashlightStrengthTile: TouchableQSTile -> SlideableQSTile _(by Dhina17)_  
[5189e5d](https://github.com/PixelOS-AOSP/frameworks_base/commit/5189e5d8369ad2e27bc2d0d1acd27419f7de7142) SystemUI: Fix flashlight strength tile in secondary user _(by Adithya R)_  
[99909ba](https://github.com/PixelOS-AOSP/frameworks_base/commit/99909ba290c27a20f39e25bdc73aabc9cc5a2f9f) FlashlightStrengthTile: Do NOT leak CameraManager TorchCallback _(by Ido Ben-Hur)_  
[216e2a1](https://github.com/PixelOS-AOSP/frameworks_base/commit/216e2a1d3ef8c3845f5c09d4c06ee3f43cf0475e) SystemUI: Introduce Flashlight Strength Tile _(by Anay Wadhera)_  
[efd9883](https://github.com/PixelOS-AOSP/frameworks_base/commit/efd988306b274b157e3b4799979d9b656ac3d8fd) OplusTypeCastingHelper: update stub _(by arnodorian-r)_  
[58ce426](https://github.com/PixelOS-AOSP/frameworks_base/commit/58ce426d05a0c135bac967bfd281a93ccc490241) Add some fwb stubs from Oplus _(by DennySPb)_  
[9de25ec](https://github.com/PixelOS-AOSP/frameworks_base/commit/9de25eccc8e824fbc35eecd359c8fa807a7f2aff) core: Expose method to toggle recent apps through Binder _(by someone5678)_  
[eab4166](https://github.com/PixelOS-AOSP/frameworks_base/commit/eab416643dc7dd3e86201e159db6d2748d8417ac) SystemUI: Update UdfpsTouchOverlay sensorRect on updating overlay params _(by Dhina17)_  
[e00d4fe](https://github.com/PixelOS-AOSP/frameworks_base/commit/e00d4fe00980a1f6a1239408248ec4d7692795fa) Biometrics: Allow disabling of fingerprint cleanups _(by jhenrique09)_  
[505a57b](https://github.com/PixelOS-AOSP/frameworks_base/commit/505a57bad0a4c0929c8643431890870fbac3168c) LayoutInflater: Opportunistically create views directly for performance _(by Danny Lin)_  
[de17498](https://github.com/PixelOS-AOSP/frameworks_base/commit/de17498966d687ec9e3f28fdf49038a9bde0c892) Textutils: Optimize writeToParcel for performance _(by minaripenguin)_  
[1b51191](https://github.com/PixelOS-AOSP/frameworks_base/commit/1b511914bf6a8a51410c8ed27695ab6467ae94b8) EventLog: Optimize writeEventArray for performance _(by minaripenguin)_  
[bcb021c](https://github.com/PixelOS-AOSP/frameworks_base/commit/bcb021cddadb7fe3b13d1d7fdd5738e2b785ef95) SystemServiceRegistry: Replace ArrayMap with HashMap for performance _(by Danny Lin)_  
[5cb5ace](https://github.com/PixelOS-AOSP/frameworks_base/commit/5cb5ace1ace0a6b45f11c3e5da2d75136110bdc5) ThemedResourceCache: Replace ArrayMap with HashMap for performance _(by Danny Lin)_  
[61e9a71](https://github.com/PixelOS-AOSP/frameworks_base/commit/61e9a716b7ac4fc2ecdbd6437f100b89ef34f225) SettingsLib: Migrate MainSwitchPreference to Material3 _(by Bruno Martins)_  
[705fc6f](https://github.com/PixelOS-AOSP/frameworks_base/commit/705fc6f6078e618564dbd2d2029f23e6bfca8fd6) Correction in logic of roundend size calculation of SD card _(by Chetan Gurjar)_  
[3da38dd](https://github.com/PixelOS-AOSP/frameworks_base/commit/3da38dd995d7320231c7b9a2efc2ef3227e2d182) SQLiteDatabase: Catch corrupt exception during transaction _(by muzbit.kim)_  
[3917ee4](https://github.com/PixelOS-AOSP/frameworks_base/commit/3917ee4dd4fecd7b9c43d458ece440cdfb6cc430) SQLite: Do integrity_check only once _(by yi.jang)_  
[5f5f5cc](https://github.com/PixelOS-AOSP/frameworks_base/commit/5f5f5cca8f58d5b478434ef6a24f299567791d52) SystemUI: Fix double unlock sound issue _(by timjosten)_  
[4335285](https://github.com/PixelOS-AOSP/frameworks_base/commit/433528572cf3362f9f5cbd69aa2c0840f58782f1) Use getPackagesForOps instead of iterating packages by checkOperation _(by yinwei.sun1)_  
[57e7d35](https://github.com/PixelOS-AOSP/frameworks_base/commit/57e7d358a4bbfafd443c24a510c63bd914af73c2) Set alert dialog message to use system font _(by maxwen)_  
[b76b27c](https://github.com/PixelOS-AOSP/frameworks_base/commit/b76b27c45dcd1b400533d248e1936ddab9480340) pm: actually check fs verity support _(by Thomas Makin)_  
[f2a4efe](https://github.com/PixelOS-AOSP/frameworks_base/commit/f2a4efe6ab54f6f06d6a5db31d837ebe7bfb6f46) Don't fail setDeviceConnectionState if not implemented in hal _(by Aaron Kling)_  
[1532914](https://github.com/PixelOS-AOSP/frameworks_base/commit/15329146453c14e6f6f1044126d5526438798105) SystemUI: Use AVCProfileMain for screen recorder _(by Arne Coucheron)_  
[e94b487](https://github.com/PixelOS-AOSP/frameworks_base/commit/e94b487ebd50f1a7929da2a0a99ff519a6cd2ff8) power: Keep file scheme when not using content URI _(by Han Wang)_  
[c98fe48](https://github.com/PixelOS-AOSP/frameworks_base/commit/c98fe4848dbd6a43eb4a69deb5dca843e6d9f755) SystemUI: Redraw display cutout on overlay changes _(by Adithya R)_  
[1f15567](https://github.com/PixelOS-AOSP/frameworks_base/commit/1f15567b4ffeb7af0b288a09ab56d1815d8078ce) SystemUI: Let screenshot window ignore screen decorations _(by LuK1337)_  
[c883cce](https://github.com/PixelOS-AOSP/frameworks_base/commit/c883cce5c2fc4d6ff68d32064538d416527efad2) SystemUI: screenshot: close QS after launching long screenshot activity _(by LuK1337)_  
[ab28f1a](https://github.com/PixelOS-AOSP/frameworks_base/commit/ab28f1aad302186f016b6f33f240da9501e755f2) SystemUI: screenshot: disable magnification for partial screenshots _(by Cosmin Tanislav)_  
[d1bfb57](https://github.com/PixelOS-AOSP/frameworks_base/commit/d1bfb57e3039800774f40559dc561779e48e3e43) SystemUI: screenshot: add extra crop boundaries _(by Cosmin Tanislav)_  
[b86084b](https://github.com/PixelOS-AOSP/frameworks_base/commit/b86084bbb1576f4a6852ebb82d3bef9b2c95d9e0) SystemUI: screenshot: remove duplicate clamping on move action _(by Cosmin Tanislav)_  
[194f1dd](https://github.com/PixelOS-AOSP/frameworks_base/commit/194f1ddc4698873b801c9522b1b981c91deb2c14) SystemUI: screenshot: open long screenshot activity for partial scree… _(by Cosmin Tanislav)_  
[1739298](https://github.com/PixelOS-AOSP/frameworks_base/commit/17392986e3e94e864bf592279bcc6b195e0f5957) Implement click to take partial screenshot [1/3] _(by Jesse Chan)_  
[3e35911](https://github.com/PixelOS-AOSP/frameworks_base/commit/3e35911786d1f9061327402e313d9997fcba7240) SystemUI: screenshot: Add delete action chip intent _(by ganeshi4u)_  
[543e28f](https://github.com/PixelOS-AOSP/frameworks_base/commit/543e28fdba42dffab74b3efe5ada352748870943) base: Allow disabling turbulence noise after clicking the play button _(by Ido Ben-Hur)_  
[f08ba2a](https://github.com/PixelOS-AOSP/frameworks_base/commit/f08ba2a5d0a2ea48785746d4322a36a0e009f714) SystemUI: screenshot: Hide action chips text labels _(by Ido Ben-Hur)_  
[92fcc6e](https://github.com/PixelOS-AOSP/frameworks_base/commit/92fcc6eff15588671119518653794f7108fcac6d) SystemUI: Dismiss screenshot window on touch outside _(by LibXZR)_  
[c464905](https://github.com/PixelOS-AOSP/frameworks_base/commit/c464905071aa6581cc42806f9f96d88b75899441) SystemUI: Reduce screenshot dismiss delay to 3 seconds _(by Danny Lin)_  
[7a3ef2d](https://github.com/PixelOS-AOSP/frameworks_base/commit/7a3ef2d51ae75e631991bd75ce70d709d459034e) SystemUI: Cleanup screenshot sound/vibration logic _(by Adithya R)_  
[e0f1be5](https://github.com/PixelOS-AOSP/frameworks_base/commit/e0f1be5706d7f4ba28b8443243c50cda0be63bf8) SystemUI: Adapt screenshot sound to ringer modes _(by Ashwin R C)_  
[84f2392](https://github.com/PixelOS-AOSP/vendor_aosp/commit/84f2392347227f4ef42859ccb822de93fc975ad6) soong: Add camera package name flag _(by Jake Weinstein)_  
[42b90e8](https://github.com/PixelOS-AOSP/vendor_aosp/commit/42b90e86f3ef7dbe442d20135b60505421bb0436) Revert "soong: Add TARGET_USES_OPLUS_CAMERA" _(by Hridaya Prajapati)_  
[3d06251](https://github.com/PixelOS-AOSP/vendor_aosp/commit/3d0625198bc440299fc0610cec6c447707985d5a) Revert "soong: Add TARGET_USES_NOTHING_CAMERA" _(by Hridaya Prajapati)_  
[0122777](https://github.com/PixelOS-AOSP/vendor_aosp/commit/0122777ba27080b729b50633726ef4042d92c883) soong: Remove LD_SHIM_LIBS support _(by LuK1337)_  
[b43e5bd](https://github.com/PixelOS-AOSP/vendor_aosp/commit/b43e5bd6fcac5a77ea778ac2ef1346d4146a23d3) envsetup.sh: Always use AOSP latest clang version _(by micky387)_  
[2ea1489](https://github.com/PixelOS-AOSP/vendor_aosp/commit/2ea1489eb23a16a08a38ad53977b4bcae84a4a41) release: Enable screen_off_unlock_udfps _(by Michael Bestas)_  
[ed84418](https://github.com/PixelOS-AOSP/vendor_aosp/commit/ed84418e701cd3a732621843c40a23b484da9b0f) release: Bump aconfig flags extension to BP1A _(by Michael Bestas)_  
[7a84ed5](https://github.com/PixelOS-AOSP/vendor_aosp/commit/7a84ed5fdd148ce7556e9827172236b90f7a9ae4) tablet: Enable desktop windowing mode _(by Yumi Yukimura)_  
[a1fbb91](https://github.com/PixelOS-AOSP/vendor_aosp/commit/a1fbb91316f775a946001294b2d3179df8ef7ff6) overlay: tablet: Enable communal service _(by Yumi Yukimura)_  
[917c958](https://github.com/PixelOS-AOSP/vendor_aosp/commit/917c958498f657068e6e166a9c911ba98edff7b8) config: tablet: Include tablet-specific overlay _(by Yumi Yukimura)_  

## 2025-03-16
[2d04d49](https://github.com/PixelOS-AOSP/frameworks_native/commit/2d04d49763a268234a4c2bf21b55d4cd8e48ad62) fixup! surfaceflinger: Add support for Udfps extension lib _(by LuK1337)_  
[6affb2c](https://github.com/PixelOS-AOSP/device_lineage_sepolicy/commit/6affb2c19ca8dd56332870c68d7c6bf3e64d58b4) common: private: Allow tombstoned to read custom version prop _(by Hridaya Prajapati)_  

## 2025-03-15
[07f25e5](https://github.com/PixelOS-AOSP/frameworks_av/commit/07f25e5d45f766b6cdec0d11a6a2bb90f5ebdd36) libcameraservice: Add support to set vendor tag with client package name _(by cjh1249131356)_  
[7140829](https://github.com/PixelOS-AOSP/frameworks_av/commit/7140829f8bec1aafb4f2238142744b6f88f72376) Revert "libcameraservice: Add support to set vendor tag with client p… _(by Hridaya Prajapati)_  
[97a8ce9](https://github.com/PixelOS-AOSP/frameworks_base/commit/97a8ce98db121cf1d632a834de515e3a9f1755e7) base: Rework lock gesture feature _(by cjh1249131356)_  
[58e0b90](https://github.com/PixelOS-AOSP/frameworks_base/commit/58e0b90100e8bd4958e5b1156e8cb1e0e450f5e9) fixup! base: Add support for window ignore secure [1/2] _(by someone5678)_  
[fc8dfb3](https://github.com/PixelOS-AOSP/frameworks_base/commit/fc8dfb335b4913c24c9c806d2b7f45a0af47df01) base: Add support for window ignore secure [1/2] _(by LibXZR)_  
[d804bf0](https://github.com/PixelOS-AOSP/frameworks_base/commit/d804bf073f89b16251a079aa445ea98316544150) SurfaceControl: add more window types to consider NoVote _(by Omkar Chandorkar)_  
[f879295](https://github.com/PixelOS-AOSP/frameworks_base/commit/f87929579eda4b067f37eb8e7c4495836306f065) Make default permissions updates tied to version incremental _(by Luca Stefani)_  
[b3903b0](https://github.com/PixelOS-AOSP/frameworks_base/commit/b3903b0632c5dc960be7a987629f6ded23c9d6f7) SystemUI: Add support for udfps dim layer _(by pjgowtham)_  
[b27dc2e](https://github.com/PixelOS-AOSP/frameworks_base/commit/b27dc2e49a5e4b1a5c2dd5074cff2bfce15bfa28) udfps: Make pressed udfps view configurable _(by TheScarastic)_  
[8e933c3](https://github.com/PixelOS-AOSP/frameworks_base/commit/8e933c3ab7ba9e26eb1f08f0da1fe312225a0208) udfps: Restore illumination dot for global hbm _(by Arian)_  
[6324639](https://github.com/PixelOS-AOSP/frameworks_base/commit/6324639e471b60662d05ea841a0aec8f28a57e70) WiredAccessoryManager: support for DP/HDMI display on soc:qcom,msm-ex… _(by Sai Priyanka Thirukkovela)_  
[8c8b76b](https://github.com/PixelOS-AOSP/frameworks_base/commit/8c8b76bbb7a73f44a4ce8ae4d9aaf6d419014b4d) Force using WiredAccessoryObserver for DisplayPort _(by Harold Tan)_  
[b061fa1](https://github.com/PixelOS-AOSP/frameworks_base/commit/b061fa144221f39576130eb172e312f27fb7c77e) WiredAccessoryManager: Update stream index assignment _(by Harold Tan)_  
[a7c1c6d](https://github.com/PixelOS-AOSP/frameworks_base/commit/a7c1c6da486cf00e13cbcaaa0283867d3d44dda8) WiredAccessoryManager: use dev index from UEventInfo to form devPath _(by Harold Tan)_  
[9a6fcde](https://github.com/PixelOS-AOSP/frameworks_base/commit/9a6fcdef41b65c3cb50a6194ec565c2b61f3f89d) WiredAccessoryManager: Update display port device index _(by Aniket Kumar Lata)_  
[bd68e59](https://github.com/PixelOS-AOSP/frameworks_base/commit/bd68e59369dd65ba9579d48a568a2f4a9c310c2e) WiredAccessoryManager: support for multiple display ports _(by Vignesh Kulothungan)_  
[625cf69](https://github.com/PixelOS-AOSP/frameworks_base/commit/625cf692beed91547f31f73dca94d9b1d9010f4d) audio: update WiredAccessoryManager to use ExtconUEventObserver based… _(by Dhananjay Kumar)_  
[81f1bed](https://github.com/PixelOS-AOSP/frameworks_base/commit/81f1bed7bab86dc3250ff23311a377f1845f2259) WiredAccessoryManager: Support for multiple extconn devices _(by Haynes Mathew George)_  
[28a437a](https://github.com/PixelOS-AOSP/frameworks_base/commit/28a437a0b1770d0367c94214d02006b3db47551a) WiredAccessoryManager: update extcon file paths _(by Aalique Grahame)_  
[1de19b4](https://github.com/PixelOS-AOSP/frameworks_base/commit/1de19b4d91be954045c1d99aa67aa1f8a69b1ceb) WiredAccessoryManager: Add support for DisplayPort Audio _(by Revathi Uddaraju)_  
[94b4742](https://github.com/PixelOS-AOSP/frameworks_base/commit/94b4742d1c85f53f81d166c950704cda6d6f9903) WifiDisplayController: handle preexisting p2p connection status _(by Li Sun)_  
[faaf862](https://github.com/PixelOS-AOSP/frameworks_base/commit/faaf862abab94989c0336165f3077a1e71d08bbc) Merge changes for launching wifidisplay from system settings _(by Indranil Chakraborty)_  
[5583a9d](https://github.com/PixelOS-AOSP/frameworks_base/commit/5583a9de9a3e11980b699727413d3964a49c9959) fixup! ThemeOverlayController: Ensure we always disable the neutral o… _(by Luca Stefani)_  
[da976a5](https://github.com/PixelOS-AOSP/frameworks_base/commit/da976a5d8c51966ee2d7c973a4e018bd10c4acc6) ThemeOverlayController: Ensure we always disable the neutral overlay _(by Pranav Vashi)_  
[eaa1504](https://github.com/PixelOS-AOSP/frameworks_base/commit/eaa150477dbb1e3d976fee6d368d1224b563dda8) ThemeOverlayController: Don't enable neutral overlay when we use dark bg _(by Ido Ben-Hur)_  
[7737d56](https://github.com/PixelOS-AOSP/frameworks_base/commit/7737d5698e11be9f811b16e9698d7ec5d4923a82) BiometricScheduler: Cancel operation if not idle _(by SagarMakhar)_  
[9d9d85c](https://github.com/PixelOS-AOSP/frameworks_base/commit/9d9d85c6074d271bb1f82e5d5a065d57c271617c) SystemUI: Implement bouncer face unlock animation _(by minaripenguin)_  
[9587353](https://github.com/PixelOS-AOSP/frameworks_base/commit/95873532a37cdd8fd6313b798a3a2d31616c663b) SystemUI: biometrics: Follow user setting to confirm face unlock _(by Pranav Vashi)_  
[dde0a82](https://github.com/PixelOS-AOSP/frameworks_base/commit/dde0a820456256bc6c6b7cb937d769a1a697cd2b) SystemUI: Use proper tint for face unlock icon _(by Pranav Vashi)_  
[1f789c8](https://github.com/PixelOS-AOSP/frameworks_base/commit/1f789c8c75ded282194294c6a67a1bfdb5f1cae4) SystemUI: Implement face unlock recognition animation and text _(by minaripenguin)_  
[406c90b](https://github.com/PixelOS-AOSP/frameworks_base/commit/406c90b9ca09b54c2ec3e2b184776b46370a7671) SystemUI: Disable FaceUnlock Lockouts _(by minaripenguin)_  
[1f939e6](https://github.com/PixelOS-AOSP/frameworks_base/commit/1f939e6e93441ce39073e2febd587f4fcef0dfe0) services: Force load FaceSense providers _(by Pranav Vashi)_  
[6c846a9](https://github.com/PixelOS-AOSP/frameworks_base/commit/6c846a936639acd8a02479e81fe36e1cea6f833c) FaceSense: Vibrate on successful authentication _(by Adithya R)_  
[6d38846](https://github.com/PixelOS-AOSP/frameworks_base/commit/6d3884632a6d58ba62d509cff077048d2bc55675) FaceService: Conditionally add ParanoidSense _(by someone5678)_  
[f677747](https://github.com/PixelOS-AOSP/frameworks_base/commit/f677747b1249b13c26253cf94877a59b71b53154) services: Adapt face sense to A15-QPR1 _(by COSMIC)_  
[b101f63](https://github.com/PixelOS-AOSP/frameworks_base/commit/b101f63a76bd62b0f6d382e15ec0d62c9751dc91) base: Initial SenseProvider for FaceSense service _(by Chris Crump)_  
[d098fe8](https://github.com/PixelOS-AOSP/frameworks_base/commit/d098fe868851e5378017a3eb7d82f8aeef81ba13) SystemUI: Status bar tuner improvements _(by Rashed Abdel-Tawab)_  
[34f1c4a](https://github.com/PixelOS-AOSP/frameworks_base/commit/34f1c4a7e9a8c206d22dad639228cf51e4e2daab) SystemUI: Adapt tuner prefs to S settings style _(by SagarMakhar)_  
[9fcefb2](https://github.com/PixelOS-AOSP/frameworks_base/commit/9fcefb2943c587da248a0d31e8c5c8d09da6df30) SystemUI: Don't show tuner warning _(by Danny Lin)_  
[f6cba8a](https://github.com/PixelOS-AOSP/frameworks_base/commit/f6cba8a74cbde5be6099c94fadc36d04df1aa2cf) SystemUI: Hide more tuner preferences on production builds _(by Danny Lin)_  
[3b5d4e1](https://github.com/PixelOS-AOSP/frameworks_base/commit/3b5d4e11a60bfa9fde277a789320506a37ba803f) StatusBarIconController: Don't crash at boot _(by Ido Ben-Hur)_  
[7308fdb](https://github.com/PixelOS-AOSP/frameworks_base/commit/7308fdb2512ed4ee2b5b23786ad43bd352cebf0b) SystemUI: Do not duplicate SPN and PLMN in network name _(by Adithya R)_  
[19c679e](https://github.com/PixelOS-AOSP/frameworks_base/commit/19c679e200cfa2a69336e54d75b2b05908f7a478) Flags: Enable color fidelity _(by aswin7469)_  
[e6c0775](https://github.com/PixelOS-AOSP/frameworks_base/commit/e6c0775763fd7f26bf4948c8e302a1c011295246) SystemUI: Update Bluetooth battery level assets _(by Hernán Castañón Álvarez)_  
[6434df0](https://github.com/PixelOS-AOSP/frameworks_base/commit/6434df034d2f62db501d0585cf057896eceb2ad6) services: Fix crash of boot-time info dialog due to delayed font init _(by Dmitry Muhomor)_  
[4bcb7fb](https://github.com/PixelOS-AOSP/frameworks_base/commit/4bcb7fb54e5ea5aa7bb4162188f4c9cb655b1a68) ShutdownThread: Shorten wait time for shutdown time optimization _(by zljing)_  
[5677c52](https://github.com/PixelOS-AOSP/frameworks_base/commit/5677c5273d27aa81c991125f20a89d83ef54c7ea) base: Allow setting wake for notifications separately from doze [1/2] _(by Ido Ben-Hur)_  
[f56b343](https://github.com/PixelOS-AOSP/frameworks_base/commit/f56b34345205a28aabc5fee0d3f398e3ab4a49c7) base: Allow showing Ambient instead of fully waking [1/2] _(by ezio84)_  
[982c499](https://github.com/PixelOS-AOSP/frameworks_base/commit/982c4991148e0b82ab871fd17f849c98f72b30cd) core: res: Use accent color for progress bar background _(by Danny Lin)_  
[35efbb9](https://github.com/PixelOS-AOSP/frameworks_base/commit/35efbb9d115aaa1378a65eb3e94fd94b2173c18c) Make all activities resizable _(by Andy CrossGate Yan)_  
[573a809](https://github.com/PixelOS-AOSP/frameworks_base/commit/573a8096714cafb1f9392ccd3fa5076d68379dba) UI: Follow Monet and light/dark theme in user 1 icon _(by Andy CrossGate Yan)_  
[1f83d45](https://github.com/PixelOS-AOSP/frameworks_base/commit/1f83d45e3f35e07b5a9a4c53388d1a90d8f458cd) NightLight: Allow lower temperatures _(by Joe Maples)_  
[95a028b](https://github.com/PixelOS-AOSP/frameworks_base/commit/95a028be1863d4afc53dbde193562b6f2bc65922) SystemUI: Fix suspicious spaces around new mobile icons _(by lgjint)_  
[a97ef1a](https://github.com/PixelOS-AOSP/frameworks_base/commit/a97ef1ab5cb4ec94663e27932150e781470718f3) Configurable 0, 90, 180 and 270 degree rotation [1/2] _(by Ricardo Cerqueira)_  
[f60dff0](https://github.com/PixelOS-AOSP/frameworks_base/commit/f60dff0954005aee9a0f95b62967f7a88dec17d3) core: Fix uninitialized settings in NotificationAttentionHelper _(by LuK1337)_  
[b7626b1](https://github.com/PixelOS-AOSP/frameworks_base/commit/b7626b18a9471036d58928a0bdc27fb02f8a2164) Support enforcing a minimum delay between notification sounds of an app. _(by Danny Baumann)_  
[1452670](https://github.com/PixelOS-AOSP/frameworks_base/commit/1452670cca5b0ed2dc16e95aa337018704dc0f2c) base: Forward Port Volume Long Press Skip Tracks [1/2] _(by Austin T. Conn)_  
[677f847](https://github.com/PixelOS-AOSP/frameworks_base/commit/677f8471c6151818519b2e20173e918ecb7c61f0) SystemUI: use DOUBLE_TAP_TO_WAKE setting also for wake from aod _(by maxwen)_  
[7dca6f7](https://github.com/PixelOS-AOSP/frameworks_base/commit/7dca6f71edad9fefc348b2e092d7682509d9445c) core: Allow to hide and set a default for status bar DT2S gesture _(by Bruno Martins)_  
[f75a618](https://github.com/PixelOS-AOSP/frameworks_base/commit/f75a6189bccfe84ea22d703a6ed0784b80e26943) fixup! SystemUI: Add double tap to sleep gesture _(by Chirayu Desai)_  
[7439e1b](https://github.com/PixelOS-AOSP/frameworks_base/commit/7439e1bc6d166926cfb2acbe0f58598a8f6aa775) SystemUI: Add double tap to sleep gesture _(by Rashed Abdel-Tawab)_  
[bb501b8](https://github.com/PixelOS-AOSP/frameworks_base/commit/bb501b8d12263a7c5a430fdc356037f9fac71d6b) AutoBrightness: Add support for one shot auto-brightness _(by Cédric Bellegarde)_  
[a5fb871](https://github.com/PixelOS-AOSP/frameworks_base/commit/a5fb871fac434246d72479a75a93b03b32f61e69) fw/b: Add capability to allow tethering to use VPN upstreams _(by Sam Mortimer)_  
[a66a889](https://github.com/PixelOS-AOSP/frameworks_base/commit/a66a889906d3de148de0f352268196cc3d5abc25) SystemUI: Remove nav bar background in QS customizer _(by Danny Lin)_  
[f814de3](https://github.com/PixelOS-AOSP/frameworks_base/commit/f814de3fb613f28755c415b08a7f6156612afcd1) base: Incall vibration options [1/3] _(by beanstown106)_  
[1bd5661](https://github.com/PixelOS-AOSP/frameworks_base/commit/1bd56610100d5509c2ecf68f493cfa1391738836) NetworkPolicyManagerService: turn this into just a warning _(by Simão Gomes Viana)_  
[d52dc88](https://github.com/PixelOS-AOSP/frameworks_base/commit/d52dc88aad0345fa09a37f59a97d7add2757fd8b) base: Squash import NetworkTraffic _(by Jon Haus)_  
[c22cb46](https://github.com/PixelOS-AOSP/frameworks_base/commit/c22cb46e6293ed276add4e7e6a00e0f23322cbac) Keyguard: Add option to scramble pin layout when unlocking [2/2] _(by Adnan)_  
[7650bc6](https://github.com/PixelOS-AOSP/frameworks_base/commit/7650bc68c9c3d05f9d097cecef33f2aec992d4c3) LockPatternView: Fix showing pattern error _(by Dhina17)_  
[c7e320b](https://github.com/PixelOS-AOSP/frameworks_base/commit/c7e320b8e754c80fb2279c9cfb17a0159ae96722) fixup! Forward port CM Screen Security settings (1/2) _(by LuK1337)_  
[9669132](https://github.com/PixelOS-AOSP/frameworks_base/commit/966913216826c77b5fb247b67b17514af374f0bd) Forward port CM Screen Security settings [1/2] _(by Michael Bestas)_  
[6151e9a](https://github.com/PixelOS-AOSP/frameworks_base/commit/6151e9aa35c361e496c54edf4a28cdffc072ff76) SystemUI: Launch power menu from QS only if enabled _(by DarkJoker360)_  
[c085d01](https://github.com/PixelOS-AOSP/frameworks_base/commit/c085d012e2430e8c5faf82dcddbc013e497611e4) base: Fix disabling power menu completely on secured lockscreen _(by Pranav Vashi)_  
[a9458df](https://github.com/PixelOS-AOSP/frameworks_base/commit/a9458dfc124c72ac77354d051ebc7eb807d27b6c) base: Hide power menu on secure lockscreen [1/2] _(by Altaf-Mahdi)_  
[82234f0](https://github.com/PixelOS-AOSP/frameworks_base/commit/82234f048853fa8f4f657c1cf0390055d97c5f3a) SystemUI: Show big keyguard clock when media controls are hidden _(by Ido Ben-Hur)_  
[ccb0c3e](https://github.com/PixelOS-AOSP/frameworks_base/commit/ccb0c3e27bf773523367b06335e68bf16af3db59) base: Long press power button to toggle flashlight [1/2] _(by ezio84)_  
[9d6b25f](https://github.com/PixelOS-AOSP/frameworks_base/commit/9d6b25f688db2ab7b7be46200ec06e83d2a7cac8) SystemUI: MediaHierarchyManager: Initiate allowMediaPlayerOnLockScreen _(by Ido Ben-Hur)_  
[f4909d4](https://github.com/PixelOS-AOSP/frameworks_base/commit/f4909d43d5abc8a070f0a1a910a551b0bafe2ad6) fixup! SystemUI: Implement hide gestural navigation hint bar _(by Dhina17)_  
[03bc65f](https://github.com/PixelOS-AOSP/frameworks_base/commit/03bc65f3db2bcf7d0d9a5263e8f957eb2ac1ce2b) SystemUI: Implement hide gestural navigation hint bar _(by Jesse Chan)_  
[0a44ec2](https://github.com/PixelOS-AOSP/frameworks_base/commit/0a44ec297b2ac9d02615334288dbedb8e9eddb2d) SystemUI: Add Autobrightness tile _(by Dil3mm4)_  
[8f051d3](https://github.com/PixelOS-AOSP/frameworks_base/commit/8f051d382dc5c7cdd6f0fdffe2c14b4d9507c918) SystemUI: Add powershare QS tile _(by Linux4)_  
[285b1ed](https://github.com/PixelOS-AOSP/frameworks_base/commit/285b1ed58fcca9715ee87e5bda93b67203c24fab) SystemUI: Add USB Tether tile _(by BestPig)_  
[e38e173](https://github.com/PixelOS-AOSP/frameworks_base/commit/e38e173b01b35e3131c826fb20f6e449439e4bbf) SystemUI: Add AOD QS tile _(by Marko Man)_  
[11b2ec0](https://github.com/PixelOS-AOSP/frameworks_base/commit/11b2ec058c92db147d331bc0c527d95b906ee3df) SystemUI: Add heads up tile _(by Michael Bestas)_  
[92891ea](https://github.com/PixelOS-AOSP/frameworks_base/commit/92891ea6c913b964402d308fbdc8f03f0aebf1fd) Revert "[DO NOT MERGE] Make sure WiFi and Cell tiles are not created … _(by Danny Lin)_  
[f572022](https://github.com/PixelOS-AOSP/frameworks_base/commit/f572022dc6db67e189e8a26edb1a1ca3c4bfe8ec) Reapply "SystemUI: Allow Wi-Fi/cell tiles to co-exist with provider m… _(by Danny Lin)_  
[a6ae7a8](https://github.com/PixelOS-AOSP/frameworks_base/commit/a6ae7a8097ab3371f32c16c86e0839cf0dfc4b42) SystemUI: Restore wifi and cellular QS tiles _(by Michael Bestas)_  
[8400a8e](https://github.com/PixelOS-AOSP/frameworks_base/commit/8400a8e704e23d4975d42d6bdc62c045ce2a17db) SystemUI: Introduce Data Switch QS Tile _(by Christian Oder)_  
[bad464e](https://github.com/PixelOS-AOSP/frameworks_base/commit/bad464e80f8c848ff9d350f7359bf7583c8abd5c) SystemUI: Add caffeine QS tile _(by Keith Mok)_  
[845b2b2](https://github.com/PixelOS-AOSP/frameworks_base/commit/845b2b2468ada357811bed9933d3af3bb527cd6c) SystemUI: Enable NFC tile _(by Tim Schumacher)_  
[61ae1d1](https://github.com/PixelOS-AOSP/frameworks_base/commit/61ae1d1e3514586d46a5164d26b9e564385774da) SystemUI: Update NFC tile drawable _(by mydongistiny)_  
[c732594](https://github.com/PixelOS-AOSP/frameworks_base/commit/c732594dded3bc8f40d29f59852a2a96ba7fc97d) core: Fix menu popup ripple _(by timjosten)_  
[929b36a](https://github.com/PixelOS-AOSP/frameworks_base/commit/929b36a5f734e98738cc4ba49cb2fccc2eb3c0ca) SystemUI: Add navbar layout inversion tuning [1/2] _(by LuK1337)_  
[fe8fdf8](https://github.com/PixelOS-AOSP/frameworks_base/commit/fe8fdf87cc7ab9de6e4ad2620eefbec194eb9829) policy: Add support for device alert sliders. _(by thecrazyskull)_  
[556815f](https://github.com/PixelOS-AOSP/frameworks_base/commit/556815f7a7ad964244bfb2280e85c29904a43986) base: Introduce Smart 5G service [1/2] _(by Adithya R)_  
[3f873ea](https://github.com/PixelOS-AOSP/frameworks_base/commit/3f873ea2f982bea82fb3f83b55a620a7241e925a) s2ss: Remove property usage _(by LibXZR)_  
[b728ccc](https://github.com/PixelOS-AOSP/frameworks_base/commit/b728ccc94d3570ba93c2cb7be4241a7c6af0ce64) base: Add three-fingers-swipe to screenshot [1/2] _(by ghbhaha)_  
[88f60c3](https://github.com/PixelOS-AOSP/frameworks_base/commit/88f60c3689cdaf9af5aa073878c8d809852f60fc) [SQUASH] base: Add option to cycle through ringer modes [1/2] _(by rituj)_  
[5baf8fc](https://github.com/PixelOS-AOSP/frameworks_base/commit/5baf8fcd65bd862e91b9147b510f894fc1718fda) SystemUI: Introduce Adaptive Playback [1/2] _(by Jyotiraditya)_  
[b121f6e](https://github.com/PixelOS-AOSP/frameworks_base/commit/b121f6eb5e3edcf7fab943cb99a1ef4fc6618132) core: Broadcast intent when display power state changes _(by Adithya R)_  
[92060d6](https://github.com/PixelOS-AOSP/frameworks_base/commit/92060d63a1463563195bad16042118dc91c97be8) base: Update some icons to MD2 _(by Anushek Prasal)_  
[e487e14](https://github.com/PixelOS-AOSP/frameworks_base/commit/e487e1458f69433179a1dd31130d5033c9acb082) Report success on every fingerprint removal _(by Kishan Dudhatra)_  
[ec489bd](https://github.com/PixelOS-AOSP/frameworks_base/commit/ec489bd805e3c11850111016a790ace895faa3bc) Apply monet to fingerprint authentication ripple animation _(by SagarMakhar)_  
[50d75c8](https://github.com/PixelOS-AOSP/frameworks_base/commit/50d75c87f4e6da4801997d284ea0242bc3405dc3) SystemUI: support black theme for dark mode [1/3] _(by Jesse Chan)_  
[7b87063](https://github.com/PixelOS-AOSP/frameworks_base/commit/7b8706360a7c3cffba4fa692f7a71ac778d73b54) SystemUI: Fix uneven DND icon padding in status bar _(by Ido Ben-Hur)_  
[012b37b](https://github.com/PixelOS-AOSP/frameworks_base/commit/012b37bab7b2773621ef194036a6e090548718a9) SystemUI: Update string for add tiles with one click _(by mydongistiny)_  
[e2e68cb](https://github.com/PixelOS-AOSP/frameworks_base/commit/e2e68cbb677a0fe6ef128544ea57763dc0f9ba95) SystemUI: Allow user to add/remove QS with one click _(by Andrzej Ressel)_  
[eacd51f](https://github.com/PixelOS-AOSP/frameworks_base/commit/eacd51f9b8b0f5d53bdba95607d7b840b0d88234) SystemUI: Make battery clickable again _(by Michael W)_  
[a847e3c](https://github.com/PixelOS-AOSP/frameworks_base/commit/a847e3cab210ba9882395c9fa09422f37ed347c2) SystemUI: Enable cast tile without Wi-Fi connection _(by nift4)_  
[040930c](https://github.com/PixelOS-AOSP/frameworks_base/commit/040930cf3757199fdf962d19cb9de38d90a9f4c4) AutofillManager: Make userdebug default to NO_LOGGING _(by LuK1337)_  
[da3f6e0](https://github.com/PixelOS-AOSP/frameworks_base/commit/da3f6e0658fcc2b5226942b0729a3b8019fa74e5) SystemServer: only enable fd leak tracker on eng _(by Simao Gomes Viana)_  
[99c831b](https://github.com/PixelOS-AOSP/frameworks_base/commit/99c831bebc5bf5678a3bac15f496c6f93a451cc7) core: BatteryManager: Add few more Battery broadcast intents _(by Jyotiraditya Panda)_  
[434ad25](https://github.com/PixelOS-AOSP/frameworks_base/commit/434ad25c7125b3f57c14a0490071d059cb990351) PowerOffAlarmService: Handle NPE with shared preferences _(by Adithya R)_  
[c5890b1](https://github.com/PixelOS-AOSP/frameworks_base/commit/c5890b19a8116f8531ba156d3fdc8f97c44ead5b) base: Introduce PowerOffAlarmService _(by Ido Ben-Hur)_  
[fe7d7d1](https://github.com/PixelOS-AOSP/frameworks_base/commit/fe7d7d15dd4994a7d4fff1496d2b835a0e77bdfe) SystemUI: Update QS header fields text appearance on theme change _(by Dhina17)_  
[4bc3b74](https://github.com/PixelOS-AOSP/frameworks_base/commit/4bc3b74aceace19a40b5990536869105b86d228f) Fix default values for 5G Ultra Wideband icon carrier config keys _(by Vala Zadeh)_  
[cc7c9f8](https://github.com/PixelOS-AOSP/frameworks_base/commit/cc7c9f8ebb1dd580711ffcdd86b7a09cb7db6739) Add 5G Ultra Wideband icon carrier config keys _(by Vala Zadeh)_  
[044e31b](https://github.com/PixelOS-AOSP/frameworks_base/commit/044e31b4f4235530c0552ebf9f8174b0c8c514c4) base: SystemUI: Allow flags to be overrideable _(by Jeferson)_  
[08509d9](https://github.com/PixelOS-AOSP/frameworks_base/commit/08509d9216f620773dc6af7c9308acb48edddd8c) SystemUI: handle camera launch gesture from keyhandler _(by Roman Birg)_  
[9dd729a](https://github.com/PixelOS-AOSP/frameworks_base/commit/9dd729ad8f5917389a8346aff87c3ef524887f3c) DozeSensors: only use proximity sensor if supported _(by Demon000)_  
[e81c1b2](https://github.com/PixelOS-AOSP/frameworks_base/commit/e81c1b21d6dc95a7acfa477e584b7405c90d58a3) SystemUI: doze: add config for long press sensors that need a proximi… _(by Cosmin Tanislav)_  
[b057a63](https://github.com/PixelOS-AOSP/frameworks_base/commit/b057a63b4f18694cdf91f33b61009ec0c490455b) SystemUI: doze: add config for double tap sensors that need a proximi… _(by Cosmin Tanislav)_  
[aa546d1](https://github.com/PixelOS-AOSP/frameworks_base/commit/aa546d14ddc92434eba39448e5165ec7383544d0) Partially revert "Assume sensors perform prox check" _(by Cosmin Tanislav)_  
[243abc2](https://github.com/PixelOS-AOSP/frameworks_base/commit/243abc287d8fb0e0a1095fc554db9c2509d89c72) SettingsLib: Update 5G+ icon to Silk design _(by Adithya R)_  
[63efcdb](https://github.com/PixelOS-AOSP/frameworks_base/commit/63efcdb94866dc6e8ed6ee6d2a30f693205f7694) SystemUI: Enable production-ready feature flags _(by Danny Lin)_  
[a45718f](https://github.com/PixelOS-AOSP/frameworks_base/commit/a45718fc854aa34a793656aedfe8d207d97ce1b2) SystemUI: Internet tile: Allow long-pressing on mobile network _(by Michael W)_  
[eeeaba8](https://github.com/PixelOS-AOSP/frameworks_base/commit/eeeaba8c0f63d6b23fb7a3caeee61c8585d70f75) SystemUI: More rounded corners _(by Lucchetto)_  
[e799828](https://github.com/PixelOS-AOSP/frameworks_base/commit/e799828b326b5eb8a5b7a75003c91058d642c144) Add config to exempt telephony-related app from location indicators _(by Danny Lin)_  
[082604b](https://github.com/PixelOS-AOSP/frameworks_base/commit/082604b661aff27a846da1c35ef7d047c41b1028) wm: Follow rounded corners by split divider corner size _(by ReallySnow)_  
[4eb9700](https://github.com/PixelOS-AOSP/frameworks_base/commit/4eb97001df055dab4a82b6d29b6c8986ab0f7b72) graphics: Override system fonts with user-selected overlays _(by Danny Lin)_  
[63522be](https://github.com/PixelOS-AOSP/frameworks_base/commit/63522be783ff0ce82f9ee6f02b92ae980e104faa) base: Add deep sleep info to uptime preference _(by maxwen)_  
[da0a186](https://github.com/PixelOS-AOSP/frameworks_base/commit/da0a1867eaa40a8b3269b9a19211fd7ad13e8ffd) SettingsProvider: Set device name to marketname if available _(by Adithya R)_  
[50923aa](https://github.com/PixelOS-AOSP/frameworks_base/commit/50923aa366598dc5bb41984b6a82cda2d0d57ed7) TtsEngines: avoid crashes caused by null engine name _(by Oliver Scott)_  
[df1119e](https://github.com/PixelOS-AOSP/frameworks_base/commit/df1119e39b87ac8a60ae174f1008fbcf0da0ce1f) Do not ignore background vibrations from shell _(by Tommy Webb)_  
[26a59a2](https://github.com/PixelOS-AOSP/frameworks_base/commit/26a59a2b0ed9504485cfa9306fadc9b0fa3ee7f0) Fix MtpDatabase multithreading NullPointerException _(by katao)_  
[5b630a3](https://github.com/PixelOS-AOSP/frameworks_base/commit/5b630a352879cca4fd8718eede9da59231f2ec2c) Allow disabling USB notifications _(by Danny Lin)_  
[4e0ca3d](https://github.com/PixelOS-AOSP/frameworks_base/commit/4e0ca3df067d3f87398dfc26e49a3b29183f3bd4) UpdateEngine: Add perf mode binder interface _(by Luca Stefani)_  
[de47938](https://github.com/PixelOS-AOSP/frameworks_base/commit/de47938e2c8f8fc35342c32433debc1b8d388504) TwilightService: Use temporary TwilightState when location is not ava… _(by rituj)_  
[4ce384f](https://github.com/PixelOS-AOSP/frameworks_base/commit/4ce384f03e605914870bbd2f30887e3f1f3e240c) Fix bug Device that can't support adoptable storage cannot read the s… _(by sangho.yoon)_  
[13512a2](https://github.com/PixelOS-AOSP/frameworks_base/commit/13512a20cd5bf69929bbba7370c8ddd552e1be1d) ScreenRecord: Save recordings in ScreenRecords _(by El Dainosor)_  
[b8bc127](https://github.com/PixelOS-AOSP/frameworks_base/commit/b8bc127f4d48233a9ed225df12df0255b1460637) SystemUI: Add colors to assistant animation _(by paphonb)_  
[2d1d271](https://github.com/PixelOS-AOSP/frameworks_base/commit/2d1d2716b68f1c9483203b9527e0772598ba175b) SystemUI: Fix the unlock sound played repeatedly _(by Shufeng Hou)_  
[f7e9d3c](https://github.com/PixelOS-AOSP/frameworks_base/commit/f7e9d3cb87b3350b8fab451b6ce2b6fbaf244bf8) SystemUI: Fix status bar alarm icon _(by Michael W)_  
[6795d82](https://github.com/PixelOS-AOSP/frameworks_base/commit/6795d8220b018ce046e22ab3ed49b4a27cc24eff) SystemUI: Remove alarm from statusbar icon blocklist _(by Adithya R)_  
[eb3d262](https://github.com/PixelOS-AOSP/frameworks_base/commit/eb3d262c882f1ca074bccbc86587dd3080daef56) base: Rearrange bluetooth icon on statusbar _(by Adithya)_  
[c7afb5c](https://github.com/PixelOS-AOSP/frameworks_base/commit/c7afb5c96b24bfa93cdcc905a5ff195114d4eed1) themes: Fix list style alert dialog to use system font _(by maxwen)_  
[e1b4685](https://github.com/PixelOS-AOSP/frameworks_base/commit/e1b4685215754124fe47bb8a33c9c5cf1795136e) SystemUI: Remove excess margin in few statusbar icons _(by Adithya R)_  
[f922fc0](https://github.com/PixelOS-AOSP/frameworks_base/commit/f922fc0cf011afd79632961c66509b1f46dd5010) SystemUI: Internet tile: Allow long-pressing on mobile network _(by Michael W)_  
[f4fb4b8](https://github.com/PixelOS-AOSP/frameworks_base/commit/f4fb4b8d60c9be37b632454acf6e642bb9c2e102) SystemUI: Fix uneven volume icon padding in status bar _(by Danny Lin)_  
[cfd3732](https://github.com/PixelOS-AOSP/frameworks_base/commit/cfd37322251127a01e69ec954b28f87c226caad8) SystemUI: Check if primitive vibrations are supported in new quick af… _(by Fabian Leutenegger)_  
[0cbd546](https://github.com/PixelOS-AOSP/frameworks_base/commit/0cbd54606946c55bd81174b5ee69020dad0d7e66) camera: Skip HFR checks for privileged apps. _(by Sai Kumar Sanagavarapu)_  
[91165ed](https://github.com/PixelOS-AOSP/frameworks_base/commit/91165edf21f1559b43bc5a7cd180072377473ff8) Camera: Skip stream size check for whitelisted apps. _(by Gaoxiang Chen)_  
[32bdea1](https://github.com/PixelOS-AOSP/frameworks_base/commit/32bdea19df983ab309a17c22c667ae036d5a7f8d) camera: Support exposing aux camera to apps _(by Sauhard Pande)_  
[bf655ec](https://github.com/PixelOS-AOSP/frameworks_base/commit/bf655ec4dce0f9b2ae33df078452ffc78d60d550) camera: Add backwards-compatible CaptureResultExtras constructor _(by Adithya R)_  
[177bc27](https://github.com/PixelOS-AOSP/frameworks_base/commit/177bc27c6b84c4fd30b2afd8edecbcf5c3e48b90) core: camera2: StreamConfigurationMap: add constructor for MIUI camera _(by Pulkit077)_  
[59c1a08](https://github.com/PixelOS-AOSP/frameworks_base/commit/59c1a0810d2a2d659df4d1e36179fd3c156e1126) base: Follow Dark/Light theme for Safe Mode dialog _(by Pulkit077)_  
[6bb02ba](https://github.com/PixelOS-AOSP/frameworks_base/commit/6bb02ba2b77269153ecffce258e4b4a01c0d34bd) Enable Binder Proxy Tracking by Uid only on eng builds _(by dianlujitao)_  
[a5f34a0](https://github.com/PixelOS-AOSP/frameworks_base/commit/a5f34a0ac2044029c757a2abbc5f13b981fe0830) frameworks: Exempt location packages from location indicators _(by Chirayu Desai)_  
[5a97e63](https://github.com/PixelOS-AOSP/frameworks_base/commit/5a97e634686179533416d1d795a2123034258b6f) AbsListView: Improve scrolling cache _(by Pawit Pornkitprasan)_  
[b99809a](https://github.com/PixelOS-AOSP/frameworks_base/commit/b99809a01228a91854e64df47b822af9a0480a17) Trace: Disable debug tracing on production builds _(by Danny Lin)_  
[af75948](https://github.com/PixelOS-AOSP/frameworks_base/commit/af75948a60459544fa0bb938f8871c0a19a232cd) Paint: Enable subpixel text positioning by default _(by Danny Lin)_  
[494556d](https://github.com/PixelOS-AOSP/frameworks_base/commit/494556d8f9c164ea6e136a4ad0c58141368083ef) base: Deprioritize important developer notifications _(by Danny Lin)_  
[0beb48e](https://github.com/PixelOS-AOSP/frameworks_base/commit/0beb48e50185ebad34c81e49d89e66bce2a32d9b) SettingsLib: Update 4G+ icon to Silk design as well _(by TH779)_  
[9951c7f](https://github.com/PixelOS-AOSP/frameworks_base/commit/9951c7fa37d1765faedfb160388b265d1aeeab41) SettingsLib: Update LTE+ icon as per new Silk design _(by Adithya)_  
[429eb82](https://github.com/PixelOS-AOSP/frameworks_base/commit/429eb823abe69fe8d2419437a121b7a463805b90) SystemUI: Remove Android build number from QS footer _(by Danny Lin)_  
[233ec9b](https://github.com/PixelOS-AOSP/frameworks_base/commit/233ec9b0a1c8e725bf23ff5d479cee1aff7fd21c) SystemUI: Remove build version from qs footer _(by jhenrique09)_  
[eb4d814](https://github.com/PixelOS-AOSP/frameworks_base/commit/eb4d814f28b6fa889965c9c82e832fe380a50b0d) Squash of SystemUI: Show bluetooth battery level _(by LuK1337)_  
[f4fa341](https://github.com/PixelOS-AOSP/frameworks_base/commit/f4fa341be880f5ca493bfceaef769f835d0b47d3) Fallback to global actions if assistant is not available _(by LuK1337)_  
[dc66ac5](https://github.com/PixelOS-AOSP/frameworks_base/commit/dc66ac5bb01c02de3b1cc03cfa0c926596986782) SystemUI: Add support for persistent usb drive notification. _(by Adnan Begovic)_  
[ad5d235](https://github.com/PixelOS-AOSP/frameworks_base/commit/ad5d235bcb6341837cc4640de1d3d4e3f72cd7be) SystemUI: Allow snoozing SD card notification unconditionally _(by LuK1337)_  
[a228f4e](https://github.com/PixelOS-AOSP/frameworks_base/commit/a228f4ed72a5c5af940423206f41fa63d9421fe4) SystemUI: Allow privileged system apps to access screenshot service _(by Danny Lin)_  
[53bf752](https://github.com/PixelOS-AOSP/frameworks_base/commit/53bf752ba0b3df7c5ddcd498a078dc9784e175a3) core: Expose method to start assistant through Binder _(by Danny Lin)_  
[a9e58fa](https://github.com/PixelOS-AOSP/frameworks_base/commit/a9e58fa11b0f876bdf8991f65b8dc998280ebe16) base: Support for device specific key handlers _(by Bruno Martins)_  
[fbae9ab](https://github.com/PixelOS-AOSP/frameworks_base/commit/fbae9abf4200c0931e4d09e45cb018b898c1d239) Check for null callerPackage in getStorageEncryptionStatus _(by Ethan Chen)_  
[e2e9634](https://github.com/PixelOS-AOSP/frameworks_base/commit/e2e96341592d317bce20302e31eba2f4ca68fdbc) Show the vibrate icon in the Status Bar by default _(by Chirayu Desai)_  
[2b71ae4](https://github.com/PixelOS-AOSP/frameworks_base/commit/2b71ae4c048f0c4f1f694e47f18eb329ef45e688) Updates to various icons: _(by Dan Sandler)_  
[c6d6368](https://github.com/PixelOS-AOSP/frameworks_base/commit/c6d6368fe146936b9f150e5c7f43a0075a191b66) SettingsLib: Don't show system overlays on apps list _(by Henrique Silva)_  
[ef2631d](https://github.com/PixelOS-AOSP/frameworks_base/commit/ef2631dbafa2e73108f01c913558e8b85ae83c2a) Download: Add support to manually pause/resume download _(by qqzhou)_  
[5c226e2](https://github.com/PixelOS-AOSP/frameworks_base/commit/5c226e218525edb1375def146d0c309ec025d31d) Allow adjusting screen density to smaller sizes. _(by Danny Baumann)_  
[aa9865e](https://github.com/PixelOS-AOSP/frameworks_base/commit/aa9865e2e1178c17cf5cc6b870d93eb77571c769) Allow adjusting progress on touch events. _(by Danny Baumann)_  
[d540422](https://github.com/PixelOS-AOSP/frameworks_base/commit/d5404224f48cbe57826242898c2eec9d7696c246) [SQUASH] Implement DeviceConfigUtils and service _(by jhenrique09)_  
[7e92a90](https://github.com/PixelOS-AOSP/frameworks_base/commit/7e92a90efff6ee722fdc2ee72cda771438e28cb9) fixup! Introduce high touch polling rate feature control _(by Michael Bestas)_  
[f698498](https://github.com/PixelOS-AOSP/frameworks_base/commit/f6984981455690d16aa4432a6b2691598093d98c) Introduce high touch polling rate feature control _(by Ramii Ahmed)_  
[55e86e6](https://github.com/PixelOS-AOSP/frameworks_base/commit/55e86e628cac6023dd9a19a50215f9f811be5315) fixup! Add high touch sensitivity and hovering to InputService _(by Chirayu Desai)_  
[180d7fc](https://github.com/PixelOS-AOSP/frameworks_base/commit/180d7fca37a755abf8b3c55cfeb856b5b5eb9cec) Move high touch sensitivity and hovering to InputService _(by Danesh M)_  
[3e1ce40](https://github.com/PixelOS-AOSP/frameworks_base/commit/3e1ce407c03fba606ddabce9e6c4be1cb873992e) base: Add Touch HIDL support _(by Anushek Prasal)_  
[3135306](https://github.com/PixelOS-AOSP/frameworks_base/commit/3135306c132c487d16208dcd4b8c4ea4bcd2702c) Shell: Don't show bugreport on DocumentsUI _(by jhenrique09)_  
[7d804b3](https://github.com/PixelOS-AOSP/frameworks_base/commit/7d804b3b4c4c7dff37dd5c3cc47bd6e93b3a03fe) Introduce anti flicker mode in LiveDisplay _(by Arian)_  
[0f1e076](https://github.com/PixelOS-AOSP/frameworks_base/commit/0f1e076634b1e7c08faf59bdf11b39df9fe7046d) services: TwilightTracker: create an attribution context and use it i… _(by jhonboy121)_  
[fa1bb4f](https://github.com/PixelOS-AOSP/frameworks_base/commit/fa1bb4f1abe6b7b56eac739438e7d5dbc8a9cc50) Introduce LiveDisplay from Lineage _(by Henrique Silva)_  
[a6060a0](https://github.com/PixelOS-AOSP/frameworks_base/commit/a6060a05b98aea5b4c43ad7f5776addd9127c22f) Initial import of lineagehw _(by jhenrique09)_  
[6390d8a](https://github.com/PixelOS-AOSP/frameworks_base/commit/6390d8ac8cca326f12e7a2d78ca7c7ccea6a729a) health: Catch all setCharging*() exceptions _(by LuK1337)_  
[c8adbfb](https://github.com/PixelOS-AOSP/frameworks_base/commit/c8adbfb639dd7a8fc42023b4fbcd352ce6094a00) health: Rename msToUTCString to msToHMSString _(by Luofan Chen)_  
[9687526](https://github.com/PixelOS-AOSP/frameworks_base/commit/9687526533926f10b91ee14c78a30cec6f2fb3e2) health: Format notification's target time according to locale _(by наб)_  
[2935da2](https://github.com/PixelOS-AOSP/frameworks_base/commit/2935da2f917611d956290d1f32886b891c7e05d5) base: Decouple charging control and main logic _(by Luofan Chen)_  
[a17fcc6](https://github.com/PixelOS-AOSP/build/commit/a17fcc6ad8bfac75fe0d43f6a4c233b69296989d) Reapply "Add DeviceDiagnostics.apk" _(by Hridaya Prajapati)_  
[f27d510](https://github.com/PixelOS-AOSP/build/commit/f27d510f617aa7e446bec86c571bf3c1bbf4b384) Revert "Remove additional DeviceDiagnostics reference" _(by Hridaya Prajapati)_  
[655e1ee](https://github.com/PixelOS-AOSP/system_core/commit/655e1eed9279f6561548620b1417075ee77e5b95) Revert "init: Remove schedtune support" _(by Giovanni Ricca)_  
[b89203a](https://github.com/PixelOS-AOSP/frameworks_base/commit/b89203ad0c242e2c5caf271791a0ca7a19477476) base: Implement Lineage Health Service _(by Luofan Chen)_  
[b6af1a4](https://github.com/PixelOS-AOSP/frameworks_base/commit/b6af1a4ec9efff0d864dc2be359e5dc58faa5cfe) utils: Introduce FileUtils class _(by Michael Bestas)_  
[83ed1b5](https://github.com/PixelOS-AOSP/frameworks_base/commit/83ed1b588661fd906a4217e93932e81893e05e79) base: Add CUSTOM metrics const. _(by Bauuuuu)_  
[90f5ca9](https://github.com/PixelOS-AOSP/frameworks_base/commit/90f5ca9bdfed38de8ebb0ee38fcc4da243c085e2) core: Switch to mkrbin for copying crash logs _(by NurKeinNeid)_  
[cba469c](https://github.com/PixelOS-AOSP/frameworks_base/commit/cba469cb5071e01deaf7cef03447fa099a9dfabd) base: Add button to upload crash log to memocho _(by Till Kottmann)_  
[b8fdd12](https://github.com/PixelOS-AOSP/frameworks_base/commit/b8fdd128a1f1bf562430d1d4b07be50d732c3797) FrameTracker: Silence logspam _(by cjh1249131356)_  
[5d97d6b](https://github.com/PixelOS-AOSP/frameworks_base/commit/5d97d6bc8ec07da6ff50f5e724e1e0ae647c356f) fw/b: Use ro.build.version.incremental to signal OTA upgrades _(by dhacker29)_  
[45e9270](https://github.com/PixelOS-AOSP/frameworks_base/commit/45e92708b4b70490fb1bb9dbbcff23b6c5600405) KernelCpuUidTimeReader: Decrease log level on non-eng builds _(by Han Wang)_  
[fe29dc3](https://github.com/PixelOS-AOSP/frameworks_base/commit/fe29dc3edddbc8f4150f54862c03c5e8fe11b2f5) styles: Use user fonts for Material UI themes _(by Danny Lin)_  
[d22158b](https://github.com/PixelOS-AOSP/frameworks_base/commit/d22158b23db9cda0b765f0c0ebe15b5ed94dd950) SettingsLib: Use framework resource for headline font _(by Adithya R)_  
[4679c6e](https://github.com/PixelOS-AOSP/frameworks_base/commit/4679c6eabbc8426a7ea2093ab2f616f07da0aa25) base: Allow disabling refresh rate lowering in battery saver _(by Adithya R)_  

## 2025-03-13
[46b6d53](https://github.com/PixelOS-AOSP/frameworks_av/commit/46b6d536fd7c785a6944ed7d1a060a0375c4e7aa) fixup! Camera: Skip stream size check for whitelisted apps _(by Michael Bestas)_  
[16b748d](https://github.com/PixelOS-AOSP/frameworks_av/commit/16b748da7b2854746a01bff5abe472fe35f5e225) Merge tag 'android-15.0.0_r20' into fifteen _(by Hridaya Prajapati)_  
[e2fa2e6](https://github.com/PixelOS-AOSP/packages_apps_ParanoidSense/commit/e2fa2e6a99de972eada6ae4569bb1255ba88ba09) ParanoidSense: Fix build errors with latest kotlin version _(by Jyotiraditya Panda)_  
[1b32ab1](https://github.com/PixelOS-AOSP/packages_apps_ParanoidSense/commit/1b32ab11365f6782b59614e44e221e34fad07c6d) Revert "ParanoidSense: Fix build error for QPR2" _(by Hridaya Prajapati)_  
[1d95f7e](https://github.com/PixelOS-AOSP/build/commit/1d95f7e100532f24a857dd251a4c50460c315529) Revert "Always include vendor_manifest.xml in PRODUCT_PACKAGES" _(by Michael Bestas)_  
[f872f5a](https://github.com/PixelOS-AOSP/build/commit/f872f5affca39cca2b5b9524cb455903cea7952b) build: Move inclusion of BoardConfigExtra.mk to board_config.mk _(by Yumi Yukimura)_  
[88be538](https://github.com/PixelOS-AOSP/build_soong/commit/88be538970efaa24ec4b488dd78b5e975e3e8270) Use system server jar module stem instead of its name _(by Luca Stefani)_  
[3f6b4f8](https://github.com/PixelOS-AOSP/build_soong/commit/3f6b4f8933b4bed6b15decb8ae1833e8e6a33f0e) Revert "Add vendor/aosp to kotlin plugins neverallow" _(by Michael Bestas)_  
[0f12f61](https://github.com/PixelOS-AOSP/build_soong/commit/0f12f6189fb717b862223ce03506bc16a7b49e2d) Merge tag 'android-15.0.0_r20' into fifteen _(by Hridaya Prajapati)_  

## 2025-03-12
[a5983b0](https://github.com/PixelOS-AOSP/vendor_aosp/commit/a5983b0c3719f115037e22597a9afcde23814f55) soong: generator: Update for BP1A _(by LuK1337)_  
[b2d8fa5](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/b2d8fa57b9b35b0c4e232a5742d62723a2dc36e5) Settings: Move window ignore secure to global settings _(by someone5678)_  
[6b34676](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/6b3467667556d4659ac560082d1c06d4d3ca7214) Settings: Improve strings for window ignore secure feature _(by Adithya R)_  
[0658e68](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/0658e683bbe8c4a7900dca0f90ca4b4ed9e746df) Settings: Add window ignore secure feature [2/2] _(by LibXZR)_  
[824a249](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/824a249832850bac71a743186b1d4339d3ffca87) Settings: Add Face Unlock with ParanoidSense _(by Chris Crump)_  
[aafd490](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/aafd490093b2fa16a99f69f9149554cb3d1c4e8a) Settings: Migrate from SwitchPreference to SwitchPreferenceCompat _(by Hridaya Prajapati)_  
[109673c](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/109673c7b9bed7d65aa67c94dcc0edac4c8172a1) Settings: Add option to launch statusbar tuner [2/2] _(by Jyotiraditya)_  
[f055094](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/f055094862ed38872070fef2a8d0de2ffc9e7271) Settings: Use List Preference for NightLight settings _(by Akash)_  
[853a61d](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/853a61dcf2bf8d2e8d325c96500284c1144f0c07) Settings: Use List Preference for NightMode _(by Pranav Vashi)_  
[c5317c5](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/c5317c5b744503ae758f3fe9b397eede92e6b8a3) Settings: Make Ambient Display toggle show on single tap sensor _(by Cyber Knight)_  
[dc3917e](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/dc3917eea606d371fad10acdbaae5522ed204c00) Settings: Allow setting wake for notification separately from doze [2/2] _(by Ido Ben-Hur)_  
[6bd6ab0](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/6bd6ab095a16737432bd033f9481dd842c256bc3) Settings: Allow showing Ambient instead of fully waking [2/2] _(by Ido Ben-Hur)_  
[3f22a1b](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/3f22a1b4491e31a81d9722229a6e2c641d36c3dc) fixup! Settings: Add FastCharge preference into Battery settings _(by Michael Bestas)_  
[4b2d19e](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/4b2d19e28d44e1138724f7fc75be4e486912e168) Settings: Add FastCharge preference into Battery settings _(by Bruno Martins)_  
[3188b27](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/3188b27b3e0ed5e740b2ea27af9e76295d7d67bb) Settings: Configurable 0, 90, 180 and 270 degree rotation [2/2] _(by kufikugel)_  
[9c5d069](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/9c5d069076aaed39427a3a9adb85c8a85096c2de) Settings: Add setup UI for minimum delay between an app's notificatio… _(by Danny Baumann)_  
[e96d341](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/e96d3415ecb3977c2e987f3a20c6ecf9e0d29912) Settings: Forward Port Volume Long Press Skip Tracks [2/2] _(by Chris Crump)_  
[23ddd07](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/23ddd079747eb3aabaddf6777d00806c412113e7) Settings: Add advanced restart with global actions _(by Adin Kwok)_  
[7af5d82](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/7af5d82c9e6d9e33e9f326b03e2daf6e26f2c7e8) Settings: Add double tap to sleep preference _(by Rashed Abdel-Tawab)_  
[ba43a57](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/ba43a57a3196db144d049b85730f10e61644e490) Settings: Add preference for one shot auto-brightness _(by Cédric Bellegarde)_  
[02d358b](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/02d358b5ab354307c315b6d7515d8545db977df8) Settings: Add hotspot setting to allow VPN upstreams _(by Sam Mortimer)_  
[e79f3f1](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/e79f3f1d439a18a321873c687d7ea0f497fafb5f) SoftAp: add client manager _(by cjybyjk)_  
[fe6f87e](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/fe6f87ed6b00aa808313cc2ec0cce650e3717631) Settings: add TextView for summary into SeekBarDialogPreference _(by cjybyjk)_  
[03bf6ee](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/03bf6ee2891299620b60f26f57e1fa0208fca3d3) SoftAp: add Hidden SSID preference _(by cjybyjk)_  
[33f82c2](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/33f82c25aa25a56dce278bc36187ab1fded5ffda) Settings: Add incall vibration options [3/3] _(by beanstown106)_  
[453e67f](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/453e67f52b6eecfc7ae7c322173115d10ec63352) Settings: Import network traffic _(by Jon Haus)_  
[2c39ed0](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/2c39ed044ada972237dcd60bc42a19f1c2156a19) Settings: Add option to scramble pin layout when unlocking (1/2). _(by Adnan)_  
[b08bf8c](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/b08bf8cd1de0966395473f04e95e8ea7abc16d81) Settings: Forward port pattern visibility settings (2/2) _(by Michael Bestas)_  
[f4e7f36](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/f4e7f3613934bca4e3e8b4e7cc7331d40599cd36) Settings: Forward port lock pattern grid size (2/2) _(by Michael Bestas)_  
[f14191e](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/f14191e241263f6af1b6e58e399b3a289c159bc1) Settings: Hide power menu on secure lockscreen [2/2] _(by Altaf-Mahdi)_  
[6fd97fe](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/6fd97fe83f066c61022c1d6441cae880fcfc9ec4) Settings: Implement hide gestural navigation hint bar [2/2] _(by Jesse Chan)_  
[ac64ed1](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/ac64ed1d2c143393cd7ae96d8a8bfd0a9271fff5) Settings: Add toggle for 3-button navbar inversion [2/2] _(by Adithya R)_  
[e36bb4d](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/e36bb4d8df8cff20163ee8284b3d6e6ed6ff6e40) Settings: Re-organize sound settings page _(by Karan Parashar)_  
[c830256](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/c830256e010430fc30b4da3fb4d7ced34edf98f3) Settings: Allow disabling screenshot shutter sound [2/2] _(by maxwen)_  
[ea50083](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/ea5008302996d6423f738eb99bf499112b5239cb) Settings: Long press power button to toggle flashlight [2/2] _(by Chris Crump)_  
[8695647](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/86956473299287777e1f0ca2fb8375a4adde9713) Settings: Add toggle for Smart 5G [2/2] _(by Adithya R)_  
[cacc20b](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/cacc20b2f652233908325e99a14ad1d615550675) Settings: Add three-fingers-swipe to screenshot [2/2] _(by ghbhaha)_  
[87026e1](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/87026e1f556c16b3a0d981aca84dc7383cddb8d3) Settings: Add option to cycle through ringer modes [2/2] _(by rituj)_  
[6dc1d8c](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/6dc1d8c786a67e672cc2b0f213550f639532d4bf) Settings: Improve code for time spent in app _(by Jyotiraditya Panda)_  
[f91ca39](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/f91ca3999c58bce604c53cb12185f27e25125c10) AppInfo: Add time spent in app from Wellbeing _(by Jason Edson)_  
[eed5d2c](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/eed5d2c161af049b1653a5e8ef706a8f67a0725d) Settings: support black theme for dark mode [2/3] _(by Jesse Chan)_  
[fd344d4](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/fd344d4efbbd6091c173ae3860f2d52cf3fa5ab0) Settings: Refactor battery info strings for translation _(by Karan Parashar)_  
[3b31454](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/3b3145407c5c5e3393284d91fadd6d4da14fc720) Settings: Make some strings untranslatable _(by Karan Parashar)_  
[f3ead0f](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/f3ead0f11ab2643f14774629e8b8594fa3120a2a) Hide unavailable battery info _(by Michael Bestas)_  
[834944d](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/834944d5b15d8c7213897307115d6a0caf617c99) fixup! Settings: deviceinfo: Extend Battery info page _(by Michael Bestas)_  
[730ec00](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/730ec0091852d6ccaaa04f3764ae7d4ac31f101a) Settings: deviceinfo: Extend Battery info page _(by Jyotiraditya Panda)_  
[80deac9](https://github.com/PixelOS-AOSP/frameworks_base/commit/80deac94b74dcaf900316c4b9d57f5f945d3a36c) display: Consider peak refresh rate in BrightnessObserver _(by Adithya R)_  
[f74c352](https://github.com/PixelOS-AOSP/frameworks_base/commit/f74c352039afd536be05ab557aaee116c6371600) display: Don't spam log when display state changes _(by Adithya R)_  
[f77ddc9](https://github.com/PixelOS-AOSP/frameworks_base/commit/f77ddc93e6a1fe2d23192c5af8aeee3b16f32de1) core: Update freeze IDs of ContextualSearch for QPR1 _(by COSMIC)_  
[fb331bb](https://github.com/PixelOS-AOSP/frameworks_base/commit/fb331bb8766b33c11b4e1d3dad72d7f88c5db152) aapt2: add freeze IDs for ContextualSearch _(by Matt Filetto)_  
[05b2057](https://github.com/PixelOS-AOSP/frameworks_base/commit/05b20571b43fc9e36856043447739969be165cae) aapt2: support freezing private resource IDs _(by nift4)_  
[a80a27e](https://github.com/PixelOS-AOSP/frameworks_base/commit/a80a27eb82cb6c217788b3a2c9525f34317217c8) usb: Show charging notification only if power brick is disconnected _(by Adithya R)_  
[b1ef8a9](https://github.com/PixelOS-AOSP/frameworks_base/commit/b1ef8a92441bacce0776533d073742ab7aa49be7) LockPatternUtils: Decrease minimum pin length for auto confirmation _(by Mesquita)_  
[ce8ed38](https://github.com/PixelOS-AOSP/frameworks_base/commit/ce8ed385eb5a2f7a3646bc3480c5c47d00fc54d0) toast: fix bg color not changing with theme change _(by SuperDroidBond)_  
[58c7821](https://github.com/PixelOS-AOSP/frameworks_base/commit/58c7821e4eb09eaf35eb77a33f9001906fb05cdf) GnssLocationProvider: Implement xtra-daemon toggle _(by Michael Bestas)_  
[6fa986f](https://github.com/PixelOS-AOSP/frameworks_base/commit/6fa986f88dffbbf10861a9c2854d4a3988bf09e8) GnssLocationProvider: Implement PSDS periodic download toggle _(by Michael Bestas)_  
[ec19dcb](https://github.com/PixelOS-AOSP/frameworks_base/commit/ec19dcb215686956f41a67f42786540c135528a5) GnssLocationProvider: Disable AGPS by default, it'll be enabled in Se… _(by Chirayu Desai)_  
[2c9c690](https://github.com/PixelOS-AOSP/frameworks_base/commit/2c9c690ef2cf4d9d42e83914f24cb82e6849db0f) Ignore AGPS toggle during user-initiated emergency calls _(by Chirayu Desai)_  
[accba6f](https://github.com/PixelOS-AOSP/frameworks_base/commit/accba6fd1626a0ee24bd1770663c1d0395a8052a) Remove sensitive info from SUPL requests _(by Tommy Webb)_  
[e6d04a8](https://github.com/PixelOS-AOSP/frameworks_base/commit/e6d04a8cbb0744b88cbe52860f22041605d2be6e) SystemUI: Restore 14 QPR1 FingerprintInteractiveToAuth handling _(by LuK1337)_  
[94d4977](https://github.com/PixelOS-AOSP/frameworks_base/commit/94d49771046faac61cb6b31ec950928e5dab87a2) SystemUI: Add FingerprintInteractiveToAuthProvider implementation _(by Adithya R)_  
[14c74a8](https://github.com/PixelOS-AOSP/frameworks_base/commit/14c74a89db1812fa47f7a8bef6b87760619af93e) HidlFingerprintSensorConfig: UNKNOWN -> UNDER_DISPLAY_OPTICAL _(by LuK1337)_  
[fec76b7](https://github.com/PixelOS-AOSP/frameworks_base/commit/fec76b79463cca66ef2339317c93ec16b37804f4) HidlFingerprintSensorConfig: Add support for HIDL workaround props _(by LuK1337)_  
[0a456ea](https://github.com/PixelOS-AOSP/frameworks_base/commit/0a456eaaabef80e04a3b63cbd3f71de7e48b5c6f) core: Implement ADBRootService _(by LuK1337)_  
[17c2fa0](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/17c2fa0732981e7a1f29af19630e0345f3b1cd18) Settings: Hide Flashlight _(by Michael W)_  
[a6a311f](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/a6a311f25df198617353833597d899a94a93cb57) Settings: make sure Wifi exists before adding controllers _(by Timi Rautamäki)_  
[2709ac0](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/2709ac05d5136ad52595ca9b72f3e7cdfb9365a4) Settings: Improve touch gestures preferences _(by jhenrique09)_  
[bb72c63](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/bb72c6300dba8cea85cddf1c69fb81aba91de7a8) Settings: Allow devices to provide remote gesture preferences _(by Bruno Martins)_  
[dabd99f](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/dabd99f3cf1d0b773cc579d43e72c40457f94929) Settings: Add preference for TouchGestures _(by Anushek Prasal)_  
[8449a7b](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/8449a7b8aff79ee9982fd55cdda2aff4a34c2a3b) Settings: Display: Add High Touch Polling Rate Support _(by Ramii Ahmed)_  
[a778e8c](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/a778e8c2b68e73aaf0c632ec7607da6072f96895) Settings: Add high touch sensitivity and touchscreen hovering toggles _(by LuK1337)_  
[ed7815c](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/ed7815c28bf97bdcd9b3b0123fb4cd526c269bb0) Settings: Changes for LiveDisplay _(by jhenrique09)_  
[d334365](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/d33436561a05b094c2422291900f456ca759eadd) Settings: Add charging control preferences _(by Danny Trunk)_  
[dd5a2fd](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/dd5a2fde9c146a675679a4af6b84f41320449705) Settings: IS_DEBUGGABLE -> IS_ENG _(by jhenrique09)_  
[0774353](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/07743530508fb3a1de8a8e549b7bbe9ad9b54c4f) Settings: Bring in missing lottie animations _(by Adithya R)_  
[51a3992](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/51a3992472c4426227c833134e28e0517eed69d1) Settings: Add missing illustration for camera gesture _(by Adithya R)_  
[5ef510d](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/5ef510d643982058435232d71d53247e9077238a) Settings: Add private dns icons _(by penglezos)_  
[64f208f](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/64f208f0015446f9aa9cdd34792fc3500178703d) Settings: Use font configs instead fonts directly _(by Pranav Vashi)_  
[14b405e](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/14b405ee2256447f562c92d48a72df028cec40dc) Settings: use Glif themed button bar _(by Timi Rautamäki)_  
[94f89cf](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/94f89cf7793d96f785f27b975c27093df57279e0) Settings: Expose radio info (*#*#4636#*#*) _(by xyyx)_  
[a102040](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/a102040427ae80434cee0e041a8e5e7e4cfc579d) Settings: Long press to copy wifi password _(by Ido Ben-Hur)_  
[88a5969](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/88a5969badadd0cb61699585472992be38a852f7) Settings: Use default letter spacing for category titles _(by Danny Lin)_  
[b71e617](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/b71e6178ffef6c0c8188747a8b5bef3b4c5e31c2) Settings: Show user's Google avatar on the homepage _(by Jason Edson)_  
[e96d7c1](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/e96d7c12503df4b19d27d681e1c83a49756b78c6) Settings: Force disable top level support preference _(by jhenrique09)_  
[fd973bc](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/fd973bc97142c95c7c7e3bab548e6de507b33b09) Expand abbreviation in average memory usage string _(by Danny Lin)_  
[772464c](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/772464c904b5e1eb2f36b6dd9d3892f756b9eb98) Settings: Build custom-preference library _(by jhenrique09)_  
[29588ee](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/29588eeffeeae1c5e00309432e2161919cf919bc) Settings: Switch to VERSION.INCREMENTAL instead of FINGERPRINT _(by palaych)_  
[ceec196](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/ceec19615ee9a064087a9721dd156091f2fdf109) Settings: Allow sorting Applications by size _(by Roman Royer)_  
[69be951](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/69be951811f5ddf0411d5f3dbd98b36fedc09a97) Disable notification channel warnings by default _(by Bruno Martins)_  
[a5b64b9](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/a5b64b99811a1ebec6c9249128eeca09606930a6) DevelopmentSettings: Disable automatic updates _(by Henrique Silva)_  
[f04a1dc](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/f04a1dc45597e5b0d9da7b54472062b1a0862dd6) Settings: Don't show module version if isn't a date _(by jhenrique09)_  
[111c949](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/111c949a8c474102728bcc6c4fd503a3d3e14190) QS dev tiles: Don't set them to active area _(by Alex Cruz)_  
[c38afac](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/c38afacc50aa32a149e76e4d915e710ae5690510) Settings: Set the default account provider to Google _(by jhenrique09)_  
[b3c5914](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/b3c5914f3da883c9e2d1078c1968e7041181175f) Remove the Automatic ota check option but be sure it's disabled _(by ezio84)_  
[c63ccd4](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/c63ccd44b66c76c56b03fe7541aa352a628e99f4) Settings: Append custom version on build display id _(by jhenrique09)_  
[bcdb1ed](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/bcdb1edda2ca62ae9c1699d09a91015290feb08f) Settings: Fix regulatory info availability check _(by Ido Ben-Hur)_  
[2d1f23c](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/2d1f23c374bf5b098e6e263a308a45a0db3467d2) Settings: Redo "Good news, `encryptable=footer` is broken" _(by Michael W)_  
[23e44f4](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/23e44f4b346367f222838564a34bc54116a4903d) Settings: Add toggle for 60Hz refresh rate on battery saver _(by Adithya R)_  
[f4ac325](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/f4ac325404b4df4f7fd2adda7cdf085aef3476cc) AGPS: Mention that it's ignored during user-initiated emergency calls _(by Chirayu Desai)_  
[908d0aa](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/908d0aa4bd06cb0b3908f00c989def90665d1c97) Settings: Add switch preference for AGPS _(by juwei)_  
[a6db874](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/a6db8746366e072a9b3c98db5f9452b88f74f981) Settings: Add global heads up toggle _(by Adithya R)_  
[a78941e](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/a78941ebb9645b60a5f07f95aaf7706f00e733a2) Settings: Add QS tile for refresh rate indicator _(by Adithya R)_  
[4a3d6f6](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/4a3d6f63bf496ef1ff856ac6b8698e74a8e03463) Settings: Introduce new refresh rate selector page _(by Adithya R)_  
[c96db47](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/c96db47e38df2d64674c195284eef9e2c155eb51) ChooseLockPassword: Decrease minimum pin length for auto confirm _(by Vishalcj17)_  
[cf7a076](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/cf7a0764b28121075f6f4b132f942649bbaae654) Settings: Move adb root toggle and make it independent _(by Bruno Martins)_  
[35324ee](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/35324eed165065827c2a183e4a9bbb892583eb4a) Settings: Disable adb root if developer options are disabled _(by Bruno Martins)_  
[749ddbb](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/749ddbbc6ea0c642afb76fe2095f6e648c78e877) Add toggle to enable ADB root _(by Luca Stefani)_  

## 2025-03-11
[f441986](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/f44198688feb43dc253d612637582937b194398a) Settings: Only show gesture navigation if device has a software nav bar _(by Rashed Abdel-Tawab)_  
[c0a549a](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/c0a549a530b7a69b4f87fef646ceb75fe94a8454) Remove useless USB page header _(by Michael Bestas)_  
[756b6a5](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/756b6a589424cd0beaeccfb6b191bdc5265488f4) get outer NFC preference to listen for changes _(by inthewaves)_  
[c96a614](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/c96a6147466b7e8040e3ef5728d162d533af43ff) Fix inconsistent USB preference screen title _(by Danny Lin)_  
[700f151](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/700f151643a8a4fdb284f7e70d1c98120cb2a8d0) Settings: Hide unsupported USB modes automatically _(by Wang Han)_  
[7b70c31](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/7b70c31558dd60d0c795c57e48fbd47a2dd45713) Settings: Check if we have any color modes declared in overlay _(by Luca Stefani)_  
[6fbd647](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/6fbd647a4c853066939ef0f176256896bcfcc9b0) Settings: Fix the failing strings _(by Michael Bestas)_  
[329c5b3](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/329c5b3502be8a8fe4823d905f8e6311d028e592) Don't reset A2DP offload when disabling developer settings _(by Michael Bestas)_  
[fa3c041](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/fa3c0419b63fd28376876e0aa135a9f85da2e4cf) Settings: Hide "Mainline module version" preference _(by Michael Bestas)_  
[cb44f05](https://github.com/PixelOS-AOSP/packages_apps_Settings/commit/cb44f05d79c5c9f596c715505c61d2bd99e12458) BasebandVersionPreferenceController: Trim baseband if needed _(by Bruno Martins)_  
[ded07f3](https://github.com/PixelOS-AOSP/build/commit/ded07f3846c1389d87190ae2bdc7db5fc668eade) Add `CHRE_DAEMON_LOAD_INTO_SENSORSPD` to soong_config_variable _(by Michael Bestas)_  
[f19e4f6](https://github.com/PixelOS-AOSP/build/commit/f19e4f6070680c93ee8cba6d27e55299b40ae099) Correct typo in chre_daemon_lpma_enabled Soong config _(by Nelson Li)_  

## 2025-03-10
[7b66260](https://github.com/PixelOS-AOSP/system_core/commit/7b6626056103b479992a7ba44e89b82214e6aa25) Revert "libprocessgroup: Remove schedtune support" _(by Nolen Johnson)_  
[f9d9341](https://github.com/PixelOS-AOSP/frameworks_av/commit/f9d93416ae939504bf98947fe2aabea4ce429b66) Reapply "Fix audio AppOps refcount mismatch" _(by Chirayu Desai)_  
[be994cd](https://github.com/PixelOS-AOSP/frameworks_av/commit/be994cde39b76eb798a6c5224d4e5715ef6edaa8) audioflinger: Adapt audio fix for wifi display to A15/r14 _(by Ido Ben-Hur)_  
[9a6a361](https://github.com/PixelOS-AOSP/vendor_aosp/commit/9a6a3617e8418b494739cd0ca6883ff658fc1c16) Revert "Add `androidx.compose.compiler_compiler-hosted-plugin` define" _(by Michael Bestas)_  
[3f5a953](https://github.com/PixelOS-AOSP/vendor_aosp/commit/3f5a95359bc84a574adc3473a30e84b70a2f9492) vars: March 2025 Security update and Quarterly Platform Release _(by Chirayu Desai)_  
[e1dc5ca](https://github.com/PixelOS-AOSP/build/commit/e1dc5ca304bf88e5e7a62483ca9ecf79e9d05450) Revert "Add tradeinmode to the system image." _(by Michael Bestas)_  
[ebad7c0](https://github.com/PixelOS-AOSP/build/commit/ebad7c00aa72ba765df9be099bcac458dfaa70ed) Remove additional DeviceDiagnostics reference _(by Michael Bestas)_  
[757b7e7](https://github.com/PixelOS-AOSP/build/commit/757b7e7ab238e4a3cedafcbf5dcd1b19f9f645b2) Merge tag 'android-15.0.0_r20' into fifteen _(by Hridaya Prajapati)_  
[c4f2657](https://github.com/PixelOS-AOSP/frameworks_native/commit/c4f2657e5e6bcd8d70f38f16c744f6f5f2c76b0f) Merge tag 'android-15.0.0_r20' into fifteen _(by Hridaya Prajapati)_  
[c00d454](https://github.com/PixelOS-AOSP/packages_modules_Connectivity/commit/c00d454124278198da5136599e5120928c8acf59) Merge tag 'android-15.0.0_r20' into fifteen _(by Hridaya Prajapati)_  
[f4439a7](https://github.com/PixelOS-AOSP/packages_services_Telecomm/commit/f4439a76fa51d9ae0670cc071924fef580a571f7) Merge tag 'android-15.0.0_r20' into fifteen _(by Hridaya Prajapati)_  
[61f8531](https://github.com/PixelOS-AOSP/system_core/commit/61f85312ad36b509dbbbbadb979fa7bd6f068820) Merge tag 'android-15.0.0_r20' into fifteen _(by Hridaya Prajapati)_  
[22a7f9c](https://github.com/PixelOS-AOSP/bootable_recovery/commit/22a7f9cad02e3159f929ad02d0cfb4b1b3084eab) recovery_ui: Bump to android.hardware.health-V4-ndk _(by Michael Bestas)_  
[0033057](https://github.com/PixelOS-AOSP/bootable_recovery/commit/0033057d75bdcaac57fd1ed1c81ab56c1b34964a) Merge tag 'android-15.0.0_r20' into fifteen _(by Hridaya Prajapati)_  
[1d5b40c](https://github.com/PixelOS-AOSP/bionic/commit/1d5b40c343edbd7ad7fb49aee74fde02c1b3aadb) Merge tag 'android-15.0.0_r20' into fifteen _(by Hridaya Prajapati)_  

## 2025-03-08
[f62e5a5](https://github.com/PixelOS-AOSP/vendor_aosp/commit/f62e5a56056f640f793be4c5e673fc06e4e90bd8) config: Move wifionly defination to tablet wifionly makefile _(by AdarshGrewal)_  

## 2025-03-01
[480eaff](https://github.com/PixelOS-AOSP/vendor_google_overlays_ThemeIcons/commit/480eaff9890b76438adc3595f7d697723b59a8e1) PixelLauncherIconsOverlay: Use MIUICamera icon for OPlus Camera app _(by Karan Parashar)_  
