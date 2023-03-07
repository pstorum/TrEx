import json
import os

def qgis_env():
  with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "..\\..\\env-vars.json"), "w") as f:
    f.write(json.dumps(dict(os.environ)))

qgis_env()