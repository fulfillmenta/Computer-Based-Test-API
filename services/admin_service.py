import uuid
from utilities.json_handler import load_json, save_json, append_json
from utilities.validators import validate_question_data


def add_question(data):
    data_dict = data.model_dump()

    is_valid, message = validate_question_data(data_dict)
    if not is_valid:
        return {"message": message}

    new_question = {
        "id": str(uuid.uuid4()),
        "subject": data_dict["subject"],
        "question_text": data_dict["question_text"],
        "options": data_dict["options"],
        "answer": data_dict["answer"],
    }

    append_json("data_storage/questions.json", new_question)

    return {"message": "Question added successfully"}

def update_question(question_id, data):
    data_dict = data.model_dump()

    is_valid, message = validate_question_data(data_dict)
    if not is_valid:
        return {"message": message}

    questions = load_json("data_storage/questions.json")

    updated_questions = []
    found = False
    for question in questions:
        if question["id"] == question_id:
            updated_question = {
                "id": question_id,
                "subject": data_dict["subject"],
                "question_text": data_dict["question_text"],
                "options": data_dict["options"],
                "answer": data_dict["answer"],
            }
            updated_questions.append(updated_question)
            found = True
        else:
            updated_questions.append(question)

    if not found:
        return {"message": "Question not found"}

    save_json("data_storage/questions.json", updated_questions)

    return {"message": "Question updated successfully"}


def delete_question(question_id):
    questions = load_json("data_storage/questions.json")

    updated_questions = []
    found = False
    for question in questions:
        if question["id"] == question_id:
            found = True
        else:
            updated_questions.append(question)

    if not found:
        return {"message": "Question not found"}

    save_json("data_storage/questions.json", updated_questions)

    return {"message": "Question deleted successfully"}

def get_all_users():
    users = load_json("data_storage/users.json")

    safe_users = []
    for user in users:
        safe_user = {
            "id": user["id"],
            "first_name": user["first_name"],
            "last_name": user["last_name"],
            "email": user["email"],
            "username": user["username"],
            "role": user["role"],
        }
        safe_users.append(safe_user)

    return safe_users


def get_all_results():
    results = load_json("data_storage/results.json")
    return results


