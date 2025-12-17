from Models.institution import Institution
from mongoengine import Document, ReferenceField, DateTimeField, BooleanField,StringField,NULLIFY,CASCADE
from datetime import datetime, timezone

class InstitutionUsers(Document):
    institution = ReferenceField(Institution, required=True, reverse_delete_rule=CASCADE)
    name=StringField(required=True)
    email=StringField(required=True, unique=True)
    password=StringField(required=True)
    auth_token=StringField()
    role=StringField(choices=['admin','teacher'])
    disabled=BooleanField(default=False)
    is_deleted=BooleanField(default=False)
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    created_by=StringField()
    updated_by=StringField()

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(InstitutionUsers, self).save(*args, **kwargs)

    def to_json(self):
        return {
            "id": str(self.id),
            "institution": self.institution.to_json() if self.institution else None,
            "name": self.name,
            "email": self.email,
            "role": self.role,
            "disabled":self.disabled if self.disabled else False,
            # "is_active": self.is_active,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
    def to_user(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "email": self.email,
        }