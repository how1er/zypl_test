from fastapi import Depends, HTTPException, APIRouter
from fastapi.security import OAuth2PasswordBearer
from models import User, Message
from typing import List
from schemas import Message_Pydantic, MessageIn_Pydantic
from users_auth import get_current_user

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

router = APIRouter()


@router.post("/", response_model=Message_Pydantic)
async def create_message(message: MessageIn_Pydantic, current_user: User = Depends(get_current_user)):
    message_obj = Message(user_id=current_user.id, text=message.text)
    await message_obj.save()
    return await Message_Pydantic.from_tortoise_orm(message_obj)


@router.get("/", response_model=List[Message_Pydantic])
async def get_messages(current_user: User = Depends(get_current_user)):
    return await Message_Pydantic.from_queryset(Message.all())


@router.delete("/{message_id}")
async def delete_message(message_id: int,
                         current_user: User = Depends(get_current_user)):
    message_obj = await Message.get(id=message_id)
    if message_obj.user_id != current_user.id:
        raise HTTPException(status_code=403,
                            detail="You are not allowed to delete this message")

    await message_obj.delete()
    return "success"
