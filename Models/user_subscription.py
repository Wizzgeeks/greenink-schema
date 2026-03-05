from mongoengine import Document,IntField,ReferenceField,DateTimeField,CASCADE, StringField
# from Models.coupon_model import Coupon
from Models.subscription import Subscription
from Models.user import Users
from datetime import datetime, timezone


class User_subscription(Document):
    user = ReferenceField(Users,reverse_delete_rule=CASCADE,required=True)
    subscription = ReferenceField(Subscription,reverse_delete_rule=CASCADE,required=True)
    # coupon = ReferenceField(Coupon,reverse_delete_rule=CASCADE)
    coins_redeemed=IntField()
    expiry = DateTimeField(required=True)
    cashfree_subscription_id = StringField()
    status = StringField(default="INITIATED")
    start_date = DateTimeField()
    next_charge_date = DateTimeField()

    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    

    def to_json(self):
        return {
            "id":str(self.id),
            "user":str(self.user.id) if self.user else None,
            "subscription":self.subscription.to_json() if self.subscription else None,
            "coupon":str(self.coupon.id) if self.coupon else None,
            "coins_redeemed":self.coins_redeemed if self.coins_redeemed else None,
            "expiry":self.expiry,
            "created_at":self.created_at,
            "updated_at":self.updated_at
        }
    
    # def with_key(self):
    #     return {
    #         "id":str(self.id),
    #         "user":self.user.to_json() if self.user else None,
    #         "subscription":self.subscription.to_json() if self.subscription else None,
    #         "coupon":self.coupon.to_json() if self.coupon else None,
    #         "coins_redeemed":self.coins_redeemed if self.coins_redeemed else None,
    #         "expiry":self.expiry.strftime('%d/%m/%Y')
    #     }