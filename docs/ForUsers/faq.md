# Frequently Asked Questions

## What is the aim of PixelOS?

To provide an experience similar to Google Pixel phones with numerous performance enhancements and a small amount of useful additional features.

## Is this a Pixel GSI/Port?

No, this a source-built custom Android ROM [just like LineageOS].

## How do I flash it on my device?

Head over to the [download page](https://pixelos.net/download) for your device, you should find instructions for your device there. [Note: Instructions may not appear for few devices, ask your maintainer to add it]

## Can I get all features of Google Pixel devices on PixelOS?

No, it is practically not possible. Some features need hardware support and have different other requirements.

## Why is the Quick Settings black in light mode?

With the aim of the project being to provide a similar experience in look and feel to a Google Pixel device, the quick settings will always remain black in light and dark theme the same way it does on Pixel devices.

## When is the next update?

PixelOS is free to use and open-source. None of the maintainers are obligated to release updates whenever you want them to, and you are not entitled to them. **Be patient; updates will be released when they are ready.**

:::danger Asking for ETAs

Repeatedly asking for updates ("ETAs") through the use of euphemisms in the community, such as "Is there an update coming soon?" will not be tolerated.

:::

## How to report bugs?

[Refer to this guide](/docs/guides/BugReport) to learn how to take proper logs. Then send these logs over to your maintainer through our community.

## Should I clean flash to upgrade to a newer version?

If a clean flash is necessary, it will be mentioned on either the release post on Telegram or in the changelog section of the device page on the website. If a clean flash isn't mentioned as being necessary, a dirty flash should be fine.

## Does PixelOS give good battery life?

We can't give estimates battery life or SOT (Screen On Time) as it is very subjective and depends on a lot of variables from obvious things like Screen Brightness to things which you probably did not know could affect your battery like your network/Wi-Fi coverage.

## When PixelOS for my XYZ device?

Head over to our Official Downloads Page, if you find your device there, then it has/had an official PixelOS build, if not, it does not.
If you really want to try out PixelOS for your device, ask a developer/maintainer to build it for you, otherwise you can learn how to build ROMs and do it yourself.

## Can I PM you?

No.

## Why we use cat pics everywhere? [Seriously...](https://t.me/pixeloschat/134098)

Because they are cute and adorable.

## Will we add x feature?

We don't accept feature requests.

## DFE

DFE is not recommended or supported on PixelOS. Android expects the system to be encrypted, so decrypting it introduces all manner of strange behaviour, so we don't accept bug reports from decrypted users. Use at your own risk and do not expect support.

Credit to SebaUbuntu for this explanation as to why we don't support it. For further reading you can check out [this](https://kubersharma001.com/reasons-to-stay-encrypted-on-android-and-the-risks-otherwise) blog post.

Little reminder on why you should not flash DFEs

- Userdata is NOT a sensitive partition, you can do whatever you want with it, but you'll never do damages, and also encryption process is 100% secure and there are 0 risks of bricking (you can actually have more issues if you flash DFE, will explain later)
  "But I need to format data everytime I flash a new ROM!" Stop flashing multiple ROMs, you should daily drive one, not ruining your EMMC/UFS by flashing 1747858 ROMs
  Also, if ROM maintainers recommends to not use DFE, don't use it
  Being decrypted or encrypted actually changes how Android handles booting
  TL;DR
  Basically Android has 2 phases during boot: pre-decryption and after-decryption
  If you disable encryption, there can be race conditions where stuff expects to start only after data has been decrypted but it starts together with core services, creating issues
  One example is in X00H and X00I, where if you run decrypted will break camera completely

- "data encryption on custom ROMs is useless": It's actually even more useful! If your device gets stolen, no one will be able to access your data, and the only way is to format data

Conclusion:
Unless you have a good reason (and there are none), do not never ever flash DFEs
We support DFE in PixelOS, if you report a bug and you're decrypted your issue will be happily discarded
