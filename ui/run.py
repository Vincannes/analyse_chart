import subprocess

cmd = "C:\\Users\\vince\\AppData\\Roaming\\Python\\Python39\\Scripts\\pyside2-uic.exe graphic_view.ui > graphic_view.py"
cmd = "C:\\Users\\vince\\AppData\\Roaming\\Python\\Python39\\Scripts\\pyside2-uic.exe search.ui > search.py"

subprocess.run(cmd, shell=True)