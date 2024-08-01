import json

with open('db.json', 'r') as f:
    db = json.load(f)
    for item in db:
        db[item] = [db[item][0], db[item][1], 0]
with open('db.json','w') as f:
    json.dump(db, f)