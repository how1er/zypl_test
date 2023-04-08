from tortoise import fields
from tortoise.models import Model
from passlib.hash import bcrypt


class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(50, unique=True)
    password_hash = fields.CharField(128)
    messages: fields.ReverseRelation["Message"]

    def verify_password(self, password):
        return bcrypt.verify(password, self.password_hash)


class Message(Model):
    id = fields.IntField(pk=True)
    text = fields.TextField()
    user = fields.ForeignKeyField("models.User", related_name="messages")
