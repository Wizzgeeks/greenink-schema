from Models.institution import Institution
from Models.course import Course
from mongoengine import Document,ReferenceField,DateTimeField,BooleanField,ListField,NULLIFY,StringField
from datetime import datetime, timezone

class InstitutionCourse(Document):
    institution = ReferenceField(Institution, required=True)
    course =ListField(ReferenceField(Course,reverse_delete_rule=NULLIFY))
    created_by=StringField()
    updated_by = StringField()
    created_at = DateTimeField(default=datetime.now(timezone.utc))
    updated_at = DateTimeField(default=datetime.now(timezone.utc))
    is_active = BooleanField(default=True)
    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(InstitutionCourse, self).save(*args, **kwargs)
    def to_json(self):
        return {
            "id": str(self.id),
            # "institution": self.institution.to_json() if self.institution else None,
            "course": [
                c.to_json() for c in self.course
                if hasattr(c, "is_deleted") and not getattr(c, "is_deleted", False)
            ],
            "is_active": self.is_active,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
