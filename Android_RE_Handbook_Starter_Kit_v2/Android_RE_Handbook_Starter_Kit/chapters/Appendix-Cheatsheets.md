# Appendix — Cheatsheets

| Task | Command |
|---|---|
| Decompile | `apktool d app.apk -o out` |
| Rebuild | `apktool b out -o app.apk` |
| Sign (modern) | `apksigner sign --ks k.jks --out s.apk app.apk` |
| Sign (legacy) | `jarsigner -verbose -keystore k.jks app.apk alias` |
| Install | `adb install -r s.apk` |
| Full decompile | `jadx -d jadx_out app.apk` |
| Processes | `frida-ps -U` |
| Attach | `frida -U -f com.pkg -l hook.js --no-pause` |
| No-root explore | `objection -g com.pkg explore` |
| Disable pinning (test only) | `android sslpinning disable` |
| Logs | `adb logcat \| grep <pid>` |
| String hunt | `grep -RniE "api[_-]?key\|secret\|token" out --include=*.java` |

Manifest checklist: exported components, permissions, `debuggable`,
`usesCleartextTraffic`, backup rules, deep-link schemes.
