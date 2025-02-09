from bunnet import Indexed
from pymongo import IndexModel, ASCENDING, DESCENDING
from app.models import BaseDocument
from bunnet.odm.fields import PydanticObjectId
from pydantic import Field
from bunnet import Document
from uuid import UUID, uuid4

class User(Document):
    id: int | PydanticObjectId = Field(default_factory=PydanticObjectId)
    name: str
    verified: bool

    class Settings:
        name = "users"
        validate_on_save = True
        use_state_management = True
