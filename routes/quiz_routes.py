from fastapi import APIRouter, Depends, HTTPException
from utilities.validators import validate_subject_selection
from services.quiz_service import get_questions_by_subjects, score_quiz, save_result, get_my_results
from middleware.auth_middleware import get_current_user

router = APIRouter()


@router.get("/subjects")
def get_subjects():
    return {"subjects": ["maths", "chemistry", "physics", "english"]}


@router.post("/quiz/start")
def start_quiz(subjects: list[str], current_user: dict = Depends(get_current_user)):
    if not validate_subject_selection(subjects):
        raise HTTPException(status_code=400, detail="You must select between 1 and 4 subjects")

    questions = get_questions_by_subjects(subjects)
    return {"questions": questions}


@router.post("/quiz/submit")
def submit_quiz(answers: list[dict], current_user: dict = Depends(get_current_user)):
    result = score_quiz(answers)
    save_result(current_user["user_id"], result["subjects"], result["score"], result["total"], result["percentage"])
    return result


@router.get("/results/me")
def my_results(current_user: dict = Depends(get_current_user)):
    return get_my_results(current_user["user_id"])