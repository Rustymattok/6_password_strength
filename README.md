# Password Strength Calculator

This script for score level of password:

 - score 2.5 if password include numeric
 - score 2.5 if password include upper letter
 - score 2.5 if password include symbols
 - score 2.5 if password not contain words form blacklist

# Quick start

The script requires installed Python 3.5 or higher
The script requires file with black list,download it to the folder of script(link below) 
[link to github](https://github.com/danielmiessler/SecLists/blob/master/Passwords/Most-Popular-Letter-Passes.txt)

```bash
$ python password_strength.py
password: <enter your password>
```

# The sample of result script
We receive common score of password

```bash
score of password: <your password> : 10.0
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
