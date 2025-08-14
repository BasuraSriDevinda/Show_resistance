import os
import platform
import subprocess

file_path = r"C:\Users\Win 10\OneDrive - University of Kelaniya\Desktop\PythonProject\resistor_color_code_complete.xlsx"  # Put your actual Excel file path here
def exelOpen(n):

    if platform.system() == "Windows":
        os.startfile(file_path)
    elif platform.system() == "Darwin":
        subprocess.call(["open", file_path])
    else:
        subprocess.call(["xdg-open", file_path])

    pass