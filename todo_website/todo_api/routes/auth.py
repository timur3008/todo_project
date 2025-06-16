from todo_api.schemas.auth import UserSchema, UserLoginSchema, UserRegistrationSchema

from django.http import HttpRequest
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from ninja import Router
from ninja.errors import ValidationError

router = Router(tags=['Users'])

@router.post('/user/login/', response=UserSchema)
def login_user(request: HttpRequest, login_data: UserLoginSchema):
    user = authenticate(request=request, username=login_data.username, password=login_data.password)
    if user is None:
        raise ValidationError('User not found')
    login(request, user=user)
    return user

@router.post('/user/register/', response=UserSchema)
def register_user(request: HttpRequest, register_data: UserRegistrationSchema):
    if User.objects.filter(username=register_data.username, email=register_data.email).exists():
        raise ValidationError(f'User with this username and email is already registered')
    
    if '@' not in register_data.email and '.' not in register_data.email:
        ValidationError('Email is incorrect')

    data = register_data.dict()
    password1 = data.pop('password1')
    password2 = data.pop('password2')

    if password1 != password2:
        ValidationError('Passwords are not similar')

    user = User.objects.create(**data)
    user.set_password(password1)
    user.save()
    return user

@router.post('/user/logout')
def logout_user(request: HttpRequest):
    logout(request)
    return {'is_authenticated': request.user.is_authenticated}