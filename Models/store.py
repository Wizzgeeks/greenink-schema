from mongoengine import (
    Document,
    ListField,
    StringField,
    ReferenceField,
    BooleanField,
    DateTimeField,
    FloatField,
    IntField,
    CASCADE,
    DictField
)
from Models.course import Course
from datetime import datetime, timezone


class Store(Document):
    course = ReferenceField(Course, reverse_delete_rule=CASCADE, required=True)

    item_name = StringField(required=True)  
    

    store_tier = StringField(required=True)

    price = FloatField(required=True)

    days_count = IntField(required=True)   

    activate = BooleanField(default=True)

    permissions = ListField(DictField(), default=[])
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    is_deleted = BooleanField(default=False)


    def to_json(self):
        return {
            "id": str(self.id),
            "course": str(self.course.id) if self.course else None,
            "item_name": self.item_name,
            "store_tier": self.store_tier,
            "price": self.price,
            "days_count": self.days_count,
            "activate": self.activate,
            "permissions": self.permissions if self.permissions else {}
        }

    def with_key(self):
        return {
            "id": str(self.id),
            "course": self.course.to_json() if self.course else None,
            "item_name": self.item_name,
            "store_tier": self.store_tier,
            "price": self.price,
            "days_count": self.days_count,
            "activate": self.activate,
            "permissions": self.permissions if self.permissions else []
        }

    def admin_json(self):
        return self.with_key()