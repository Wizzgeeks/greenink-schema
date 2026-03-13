from mongoengine import (
    Document, StringField, ReferenceField, DateTimeField,
    CASCADE, ListField, DictField,BooleanField,IntField
)
from datetime import datetime, timezone
from Models.games_completed import GamesCompleted
from Models.user import Users
from Models.practice_sprint_games import PracticeSprintGame 
class PracticeSprintGameCompleted(Document):
    user = ReferenceField(Users, reverse_delete_rule=CASCADE, required=True)
    practicesprintgame = ReferenceField(PracticeSprintGame, reverse_delete_rule=CASCADE, required=True)
    score = IntField(required=True)
    completed=BooleanField(default=False)
    attempt_data=ListField(DictField(),default=[])
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(PracticeSprintGameCompleted, self).save(*args, **kwargs)

    def to_json(self):
        return {
            "id": str(self.id),
            # "user": self.user.to_json() if self.user else None,
            # "game": self.game.to_json() if self.game else None,
            "score": self.score,
            "completed": self.completed,
            "attempt_data": self.attempt_data,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
    def to_mini_json(self):
        return {
            "id": str(self.id),
            "user": str(self.user.id) if self.user else None,
            "score": self.score,
            "completed": self.completed,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
