from mongoengine import Document,StringField,ReferenceField,BooleanField,DateTimeField,FloatField,IntField,ListField,EmbeddedDocument,EmbeddedDocumentField,CASCADE,DictField
from Models.course import Course
from datetime import datetime, timezone


class Permission(EmbeddedDocument):
    name = StringField(required=True)
    active = BooleanField(default=True)

    def to_json(self):
        return {
            "name": self.name,
            "active": self.active
        }


class Subscription(Document):
    course = ReferenceField(Course,reverse_delete_rule=CASCADE,required=True)
    
    package_name = StringField(required=True)
    plan_type = StringField(required=True, choices=("week", "month", "year"))
    subscription_tier=StringField(required=True)
    price = FloatField(required=True)
    plan_duration=IntField(required=True)
    activate = BooleanField(default=True)
    cashfree_subscription_id = StringField()
    premissions = ListField(DictField(), default=[])
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))

    def to_json(self):
        return {
            "id": str(self.id),
            "course":str(self.course.id) if self.course else None,
            "package_name":self.package_name,
            "plan_type":self.plan_type,
            "subscription_tier":self.subscription_tier,
            "price":self.price,
            "plan_duration":self.plan_duration,
            "activate":self.activate,
            "premissions":[p.to_json() for p in self.premissions] if self.premissions else []
        }
    
    def with_key(self):
        return {
            "id": str(self.id),
            "course":self.course.to_json() if self.course else None,
            "package_name":self.package_name,
            "plan_type":self.plan_type,
            "subscription_tier":self.subscription_tier,
            "price":self.price,
            "plan_duration":self.plan_duration,
            "activate":self.activate,
            "premissions":[p.to_json() for p in self.premissions] if self.premissions else []
        }
    def admin_json(self):
        return {
            "id": str(self.id),
            "course":self.course.to_json() if self.course else None,
            "package_name":self.package_name,
            "plan_type":self.plan_type,
            "subscription_tier":self.subscription_tier,
            "price":self.price,
            "plan_duration":self.plan_duration,
            "activate":self.activate,
            "premissions":[p.to_json() for p in self.premissions] if self.premissions else []
        }   
    
    
    
   