from mongoengine import Document, ReferenceField, DateTimeField, BooleanField, CASCADE, StringField,ListField,NULLIFY
from datetime import datetime, timezone
from Models.course import Course
from Models.institution import Institution
from Models.institution_users import InstitutionUsers


class Batches(Document):
    institution = ReferenceField(Institution, reverse_delete_rule=CASCADE)
    course = ReferenceField(Course, reverse_delete_rule=CASCADE)
    name = StringField(required=True)
    teachers = ListField(ReferenceField(InstitutionUsers, reverse_delete_rule=NULLIFY))
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    created_by = StringField()
    updated_by = StringField()

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(Batches, self).save(*args, **kwargs)

    def to_json(self):
        return {
            "id": str(self.id),
            "institution": self.institution.to_json() if self.institution else None,
            "course": self.course.to_json() if self.course else None,
            "name": self.name,
            "teachers": [teacher.to_user() for teacher in self.teachers] if self.teachers else [],
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }