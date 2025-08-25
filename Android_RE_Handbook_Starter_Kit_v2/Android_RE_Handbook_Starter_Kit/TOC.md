# Table of Contents (Detailed)

## Part I — Foundations
1. Android Internals Overview
   1.1 OS Architecture (Linux kernel, HAL, Native, ART)  
   1.2 App Components (Activities, Services, Receivers, Providers)  
   1.3 Build Artifacts: AAB vs APK, DEX/ODEX, resources.arsc, V2/V3 signatures  
   1.4 Package formats, ABI/arch, shared libraries (.so)  
   1.5 Security model: permissions, sandboxing, SELinux, keystores

2. Legal & Ethics
   2.1 Authorized testing vs piracy  
   2.2 Handling personal data and secrets  
   2.3 Coordinated disclosure basics

3. Lab Setup
   3.1 Host OS setup (Windows/Linux/macOS)  
   3.2 Android Studio SDK/NDK essentials  
   3.3 Emulators: AVD, Genymotion, alternative emus  
   3.4 Physical devices: bootloader, root, Magisk basics  
   3.5 Proxying traffic: mitmproxy/Burp, cert installation, certificate pinning

## Part II — Static Analysis
4. Unpacking & Inspecting
   4.1 Extracting APK/AAB, bundletool, apks/apkm splits  
   4.2 signatures: apksigner, uber-apk-signer, checking integrity  
   4.3 File reconnaissance (aapt/aapt2, androguard, strings, file, binwalk)

5. Resources & Manifest
   5.1 AndroidManifest.xml (binary XML)  
   5.2 resources.arsc decoding, 9-patch assets  
   5.3 Localization, layouts, drawables

6. Bytecode & Decompilation
   6.1 DEX format, opcodes, registers  
   6.2 JADX & deobfuscation pipelines  
   6.3 dex2jar + JD-GUI vs JADX  
   6.4 Baksmali/Smali workflows  
   6.5 Architecture-aware disassembly (ARM/ARM64) for JNI bridges

7. Native Libraries
   7.1 ELF basics, symbols, relocations  
   7.2 Ghidra/Cutter (Rizin) navigation & decompilation  
   7.3 JNI entry points and signature mapping  
   7.4 String/crypto function hunting  
   7.5 Patch workflows (hex-editing, re-signing)

## Part III — Dynamic Analysis
8. Instrumentation & Hooking
   8.1 Frida basics: gadgets, server/client, spawn/attach  
   8.2 Objection quick start (hooking common APIs)  
   8.3 Logging, tracing, and inline patching  
   8.4 SSL pinning bypass techniques  
   8.5 Anti-debug/anti-hook detection and evasions

9. Traffic & Storage
   9.1 HTTP(S)/WebSockets, cert pinning patterns  
   9.2 Local storage (SharedPrefs/Room/SQLite)  
   9.3 Key/secret discovery, keystore handling  
   9.4 IPC and Binder analysis

10. Automation & Scripting
   10.1 Androguard programmatic analysis (Python)  
   10.2 Ghidra scripting (Java/Python)  
   10.3 Frida scripts patterns and templating  
   10.4 Batch pipelines (analyze fleets of APKs)

## Part IV — Protections & Countermeasures
11. Obfuscation/Protection
   11.1 R8/ProGuard, name/resource obfuscation  
   11.2 Control-flow/data-flow obfuscation  
   11.3 Packing/encryption and loaders  
   11.4 Emulator/root/debugger checks  
   11.5 Detecting protections in the wild

12. Unpacking & De-obfuscation Case Studies
   12.1 Resource-only packers  
   12.2 DEX-in-memory loaders (dump at runtime)  
   12.3 Native protectors and integrity checks  
   12.4 Case: MultiDex & split APKs  
   12.5 Case: In-app updates, dynamic features

## Part V — Hands-on Projects
13. Project A: Static Audit of a Medium App  
14. Project B: Hooking business logic and bypassing SSL pinning  
15. Project C: JNI reverse engineering and patching a native check  
16. Project D: Automating large-scale APK triage (CLI + Python)  
17. Project E: End-to-end report and remediation plan

## Part VI — Appendices
A. Tooling Cheat Sheets (APKTool, JADX, Androguard, Ghidra, Frida, Objection)  
B. Common Smali patterns & recipes  
C. ARM/ARM64 quick reference  
D. TLS pinning patterns & bypass matrix  
E. Sample Frida scripts repository map  
F. Glossary, Further Reading, and References
