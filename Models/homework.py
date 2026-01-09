from mongoengine import Document, ReferenceField, DateTimeField,ListField,DictField,CASCADE,IntField,NULLIFY
from datetime import datetime, timezone
from Models.user import Users
from Models.institution_users import InstitutionUsers



class Homework(Document):
    teacher=ReferenceField(InstitutionUsers,reverse_delete_rule=CASCADE)
    content=ListField(DictField(),default=[])
    users = ListField(ReferenceField(Users, reverse_delete_rule=NULLIFY))
    deadline=DateTimeField()
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(Homework, self).save(*args, **kwargs)

    def to_json(self):
        return {
            "id": str(self.id),
            'teacher':str(self.teacher),
            "content":self.content,
            'users':[s.to_json() for s in self.users],
            'deadline':self.deadline,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
