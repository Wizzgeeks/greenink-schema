from Models.course import Course
from mongoengine import Document, ReferenceField, DateTimeField, BooleanField, CASCADE, ListField,DictField,IntField,StringField
from datetime import datetime, timezone

class CoursePageQuestionBank(Document):
    course = ReferenceField(Course, reverse_delete_rule=CASCADE)
    name=StringField()
    question_bank_type=StringField(choices=['pdf','video','practise_test'], required=True)
    content=ListField(DictField(),default=[])
    duration=IntField(default=0)
    sequence=IntField(default=0)
    is_active=BooleanField(default=True)
    created_by=StringField()
    updated_by=StringField()
    created_at=DateTimeField(default=datetime.now(timezone.utc))
    updated_at=DateTimeField(default=datetime.now(timezone.utc))
    
    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(CoursePageQuestionBank, self).save(*args, **kwargs)
    
    def to_json(self):
        return {
            "id": str(self.id),
            "course": self.course.to_json() if self.course else None,
            "name": self.name,
            "question_bank_type": self.question_bank_type,
            "content": self.content or [],
            "duration": self.duration,
            "is_active": self.is_active,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
    def to_minimal_json(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "question_bank_type": self.question_bank_type,
            "sequence": self.sequence,
            "is_active": self.is_active,
        }