from mongoengine import Document, StringField, ReferenceField, DateTimeField, BooleanField,CASCADE
from datetime import datetime, timezone


class Admin(Document):
    name=StringField(required=True)
    email=StringField(unique=True,sparse=True)
    # student_identification_number=StringField(unique=True,sparse=True)
    password=StringField(required=True)
    auth_token=StringField()
    disabled=BooleanField(default=False)
    is_deleted=BooleanField(default=False)
    created_at=DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at=DateTimeField(default=lambda: datetime.now(timezone.utc))
    created_by=StringField()
    updated_by=StringField()


    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(Admin, self).save(*args, **kwargs)

    def to_json(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "email": self.email,
            # "student_identification_number": self.student_identification_number,
            "password": self.password,
            "auth_token": self.auth_token,
            "disabled": self.disabled if self.disabled else False,
            "is_deleted": self.is_deleted,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "created_by": self.created_by,
            "updated_by": self.updated_by,
        }


    
    

