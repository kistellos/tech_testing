from pymongo import MongoClient
from datetime import datetime

client = MongoClient()

# Access database
# db = client.primer
# db = client['primer']

# Access collection
# coll = db.dataset
# coll = db['dataset']

db = client.test

result = db.restaurants.insert_one(
    {
        "address": {
            "street": "2 Avenue",
            "zipcode": "10075",
            "building": "1480",
            "coord": [-73.9557413, 40.7720266]
        },
        "borough": "Manhattan",
        "cuisine": "Italian",
        "grades": [
            {
                "date": datetime.strptime("2014-10-01", "%Y-%m-%d"),
                "grade": "A",
                "score": "A"
            },
            {
                "date": datetime.strptime("2014-01-16", "%Y-%m-%d"),
                "grade": "B",
                "score": 17
            }
        ],
        "name": "Vella",
        "restaurant_id": "41704620"
    }
)

print result.inserted_id
print dir(result)

# cursor = db.restaurants.find()
# for doc in cursor:
#     print doc

cursor = db.restaurants.find({"borough": "Manhattan"})
cursor = db.restaurants.find({"address.building": "208"})
cursor = db.restaurants.find({"grades.grade": "B"})

for doc in cursor:
    print doc