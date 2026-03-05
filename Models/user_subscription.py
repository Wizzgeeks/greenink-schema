from mongoengine import Document,IntField,ReferenceField,DateTimeField,CASCADE, StringField,DictField
# from Models.coupon_model import Coupon
from Models.subscription import Subscription
from Models.user import Users
from datetime import datetime, timezone


# class User_subscription(Document):
#     user = ReferenceField(Users,reverse_delete_rule=CASCADE,required=True)
#     subscription = ReferenceField(Subscription,reverse_delete_rule=CASCADE,required=True)
#     # coupon = ReferenceField(Coupon,reverse_delete_rule=CASCADE)
#     coins_redeemed=IntField()
#     expiry = DateTimeField(required=True)
#     cashfree_subscription_id = StringField()
#     order_details = DictField()
#     status = StringField(default="INITIATED")
#     subscription_status=StringField(default="ACTIVE",choices=["ACTIVE","EXPIRED","CANCELLED","UPCOMING"])
#     start_date = DateTimeField()
#     next_charge_date = DateTimeField()
class UserSubscription(Document):
    user = ReferenceField(Users, reverse_delete_rule=CASCADE, required=True)
    subscription = ReferenceField(Subscription, reverse_delete_rule=CASCADE, required=True)

    start_date = DateTimeField()
    expiry = DateTimeField(required=True)
    subscription_status = StringField(
        default="ACTIVE",
        choices=["ACTIVE", "EXPIRED", "CANCELLED", "UPCOMING"]
    )
    next_charge_date = DateTimeField()
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    

    def to_json(self):
        return {
            "id": str(self.id),
            "user": str(self.user.id) if self.user else None,
            "subscription": self.subscription.to_json() if self.subscription else None,
            "start_date": self.start_date.isoformat() if self.start_date else None,
            "expiry": self.expiry.isoformat() if self.expiry else None,
            "subscription_status": self.subscription_status,
            "next_charge_date": self.next_charge_date.isoformat() if self.next_charge_date else None,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }