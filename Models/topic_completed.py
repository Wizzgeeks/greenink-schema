from mongoengine import Document, ReferenceField, DateTimeField, StringField, BooleanField, CASCADE,IntField
from datetime import datetime, timezone
from Models.subject import Subject
from Models.user import Users
from Models.course import Course
from Models.topic import Topic

class TopicCompleted(Document):
    course = ReferenceField(Course, reverse_delete_rule=CASCADE, required=True)
    subject = ReferenceField(Subject, reverse_delete_rule=CASCADE, required=True)
    topic = ReferenceField(Topic, reverse_delete_rule=CASCADE, required=True)
    user = ReferenceField(Users, reverse_delete_rule=CASCADE, required=True)
    completed = BooleanField(default=False)
    total_page_count=IntField(default=0)
    completed_page_count=IntField(default=0)
    total_subtopic_count=IntField(default=0)
    completed_subtopic_count=IntField(default=0)
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(TopicCompleted, self).save(*args, **kwargs)

    def to_json(self):
        return {
            "id": str(self.id),
            # "course": self.course.id if self.course else None,
            # "subject": self.subject.id if self.subject else None,
            # "topic": self.topic.id if self.topic else None,
            # "user": self.user.to_json() if self.user else None,
            "completed": self.completed,
            "total_page_count": self.total_page_count,
            "completed_page_count": self.completed_page_count,
            "total_subtopic_count": self.total_subtopic_count,
            "completed_subtopic_count": self.completed_subtopic_count,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }