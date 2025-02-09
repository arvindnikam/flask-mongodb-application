from bunnet import Indexed
from pymongo import IndexModel, ASCENDING, DESCENDING
from app.models import BaseDocument

class Location(BaseDocument):
    country: str | None = None
    state: str | None = None
    city: Indexed(str, background=True)
    area: Indexed(str, background=True)
    pincode: Indexed(str, background=True)

    class Settings:
        name = "locations"
        validate_on_save = True
        use_state_management = True
        indexes = [
            IndexModel(
                [
                    ("area", ASCENDING),
                    ("pincode", DESCENDING)
                ],
                name="index_location_area_pincode"
            )
        ]
