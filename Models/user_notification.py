from mongoengine import Document, StringField, ListField,ReferenceField,DateTimeField,BooleanField,CASCADE,EmbeddedDocumentField,EmbeddedDocument
from Models.user import Users
from datetime import datetime, timezone
import uuid

class Notification(EmbeddedDocument):
    notification_id = StringField(default=lambda: str(uuid.uuid4()))
    message = StringField(default="You have a new notification")
    name=StringField(default="")
    notification_type = StringField(
        choices=("homework", "blog", "general","test"),
        default="general"
    )
    mark_as_read = BooleanField(default=False)
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))

    def to_json(self):
        return {
            "notification_id": self.notification_id,
            "message": self.message,
            "name":self.name,
            "notification_type": self.notification_type,
            "mark_as_read": self.mark_as_read,
            "created_at": self.created_at.isoformat()
        }


class UserNotification(Document):
    user = ReferenceField(Users, required=True, reverse_delete_rule=CASCADE)
    notifications = ListField(EmbeddedDocumentField(Notification), default=[])
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(UserNotification, self).save(*args, **kwargs)
    

    def to_json(self):
        return {
            "id": str(self.id),
            "user": str(self.user.id) if self.user else None,
            "notifications": [n.to_json() for n in self.notifications]
        }
    