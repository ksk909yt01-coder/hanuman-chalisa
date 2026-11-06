# Hanuman Chalisa app

The whole app is one offline page: `app/src/main/assets/index.html` (source: `src/app.html`).
`MainActivity.java` is a small WebView wrapper that adds vibration, keep-screen-on, sharing and read-aloud.

## Get the APK (no Android Studio needed)
1. Create a free GitHub account and a new empty repository.
2. Upload all files from this folder (keep the folder structure, including `.github/workflows`).
3. Open the repository's **Actions** tab, choose **Build APK**, tap **Run workflow**.
4. When it finishes (about 5 minutes) open the run and download the **HanumanChalisa-apk** file. Unzip it and install `app-debug.apk` (allow "install unknown apps" when asked).

## Or build locally
Install Android Studio, open this folder, choose Build > Build APK(s).
If you change `src/app.html`, run `python3 tools/build_assets.py` to refresh the page inside the app.
