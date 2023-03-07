import json
import os

def doEnv():
  with open("..\\..\\env-vars.json", "w") as f:
    f.write(json.dumps(dict(os.environ)))
doEnv()
