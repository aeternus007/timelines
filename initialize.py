from os import path, remove
from subprocess import run

base_path = path.split(__file__)[0]
run(f"python -m pip install -r {path.join(base_path, "requirements.txt")}")


with open(path.join(base_path, "startup.cmd"), "w") as startup:
    startup.truncate(0)
    startup.write(r"start python %~dp0update.py && start python %~dp0src\server.py && start python %~dp0src\client.py")

remove(__file__)