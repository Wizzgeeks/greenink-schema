from mongoengine import Document, ReferenceField, DateTimeField,ListField,BooleanField,CASCADE,StringField,IntField
from datetime import datetime, timezone
from Models.course import Course

class Blog(Document):
    course=ReferenceField(Course,required=True,reverse_delete_rule=CASCADE)
    title=StringField()
    blog_type=StringField(choices=['text','video','audio'],default='text')
    image_url=StringField()
    content_url = StringField()
    source_type = StringField(
        choices=["upload", "youtube", "public_url"],
        required=True
    )
    blog_description=StringField()
    description=StringField()
    publish=BooleanField(default=False)
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(Blog, self).save(*args, **kwargs)

    def to_json(self):
        return {
            "id": str(self.id),
            "title":self.title,
            "image_url":self.image_url,
            "blog_description":self.blog_description,
            'description':self.description,
            "publish":self.publish,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "blog_type": self.blog_type,
            "content_url": self.content_url,
            "source_type": self.source_type
        }
    
    
    def to_minimal_json(self):
        return {
            "id": str(self.id),
            "title":self.title,
            "image_url":self.image_url,
            "blog_description":self.blog_description,
            "publish":self.publish,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "blog_type": self.blog_type,
        }
