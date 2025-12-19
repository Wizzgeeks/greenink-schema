from mongoengine import CASCADE, Document, StringField, ListField, ReferenceField, DateTimeField,DictField,BooleanField  
from datetime import datetime, timezone
from Models.materials_folders import MaterialsFolders


class InstitutionMaterials(Document):
    materials_folders=ReferenceField(MaterialsFolders,required=True,reverse_delete_rule=CASCADE)
    name =StringField(required=True)
    content =StringField(required=True)
    publish=BooleanField(default=False)
    materials_type = StringField(choices=["pdf", "videos", "image", "ppt", "audio"],required=True)
    created_by=StringField()
    updated_by = StringField()
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(InstitutionMaterials, self).save(*args, **kwargs)
    def to_json(self):
        return {
            "id": str(self.id),
            "materials_folders":str(self.materials_folders.id) if self.materials_folders else None,
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
            "materials_folders":str(self.materials_folders.id) if self.materials_folders else None,
            "name": self.name,
            "publish": self.publish,
            "materials_type":self.materials_type,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }