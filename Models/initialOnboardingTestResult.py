from mongoengine import Document, ReferenceField, DateTimeField, BooleanField, CASCADE, ListField,DictField,IntField,StringField,EmbeddedDocument,EmbeddedDocumentField,FloatField
from datetime import datetime, timezone
from Models.initialOnboardingTest import InitialOnboardingTest
from Models.user import Users

class CategoryScores(EmbeddedDocument):
    cognitive_function = FloatField(default=0, min_value=0, max_value=100)
    social_emotional_skill = FloatField(default=0, min_value=0, max_value=100)
    physical_development_skill = FloatField(default=0, min_value=0, max_value=100)
    creative_imagination = FloatField(default=0, min_value=0, max_value=100)
    critical_thinking_curiosity = FloatField(default=0, min_value=0, max_value=100)
    language_communication = FloatField(default=0, min_value=0, max_value=100)
    self_regulation_behavior = FloatField(default=0, min_value=0, max_value=100)

class InitialOnboardingTestResult(Document):
    initial_onboarding_test=ReferenceField(InitialOnboardingTest,required=True)
    user=ReferenceField(Users,required=True,reverse_delete_rule=CASCADE)
    attempt_data=ListField(DictField(),default=[])
    completed=BooleanField()
    attempt_questions=IntField()
    score=FloatField(min_value=0, max_value=100)
    category_scores = EmbeddedDocumentField(CategoryScores, default=CategoryScores)

    duration=IntField(default=0)
    
    created_at=DateTimeField(default=datetime.now(timezone.utc))
    updated_at=DateTimeField(default=datetime.now(timezone.utc))
    
    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(InitialOnboardingTestResult, self).save(*args, **kwargs)
    
    def to_json(self):
        return {
            "id": str(self.id),
            "initial_onboarding_test": str(self.initial_onboarding_test.id) if self.initial_onboarding_test else None,
            "attempt_data": self.attempt_data,
            "completed": self.completed,
            "attempt_questions": self.attempt_questions,
            "score": self.score,
            "category_scores": {
                "cognitive_function": self.category_scores.cognitive_function,
                "social_emotional_skill": self.category_scores.social_emotional_skill,
                "physical_development_skill": self.category_scores.physical_development_skill,
                "creative_imagination": self.category_scores.creative_imagination,
                "critical_thinking_curiosity": self.category_scores.critical_thinking_curiosity,
                "language_communication": self.category_scores.language_communication,
                "self_regulation_behavior": self.category_scores.self_regulation_behavior,
            } if self.category_scores else None,
            "duration": self.duration,
            "created_at": self.created_at if self.created_at else None,
            "updated_at": self.updated_at if self.updated_at else None,
        }

    def to_minimal_json(self):
        return {
            "id": str(self.id),
            "score": self.score,
            "completed": self.completed,
            "duration": self.duration,
            "attempt_questions": self.attempt_questions,
            "created_at": self.created_at if self.created_at else None,
        }

    
    