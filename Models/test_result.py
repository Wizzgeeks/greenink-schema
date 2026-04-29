from mongoengine import Document, FloatField, StringField, IntField, ListField,ReferenceField,DateTimeField,BooleanField,CASCADE,DictField
from datetime import datetime, timezone
from Models.course_page_content import CoursePageContent
from Models.subject_page_content import SubjectPageContent
from Models.topic_page_content import TopicPageContent
from Models.subtopic_page_content import SubtopicPageContent
from Models.course import Course
from Models.subject import Subject
from Models.subtopic import Subtopic
from Models.topic import Topic
from Models.user import Users

class TestResult(Document):
    course=ReferenceField(Course,reverse_delete_rule=CASCADE)
    subject=ReferenceField(Subject,reverse_delete_rule=CASCADE)
    topic=ReferenceField(Topic,reverse_delete_rule=CASCADE)
    subtopic=ReferenceField(Subtopic,reverse_delete_rule=CASCADE)
    course_page_test = ReferenceField(
            CoursePageContent, reverse_delete_rule=CASCADE)  
    subject_page_test = ReferenceField(
            SubjectPageContent, reverse_delete_rule=CASCADE)  
    topic_page_test = ReferenceField(
            TopicPageContent, reverse_delete_rule=CASCADE)  
    subtopic_page_test = ReferenceField(
            SubtopicPageContent, reverse_delete_rule=CASCADE)
    user=ReferenceField(Users,required=True,reverse_delete_rule=CASCADE)
    attempt_data=ListField(DictField(),default=[])
    completed=BooleanField()
    no_of_questions_attempted=IntField()
    no_of_question_correct=IntField()
    score=FloatField()
    feedback=ListField(DictField(),default=[])
    total_questions=IntField()
    created_by=StringField()
    updated_by = StringField()
    test_score_band= StringField()
    test_score_coins= IntField()
    test_score_xp= IntField()
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(TestResult, self).save(*args, **kwargs)
    def to_json(self):
        return {
            "id": str(self.id),
            "attempt_data": self.attempt_data,
            "completed": self.completed,
            "no_of_questions_attempted": self.no_of_questions_attempted,
            "no_of_question_correct": self.no_of_question_correct,
            "total_questions": self.total_questions,
            "feedback": self.feedback,
                "score": self.score,
        }





    

    
