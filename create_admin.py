import uuid
from utilities.json_handler import append_json, load_json
from utilities.security import hash_password


first_name = "odogwu"
last_name = "fca"
date_of_birth = "2006-06-02"
email = "aodogwufca@gmail.com.com"
username = "odogwufca"
password = "odogwufca1234"

existing_users = load_json("data_storage/users.json")
already_exists = any(user["username"] == username for user in existing_users)

if already_exists:
    print(f"A user with username '{username}' already exists. Nothing was created.")
else:
    new_admin = {
        "id": str(uuid.uuid4()),
        "first_name": first_name,
        "last_name": last_name,
        "date_of_birth": date_of_birth,
        "email": email,
        "username": username,
        "password_hash": hash_password(password),
        "role": "admin",
    }

    append_json("data_storage/users.json", new_admin)
    print(f"Admin account '{username}' created successfully.")