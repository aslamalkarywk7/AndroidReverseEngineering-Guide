# Tooling Overview

This chapter introduces the **essential open-source tools** for Android reverse engineering.  
We focus on reproducible installation, version pinning, and sanity checks.

---

## APKTool
- **Purpose**: Decode and rebuild APK resources and Smali code.  
- **Website**: https://ibotpeaches.github.io/Apktool/  
- **Install (Linux/Mac/WSL)**:  
```bash
wget https://bitbucket.org/iBotPeaches/apktool/downloads/apktool_2.9.3.jar -O apktool.jar
chmod +x apktool.jar
sudo mv apktool.jar /usr/local/bin/apktool
```
- **Basic usage**:  
```bash
apktool d app.apk -o out_dir   # decode resources + smali
apktool b out_dir -o new.apk   # rebuild
```

---

## JADX
- **Purpose**: Decompile DEX → Java source. GUI + CLI.  
- **Website**: https://github.com/skylot/jadx  
- **Install**:  
```bash
git clone https://github.com/skylot/jadx.git
cd jadx
./gradlew dist
./build/jadx/bin/jadx-gui   # run GUI
```
- **Basic usage (CLI)**:  
```bash
jadx -d out app.apk   # output Java sources
```

---

## Ghidra
- **Purpose**: Reverse engineering native libraries (.so) and JNI functions.  
- **Website**: https://ghidra-sre.org  
- **Install**: Download ZIP, extract, run `ghidraRun`.  
- **Usage**: Import `.so` library, analyze with decompiler, search for crypto APIs, etc.

---

## Frida
- **Purpose**: Dynamic instrumentation of apps at runtime.  
- **Website**: https://frida.re  
- **Install (pip)**:  
```bash
pip install frida-tools
frida-ps -U   # list processes on USB device
```
- **Usage**: Write hooks in JavaScript to intercept methods.

---

## Objection
- **Purpose**: Convenience wrapper around Frida for mobile exploration.  
- **Website**: https://github.com/sensepost/objection  
- **Install**:  
```bash
pip install objection
objection --help
```
- **Example**:  
```bash
objection -g com.example.app explore
```

---

## Androguard
- **Purpose**: Python toolkit for DEX/APK/XML analysis.  
- **Website**: https://github.com/androguard/androguard  
- **Install**:  
```bash
pip install androguard
```
- **Usage**:  
```python
from androguard.misc import AnalyzeAPK
a,d,dx = AnalyzeAPK("app.apk")
print(a.get_package())
```

---

## MobSF
- **Purpose**: Automated static & dynamic analysis of Android/iOS apps.  
- **Website**: https://github.com/MobSF/Mobile-Security-Framework-MobSF  
- **Run with Docker**:  
```bash
docker run -it --rm -p 8000:8000 opensecurity/mobile-security-framework-mobsf:latest
```

---

## Cutter (Rizin)
- **Purpose**: GUI for Rizin (fork of Radare2).  
- **Website**: https://cutter.re  
- **Usage**: Great for ELF binaries used in Android apps.  

---

## Additional Utilities
- **dex2jar + JD-GUI**: Convert DEX → JAR, then browse with JD-GUI.  
- **uber-apk-signer**: Re-sign modified APKs easily.  
- **mitmproxy / Burp Suite**: Inspect HTTPS traffic.

---

> **Tip**: Keep each tool version logged in your lab notes. Many RE issues come from version mismatches.
