from pycricbuzz import Cricbuzz
import json

c = Cricbuzz()

matches = c.matches

decode = json.dumps(matches)

# print () #for pretty prinitng
