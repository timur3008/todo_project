from rest_framework import serializers

from todo_app.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    is_completed = serializers.BooleanField(default=False)

    class Meta:
        model = Todo
        fields = ['id', 'text', 'is_completed']
        read_only_fields = ['author'] # говорит что это поле доступно только для чтения а изменять или удалять её нельзя