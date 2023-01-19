from cx_Freeze import setup, Executable
import sys

base = None

if sys.platform == 'win32':
    base = None


# Nome do Arquivo que contém seu código
executables = [Executable("auto.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {

        'packages': packages,
    },

}

setup(
    name="auto",
    options=options,
    version="4.0",
    description='autopy create by PSJoon',
    executables=executables
)
