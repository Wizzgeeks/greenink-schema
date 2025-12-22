from mongoengine import Document, ReferenceField, DateTimeField, StringField, BooleanField, CASCADE,IntField
from datetime import datetime, timezone
from Models.course import Course
from Models.institution_users import InstitutionUsers

class TeacherCourseCompleted(Document):
    course = ReferenceField(Course, reverse_delete_rule=CASCADE, required=True)
    teacher = ReferenceField(InstitutionUsers, reverse_delete_rule=CASCADE, required=True)
    completed = BooleanField(default=False)
    total_page_count=IntField(default=0)
    completed_page_count=IntField(default=0)
    total_subject_count=IntField(default=0)
    completed_subject_count=IntField(default=0)
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(TeacherCourseCompleted, self).save(*args, **kwargs)

    def to_json(self):
        return {
            "id": str(self.id),
            # "course": self.course.id if self.course else None,
            # "user": self.user.to_json() if self.user else None,
            "completed": self.completed,
            "total_page_count": self.total_page_count,
            "completed_page_count": self.completed_page_count,
            "total_subject_count": self.total_subject_count,
            "completed_subject_count": self.completed_subject_count,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }