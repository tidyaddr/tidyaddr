import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os","tidycsv"], "includes": ["tkinter"], "icon":"resources/icon.ico",}




# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name = "TidyAddr",version = "0.1",description = "Tidy up a Street Address Line",options = {"build_exe": build_exe_options},executables = [Executable("tidycsv/tidyaddr.py",base=base,shortcutName="TidyAddr",shortcutDir="DesktopFolder")])