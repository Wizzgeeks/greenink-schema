from mongoengine import Document, ReferenceField,StringField, ListField, DictField, DateTimeField, BooleanField, IntField, CASCADE
from datetime import datetime, timezone
from Models.course import Course
from Models.subject import Subject
from Models.topic import Topic
from Models.subtopic import Subtopic
from Models.course_page_content import CoursePageContent
from Models.subject_page_content import SubjectPageContent
from Models.topic_page_content import TopicPageContent
from Models.subtopic_page_content import SubtopicPageContent
from Models.user import Users
from Models.adaptive_learning_test_mcq import AdaptiveLearningTestMcq


class AdaptiveLearningTestResult(Document):
    course = ReferenceField(Course, reverse_delete_rule=CASCADE)
    subject = ReferenceField(Subject, reverse_delete_rule=CASCADE)
    topic = ReferenceField(Topic, reverse_delete_rule=CASCADE)
    subtopic = ReferenceField(Subtopic, reverse_delete_rule=CASCADE)

    course_page = ReferenceField(CoursePageContent)
    subject_page = ReferenceField(SubjectPageContent)
    topic_page = ReferenceField(TopicPageContent)
    subtopic_page = ReferenceField(SubtopicPageContent)

    user = ReferenceField(Users, required=True)
    recall_page = ReferenceField(AdaptiveLearningTestMcq)

    attempt_data = ListField(DictField(), default=[])
    completed = BooleanField(default=False)

    no_of_questions_attempted = IntField()
    no_of_question_correct = IntField()
    total_questions = IntField()

    marks = IntField()

    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(AdaptiveLearningTestResult, self).save(*args, **kwargs)

    def to_json(self):
        return {
            "id": str(self.id),
            "course": str(self.course.id) if self.course else None,
            "subject": str(self.subject.id) if self.subject else None,
            "topic": str(self.topic.id) if self.topic else None,
            "subtopic": str(self.subtopic.id) if self.subtopic else None,
            "course_page": str(self.course_page.id) if self.course_page else None,
            "subject_page": str(self.subject_page.id) if self.subject_page else None,
            "topic_page": str(self.topic_page.id) if self.topic_page else None,
            "subtopic_page": str(self.subtopic_page.id) if self.subtopic_page else None,
            "user": str(self.user.id) if self.user else None,
            "recall_page": str(self.recall_page.id) if self.recall_page else None,
            "mcq_result": self.mcq_result,
            "marks": self.marks,
            "completed": self.completed,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
