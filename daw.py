from pathlib import Path
import yaml
import json


class Daw(json.JSONEncoder):
    def default(self, o: object) -> object:
        if isinstance(o, type(self)):
            o.daw_config = self.daw_config.__dict__
            return json.dumps(o.__dict__)
        else:
            return json.JSONEncoder.default(self, o)

    def __init__(self):
        super().__init__()
        self.daw_config_folder = "data\\daw_config"
        self.daw_config = self.load_daw_config()
        # self.dbg_dump()
        # if not self.daw_config:
        #    self.daw_config = self.dialogue_daw_config()
        # dbg_print(yaml.dump(self.daw_config))

    def load_daw_config(self, config_name: str = "default"):
        print(f"loading daw_config {config_name}")
        try:
            path_str = f"{self.daw_config_folder}\\{config_name}.yaml"
            path = Path(path_str).resolve()
            with open(path, "r") as f:
                return yaml.load(f.read(), Loader=yaml.Loader)
        except Exception as e:
            print(f"Error!: {e}")
            return None

    def dbg_dump(self):
        path_str = f"{self.daw_config_folder}\\debug.yaml"
        path = Path(path_str).resolve()
        d = DawConfig("config_name", "plugin_path", "preset_path", "daw_config_path",
                      "pattern_path", "projects_path", "mrs_watson_32bit_path", "mrs_watson_64bit_path",
                      "nano_host_64bit_path", "nano_host_32bit_path", "rendered_path")
        with open(path, "w") as f:
            f.write(yaml.dump(d, Dumper=yaml.Dumper))


class DawConfig:
    def __init__(self, config_name, plugin_path, preset_path, daw_config_path,
                 pattern_path, projects_path, mrs_watson_32bit_path, mrs_watson_64bit_path,
                 nano_host_64bit_path, nano_host_32bit_path, rendered_path):
        self.nano_host_32bit_path = nano_host_32bit_path
        self.nano_host_64bit_path = nano_host_64bit_path
        self.mrs_watson_64bit_path = mrs_watson_64bit_path
        self.mrs_watson_32bit_path = mrs_watson_32bit_path
        self.rendered_path = rendered_path
        self.projects_path = projects_path
        self.pattern_path = pattern_path
        self.daw_config_path = daw_config_path
        self.preset_path = preset_path
        self.plugin_path = plugin_path
        self.config_name = config_name

class Playlist:
    # todo
    pass