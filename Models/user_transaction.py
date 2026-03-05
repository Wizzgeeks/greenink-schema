from mongoengine import Document, FloatField,IntField,ReferenceField,DateTimeField,CASCADE, StringField,DictField
from Models.coupon import Coupon
from Models.subscription import Subscription
from Models.user import Users
from datetime import datetime, timezone

from Models.user_subscription import UserSubscription

class Transaction(Document):
    user = ReferenceField(Users, required=True)
    subscription = ReferenceField(Subscription)
    user_subscription = ReferenceField(UserSubscription)
    coupon = ReferenceField(Coupon)
    net_amount = FloatField()

    coupon_discount_percentage = FloatField()
    coupon_discount_amount = FloatField()

    coins_redeemed = IntField()
    coins_discount_amount = FloatField()

    amount_paid = FloatField()
    currency = StringField(default="INR")

    order_id = StringField()
    cf_order_id = StringField()
    payment_session_id = StringField()
    order_details = DictField()


    

    payment_status = StringField(
        choices=["INITIATED", "SUCCESS", "FAILED", "PENDING"],
        default="INITIATED"
    )

    payment_method = StringField()
    payment_time = DateTimeField()

    gateway_response = DictField()

    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))


    def to_json(self):
        def _ref_json(doc):
            if not doc:
                return None
            to_json = getattr(doc, "to_json", None)
            if callable(to_json):
                return to_json()
            return str(doc.id) if getattr(doc, "id", None) else None

        return {
            "id": str(self.id),
            "user": _ref_json(self.user),
            "subscription": _ref_json(self.subscription),
            "user_subscription": _ref_json(self.user_subscription),
            "coupon": _ref_json(self.coupon),
            "net_amount": self.net_amount,
            "coupon_discount_percentage": self.coupon_discount_percentage,
            "coupon_discount_amount": self.coupon_discount_amount,
            "coins_redeemed": self.coins_redeemed,
            "coins_discount_amount": self.coins_discount_amount,
            "amount_paid": self.amount_paid,
            "currency": self.currency,
            "order_id": self.order_id,
            "cf_order_id": self.cf_order_id,
            "payment_session_id": self.payment_session_id,
            "order_details": self.order_details,
            "payment_status": self.payment_status,
            "payment_method": self.payment_method,
            "payment_time": self.payment_time.isoformat() if self.payment_time else None,
            "gateway_response": self.gateway_response,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }