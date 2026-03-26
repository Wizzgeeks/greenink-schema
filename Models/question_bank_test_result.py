from mongoengine import (
    Document, StringField, IntField, ListField, ReferenceField,
    DateTimeField, BooleanField, CASCADE, DictField
)
from datetime import datetime, timezone
from Models.qb_folders import QuestionBankFolders
from Models.question_bank import QuestionBank
from Models.user import Users


class QuestionbankTestResult(Document):
    questionbank_folders = ReferenceField(
        QuestionBankFolders, required=True, reverse_delete_rule=CASCADE
    )
    question_bank = ReferenceField(
        QuestionBank, required=True, reverse_delete_rule=CASCADE
    )
    user = ReferenceField(
        Users, required=True, reverse_delete_rule=CASCADE
    )

    attempt_data = ListField(DictField(), default=[])
    completed = BooleanField(default=False)
    no_of_questions_attempted = IntField()
    no_of_question_correct = IntField()
    feedback = ListField(DictField(), default=[])
    total_questions = IntField()

    created_by = StringField()
    updated_by = StringField()
    created_at = DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_at = DateTimeField(default=lambda: datetime.now(timezone.utc))

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(timezone.utc)
        return super(QuestionbankTestResult, self).save(*args, **kwargs)

    def to_json(self):
        return {
            "id": str(self.id),
            "questionbank_folders": str(self.questionbank_folders.id) if self.questionbank_folders else None,
            "question_bank": str(self.question_bank.id) if self.question_bank else None,
            "user": str(self.user.id) if self.user else None,
            "attempt_data": self.attempt_data,
            "completed": self.completed,
            "no_of_questions_attempted": self.no_of_questions_attempted,
            "no_of_question_correct": self.no_of_question_correct,
            "total_questions": self.total_questions,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "feedback": self.feedback,
        }