from fastapi import APIRouter, Depends, UploadFile, File, Form
from services.book_service import (
    upload_book,
    get_all_books,
    search_books,
    get_book_content,
    get_book_content_by_title,
    update_book,
    delete_book,
)
from middleware.auth_middleware import require_admin, get_current_user

router = APIRouter()


@router.post("/admin/books")
async def create_book(
    title: str = Form(...),
    author: str = Form(...),
    category: str = Form(...),
    file: UploadFile = File(...),
    current_user: dict = Depends(require_admin),
):
    file_bytes = await file.read()
    file_content = file_bytes.decode("utf-8")
    return upload_book(title, author, category, file_content)


@router.get("/books")
def list_books(current_user: dict = Depends(get_current_user)):
    return get_all_books()


@router.get("/books/search")
def search_for_books(query: str, current_user: dict = Depends(get_current_user)):
    return search_books(query, current_user["role"])


@router.get("/books/read")
def read_book_by_title(title: str, current_user: dict = Depends(get_current_user)):
    return get_book_content_by_title(title)


@router.get("/admin/books/{book_id}")
def read_book_by_id(book_id: str, current_user: dict = Depends(require_admin)):
    return get_book_content(book_id)


@router.put("/admin/books/{book_id}")
def edit_book(book_id: str, title: str, author: str, category: str, current_user: dict = Depends(require_admin)):
    return update_book(book_id, title, author, category)


@router.delete("/admin/books/{book_id}")
def remove_book(book_id: str, current_user: dict = Depends(require_admin)):
    return delete_book(book_id)