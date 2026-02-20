from mongoengine import Document,StringField,ReferenceField,BooleanField,ListField,FloatField,DictField,CASCADE
from Models.course import Course

class Subscription(Document):
    course = ReferenceField(Course,reverse_delete_rule=CASCADE,required=True)
    term_in_months = StringField(required=True)
    price = FloatField(required=True)
    package_name = StringField(required=True)
    plan_active = BooleanField(default=True)

    def to_json(self):
        return {
            "id": str(self.id),
            "course":str(self.course.id) if self.course else None,
            "term_in_months":self.term_in_months,
            "price":self.price,
            "package_name":self.package_name
        }
    
    def with_key(self):
        return {
            "id": str(self.id),
            "course":self.course.to_json() if self.course else None,
            "term_in_months":self.term_in_months,
            "price":self.price,
            "package_name":self.package_name,
            "plan_active":self.plan_active

                }
    def admin_json(self):
        return {
            "id": str(self.id),
            "course":self.course.to_json() if self.course else None,
            "term_in_months":self.term_in_months,
            "price":self.price,
            "package_name":self.package_name,
            "plan_active":self.plan_active
        }   
    
    
    
   