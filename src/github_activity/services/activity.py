from github_activity.configs.http_request import fetch_data
import json

def get_user_github_activity(username: str, path):
    events = fetch_data(path.github_base_url + username + path.github_activity_path)
    pretty_output = json.dumps(events, indent=4)
    print(pretty_output)