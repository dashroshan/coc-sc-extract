## COC Extract SC

A python script to batch extract PNG image sprite sheets from the ``...tex.sc`` files of the Clash of Clans game APK.

### Installation

This script uses a library called pylzham which requires ``Visual C++ build tools`` to install it through pip. To avoid complications, I recommend using Replit instead which is a free to use online IDE. Make an account on Replit and then [click here](https://repl.it/github/roshan1337d/cocExtractSC). Select the language as Python, enter ``python3 main.py`` in ``configure the run button`` field, and click done!





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
