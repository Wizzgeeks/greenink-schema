from mongoengine import (
    Document,
    ReferenceField,
    DateTimeField,
    CASCADE,
    StringField,
    BooleanField,
)
from Models.store import Store
from Models.user import Users
from datetime import datetime, timezone, timedelta


class UserStore(Document):
    user = ReferenceField(Users, reverse_delete_rule=CASCADE, required=True)
    store = ReferenceField(Store, reverse_delete_rule=CASCADE, required=True)

    start_date = DateTimeField(default=lambda: datetime.now(timezone.utc))
    expiry = DateTimeField(required=False)

    store_status = StringField(
        default="ACTIVE",
        choices=["ACTIVE", "EXPIRED", "CANCELLED", "FAILED"]
    )

    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))

    is_active = BooleanField(default=True)

    def to_json(self):
        return {
            "id": str(self.id),
            "user": str(self.user.id) if self.user else None,
            "store": self.store.to_json() if self.store else None,
            "start_date": self.start_date.isoformat() if self.start_date else None,
            "expiry": self.expiry.isoformat() if self.expiry else None,
            "store_status": self.store_status,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }