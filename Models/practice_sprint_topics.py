from Models.course import Course
from mongoengine import Document, EmbeddedDocument, EmbeddedDocumentListField, StringField, ReferenceField,CASCADE,BooleanField,DateTimeField,FloatField,IntField,ListField,EmbeddedDocumentField,DictField



class Topic(EmbeddedDocument):
    name = StringField(required=True)
    active = BooleanField(default=True)

    def to_json(self):
        return {
            "name": self.name,
            "active": self.active
        }


class PracticeSprintTopics(Document):
    course = ReferenceField(Course, reverse_delete_rule=CASCADE, required=True)
    topics = EmbeddedDocumentListField(Topic)

    def to_json(self):
        return {
            "id": str(self.id),
            "course": str(self.course.id) if self.course else None,
            "topics": [t.to_json() for t in self.topics] if self.topics else []
        }

    def to_user_json(self):
        return {
            "id": str(self.id),
            "course": str(self.course.id) if self.course else None,
            "topics": [t.to_json() for t in self.topics if t.active] if self.topics else []
        }
