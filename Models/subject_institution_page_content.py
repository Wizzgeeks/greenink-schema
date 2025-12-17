from mongoengine import Document, StringField, ReferenceField, DateTimeField, BooleanField,ListField,DictField,CASCADE
from datetime import datetime, timezone
from Models.course import Course
from Models.question_bank import QuestionBank
from Models.subject import Subject
from Models.institution import Institution


class SubjectInstitutionPageContent(Document):
    course=ReferenceField(Course, required=True,reverse_delete_rule=CASCADE)
    subject=ReferenceField(Subject, required=True, reverse_delete_rule=CASCADE)
    institution=ReferenceField(Institution, required=True, reverse_delete_rule=CASCADE)
    question_bank=ReferenceField(QuestionBank)
    
    name=StringField(required=True)
    page_type=StringField(choices=['content','quiz','question_bank'], required=True)
    content=ListField(DictField(),default=[])

    compulsory=BooleanField(default=False)
    start_initial=BooleanField(default=False)
    start_end=BooleanField(default=False)


    is_deleted=BooleanField(default=False)
    created_by=StringField()
    updated_by=StringField()
    created_at=DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at=DateTimeField(default=lambda: datetime.now(timezone.utc))
    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(SubjectInstitutionPageContent, self).save(*args, **kwargs)
    def to_json(self):
        return {
            "id": str(self.id),
            "course": self.course.to_json() if self.course else None,
            "subject": self.subject.to_json()if self.subject else None,
            "institution":self.institution.to_json() if self.institution else  None,
            "question_bank": self.question_bank.to_json() if self.question_bank else None,
            "name": self.name,
            "page_type": self.page_type,
            "content": self.content,
            "is_deleted": self.is_deleted,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }