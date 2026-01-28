from mongoengine import Document, IntField, ListField,ReferenceField,DateTimeField,BooleanField,CASCADE,DictField
from Models.user import Users
from datetime import datetime, timezone
from Models.overall_course_test import OverallCourseTest

class OverallCourseTestCompleted(Document):
    test=ReferenceField(OverallCourseTest,required=True,reverse_delete_rule=CASCADE)
    user=ReferenceField(Users,required=True,reverse_delete_rule=CASCADE)
    attempt_data=ListField(DictField(),default=[])
    completed=BooleanField()
    no_of_questions_attempted=IntField(default=0)
    no_of_question_correct=IntField(default=0)
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(OverallCourseTestCompleted, self).save(*args, **kwargs)
    

    def to_json(self):
        return {
            "id": str(self.id),
            "user": str(self.user.id) if self.user else None,
            "test":str(self.test.id) if self.test else None,
            "attempt_data": self.attempt_data,
            "completed": self.completed,
            "no_of_questions_attempted": self.no_of_questions_attempted,
            "no_of_question_correct": self.no_of_question_correct,
        }
    
    def to_user_list(self):
        return {
            "id": str(self.id),
            "user": str(self.user.id) if self.user else None,
            "test":str(self.test.id) if self.test else None,
            "no_of_questions_attempted": self.no_of_questions_attempted,
            "no_of_question_correct": self.no_of_question_correct,
            "created_at":self.created_at,
            "updated_at":self.updated_at

        }
    
    def to_admin_list(self):
        return {
            "id": str(self.id),
            "user": self.user.to_json() if self.user else None,
            "test":str(self.test.id) if self.test else None,
            "no_of_questions_attempted": self.no_of_questions_attempted,
            "no_of_question_correct": self.no_of_question_correct,
            "created_at":self.created_at,
            "updated_at":self.updated_at

        }