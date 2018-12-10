import json
import hashlib

def hashOfString(s):
    return hashlib.md5(str(s).encode("UTF-8")).hexdigest()

parsed_json = {}

with open("./input-hashchain.json") as f:
    parsed_json = json.loads(f.read())

curr = hashOfString("julekalender")
output = ""

while len(parsed_json) != 0:
    for obj in parsed_json:
        tmp = hashOfString(curr + obj['ch']) 
        if tmp == obj['hash']:
            curr = tmp
            output += obj['ch']
            parsed_json.remove(obj)
            break

print(output)
