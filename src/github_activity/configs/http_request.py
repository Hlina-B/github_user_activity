import urllib.request
import urllib.error
import json

def fetch_data(url: str, token: str = None):
    if url is None:
        return None
    
    request = urllib.request.Request(url)
    request.add_header("Accept", "application/json")

    if isinstance(token, str):
        request.add_header("Authorization", f"Bearer {token}")
    
    try:
        with urllib.request.urlopen(request, timeout=10) as response:
            raw_bytes = response.read()
            json_text = raw_bytes.decode("utf-8")          
            data = json.loads(json_text)
            return data
            
    except urllib.error.HTTPError as e:
        print(f"HTTP Error {e.code}: {e.reason}")
    except urllib.error.URLError as e:
        print(f"Network Connectivity/URL Error: {e.reason}")
        
    return None