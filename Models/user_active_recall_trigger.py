from mongoengine import (
    Document, ReferenceField, IntField,
    BooleanField, DateTimeField, CASCADE
)
from datetime import datetime, timezone

from Models.user import Users
from Models.course import Course
from Models.subject import Subject
from Models.topic import Topic
from Models.subtopic import Subtopic


class UserActiveRecallTrigger(Document):
    user = ReferenceField(Users, required=True, reverse_delete_rule=CASCADE)
    course = ReferenceField(Course, reverse_delete_rule=CASCADE)
    subject = ReferenceField(Subject, reverse_delete_rule=CASCADE)
    topic = ReferenceField(Topic, reverse_delete_rule=CASCADE)
    subtopic = ReferenceField(Subtopic, reverse_delete_rule=CASCADE)
    completed_at= DateTimeField()
    is_active = BooleanField(default=False)
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super().save(*args, **kwargs)

    def to_json(self):
        return {
            "id": str(self.id),
            "user": str(self.user.id),
            "course": str(self.course.id) if self.course else None,
            "subject": str(self.subject.id) if self.subject else None,
            "topic": str(self.topic.id) if self.topic else None,
            "subtopic": str(self.subtopic.id) if self.subtopic else None,
            "completed_at": self.completed_at,
            "is_active": self.is_active,

        }
