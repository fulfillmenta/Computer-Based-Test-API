def validate_subject_selection(subjects):
    if 1 <= len(subjects) <= 4:
        return True
    else:
        return False


def validate_username_unique(username, users_list):
    for user in users_list:
        if user["username"] == username:
            return False
    return True


def validate_registration_data(data):
    if not data["first_name"].strip():
        return False, "First name cannot be empty"

    if not data["last_name"].strip():
        return False, "Last name cannot be empty"

    if not data["date_of_birth"].strip():
        return False, "Date of birth cannot be empty"

    if not data["email"].strip():
        return False, "Email cannot be empty"

    if '@' not in data["email"] or '.' not in data["email"]:
        return False, "Invalid email address"

    if not data["username"].strip():
        return False, "Username cannot be empty"

    if len(data["password"]) < 4:
        return False, "Password must be at least 4 characters"

    return True, ""


def validate_question_data(data):
    if not data["subject"].strip():
        return False, "Subject cannot be empty"

    if not data["question_text"].strip():
        return False, "Question text cannot be empty"

    if len(data["options"]) != 4:
        return False, "Options must be 4"

    if not data["answer"].strip():
        return False, "Answer cannot be empty"

    if data["answer"] not in data["options"]:
        return False, "Answer must be in options"

    return True, ""
