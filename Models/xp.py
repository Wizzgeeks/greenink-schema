from mongoengine import Document,ReferenceField,IntField,StringField,CASCADE,DateTimeField,FloatField,BooleanField,EmbeddedDocument,EmbeddedDocumentField
from Models.course import Course
from datetime import datetime,timezone


class RewardEnableConfig(EmbeddedDocument):
    page_completion = BooleanField(default=True)
    test_completion = BooleanField(default=True)
    quiz_completion = BooleanField(default=True)
    login = BooleanField(default=True)
    streak = BooleanField(default=True)
    materials = BooleanField(default=True)
    test_low=BooleanField(default=True)
    test_medium=BooleanField(default=True)
    test_high=BooleanField(default=True)
    quiz_low=BooleanField(default=True)
    quiz_medium=BooleanField(default=True)
    quiz_high=BooleanField(default=True)

class XP_management(Document):
    course = ReferenceField(Course,required=True,reverse_delete_rule=CASCADE)
    page_completion_xp = IntField(required=True)
    test_completion_xp = IntField(required=True)
    quiz_completion_xp = IntField(required=True)
    login_xp = IntField(required=True)
    streak_xp = IntField(required=True)
    materials_xp= IntField(required=True)
    test_low_xp = IntField(required=False, default=0)
    test_medium_xp = IntField(required=False, default=0)
    test_high_xp = IntField(required=False, default=0)
    quiz_low_xp = IntField(required=False, default=0)
    quiz_medium_xp = IntField(required=False, default=0)
    quiz_high_xp = IntField(required=False, default=0)
    xp_enable_config = EmbeddedDocumentField(
        RewardEnableConfig,
        default=RewardEnableConfig
    )
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
            "material_xp":self.materials_xp,
            "test_low_xp": self.test_low_xp,
            "test_medium_xp": self.test_medium_xp,
            "test_high_xp": self.test_high_xp,
            "quiz_low_xp": self.quiz_low_xp,
            "quiz_medium_xp": self.quiz_medium_xp,
            "quiz_high_xp": self.quiz_high_xp,
            "streak_xp": self.streak_xp,
            "xp_enable_config": {
                "page_completion": self.xp_enable_config.page_completion,
                "test_completion": self.xp_enable_config.test_completion,
                "quiz_completion": self.xp_enable_config.quiz_completion,
                "test_low": self.xp_enable_config.test_low,
                "test_medium": self.xp_enable_config.test_medium,
                "test_high": self.xp_enable_config.test_high,
                "quiz_low": self.xp_enable_config.quiz_low,
                "quiz_medium": self.xp_enable_config.quiz_medium,
                "quiz_high": self.xp_enable_config.quiz_high,
                "login": self.xp_enable_config.login,
                "streak": self.xp_enable_config.streak,
                "materials": self.xp_enable_config.materials,
            },
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
            "material_xp":self.materials_xp,
            "test_low_xp": self.test_low_xp,
            "test_medium_xp": self.test_medium_xp,
            "test_high_xp": self.test_high_xp,
            "quiz_low_xp": self.quiz_low_xp,
            "quiz_medium_xp": self.quiz_medium_xp,
            "quiz_high_xp": self.quiz_high_xp,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "created_by": self.created_by,
            "updated_by": self.updated_by
    }
