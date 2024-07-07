import json
import os
import yaml
import re
from yaml.loader import FullLoader


class Config:
    """Clase que obtiene las variables de configuración para el servidor"""

    def __init__(self):
        pass

    def __setitem__(self, key, value):
        setattr(self, key, value)

    def __getitem__(self, key):
        return getattr(self, key)

    @staticmethod
    def get_config_os(value: str):
        """busca todas las variables de entorno que hay en un string
        
        El string debe ser el contenido obtenido de un archivo yaml.
        """
        
        pattern = re.compile(".*?\${(\w+)}.*?")
        match = pattern.findall(str(value))

        if match:
            full_value = value
            for g in match:
                full_value = full_value.replace(
                    f'${{{g}}}', os.environ.get(g, g)
                )
            return full_value
        return value

    def from_yaml(self, config_file):
        """Lee las variables del config.yaml pasado como argumento"""
        
        env = os.environ.get('FLASK_ENV', 'development')
        self['ENVIROMENT'] = env.lower()

        with open(config_file) as f:
            c = yaml.load(f, FullLoader)
        c = c[env.upper()]
        c = json.loads(self.get_config_os(json.dumps(c)))
        
        for key in c:
            if key.isupper():
                self[key] = c[key]

    @staticmethod
    def create(file: str):
        """Factory"""

        config = Config()
        config.from_yaml(file)
        return config