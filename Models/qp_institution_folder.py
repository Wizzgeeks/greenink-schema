from typing import Required
from mongoengine import CASCADE, NULLIFY, Document,StringField,BooleanField,EnumField,ReferenceField,ListField,DictField,EmbeddedDocument,DateTimeField,IntField,EmbeddedDocumentField
from Models.course import Course
from Models.subject import Subject
from Models.topic import Topic
from Models.subtopic import Subtopic
from Models.institution import Institution
from datetime import datetime,timezone


class QuestionInstitutionBankFolders(Document):
    institution=ReferenceField(Institution,reverse_delete_rule=CASCADE)
    course=ReferenceField(Course,reverse_delete_rule=CASCADE)
    subject=ReferenceField(Subject,reverse_delete_rule=CASCADE)
    topic=ReferenceField(Topic,reverse_delete_rule=CASCADE)
    subtopic=ReferenceField(Subtopic,reverse_delete_rule=CASCADE)
    name=StringField(required=True)
    created_by=StringField()
    updated_by = StringField()
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))


    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(QuestionInstitutionBankFolders, self).save(*args, **kwargs)

    def to_json(self):
        return{
            "id": str(self.id),
            "institution": self.institution.to_json() if self.institution else None,
            "course":self.course.to_json() if self.course else None,
            "subject":self.subject.to_json() if self.subject else None,
            "topic":self.topic.to_json() if self.topic else None,
            "subptopic":self.subtopic.to_json() if self.subtopic else None,
            "name":self.name,
            "created_at": self.created_at,
            "updated_at": self.updated_at,            
        }
