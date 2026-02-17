from os import path, remove
from subprocess import run

base_path = path.split(__file__)[0]
run(f"python -m pip install -r {path.join(base_path, "requirements.txt")}")


# with open(path.join(basepath, "startup.cmd"), "w") as startup:
#     startup.truncate(0)
#     startup.write(r"start python %CD%\update.py && start python %CD%\src\server.py && start python %CD%\src\client.py")

# remove(__file__)