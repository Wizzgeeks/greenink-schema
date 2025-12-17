from mongoengine import Document, StringField, IntField, ListField,ReferenceField,DateTimeField,BooleanField,CASCADE,DictField
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
    feedback=ListField(DictField(),default=[])
    total_questions=IntField()
    created_by=StringField()
    updated_by = StringField()
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(TestResult, self).save(*args, **kwargs)
    def to_json(self):
        return {
            "id": str(self.id),
            "course": str(self.course.id) if self.course else None,
            "subject": str(self.subject.id) if self.subject else None,
            "topic": str(self.topic.id) if self.topic else None,
            "subtopic": str(self.subtopic.id) if self.subtopic else None,
            "course_page_test": str(self.course_page_test.id) if self.course_page_test else None,
            "subject_page_test": str(self.subject_page_test.id) if self.subject_page_test else None,
            "topic_page_test": str(self.topic_page_test.id) if self.topic_page_test else None,
            "subtopic_page_test": str(self.subtopic_page_test.id) if self.subtopic_page_test else None,
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




    

    
