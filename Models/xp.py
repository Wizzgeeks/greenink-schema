from mongoengine import Document,ReferenceField,IntField,StringField,CASCADE,DateTimeField
from Models.course import Course
from datetime import datetime,timezone

class XP_management(Document):
    course = ReferenceField(Course,required=True,reverse_delete_rule=CASCADE)
    page_completion_xp = IntField(required=True)
    test_completion_xp = IntField(required=True)
    quiz_completion_xp = IntField(required=True)
    login_xp = IntField(required=True)
    streak_xp = IntField(required=True)
    created_at=DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at=DateTimeField(default=lambda: datetime.now(timezone.utc))
    created_by=StringField()
    updated_by=StringField()


    def to_json(self):
        return {
            "id": str(self.id),
            "course": str(self.course.id) if self.course else None,
            "page_completion_xp": self.page_completion_xp,
            "test_completion_xp": self.test_completion_xp,
            "quiz_completion_xp": self.quiz_completion_xp,
            "login_xp": self.login_xp,
            "streak_xp": self.streak_xp,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "created_by": self.created_by,
            "updated_by": self.updated_by,

    }

    def with_key(self):
        return {
            "id": str(self.id),
            "course": self.course.to_json() if self.course else None,
            "page_completion_xp": self.page_completion_xp,
            "test_completion_xp": self.test_completion_xp,
            "quiz_completion_xp": self.quiz_completion_xp,
            "login_xp": self.login_xp,
            "streak_xp": self.streak_xp,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "created_by": self.created_by,
            "updated_by": self.updated_by
    }
