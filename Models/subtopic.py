from mongoengine import Document, StringField, ReferenceField,BooleanField, DateTimeField,CASCADE,IntField
from datetime import datetime, timezone
from Models.course import Course
from Models.subject import Subject
from Models.topic import Topic


class Subtopic(Document):
    course=ReferenceField(Course, required=True,reverse_delete_rule=CASCADE)
    subject=ReferenceField(Subject, required=True)
    topic=ReferenceField(Topic, required=True)
    name=StringField(required=True)
    key=StringField(required=True, unique=True)
    sequence=IntField(default=0)
    is_deleted=BooleanField(default=False)
    created_by=StringField()
    updated_by=StringField()
    created_at=DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at=DateTimeField(default=lambda: datetime.now(timezone.utc))

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(Subtopic, self).save(*args, **kwargs)


    def to_json(self):
        return {
            "id": str(self.id),
            "course": self.course.to_json() if self.course else None,
            "subject": self.subject.to_json() if self.subject else None,
            "topic": self.topic.to_json() if self.topic else None,
            "name": self.name,
            "key": self.key,
            "sequence": self.sequence,
            "is_deleted": self.is_deleted,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

