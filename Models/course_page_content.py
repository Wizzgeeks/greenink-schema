from mongoengine import Document, StringField, ReferenceField, DateTimeField, BooleanField,ListField,DictField,CASCADE,IntField,NULLIFY
from datetime import datetime, timezone
from Models.course import Course
from Models.question_bank import QuestionBank
class CoursePageContent(Document):
    course=ReferenceField(Course, required=True,reverse_delete_rule=CASCADE)
    question_bank=ReferenceField(QuestionBank)
    name=StringField(required=True)
    page_type=StringField(choices=['content','quiz','question_bank','test','mcq','match','fillups','content','expand','update','trueorfalse','analysis','active_recall','active_recall_content','active_recall_test'], required=True)
    content=ListField(DictField(),default=[])
    medium_content=ListField(DictField())
    hard_content=ListField(DictField())

    compulsory=BooleanField(default=False)
    start_initial=BooleanField(default=False)
    start_end=BooleanField(default=False)


    child_pages = ListField(ReferenceField("CoursePageContent", reverse_delete_rule=NULLIFY))
    hierarcy_level=IntField(default=0)
    
    duration=IntField(default=0)
    pass_percentage=IntField(default=0)

    sequence=IntField(default=0)

    is_deleted=BooleanField(default=False)
    created_by=StringField()
    updated_by=StringField()
    created_at=DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at=DateTimeField(default=lambda: datetime.now(timezone.utc))
    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(CoursePageContent, self).save(*args, **kwargs)
    def to_json(self):
        return {
            "id": str(self.id),
            # "course": self.course.to_json() if self.course else None,
            # "question_bank": self.question_bank.to_json() if self.question_bank else None,
            "sequence": self.sequence,
            "name": self.name,
            "page_type": self.page_type,
            "content": self.content,
            "is_deleted": self.is_deleted,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "duration":self.duration,
            "pass_percentage":self.pass_percentage
        }
    def to_json_medium(self):
        return {
            "id": str(self.id),
            "sequence":self.sequence,
            "name": self.name,
            "page_type": self.page_type,
            "medium_content": self.medium_content if self.medium_content else [],
            "is_deleted": self.is_deleted,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "duration":self.duration,
            "pass_percentage":self.pass_percentage
        }
    def to_json_hard(self):
        return {
            "id": str(self.id),
            "sequence":self.sequence,
            "name": self.name,
            "page_type": self.page_type,
            "hard_content": self.hard_content if self.hard_content else [],
            "is_deleted": self.is_deleted,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "duration":self.duration,
            "pass_percentage":self.pass_percentage
        }
    def to_json_difficulty(self, difficulty_level):
        content_map={
            "easy":self.content,
            "medium":self.medium_content if self.medium_content else self.content,
            "hard":self.hard_content if self.hard_content else self.content
        }
        return {
            "id": str(self.id),
            # "course": self.course.to_json() if self.course else None,
            # "subject": self.subject.to_json()if self.subject else None,
            # "topic": self.topic.to_json() if self.topic else None,
            "question_bank": str(self.question_bank.to_json()) if self.question_bank else None,
            "sequence":self.sequence,
            "name": self.name,
            "page_type": self.page_type,
            "content": content_map.get(difficulty_level, self.content),
            "difficulty_level": difficulty_level,
            "is_deleted": self.is_deleted,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "duration":self.duration,
            "pass_percentage":self.pass_percentage
            
        }
    def to_minimal_json(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "page_type": self.page_type,
            "sequence": self.sequence,
            "child_pages": [cp.to_minimal_json() for cp in self.child_pages] if self.child_pages else [],
            "duration":self.duration,
            "pass_percentage":self.pass_percentage
        }