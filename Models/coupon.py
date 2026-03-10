from mongoengine import Document,StringField,ReferenceField,ValidationError,DateTimeField,IntField,CASCADE,BooleanField
from Models.course import Course
from datetime import datetime,timezone

class Coupon(Document):
    course = ReferenceField(Course,reverse_delete_rule=CASCADE,required=True)
    name = StringField(required=True)
    discount_in_percentage = StringField()
    discount_in_flat = IntField()
    max_discount_in_price = IntField(required=True)
    
    expires = DateTimeField(required=True)
    code = StringField(required=True,unique=True)
    max_usage=IntField(required=True)
    current_usage = IntField(default=0)
    activate = BooleanField(default=True)

    created_at = DateTimeField(default=datetime.now(timezone.utc))
    updated_at = DateTimeField(default=datetime.now(timezone.utc))
    created_by=StringField()
    updated_by=StringField()

    

    def clean(self):
        if not self.name.strip():
            raise ValidationError("Coupon name cannot be empty")
        if self.expires <= datetime.now(timezone.utc):
            raise ValidationError("Expiry must be future date")
        if self.max_usage <= self.current_usage:
            raise ValidationError("Max usage must be greater than current usage")
        

    def to_json(self):
        return {
            "id": str(self.id),
            "course":self.course.key if self.course else None,
            "name":self.name,
            "discount_in_percentage":self.discount_in_percentage,
            "discount_in_flat":self.discount_in_flat,
            "max_discount_in_price":self.max_discount_in_price,
            "expires":self.expires,
            "code":self.code,
            "max_usage":self.max_usage if self.max_usage else None,
            "current_usage":self.current_usage if self.current_usage else 0,
            "created_at": self.created_at if self.created_at else None,
            "updated_at": self.updated_at if self.updated_at else None,
            "activate": self.activate,
        }
    
    def with_key(self):
        return {
            "id": str(self.id),
            "course":self.course.to_json() if self.course else None,
            "name":self.name,
            "discount_in_percentage":self.discount_in_percentage,
            "discount_in_flat":self.discount_in_flat,
            "max_discount_in_price":self.max_discount_in_price,
            "expires":self.expires,
            "code":self.code,
            "max_usage":self.max_usage if self.max_usage else None,
            "current_usage":self.current_usage if self.current_usage else None,
            "created_at": self.created_at.strftime('%d/%m/%Y') if self.created_at else None,
            "updated_at": self.updated_at.strftime('%d/%m/%Y') if self.updated_at else None,
            "activate": self.activate,
        }
        
    def update(self, **kwargs):
        self.clean()
        return super().update(**kwargs)
    
    
   