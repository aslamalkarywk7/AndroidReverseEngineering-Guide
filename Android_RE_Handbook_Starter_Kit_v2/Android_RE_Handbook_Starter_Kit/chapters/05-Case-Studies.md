# 05 — Case Studies (two short, reproducible patterns)

## Case A: hardcoded API key in smali

1. `apktool d app.apk -o app_case && grep -Rni "api_key" app_case/smali | head`.
2. Note the `const-string` register holding the key.
3. Replace the value with a test key, rebuild, sign, install:
   ```bash
   apktool b app_case -o app_case.apk
   apksigner sign --ks test.jks --out app_signed.apk app_case.apk
   adb install -r app_signed.apk
   ```
4. Lesson for defenders: keys in the client are public. Move secrets
   server-side or scope them per-install with rotation.

## Case B: debuggable WebView bridge

1. Manifest shows `android:debuggable="true"`; jadx shows
   `addJavascriptInterface(new Bridge(), "Android")`.
2. Attach Frida, list the bridge methods, call one with a test string.
3. Rebuild a fixed variant: `debuggable=false`, bridge methods validating
   origin + input, and re-run the same hook to prove it no-ops.
4. Lesson for defenders: bridges are remote APIs. Treat every exposed
   method like a public endpoint: auth, validate, log.
