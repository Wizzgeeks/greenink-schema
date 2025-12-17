from mongoengine import Document, StringField, ReferenceField, DateTimeField, BooleanField,ListField,DictField,CASCADE,IntField,NULLIFY
from datetime import datetime, timezone
from Models.course import Course
from Models.question_bank import QuestionBank
from Models.subject import Subject


class SubjectPageContent(Document):
    course=ReferenceField(Course, required=True,reverse_delete_rule=CASCADE)
    subject=ReferenceField(Subject, required=True, reverse_delete_rule=CASCADE)
    question_bank=ReferenceField(QuestionBank)

    name=StringField(required=True)
    page_type=StringField(choices=['content','quiz','question_bank','test','mcq','match','fillups','content','expand','update','trueorfalse','analysis'], required=True)
    content=ListField(DictField(),default=[])

    compulsory=BooleanField(default=False)
    start_initial=BooleanField(default=False)
    start_end=BooleanField(default=False)
    sequence=IntField(default=0)
    
    child_pages = ListField(ReferenceField("SubjectPageContent", reverse_delete_rule=NULLIFY))
    hierarcy_level=IntField(default=0)
    duration=IntField(default=0)
    pass_percentage=IntField(default=0)


    is_deleted=BooleanField(default=False)
    created_by=StringField()
    updated_by=StringField()
    created_at=DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at=DateTimeField(default=lambda: datetime.now(timezone.utc))
    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(SubjectPageContent, self).save(*args, **kwargs)
    def to_json(self):
        return {
            "id": str(self.id),
            "course": self.course.to_json() if self.course else None,
            "subject": self.subject.to_json()if self.subject else None,
            "question_bank": str(self.question_bank.to_json()) if self.question_bank else None,
            "name": self.name,
            "page_type": self.page_type,
            "sequence":self.sequence,
            "content": self.content,
            "is_deleted": self.is_deleted,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "duration":self.duration,
            "pass_percentage":self.pass_percentage
        }
    def to_minimal_json(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "page_type": self.page_type,
            "sequence": self.sequence,
            "child_pages": [cp.to_minimal_json() for cp in self.child_pages] if self.child_pages else [],
            "hierarcy_level": self.hierarcy_level,
            "duration":self.duration,
            "pass_percentage":self.pass_percentage
        }