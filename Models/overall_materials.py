from mongoengine import CASCADE, Document, StringField, ReferenceField, DateTimeField,BooleanField  
from datetime import datetime, timezone
from Models.course import Course

class OverallMaterials(Document):
    course=ReferenceField(Course,required=True,reverse_delete_rule=CASCADE)
    name=StringField(required=True)
    content=StringField(required=True)
    publish=BooleanField(default=False)
    materials_type = StringField(choices=["pdf", "videos", "image", "ppt", "audio"],required=True)
    created_by=StringField()
    updated_by = StringField()
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(OverallMaterials, self).save(*args, **kwargs)
    def to_json(self):
        return {
            "id": str(self.id),
            "course":str(self.course.id) if self.course else None,
            "name": self.name,
            "publish": self.publish,
            "content": self.content,
            "materials_type":self.materials_type,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
    
    def to_minimal_json(self):
        return {
            "id": str(self.id),
            "materials_folders":str(self.course.id) if self.course else None,
            "name": self.name,
            "publish": self.publish,
            "materials_type":self.materials_type,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }