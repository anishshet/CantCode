from curses import flash
from utils.mongodb_fun import get_mongodb_collection

# POST METHOD matlab naya user create


def create_user(user_data):
    user_collection = get_mongodb_collection("user")
    # gives info about collection (tz-aware=true?)

    user_data["_id"] = user_data["user_name"]
    # transfers user_data ka username to user_data ka id when creating a new user.
    # id is never first generated when creating a new user

    #print(user_collection.find({"user_name": user_data["user_name"]}))

    if len(list(user_collection.find({"user_name": user_data["user_name"]}))) > 0:
        print("Exists!")
        return {"message": "Username already exists!", "valid":False}
    else:
        user_collection.insert_one(user_data)
        return {"message": "Account created Successfully!", "valid":True}
    # Agar usko empty string nahi mila toh uss naam ka username pehle se db mai hai
    # Agar usko empty string return mai mila to wo username db mai nahi hai, aur user wo username use kar sakta hai.

# print(get_mongodb_collection("user"))

# PUT METHOD matlab kisi user ke values update karna


def update_user(id, user_data):
    user_collection = get_mongodb_collection("user")
    # sab collection ke values fetch karta hai aur user_collection mai dalta hai.

    user = user_collection.find_one({"_id": id})
    # print(user["user_name"])
    # print(user["_id"])

    if user["user_name"] != user_data["user_name"] or user["_id"] != user_data["_id"]:
        print("Cannot Update Record!")
        return "Cannot update Record!"
    else:
        user_collection.update_one({"_id": id}, {"$set": user_data})
        return "Record updated Successfully!"
    # NOTE-User uska username update nahi kar sakta!!!
    # He can update only uska password or mail.
    # Lekin agar agar wo galat username dalta hai to he gets denied to update anything
    # Or agar sahi username hai to he can update password or mail

# GET METHOD used to fetch the user ka data


def get_user(id):
    user_collection = get_mongodb_collection("user")
    return user_collection.find_one({"_id": id})


def validate_user(user_name, password):
    user_collection = get_mongodb_collection("user")
    user = user_collection.find_one(
        {"user_name": user_name, "password": password})
    if user:
        return {"name" : user["user_name"], "valid":True}
    else:
        return {"message" : "Cannot Login. Invalid Credentials!", "valid":False} 
