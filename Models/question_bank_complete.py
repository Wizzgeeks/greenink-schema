from mongoengine import CASCADE, NULLIFY, Document,StringField,BooleanField,EnumField,ReferenceField,ListField,DictField,EmbeddedDocument,DateTimeField,IntField,EmbeddedDocumentField
from datetime import datetime,timezone
from Models.user import Users
from Models.question_bank import QuestionBank


class LevelListFeild(EmbeddedDocument):
    material=ReferenceField(QuestionBank)
    mark=IntField()
    feedback=StringField()
    def to_json(self):
        return {
            "material":str(self.material) if self.material else None,
            "mark":self.mark,
            "feedback":self.feedback
        }


class QuestionBankComplete(Document):
    user=ReferenceField(Users,reverse_delete_rule=CASCADE)
    easy_type=ListField(EmbeddedDocumentField(LevelListFeild))
    medium_type=ListField(EmbeddedDocumentField(LevelListFeild))
    hard_type=ListField(EmbeddedDocumentField(LevelListFeild))
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))


    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(QuestionBankComplete, self).save(*args, **kwargs)

    def to_json(self):
        return{
            "id": str(self.id),
            "user":str(self.user) if self.user else None,
            "easy_type": [p.to_json() for p in self.easy_type],
            "medium_type": [p.to_json() for p in self.medium_type],
            "hard_type": [p.to_json() for p in self.hard_type],
            "created_at": self.created_at,
            "updated_at": self.updated_at,            
        }
