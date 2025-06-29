from rest_framework import serializers

from django.contrib.auth.models import User

from todo_app.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    is_completed = serializers.BooleanField(default=False)

    class Meta:
        model = Todo
        fields = ['id', 'text', 'is_completed']
        read_only_fields = ['author'] # говорит что это поле доступно только для чтения а изменять или удалять её нельзя


class UserRegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password1', 'password2']

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError('Пароли не совпадают')
        return data

    def create(self, validated_data):
        user = User.objects.create_user( # хеширует пароль
            first_name=validated_data['first_name'],
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password1']
        )
        return user
    

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']