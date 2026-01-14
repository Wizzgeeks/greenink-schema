from Models.subject import Subject
from Models.course import Course
from Models.subject_page_content import SubjectPageContent
from Models.user import Users
from mongoengine import (
    Document, ReferenceField, DateTimeField, BooleanField,
    CASCADE,ListField,DictField,IntField
)
from datetime import datetime, timezone

class ActiveRecallSubjectCompleted(Document):
    course = ReferenceField(Course, reverse_delete_rule=CASCADE, required=True)
    subject = ReferenceField(Subject, reverse_delete_rule=CASCADE, required=True)
    subject_page_content = ReferenceField(SubjectPageContent, reverse_delete_rule=CASCADE, required=True)
    user = ReferenceField(Users, reverse_delete_rule=CASCADE, required=True)
    completed = BooleanField(default=False)
    #test result fields
    attempt_data=ListField(DictField(),default=[])
    completed=BooleanField()
    no_of_questions_attempted=IntField()
    no_of_question_correct=IntField()
    feedback=ListField(DictField(),default=[])
    total_questions=IntField()
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(ActiveRecallSubjectCompleted, self).save(*args, **kwargs)

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