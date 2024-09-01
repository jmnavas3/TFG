# from configuration.configuration import Config
import subprocess
import os

print("ubicacion del archivo: " + os.path.dirname(__file__))
parent_dir = os.path.join(os.path.dirname(__file__), "..")
print(parent_dir)
subprocess.run(["pwd"])
subprocess.run(["sh", "script.sh"])

# try:
#     config = Config.create('/config/config.yml').__dict__
#     print(config)
# except Exception as e:
#     print(e)
