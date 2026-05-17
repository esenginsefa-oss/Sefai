[app]
title = SefaAiBooster
package.name = sefaaibooster
package.domain = org.sefaai
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy

[buildozer]
log_level = 2
warn_on_root = 1

[android]
android.permissions = SYSTEM_ALERT_WINDOW, WAKE_LOCK, FOREGROUND_SERVICE
android.api = 33
android.build_tools_version = 33.0.1	
android.minapi = 21
android.archs = arm64-v8a	
android.accept_sdk_license = True
android.ndk = 25.2.9519653
android.sdk_components = tools,platform-tools,build-tools;33.0.1

