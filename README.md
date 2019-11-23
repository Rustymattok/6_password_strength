# Password Strength Calculator

This script for score level of password:

 - score password include numeric
 - score password include upper letter
 - score password include lower letter
 - score password include symbols
 - score password not contain words form blacklist

# Quick start

The script requires installed Python 3.5 or higher
The script requires file with black list,download it to the folder of script(link below) 
[link to github](https://github.com/danielmiessler/SecLists/blob/master/Passwords)
Download default file for compare Most-Popular-Letter-Passes.txt
```bash
$ python password_strength.py
password: <enter your password>
```
If you want to choose your file for compare from list put next command.
```bash
$ python password_strength.py -f <file name>
password: <enter your password>
```
# The sample of result script
We receive common score of password

```bash
score of password: 10.0
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
