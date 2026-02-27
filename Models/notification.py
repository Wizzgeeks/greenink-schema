import uuid

from Models.course import Course
from mongoengine import Document, ReferenceField, DateTimeField, StringField, BooleanField, CASCADE,IntField,EmbeddedDocumentField, EmbeddedDocument, ListField
from datetime import datetime, timezone


class Notification(EmbeddedDocument):
    notification_id = StringField(default=lambda: str(uuid.uuid4()))
    message = StringField(default="You have a new notification")
    name=StringField(default="")
    notification_type = StringField(
        choices=("homework", "blog", "general","test","milestone","announcement"),
        default="general"
    )
    publish=BooleanField(default=False)
    publish_date=DateTimeField()
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))

    def to_json(self):
        return {
            "notification_id": self.notification_id,
            "message": self.message,
            "name":self.name,
            "notification_type": self.notification_type,
            "created_at": self.created_at.isoformat()
        }



class GlobalNotification(Document):
    course=ReferenceField(Course, reverse_delete_rule=CASCADE)
    message=ListField(EmbeddedDocumentField(Notification), default=[])


    def to_json(self):
        sorted_messages = sorted(
        self.message,
        key=lambda x: x.publish_date if x.publish_date else x.created_at,
        reverse=True  
        )
        return {
            "id": str(self.id),
            "course": str(self.course.id) if self.course else None,
            "message": [m.to_json() for m in sorted_messages]
        }
    