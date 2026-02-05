from Models.user import Users
from mongoengine import CASCADE, Document, StringField, ReferenceField,DictField,ListField,DateTimeField
from datetime import datetime,timezone


class FlashCards(Document):
    user = ReferenceField(Users,reverse_delete_rule=CASCADE,required=True)
    cards_content=ListField(DictField())
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(FlashCards, self).save(*args, **kwargs)


