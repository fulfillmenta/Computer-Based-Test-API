import uuid
from datetime import datetime
from utilities.json_handler import load_json, append_json


def get_questions_by_subjects(subjects):
    all_questions = load_json("data_storage/questions.json")

    filtered_questions = []
    for question in all_questions:
        if question["subject"] in subjects:
            safe_question = {
                "id": question["id"],
                "subject": question["subject"],
                "question_text": question["question_text"],
                "options": question["options"]
            }
            filtered_questions.append(safe_question)

    return filtered_questions


def score_quiz(answers):
    all_questions = load_json("data_storage/questions.json")

    score = 0
    total = len(answers)
    subjects_covered = []

    for submitted in answers:
        matched_question = None
        for question in all_questions:
            if question["id"] == submitted["question_id"]:
                matched_question = question
                break

        if matched_question is not None:
            if matched_question["subject"] not in subjects_covered:
                subjects_covered.append(matched_question["subject"])

            if submitted["selected_answer"] == matched_question["answer"]:
                score += 1

    if total == 0:
        percentage = "0%"
    else:
        percentage = f"{round((score / total) * 100, 2)}%"

    return {
        "score": score,
        "total": total,
        "percentage": percentage,
        "subjects": subjects_covered
    }


def save_result(user_id, subjects, score, total, percentage):
    result_record = {
        "id": str(uuid.uuid4()),
        "user_id": user_id,
        "subjects": subjects,
        "score": score,
        "total": total,
        "percentage": percentage,
        "date_taken": datetime.now().isoformat()
    }

    append_json("data_storage/results.json", result_record)

    return {"message": "Result saved successfully"}


def get_my_results(user_id):
    all_results = load_json("data_storage/results.json")

    my_results = []
    for result in all_results:
        if result["user_id"] == user_id:
            my_results.append(result)

    return my_results