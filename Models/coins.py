from mongoengine import Document,ReferenceField,IntField,StringField,CASCADE,DateTimeField
from Models.course import Course
from datetime import datetime,timezone

class Coin_management(Document):
    course = ReferenceField(Course,required=True,reverse_delete_rule=CASCADE)
    page_completion_coins = IntField(required=True)
    test_completion_coins = IntField(required=True)
    quiz_completion_coins = IntField(required=True)
    login_coins = IntField(required=True)
    streak_coins = IntField(required=True)
    created_at=DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at=DateTimeField(default=lambda: datetime.now(timezone.utc))
    created_by=StringField()
    updated_by=StringField()


    def to_json(self):
        return {
            "id": str(self.id),
            "course": str(self.course.id) if self.course else None,
            "page_completion_coins": self.page_completion_coins,
            "test_completion_coins": self.test_completion_coins,
            "quiz_completion_coins": self.quiz_completion_coins,
            "login_coins": self.login_coins,
            "streak_coins": self.streak_coins,
            # "total_coins": self.total_coins(),
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "created_by": self.created_by,
            "updated_by": self.updated_by,

    }

    def with_key(self):
        return {
            "id": str(self.id),
            "course": self.course.to_json() if self.course else None,
            "page_completion_coins": self.page_completion_coins,
            "test_completion_coins": self.test_completion_coins,
            "quiz_completion_coins": self.quiz_completion_coins,
            "login_coins": self.login_coins,
            "streak_coins": self.streak_coins,
            # "total_coins": self.total_coins(),
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "created_by": self.created_by,
            "updated_by": self.updated_by
    }

    # def total_coins(self):
    #     return (
    #         self.page_completion_coins +
    #         self.test_completion_coins +
    #         self.quiz_completion_coins +
    #         self.login_coins +
    #         self.streak_coins
    #     )

