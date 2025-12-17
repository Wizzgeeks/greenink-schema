
from Models.course import Course
from mongoengine import Document,StringField,ReferenceField,DateTimeField,BooleanField,CASCADE
from datetime import datetime,timezone

class Subject(Document):
    course = ReferenceField(Course, required=True,reverse_delete_rule=CASCADE)
    name = StringField(required=True)
    key = StringField(required=True, unique=True)
    is_deleted = BooleanField(default=False)
    created_by=StringField()
    updated_by = StringField()
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(Subject, self).save(*args, **kwargs)



    def to_json(self):
        return {
            "id": str(self.id),
            "course": self.course.to_json() if self.course else None,
            "name": self.name,
            "key": self.key,
            "is_deleted": self.is_deleted,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }