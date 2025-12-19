from Models.institution import Institution
from Models.course import Course
from Models.batches import Batches
from mongoengine import Document, ReferenceField, DateTimeField, BooleanField, CASCADE, StringField,ListField,DictField,IntField
from datetime import datetime, timezone


class Users(Document):
    institution=ReferenceField(Institution, reverse_delete_rule=CASCADE)
    course=ReferenceField(Course, reverse_delete_rule=CASCADE)
    batch=ReferenceField(Batches, reverse_delete_rule=CASCADE)
    name=StringField(required=True)
    email=StringField(unique=True,sparse=True)
    register_no=StringField(unique=True,sparse=True)
    password=StringField(required=True)
    test_page_preference=StringField(choices=['easy','medium',"hard"],default='easy')
    ai_teaching_preference=StringField(choices=['easy','medium',"hard"],default='easy')
    auth_token=StringField()
    preference=ListField(DictField())
    grade=StringField()
    disabled=BooleanField(default=False)
    is_deleted=BooleanField(default=False)
    created_at=DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at=DateTimeField(default=lambda: datetime.now(timezone.utc))
    created_by=StringField()
    updated_by=StringField()
    
    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(Users, self).save(*args, **kwargs)
        
    def to_json(self):
        return {
            "id": str(self.id),
            # "institution": self.institution.to_json() if self.institution else None,
            # "course": self.course.to_json() if self.course else None,
            # "batch": self.batch.to_json() if self.batch else None,
           "batch_name": self.batch.name if self.batch else None,
           "batch_assigned": True if self.batch else False,
            "name": self.name,
            "email": self.email if self.email else "",
            "register_no": self.register_no if self.register_no else "",
            "disabled": self.disabled if self.disabled else False,
            "is_deleted": self.is_deleted,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "grade":self.grade if self.grade else "",



        }
    def to_user(self):
        return {
            "id": str(self.id),
            "institution_name": self.institution.name if self.institution else None,
            "intitution_type": self.institution.type if self.institution else None,
            "course_name": self.course.name if self.course else None,
            "batch_name": self.batch.name if self.batch else None,
            "name": self.name,
            "email": self.email if self.email else "",
            "register_no": self.register_no if self.register_no else "",
            "grade":self.grade if self.grade else "",   
            "preference":self.preference if self.preference else [],  
            "test_page_preference":self.test_page_preference if self.test_page_preference else "easy",
            "ai_teaching_preference":self.ai_teaching_preference if self.ai_teaching_preference else "easy",
                     
        }
    def to_admin(self):
        return {
            "id": str(self.id),
            # "institution": self.institution.to_json() if self.institution else None,
            # "course": self.course.to_json() if self.course else None,
            # "batch": self.batch.to_json() if self.batch else None,
            "name": self.name,
            "email": self.email if self.email else "",
            "register_no": self.register_no if self.register_no else "",
            "disabled": self.disabled if self.disabled else False,
            # "is_deleted": self.is_deleted,
            # "created_at": self.created_at,
            # "updated_at": self.updated_at,

        }