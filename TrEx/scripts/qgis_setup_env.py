import json
import os

def qgis_env():
  with open("env-vars.json", "w") as f:
    f.write(json.dumps(dict(os.environ)))

qgis_env()