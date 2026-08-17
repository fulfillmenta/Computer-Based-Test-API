from fastapi import APIRouter,Depends
from models.question_info import QuestionCreateInfo
from services.admin_service import add_question, update_question, delete_question, get_all_users, get_all_results
from middleware.auth_middleware import require_admin

router = APIRouter()


@router.post("/admin/questions")
def create_question(data: QuestionCreateInfo, current_user: dict = Depends(require_admin)):
    return add_question(data)


@router.put("/admin/questions/{question_id}")
def edit_question(question_id: str, data: QuestionCreateInfo, current_user: dict = Depends(require_admin)):
    return update_question(question_id, data)


@router.delete("/admin/questions/{question_id}")
def remove_question(question_id: str, current_user: dict = Depends(require_admin)):
    return delete_question(question_id)

@router.get("/admin/users")
def list_users(current_user: dict = Depends(require_admin)):
    return get_all_users()


@router.get("/admin/results")
def list_results(current_user: dict = Depends(require_admin)):
    return get_all_results()