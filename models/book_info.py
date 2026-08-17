from pydantic import BaseModel

class BookUploadInfo(BaseModel):
    title: str
    author: str
    category: str

class BookInfo(BaseModel):
    id: str
    title: str
    author: str
    category: str
    date_uploaded: str