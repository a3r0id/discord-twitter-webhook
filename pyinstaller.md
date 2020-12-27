# How to package as a portable executable


- Install Pyinstaller: `pip install pyinstaller`

- Open a terminal @ the location of `webhook.py`.

- Run `pyinstaller -F webhook.py -i icon.ico`

- Thats it! The exectuable will be located @ `../dist/webhook.exe`

- Note: The executable will run on most windows machines,
no Python installation or dependencies are required!

- Note: You must include the config.json in the directory of your executable.
