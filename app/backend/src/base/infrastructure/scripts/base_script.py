import subprocess

from app.backend.configuration.configuration import Config


class BaseScript:
    _path = None
    script_name = None
    command = ['bash']
    params = []

    def __init__(self):
        self._path = Config.create('/config/config.yml').__dict__["SCRIPTS"]["PATH"] + self.script_name

    def get_command(self):
        return self.command + [self._path] + self.params

    def run(self):
        subprocess.run(self.get_command())
