from mongoengine import Document, StringField  ,BooleanField,DateTimeField
from datetime import datetime,timezone


class Persona(Document):
    name = StringField(required=True, unique=True)
    persona=StringField()
    persona_type=StringField(choices=['ai_tutor','analysis_validation'],required=True)
    is_active= BooleanField(default=False)
    created_by=StringField()
    updated_by = StringField()
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(Persona, self).save(*args, **kwargs)

    def to_json(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "persona": self.persona,
            "persona_type": self.persona_type,
            "is_active": self.is_active,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
    def to_minimal_json(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "persona_type": self.persona_type,
            "is_active": self.is_active,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }