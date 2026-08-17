from pydantic import BaseModel


class QuestionCreateInfo(BaseModel):
    subject: str
    question_text: str
    options: list[str]
    answer: str


class QuestionInfo(BaseModel):
    id: str
    subject: str
    question_text: str
    options: list[str]
    answer: str


class QuizQuestionInfo(BaseModel):
    id: str
    subject: str
    question_text: str
    options: list[str]


class AnswerSubmissionInfo(BaseModel):
    question_id: str
    selected_answer: str
