import uuid
from utilities.json_handler import load_json, append_json
from utilities.security import hash_password, verify_password, create_token
from utilities.validators import validate_registration_data, validate_username_unique


def register_user(data):
    data_dict = data.model_dump()

    is_valid, message = validate_registration_data(data_dict)
    if not is_valid:
        return {"message": message}

    users = load_json("data_storage/users.json")

    is_unique = validate_username_unique(data_dict["username"], users)
    if not is_unique:
        return {"message": "Username already exist"}

    hashed_password = hash_password(data_dict["password"])

    new_user = {
        "id": str(uuid.uuid4()),
        "first_name": data_dict["first_name"],
        "last_name": data_dict["last_name"],
        "date_of_birth": data_dict["date_of_birth"],
        "email": data_dict["email"],
        "username": data_dict["username"],
        "password_hash": hashed_password,
        "role": "user"
    }

    append_json("data_storage/users.json", new_user)
    return {"message": f"{new_user['username']} successfully registered"}


def login_user(data):
    data_dict = data.model_dump()

    users = load_json("data_storage/users.json")

    matched_user = None
    for user in users:
        if user["username"] == data_dict["username"]:
            matched_user = user
            break

    if matched_user is None:
        return {"message": "Invalid username or password"}

    if not verify_password(data_dict["password"], matched_user["password_hash"]):
        return {"message": "Invalid username or password"}

    token = create_token(matched_user["id"], matched_user["role"])

    return {"access_token": token, "role": matched_user["role"]}
