flet build apk
adb install build/apk/app-arm64-v8a-release.apk
adb shell am start -n org.openinsectid/org.openinsectid.MainActivity
