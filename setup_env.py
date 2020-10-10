"""
Setup a python virtual environment with pip and install the dependencies from lib/
"""

import venv
from pathlib import Path
import subprocess
import os

print("Installing virtual environment...")
venv.create("venv", with_pip=True)  # create venv in venv/ dir

# find python bin path
bin_dir = Path(Path(__file__).parent.absolute() / "venv")
if Path(bin_dir / "bin").exists():  # *nix
    bin_dir = Path(bin_dir / "bin")
elif Path(bin_dir / "Scripts").exists():  # windows
    bin_dir = Path(bin_dir / "Scripts")
else:
    print("Could not find venv/bin/ or venv/Scripts")
    raise SystemExit

# find python executable path
if Path(bin_dir / "python3").exists():
    py_path = Path(bin_dir / "python3")
elif Path(bin_dir / "python").exists():
    py_path = Path(bin_dir / "python")
elif Path(bin_dir / "python3.exe").exists():
    py_path = Path(bin_dir / "python3.exe")
elif Path(bin_dir / "python.exe").exists():
    py_path = Path(bin_dir / "python.exe")
else:
    print("Could not find python executable in %s" % str(bin_dir))
    raise SystemExit

lib_dir = Path(Path(__file__).parent.absolute() / "lib")  # get path to lib/
requirements_path = Path(Path(__file__).parent.absolute() / "requirements.txt")  # path to requirements file

# install pip dependencies
print("Installing pip packages...")
command = [
    str(py_path),
    "-m", "pip", "install",
    "-r", str(requirements_path),
    "--no-index", "--find-links",
    "file://%s%s" % (str(lib_dir), os.sep)
]

subprocess.check_call(command)  # run install
print("Done")
