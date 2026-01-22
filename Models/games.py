from mongoengine import (
    Document, StringField, ReferenceField, DateTimeField,
    CASCADE, ListField, DictField
)
from datetime import datetime, timezone
from Models.course import Course

class Game(Document):
    course= ReferenceField(Course, reverse_delete_rule=CASCADE, required=True)
    name = StringField(required=True)
    content = ListField(DictField(), default=[])
    game_type = StringField(choices=["knowledge_test", "speed_test"], required=True)
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(Game, self).save(*args, **kwargs)
    def to_json(self):
        return {
            "id": str(self.id),
            "course": str(self.course.id) if self.course else None,
            "name": self.name,
            "content": self.content,
            "game_type": self.game_type,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
    def to_mini_json(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "game_type": self.game_type,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }