from mongoengine import Document,StringField,ValidationError,BooleanField,IntField,DateTimeField
from datetime import datetime,timezone

class Model(Document):
    name = StringField(required=True)
    api_key = StringField(required=True)
    type = StringField(required=True)
    provider = StringField(choices=['gemini','openai','claude'],required=True)
    is_active = BooleanField(default=False)
    max_tokens=IntField(required=True)
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(Model, self).save(*args, **kwargs)
    
    def clean(self):
        if not self.name.strip():
            raise ValidationError("Model name cannot be empty")
        if not self.api_key.strip():
            raise ValidationError("Api key cannot be empty")
        if not self.type.strip():
            raise ValidationError("model type cannot be empty")

    def to_json(self):
        return {
            "id": str(self.id),
            "name":self.name,
            "type":self.type,
            "provider":self.provider,
            "is_active":self.is_active if self.is_active else False,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
    def to_admin(self):
        return{
            "id": str(self.id),
            "name":self.name,
            "type":self.type,
            "provider":self.provider,
            "api_key":self.api_key,
            "is_active":self.is_active if self.is_active else False,
            "max_tokens":self.max_tokens,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
    
        
        
    def update(self, **kwargs):
        self.clean()
        return super().update(**kwargs)