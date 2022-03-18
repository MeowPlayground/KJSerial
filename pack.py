import os
import shutil
if os.path.exists("./dist/KJserial.exe"):
    os.remove("./dist/KJserial.exe")

os.system(r"E:\Development\Environment\anaconda3\envs\qtserial\Scripts\pyinstaller.exe -F -w -i ./img/icon.ico run.py --clean")
os.rename("./dist/run.exe", "./dist/KJserial.exe")