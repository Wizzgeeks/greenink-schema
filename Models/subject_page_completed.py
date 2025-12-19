from mongoengine import Document, ReferenceField, DateTimeField, StringField, BooleanField, CASCADE,IntField
from datetime import datetime, timezone
from Models.subject_page_content import SubjectPageContent
from Models.user import Users
from Models.course import Course
from Models.subject import Subject

class SubjectPageCompleted(Document):
    course = ReferenceField(Course, reverse_delete_rule=CASCADE, required=True)
    subject = ReferenceField(Subject, reverse_delete_rule=CASCADE, required=True)
    subject_page_content = ReferenceField(SubjectPageContent, reverse_delete_rule=CASCADE, required=True)
    user = ReferenceField(Users, reverse_delete_rule=CASCADE, required=True)
    completed = BooleanField(default=False)
    hierarcy_level=IntField(default=0)
    page_type=StringField(choices=['content','quiz','question_bank','test','mcq','match','fillups','content','expand','update','trueorfalse','analysis'], required=True)
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(SubjectPageCompleted, self).save(*args, **kwargs)

    def to_json(self):
        return {
            "id": str(self.id),
            # "course": self.course.id if self.course else None,
            # "subject": self.subject.id if self.subject else None,
            # "subject_page_content": self.subject_page_content.id if self.subject_page_content else None,
            # "user": self.user.to_json() if self.user else None,
            "completed": self.completed,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }