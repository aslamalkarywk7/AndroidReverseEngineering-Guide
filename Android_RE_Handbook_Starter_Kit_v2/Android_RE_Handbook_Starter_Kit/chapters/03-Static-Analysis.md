# 03 — Static Analysis (APK anatomy without running anything)

Static analysis reads the APK as a zip of code + resources. Workflow:

1. Unzip the APK and list the layout:
   ```bash
   apktool d app.apk -o app_static
   ls app_static            # AndroidManifest.xml, smali/, res/, lib/, assets/
   ```
2. Read `AndroidManifest.xml` first: package name, `minSdkVersion`, exported
   activities/services/receivers, permissions, `application/@debuggable`.
3. Decompile to Java for readability (try all three, compare output):
   ```bash
   jadx -d jadx_out app.apk
   ```
4. Search the decompiled tree for interesting strings:
   ```bash
   grep -RniE "api[_-]?key|secret|token|password|http" jadx_out/sources --include=*.java | head -30
   ```
5. Inspect `smali/` only when you must patch (see chapter 05). Prefer the
   jadx output for understanding; smali for editing.
6. Native code: list `lib/<abi>/*.so`, open in Ghidra, check `JNI_OnLoad`
   and exported JNI symbols (`javah` naming).

What to record: manifest attack surface, hardcoded secrets/URLs, crypto use
(`Cipher.getInstance` strings), WebView settings (`setJavaScriptEnabled`,
`addJavascriptInterface`), exported components without permissions.
