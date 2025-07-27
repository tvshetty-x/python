import os
import json

def parse_json_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            with open(os.path.join(directory, filename)) as f:
                data = json.load(f)
                print(f"Parsed {filename}: {data}")

if __name__ == "__main__":
    parse_json_files(".")
