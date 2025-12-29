[app]

# (str) Title of your application
title = IPC Calculator

# (str) Package name
package.name = ipcapp

# (str) Package domain (needed for Android package identifier)
package.domain = org.ahmednader

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf,otf

# (str) Application versioning
version = 0.1.0

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientation (portrait, landscape, all)
orientation = portrait

# (bool) Fullscreen mode
fullscreen = 0

# (str) Android entrypoint
android.entrypoint = org.kivy.android.PythonActivity

# (list) CPU architectures to build for
android.archs = arm64-v8a,armeabi-v7a

# ===================== ANDROID BUILD SETTINGS =====================

# (int) Minimum API your APK will support
android.minapi = 21

# (int) Target Android API (must match platform installed in workflow)
android.api = 34

# (str) Android NDK version (stable with Buildozer)
android.ndk = 25b

# (str) Force SDK Build Tools Version (prevents 36.x problems)
android.sdk_build_tools_version = 34.0.0

# (bool) Auto accept Android SDK license
android.accept_sdk_license = True

# (list) Permissions (none needed)
android.permissions =

# (str) Icon
icon.filename = assets/icon.png

# ================================================================


[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (bool) Show warning messages
warn_on_root = 1
