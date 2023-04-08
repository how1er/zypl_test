from tortoise.contrib.pydantic import pydantic_model_creator
from models import User, Message

User_Pydantic = pydantic_model_creator(User, name='User')
UserIn_Pydantic = pydantic_model_creator(User, name='UserIn', exclude_readonly=True)

Message_Pydantic = pydantic_model_creator(Message, name='Message')
MessageIn_Pydantic = pydantic_model_creator(Message, name='MessageIn', exclude_readonly=True)