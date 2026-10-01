# 04 — Dynamic Analysis (watch the app run)

Run the app in an emulator or rooted test device you own. Never test apps
you have no right to analyze.

1. List processes and attach Frida:
   ```bash
   frida-ps -U
   frida -U -f com.example.app -l hook.js --no-pause
   ```
2. Minimal `hook.js` (log a crypto call):
   ```js
   Java.perform(() => {
     const Cipher = Java.use("javax.crypto.Cipher");
     Cipher.getInstance.overload("java.lang.String").implementation = function (t) {
       console.log("[cipher] " + t);
       return this.getInstance(t);
     };
   });
   ```
3. No-root exploration with Objection:
   ```bash
   objection -g com.example.app explore
   android sslpinning disable
   android root disable
   ```
4. Watch traffic with an emulator proxy (HTTP Toolkit / mitmproxy), storage
   with `adb shell run-as`, logs with `adb logcat | grep <pid>`.
5. SSL pinning / root detection slow you down on purpose: bypass only on
   your own test builds to keep studying the protocol, and document each
   check you find (this is the defensive value).

What to record: runtime API calls, network endpoints + cert behavior,
anti-debug/root/pinning checks and where they live in code.
