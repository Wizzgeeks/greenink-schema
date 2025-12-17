from Models.course_page_content import CoursePageContent
from Models.subject_page_content import SubjectPageContent
from Models.topic_page_content import TopicPageContent
from Models.subtopic_page_content import SubtopicPageContent

from mongoengine import Document, StringField, ReferenceField, ListField, DateTimeField,BooleanField,EmbeddedDocument,DictField,EmbeddedDocumentField,CASCADE,NULLIFY
from datetime import datetime, timezone
from Models.user import Users

class AiTutorContent(Document):
    course_page_content=ReferenceField(CoursePageContent,reverse_delete_rule=CASCADE)
    subject_page_content=ReferenceField(SubjectPageContent,reverse_delete_rule=CASCADE)
    topic_page_content=ReferenceField(TopicPageContent,reverse_delete_rule=CASCADE)
    subtopic_page_content=ReferenceField(SubtopicPageContent,reverse_delete_rule=CASCADE)
    user=ReferenceField(Users,reverse_delete_rule=CASCADE,required=True)
    content=ListField(DictField(),default=[])
    created_by=StringField()
    updated_by = StringField()
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(AiTutorContent, self).save(*args, **kwargs)
    def to_json(self):
        return {
            "id": str(self.id),
            "course_page_content_id": str(self.course_page_content.id) if self.course_page_content else None,
            "subject_page_content_id": str(self.subject_page_content.id) if self.subject_page_content else None,
            "topic_page_content_id": str(self.topic_page_content.id) if self.topic_page_content else None,
            "subtopic_page_content_id": str(self.subtopic_page_content.id) if self.subtopic_page_content else None,
            "content": self.content,
            "created_by": self.created_by if self.created_by else "",
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }