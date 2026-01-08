from mongoengine import CASCADE, NULLIFY, Document,StringField,BooleanField,EnumField,ReferenceField,ListField,DictField,EmbeddedDocument,DateTimeField,IntField,EmbeddedDocumentField
from datetime import datetime,timezone
from Models.user import Users
from Models.course import Course
from Models.subject import Subject
from Models.topic import Topic
from Models.subtopic import Subtopic


class MilestoneListFeild(EmbeddedDocument):
    subject=ListField(ReferenceField(Subject))
    topic=ListField(ReferenceField(Topic))
    subtopic=ListField(ReferenceField(Subtopic))
   
    def to_json(self):
        return {
            "subject":str(self.subject.id) if self.subject else None,
            "topic":str(self.topic.id) if self.topic else None,
            "subtopic":str(self.subtopic.id) if self.subtopic else None,
        }


class UserMilestone(Document):
    user=ReferenceField(Users,reverse_delete_rule=CASCADE)
    course=ReferenceField(Course,reverse_delete_rule=CASCADE)
    one_month=ListField(EmbeddedDocumentField(MilestoneListFeild))
    one_week=ListField(EmbeddedDocumentField(MilestoneListFeild))
    one_day=ListField(EmbeddedDocumentField(MilestoneListFeild))
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))


    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(UserMilestone, self).save(*args, **kwargs)

    def to_json(self):
        return{
            "id": str(self.id),
            "user":str(self.user.id) if self.user else None,
            "course":str(self.course.id) if self.course else None,
            "one_month": [p.to_json() for p in self.one_month],
            "one_week": [p.to_json() for p in self.one_week],
            "one_day": [p.to_json() for p in self.one_day],
            "created_at": self.created_at,
            "updated_at": self.updated_at,            
        }
