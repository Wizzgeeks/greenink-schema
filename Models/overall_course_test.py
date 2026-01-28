from mongoengine import Document, ReferenceField, DateTimeField,ListField,DictField,CASCADE,StringField,IntField
from datetime import datetime, timezone
from Models.course import Course

class OverallCourseTest(Document):
    course=ReferenceField(Course,required=True,reverse_delete_rule=CASCADE)
    name=StringField()
    content=ListField(DictField(),default=[])
    duration=IntField(default=0)
    deadline=DateTimeField()
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(OverallCourseTest, self).save(*args, **kwargs)

    def to_json(self):
        return {
            "id": str(self.id),
            "name":self.name,
            "duration":self.duration,
            "content":self.content,
            'deadline':self.deadline,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
    
    def to_user_homework(self):
        return {
            "id": str(self.id),
            "name":self.name,
            "duration":self.duration,
            'deadline':self.deadline,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
    
    def to_homework_json(self):
        return {
            "id": str(self.id),
            "name":self.name,
            "duration":self.duration,
            "content":self.content,
            'deadline':self.deadline,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
