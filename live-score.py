from pycricbuzz import Cricbuzz
import json

c = Cricbuzz()

matches = c.matches()

# for match in matches:
#     print(match)

# print (json.dumps(matches,indent=4)) # 30419

# Fetch scorecard of a match
def scorecard(mid):
    c = Cricbuzz()
    scard = c.scorecard(mid)
    print(json.dumps(scard, indent=4, sort_keys=True))

# scorecard("30415")


# Fetch match info of a match
def match_info(mid):
    c = Cricbuzz()
    minfo = c.matchinfo(mid)
    print(json.dumps(minfo, indent=4, sort_keys=True))

# match_info("30415")


# Fetching the live score of a match
def live_score(mid):
    c = Cricbuzz()
    lscore = c.livescore(mid)
    print(json.dumps(lscore["batting"], indent=4, sort_keys=True))

live_score("30419")


# Fetch commentary of the match
def commentary(mid):
    c = Cricbuzz()
    comm = c.commentary(mid)
    print(json.dumps(comm, indent=4, sort_keys=True))

# commentary("30415")