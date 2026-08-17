# from utilities.security import hash_password, verify_password

# hashed = hash_password("mypassword")
# print(hashed)
# print(verify_password("mypassword", hashed))
# print(verify_password("wrongpassword", hashed))


# from utilities.json_handler import load_json, save_json, append_json

# print("Test 1 - load missing file:")
# print(load_json("data_storage/does_not_exist.json"))

# print("\nTest 2 - save data:")
# save_json("data_storage/test.json", [{"name": "foxtrot"}])
# print(load_json("data_storage/test.json"))

# print("\nTest 3 - append data:")
# append_json("data_storage/test.json", {"name": "charlie"})
# print(load_json("data_storage/test.json"))

# print("\nTest 4 - append again:")
# append_json("data_storage/test.json", {"name": "alpha"})
# print(load_json("data_storage/test.json"))


# from utilities.security import create_token, verify_token

# token = create_token("u001", "user")
# print(token)

# result = verify_token(token)
# print(result)

# fake_token = token + "bug"
# print(verify_token(fake_token))


# from utilities.validators import validate_subject_selection

# print(validate_subject_selection([]))
# print(validate_subject_selection(["maths"]))
# print(validate_subject_selection(["maths", "chemistry"]))
# print(validate_subject_selection(["a", "b", "c", "d"]))
# print(validate_subject_selection(["a", "b", "c", "d", "e"]))


# from utilities.validators import validate_username_unique

# existing_users = [
#     {"username": "musab"},
#     {"username": "ada123"}
# ]

# print(validate_username_unique("musab", existing_users))    # False - taken
# print(validate_username_unique("newuser", existing_users))  # True - free
# print(validate_username_unique("ada123", existing_users))   # False - taken


# from utilities.json_handler import append_json

# append_json("data_storage/questions.json", {
#     "id": "q001",
#     "subject": "maths",
#     "question_text": "What is 7 x 8?",
#     "options": ["54", "56", "58", "64"],
#     "answer": "56"
# })

# append_json("data_storage/questions.json", {
#     "id": "q002",
#     "subject": "chemistry",
#     "question_text": "What is H2O?",
#     "options": ["Salt", "Water", "Oxygen", "Hydrogen"],
#     "answer": "Water"
# })

# append_json("data_storage/questions.json", {
#     "id": "q003",
#     "subject": "physics",
#     "question_text": "What is the unit of force?",
#     "options": ["Joule", "Newton", "Watt", "Pascal"],
#     "answer": "Newton"
# })


# from models.user_info import UserRegisterInfo
# from services.auth_service import register_user

# new_user = UserRegisterInfo(
#     first_name="foxtrot",
#     last_name="alpha",
#     date_of_birth="2001-05-14",
#     email="alpha@example.com",
#     username="foxtrot",
#     password="foxtrot123"
# )

# result = register_user(new_user)
# print(result)


# from models.user_info import UserLoginInfo
# from services.auth_service import login_user

# login_data = UserLoginInfo(username="foxtrot", password="foxtrot123")
# print(login_user(login_data))

# wrong_password = UserLoginInfo(username="foxtrot", password="wrongpass")
# print(login_user(wrong_password))

# wrong_username = UserLoginInfo(username="notreal", password="foxtrot123")
# print(login_user(wrong_username))


# from services.quiz_service import score_quiz

# test_answers = [
#     {"question_id": "q001", "selected_answer": "56"},
#     {"question_id": "q002", "selected_answer": "Salt"}
# ]

# result = score_quiz(test_answers)
# print(result)


# from services.quiz_service import score_quiz

# test_answers = [
#     {"question_id": "q001", "selected_answer": "56"},
#     {"question_id": "q002", "selected_answer": "Salt"}
# ]

# result = score_quiz(test_answers)
# print(result)

# from services.quiz_service import score_quiz

# test_answers = [
#     {"question_id": "q001", "selected_answer": "56"},
#     {"question_id": "q002", "selected_answer": "Salt"}
# ]

# result = score_quiz(test_answers)
# print(result)


from models.question_info import QuestionCreateInfo
from services.admin_service import add_question, get_all_users, get_all_results

new_question = QuestionCreateInfo(
    subject="english",
    question_text="What is the opposite of 'happy'?",
    options=["Sad", "Angry", "Tired", "Bored"],
    answer="Sad"
)
print(add_question(new_question))

print(get_all_users())   
print(get_all_results())  