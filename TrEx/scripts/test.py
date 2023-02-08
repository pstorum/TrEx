import json
import os
import geopandas

def doEnv():
  with open("env-vars.json", "w") as f:
    f.write(json.dumps(dict(os.environ)))
doEnv()
