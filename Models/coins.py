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

class Coin_management(Document):
    course = ReferenceField(Course,required=True,reverse_delete_rule=CASCADE)
    page_completion_coins = IntField(required=True)
    test_completion_coins = IntField(required=True)
    quiz_completion_coins = IntField(required=True)
    login_coins = IntField(required=True)
    streak_coins = IntField(required=True)
    coin_value_per_unit = FloatField(required=True,precision=2, min_value=0.0)
    materials_coins= IntField(required=True)
    test_low_coins = IntField(required=False, default=0)
    test_medium_coins = IntField(required=False, default=0)
    test_high_coins = IntField(required=False, default=0)
    quiz_low_coins = IntField(required=False, default=0)
    quiz_medium_coins = IntField(required=False, default=0)
    quiz_high_coins = IntField(required=False, default=0)
    coins_enable_config = EmbeddedDocumentField(
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
            "page_completion_coins": self.page_completion_coins,
            "test_completion_coins": self.test_completion_coins,
            "quiz_completion_coins": self.quiz_completion_coins,
            "login_coins": self.login_coins,
            "streak_coins": self.streak_coins,
            "coin_value_per_unit": self.coin_value_per_unit,
            "test_low_coins": self.test_low_coins,
            "test_medium_coins": self.test_medium_coins,
            "test_high_coins": self.test_high_coins,
            "quiz_low_coins": self.quiz_low_coins,
            "quiz_medium_coins": self.quiz_medium_coins,
            "quiz_high_coins": self.quiz_high_coins,
            "coins_enable_config": {
                "page_completion": self.coins_enable_config.page_completion,
                "test_completion": self.coins_enable_config.test_completion,
                "quiz_completion": self.coins_enable_config.quiz_completion,
                "test_low": self.coins_enable_config.test_low,
                "test_medium": self.coins_enable_config.test_medium,
                "test_high": self.coins_enable_config.test_high,
                "quiz_low": self.coins_enable_config.quiz_low,
                "quiz_medium": self.coins_enable_config.quiz_medium,
                "quiz_high": self.coins_enable_config.quiz_high,
                "login": self.coins_enable_config.login,
                "streak": self.coins_enable_config.streak,
                "materials": self.coins_enable_config.materials,
            },
            # "total_coins": self.total_coins(),
            "material_coins":self.materials_coins,
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
            "material_coins":self.materials_coins,
            "coin_value_per_unit": self.coin_value_per_unit,
            "test_low_coins": self.test_low_coins,
            "test_medium_coins": self.test_medium_coins,
            "test_high_coins": self.test_high_coins,
            "quiz_low_coins": self.quiz_low_coins,
            "quiz_medium_coins": self.quiz_medium_coins,
            "quiz_high_coins": self.quiz_high_coins,
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

