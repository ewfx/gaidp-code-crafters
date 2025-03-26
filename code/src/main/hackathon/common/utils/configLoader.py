import yaml

class ConfigLoader:
    def __init__(self, config_file):
        with open(config_file, 'r') as file:
            self.config = yaml.safe_load(file)

    def get_config(self,*keys):
        data = self.config
        for key in keys:
            data = data.get(key,None)
            if data is None:
                return None
        return data