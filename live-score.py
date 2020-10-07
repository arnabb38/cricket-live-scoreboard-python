from pycricbuzz import Cricbuzz
import json

c = Cricbuzz()

matches = c.matches()

# for match in matches:
#     print(match)

# print (json.dumps(matches,indent=4)) # 30415

def scorecard(mid):
    c = Cricbuzz()
    scard = c.scorecard(mid)
    print(json.dumps(scard, indent=4, sort_keys=True))

scorecard("30415")

# def match_info(mid):
#     # c = Cricbuzz()
#     minfo = c.matchinfo(mid)
#     print(json.dumps(minfo, indent=4, sort_keys=True))

# match_info("30415")