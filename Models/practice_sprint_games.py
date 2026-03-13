from mongoengine import (
    Document, StringField, ReferenceField, DateTimeField,
    CASCADE, ListField, DictField
)
from datetime import datetime, timezone
from Models.course import Course


class PracticeSprintGame(Document):
    course= ReferenceField(Course, reverse_delete_rule=CASCADE,required=True)
    name = StringField(required=True)
    content = ListField(DictField(), default=[])
    topic_key=StringField(required=True)
    topic_name=StringField(required=True)
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    title=StringField()
    key=StringField()
    level=StringField(choices=["easy", "medium", "hard"])

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(PracticeSprintGame, self).save(*args, **kwargs)
    def to_json(self):
        return {
            "id": str(self.id),
            "course": str(self.course.id) if self.course else None,
            "name": self.name,
            "content": self.content,
            "level": self.level,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
    def to_mini_json(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "level": self.level,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
