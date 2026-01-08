from mongoengine import *
from datetime import datetime, timezone
from Models.user import Users
from Models.course import Course
from Models.subject import Subject
from Models.topic import Topic
from Models.subtopic import Subtopic


class SubtopicMilestoneListField(EmbeddedDocument):
    subtopics = ListField(ReferenceField(Subtopic))

    def to_json(self):
        return {
            "subtopics": [str(s.id) for s in self.subtopics]
        }


class TopicMilestoneListField(EmbeddedDocument):
    topic = ReferenceField(Topic)
    subtopics = EmbeddedDocumentField(SubtopicMilestoneListField)

    def to_json(self):
        return {
            "topic": str(self.topic.id) if self.topic else None,
            "subtopics": self.subtopics.to_json() if self.subtopics else []
        }


class SubjectMilestoneListField(EmbeddedDocument):
    subject = ReferenceField(Subject)
    topics = ListField(EmbeddedDocumentField(TopicMilestoneListField))

    def to_json(self):
        return {
            "subject": str(self.subject.id) if self.subject else None,
            "topics": [t.to_json() for t in self.topics]
        }


class UserMilestone(Document):
    user = ReferenceField(Users, reverse_delete_rule=CASCADE)
    course = ReferenceField(Course, reverse_delete_rule=CASCADE)
    one_month = ListField(EmbeddedDocumentField(SubjectMilestoneListField))
    one_week = ListField(EmbeddedDocumentField(SubjectMilestoneListField))
    one_day = ListField(EmbeddedDocumentField(SubjectMilestoneListField))
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
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
