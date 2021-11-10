## COC Extract SC

This python script allows you to extract the ``...tex.sc`` files of the Clash of Clans game APK which contains the in-game image sprite sheets in PNG format.

### Installation

```bash
pip install pillow
pip install pylzham
```

### Usage

1. Download the [Clash of Clans apk](https://clash-of-clans.en.uptodown.com/android/download) file.
2. Use [WinRAR](https://www.win-rar.com/download.html?&L=0) or any similar tool to extract the apk.
3. Open `\assets\sc` and copy the `...tex.sc` files that you want to extract into the `main.py` directory.
4. Run the `main.py` file and enter the name of the file that you want to extract. For example: `ui_tex` if you want to extract the `ui_tex.sc` file. The PNG image contents will then be extracted in the same directory as the `main.py` file.


### Known Issue

You might face trouble while installing the pylzham library. It requires Visual C++ build tools 2015+ for using this. Alternatively, you can use Replit which is a free to use online IDE to run this script. To do so, create an account there and click the button below.

[![Run on Repl.it](https://repl.it/badge/github/roshan1337d/cocExtractSC)](https://repl.it/github/roshan1337d/cocExtractSC)
