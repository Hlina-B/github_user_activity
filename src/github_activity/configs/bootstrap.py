from github_activity.configs.config import app_config
from pathlib import Path

__filename = "github_activity.toml"

def get_project_root() -> Path:
    current_dir = Path(__file__).resolve().parent
    
    # Loop upwards until we hit the drive root
    for path in [current_dir] + list(current_dir.parents):
        if (path / __filename).exists():
            return path
            
    return None

def get_root_file() -> Path:
    target_path = get_project_root() 

    if not target_path is None:
        target_path = target_path / __filename
        return target_path if target_path.is_file() else None


def bootstrap():
    config_path = get_root_file()
    
    app_config.load_from_config_file(config_path)
    return app_config