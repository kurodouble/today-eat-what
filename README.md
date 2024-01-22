# Project Title

> Help to choose where to eat (#codeIsLife)

## Table of Contents

- [Get Started](#get-started)
- [Make Executable File](#make-executable-file)

## Get Started <a name="get-started"></a>
1. [Download Git](https://www.git-scm.com/downloads)
2. Open a directory in terminal
3. Clone repository
    ```bash
    git clone https://github.com/kurodouble/today-eat-what.git
    ```
4. Make a new branch
    ```bash
    git branch -M [Your Branch Name]
    ```
5. Set upstream for that branch
   ```bash
    git --set-upstream origin [Your New Branch Name]
   ```
## Make executable file <a name="make-executable-file"></a>
1. Install PyInstaller (install npm forehand)
   ```bash
   npm install pyinstaller
   ```
3. Make exe file using PyInstaller (For single python script)
   ```bash
   pyinstaller --onefile --name [OUTPUT_NAME] --icon=[ICON_FILE_NAME] --distpath=[OUTPUT_DIRECTORY] [SCRIPT_FILE].py
   ```
