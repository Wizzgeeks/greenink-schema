from mongoengine import *
from datetime import datetime, timezone


class Videos(Document):
    title = StringField(required=True)
    description = StringField()
    source_type = StringField(
        choices=["s3", "youtube", "public_url"],
        required=True
    )
    video_url = StringField(required=True)
    mime_type = StringField()            
    duration = IntField()              
    thumbnail_url = StringField()
    publish = BooleanField(default=True) 
    created_by = StringField()
    updated_by = StringField()
    is_active = BooleanField(default=True)
    is_deleted = BooleanField(default=False)
    tags = ListField(StringField())
    visibility = StringField(
        choices=["public", "private"],
        default="public"
    )

    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))

    meta = {
        "collection": "videos",
        "indexes": [
            "source_type",
            "is_active",
            "created_at"
        ]
    }

    def to_json(self):
        return {
            "id": str(self.id),
            "title": self.title,
            "description": self.description,
            "source_type": self.source_type,
            "video_url": self.video_url,
            "mime_type": self.mime_type,
            "duration": self.duration,
            "thumbnail_url": self.thumbnail_url,
            "tags": self.tags,
            "visibility": self.visibility,
            "is_active": self.is_active,
            "is_deleted": self.is_deleted,
            "created_by": self.created_by,
            "updated_by": self.updated_by,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

