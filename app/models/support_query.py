from typing import Annotated
from enum import Enum
from bson import ObjectId
from app.models import BaseDocument
from bunnet.odm.fields import PydanticObjectId

class StatusEnum(str, Enum):
    created = 'created'
    in_progress = 'in_progress'
    resolved = 'resolved'
    discarded = 'discarded'

class SupportQuery(BaseDocument):
    # user_id: Annotated[ObjectId, PydanticObjectId] | None = None
    company_name: str | None = None
    mobile_number: str | None = None
    assistence_required: str
    description: str
    status: StatusEnum = StatusEnum.created
    user_type: str = 'user'

    class Settings:
        name = "support_queries"
