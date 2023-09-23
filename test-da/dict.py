users = {
    "user1": {
        "id": 1,
        "name": "Xaxaxa",
        "email": "Xaxaxa@gmail.com",
    },
    "user2": {
        "id": 2,
        "name": "asdfg",
        "email": "asdfg@gmail.com"
    }
}

print("\nDict")
print(users)
print(users["user1"])
print(users["user2"])
print(users["user1"]["id"])
print(type(users))

print("\n To String")
import json
result = json.dumps(users)
print(result)
print(type(result))

print("\n To file")
with open('result.json', 'w') as file:
    json.dump(users, file)
