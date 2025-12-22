from mongoengine import Document, ReferenceField, DateTimeField, BooleanField, CASCADE, IntField,StringField
from datetime import datetime, timezone
from Models.course import Course
from Models.institution_users import InstitutionUsers
from Models.course_page_content import CoursePageContent

class TeacherCoursePageCompleted(Document):
    course = ReferenceField(Course, reverse_delete_rule=CASCADE, required=True)
    course_page_content = ReferenceField(CoursePageContent, reverse_delete_rule=CASCADE, required=True)
    teacher = ReferenceField(InstitutionUsers, reverse_delete_rule=CASCADE, required=True)
    completed = BooleanField(default=False)
    hierarcy_level = IntField(default=0)
    page_type = StringField(choices=['content','quiz','question_bank','test','mcq','match','fillups','content','expand','update','trueorfalse','analysis'], required=True)
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(TeacherCoursePageCompleted, self).save(*args, **kwargs)

    def to_json(self):
        return {
            "id": str(self.id),
            # "course": self.course.id if self.course else None,
            # "course_page_content": self.course_page_content.id if self.course_page_content else None,
            # "user": self.user.to_json() if self.user else None,
            "completed": self.completed,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "hierarcy_level": self.hierarcy_level,
            "page_type": self.page_type,
        }
