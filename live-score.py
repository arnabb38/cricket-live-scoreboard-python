from pycricbuzz import Cricbuzz
import json

c = Cricbuzz()

matches = c.matches()

# for match in matches:
#     print(match)

# print (json.dumps(matches,indent=4))

def scorecard(mid):
    c = Cricbuzz()
    scard = c.scorecard(mid)
    print(json.dumps(scard, indent=4, sort_keys=True))

scorecard()