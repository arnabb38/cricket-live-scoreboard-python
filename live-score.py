from pycricbuzz import Cricbuzz
import json

c = Cricbuzz()

matches = c.matches()

# for match in matches:
#     print(match)

print (json.dumps(matches,indent=4))