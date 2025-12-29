[app]

# (str) Title of your application
title = IPC Calculator

# (str) Package name
package.name = ipcapp

# (str) Package domain (needed for Android package identifier)
package.domain = org.ahmednader

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (keep this default unless you add assets)
source.include_exts = py,png,jpg,kv,atlas,ttf,otf

# (str) Application versioning (you can bump this any time)
version = 0.1.0

# (list) Application requirements
# NOTE: keep it simple: python3 + kivy is enough for this app
requirements = python3,kivy

# (str) Supported orientation (portrait, landscape, all)
orientation = portrait

# (bool) Fullscreen mode
fullscreen = 0

# (str) Android entrypoint
android.entrypoint = org.kivy.android.PythonActivity

# (list) CPU architectures to build for
# arm64-v8a is required for modern devices; armeabi-v7a helps older ones
android.archs = arm64-v8a,armeabi-v7a

# (int) Minimum API your APK will support
android.minapi = 21

# (int) Target API (optional)
# android.api = 34

# (str) Android NDK (optional) - keep empty so Buildozer chooses a compatible one
# android.ndk = 25b

# (list) Permissions (not needed for this offline calculator)
android.permissions =

# (str) Icon (optional). Put an icon at assets/icon.png
icon.filename = assets/icon.png


[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2
