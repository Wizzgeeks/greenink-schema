from mongoengine import Document,StringField,BooleanField,EnumField,ReferenceField,ListField,DictField,EmbeddedDocument,DateTimeField,IntField,EmbeddedDocumentField
from datetime import datetime,timezone


class Prompt(Document):
    name = StringField(required=True)
    prompt=StringField()
    json_mode=BooleanField(default=False)
    json_schema=StringField()
    persona=StringField()
    json_schema_google=StringField()
    types=StringField(choices=['mcq','match','fillups','content','expand','update','trueorfalse','analysis'],required=True)
    default=BooleanField(default=False)
    created_by=StringField()
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    
    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(Prompt, self).save(*args, **kwargs)
    def to_json(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "prompt": self.prompt if self.prompt else "",
            "json_schema": self.json_schema if self.json_schema else "",
            "json_schema_google":self.json_schema_google if self.json_schema_google else "",
            "persona": self.persona if self.persona else "",
            "json_mode": self.json_mode,
            "created_at": self.created_at if self.created_at else None,
            "updated_at": self.updated_at if self.updated_at else None,
            "persona": self.persona if self.persona else "",
            "types": self.types,
            "default": self.default
        }
    def to_minimal_json(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "types": self.types,
            "created_at": self.created_at if self.created_at else None,
            "updated_at": self.updated_at if self.updated_at else None,
        }




