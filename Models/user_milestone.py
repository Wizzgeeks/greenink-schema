from mongoengine import *
from datetime import datetime, timezone
from Models.user import Users
from Models.course import Course
from Models.subject import Subject
from Models.topic import Topic
from Models.subtopic import Subtopic


class TrackedMilestoneItem(EmbeddedDocument):
    milestone_type = StringField(choices=['one_day', 'one_week', 'one_month'], required=True)

    course = StringField(required=True)
    subject = StringField()
    topic = StringField()
    subtopic = StringField()

    start_date = DateTimeField(default=lambda: datetime.now(timezone.utc))
    end_date = DateTimeField(required=True)

    status = StringField(choices=['active', 'expired', 'completed'], default='active')
    notified = BooleanField(default=False)


class TopicMilestoneListField(EmbeddedDocument):
    topic = StringField(required=True)
    subtopics = ListField(StringField())

    def to_json(self):
        return {
            "topic": self.topic,
            "subtopics": self.subtopics
        }


class SubjectMilestoneListField(EmbeddedDocument):
    subject = StringField(required=True)
    topics = ListField(EmbeddedDocumentField(TopicMilestoneListField))

    def to_json(self):
        return {
            "subject": self.subject,
            "topics": [t.to_json() for t in self.topics]
        }



class UserMilestone(Document):
    user = ReferenceField(Users, reverse_delete_rule=CASCADE)
    course = ReferenceField(Course, reverse_delete_rule=CASCADE)
    one_month = ListField(EmbeddedDocumentField(SubjectMilestoneListField))
    one_week = ListField(EmbeddedDocumentField(SubjectMilestoneListField))
    one_day = ListField(EmbeddedDocumentField(SubjectMilestoneListField))
    tracked_items = ListField(EmbeddedDocumentField(TrackedMilestoneItem)) 
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super().save(*args, **kwargs)

    def to_json(self):
        return {
            "id": str(self.id),
            "user": str(self.user.id) if self.user else None,
            "course": str(self.course.id) if self.course else None,
            "one_month": [s.to_json() for s in self.one_month],
            "one_week": [s.to_json() for s in self.one_week],
            "one_day": [s.to_json() for s in self.one_day],
            "tracked_items":self.tracked_items,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
