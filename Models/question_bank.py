from mongoengine import CASCADE, Document, StringField, ListField, ReferenceField, DateTimeField,DictField,BooleanField,IntField
from datetime import datetime, timezone
from Models.qb_folders import QuestionBankFolders


class QuestionBank(Document):
    questionbank_folders=ReferenceField(QuestionBankFolders,required=True,reverse_delete_rule=CASCADE)
    name =StringField(required=True)
    content =ListField(DictField(),default=[])
    publish=BooleanField(default=False)
    duration=IntField(default=0)
    created_by=StringField()
    updated_by = StringField()
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(QuestionBank, self).save(*args, **kwargs)
    def to_json(self):
        return {
            "id": str(self.id),
            "questionbank_folders":str(self.questionbank_folders.id) if self.questionbank_folders else None,
            "name": self.name,
            "publish": self.publish,
            "content": self.content,
            "duration":self.duration,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
    def to_minimal_json(self):
        return {
            "id": str(self.id),
            "questionbank_folders":str(self.questionbank_folders.id) if self.questionbank_folders else None,
            "name": self.name,
            "publish": self.publish,
            "duration":self.duration,

            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }