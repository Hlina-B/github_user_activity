from pathlib import Path
import tomllib
import sys

class AppConfig:

    def __init__(self):
        self.github_base_url = ""
        self.github_activity_path = ""

    def load_from_config_file(self, config_path: Path):
        if config_path is None or not config_path.exists():
            print("No configuration. App cannot start. Closing...")
            sys.exit(1)

        with open(config_path, 'rb') as file:
            config = tomllib.load(file)
        
        api = config.get("api", {})
        self.github_base_url = api.get("github_base_url", "")
        self.github_activity_path = api.get("github_activity_path", "")

app_config = AppConfig()