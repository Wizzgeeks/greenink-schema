from Models.user import Users
from mongoengine import (
    Document, ReferenceField, IntField,
    BooleanField, DateTimeField, CASCADE
)
from datetime import datetime, timezone

class UserActiveRecallDays(Document):
    user = ReferenceField(Users, required=True, reverse_delete_rule=CASCADE)
    course_active_recall_interval_days = IntField(default=7)
    subject_active_recall_interval_days = IntField(default=7)
    topic_active_recall_interval_days = IntField(default=7)
    subtopic_active_recall_interval_days = IntField(default=7)
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super().save(*args, **kwargs)

    def to_json(self):
        return {
            "id": str(self.id),
            "user": str(self.user.id),
            "course_active_recall_interval_days": self.course_active_recall_interval_days,
            "subject_active_recall_interval_days": self.subject_active_recall_interval_days,
            "topic_active_recall_interval_days": self.topic_active_recall_interval_days,
            "subtopic_active_recall_interval_days": self.subtopic_active_recall_interval_days,
        }
