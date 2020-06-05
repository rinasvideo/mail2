@echo off
pyinstaller addhost.py -F --exclude tkinter --exclude xml
pause