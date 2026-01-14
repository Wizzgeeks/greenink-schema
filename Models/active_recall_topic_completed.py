from Models.course import Course
from Models.subject import Subject
from Models.topic import Topic
from mongoengine import Document, ReferenceField, DateTimeField, StringField, BooleanField, CASCADE,ListField,DictField,IntField
from datetime import datetime, timezone
from Models.user import Users
from Models.topic_page_content import TopicPageContent
class ActiveRecallTopicCompleted(Document):
    course = ReferenceField(Course, reverse_delete_rule=CASCADE, required=True)
    subject = ReferenceField(Subject, reverse_delete_rule=CASCADE, required=True)
    topic = ReferenceField(Topic, reverse_delete_rule=CASCADE, required=True)
    user = ReferenceField(Users, reverse_delete_rule=CASCADE, required=True)
    topic_page_content = ReferenceField(TopicPageContent, reverse_delete_rule=CASCADE, required=True)
    #test result fields
    attempt_data=ListField(DictField(),default=[])
    completed=BooleanField()
    no_of_questions_attempted=IntField()
    no_of_question_correct=IntField()
    feedback=ListField(DictField(),default=[])
    total_questions=IntField()
    completed = BooleanField(default=False)
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(ActiveRecallTopicCompleted, self).save(*args, **kwargs)

    def to_json(self):
        return {
            "id": str(self.id),
            "completed": self.completed,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
    def to_active_recall_test_result(self):
        return {
            "user": str(self.user.id) if self.user else None,
            "attempt_data": self.attempt_data,
            "completed": self.completed,
            "no_of_questions_attempted": self.no_of_questions_attempted,
            "no_of_question_correct": self.no_of_question_correct,
            "total_questions": self.total_questions,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "feedback": self.feedback,
        }
        