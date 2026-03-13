from mongoengine import (
    Document, StringField, ReferenceField, DateTimeField,
    CASCADE, ListField, DictField,BooleanField,IntField
)
from datetime import datetime, timezone
from Models.user import Users
from Models.games import Game

class GamesCompleted(Document):
    user = ReferenceField(Users, reverse_delete_rule=CASCADE, required=True)
    game = ReferenceField(Game, reverse_delete_rule=CASCADE, required=True)
    score = IntField(required=True)
    completed=BooleanField(default=False)
    attempt_data=ListField(DictField(),default=[])
    game_type = StringField(choices=["knowledge_test", "speed_test", "aptitude_test"], required=True)
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(GamesCompleted, self).save(*args, **kwargs)

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
            "game": str(self.game.id) if self.game else None,
            "score": self.score,
            "completed": self.completed,
            "game_type": self.game_type,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
