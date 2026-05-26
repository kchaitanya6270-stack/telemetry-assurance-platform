import json

def load_mock_events(path):

    with open(path, "r") as f:
        return json.load(f)