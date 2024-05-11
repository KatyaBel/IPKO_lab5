from typing import Dict
import datetime
from pydantic import BaseModel


class GetNotes(BaseModel):
    notes: Dict[int, str]


class GetNoteInfo(BaseModel):
    created_at: datetime.datetime
    updated_at: datetime.datetime


class GetNoteText(BaseModel):
    id: int
    text: str


class CreateNote(BaseModel):
    new_id: int


class UpdateNote(BaseModel):
    upd_id: int
    new_text: str


class DeleteNote(BaseModel):
    del_id: int


