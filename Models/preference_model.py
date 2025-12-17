from mongoengine import Document, DateTimeField, BooleanField, ListField, DictField,StringField
from datetime import datetime, timezone


class PreferenceQuestion(Document):
    name=StringField(required=True)
    content = ListField(DictField(), default=[])
    default = BooleanField(default=False)
    created_by=StringField()
    updated_by = StringField()
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))

    

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(PreferenceQuestion, self).save(*args, **kwargs)

    def to_json(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "content": self.content,
            "default": self.default,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
    def to_min_json(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "default": self.default,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }