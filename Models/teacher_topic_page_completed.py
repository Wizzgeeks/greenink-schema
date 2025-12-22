from mongoengine import Document, ReferenceField, DateTimeField, StringField, BooleanField, CASCADE,IntField
from datetime import datetime, timezone
from Models.topic_page_content import TopicPageContent
from Models.institution_users import InstitutionUsers
from Models.course import Course
from Models.subject import Subject
from Models.topic import Topic

class TeacherTopicPageCompleted(Document):
    course = ReferenceField(Course, reverse_delete_rule=CASCADE, required=True)
    subject = ReferenceField(Subject, reverse_delete_rule=CASCADE, required=True)
    topic = ReferenceField(Topic, reverse_delete_rule=CASCADE, required=True)
    topic_page_content = ReferenceField(TopicPageContent, reverse_delete_rule=CASCADE, required=True)
    teacher = ReferenceField(InstitutionUsers, reverse_delete_rule=CASCADE, required=True)
    completed = BooleanField(default=False)
    hierarcy_level=IntField(default=0)
    page_type=StringField(choices=['content','quiz','question_bank','test','mcq','match','fillups','content','expand','update','trueorfalse','analysis'], required=True)
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(TeacherTopicPageCompleted, self).save(*args, **kwargs)

    def to_json(self):
        return {
            "id": str(self.id),
            # "course": self.course.id if self.course else None,
            # "subject": self.subject.id if self.subject else None,
            # "topic": self.topic.id if self.topic else None,
            # "topic_page_content": self.topic_page_content.id if self.topic_page_content else None,
            # "user": self.user.to_json() if self.user else None,
            "completed": self.completed,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "page_type": self.page_type,
        }