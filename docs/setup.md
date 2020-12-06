# Setup
Notes on the setup process and templates

## Virtual Environment
It is highly recommended to use a Python virtual environment to install
dependencies and run the program. This can be done with `python -m venv <env_name>`
and pip can be used from the venv with `<venv_path>/bin/python3 -m pip`.

## Building Dependencies
Dependencies for the project include `yarl` and `multidict` which follow PEP 517 and must be
compiled and built at install time (unless a pre-built wheel is available).

### Windows
On Windows building these require the
[C++ Build Tools](https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2019)
installed. Often times trying to install without this is met with an error along the lines of,
"Microsoft Visual C++ 14.0 or greater is required," or
"Could not build wheels for yarl, multidict which use PEP 517 and cannot be installed directly."

### Linux
Usually all the necessary tools are installed and you won't need to do anything extra. In the rare case
something is missing, do the following:
* Ensure GCC is installed
* Ensure python3-dev is installed
    * Ensure the necessary headers can be found in /usr/include/
    * `sudo ln -sv /usr/include/<python_version>/* /usr/include/`
  
## System Service
Creating a system service is the best way to manage and run the package.

*/etc/systemd/system/subpar.service*
```text
[Unit]
Description=Insult Bot Runtime Service
After=network.target
StartLimitIntervalSec=0

[Service]
Type=simple
Restart=always
RestartSec=1
User=<user>
WorkingDirectory=<package_root>
ExecStart=<python_path> <path_to_main.py>

[Install]
WantedBy=multi-user.target
```
