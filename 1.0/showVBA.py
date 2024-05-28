import os
import subprocess
from subprocess import run


#!/usr/bin/env python
# os.system
# C:\Users\Bruger\OneDrive\Desktop\oledump\
cmdString = r"python C:\datamatiker\dat4sem\Python\excel_cracker2\oledump\oledump.py -p plugin_vbaproject -q C:\Users\Bruger\OneDrive\Desktop\excelpassword\vba\passwordr.xlsm"

# subprocess.call(cmdString)
output = run(cmdString, capture_output=True).stdout
print(output.decode("utf-8"))
output_decoded = output.decode("utf-8")

temp = output_decoded.splitlines()

for line in temp:
    print(line[2:10])

for line in temp:
    if line[2:10] == "Password":
        print("PASSWORD:", line[12:])

