from todo_app.models import Todo

from todo_api.schemas.todos import TodoSchema, TodoCreateSchema, TodoUpdateSchema, TodoDeleteSchema

from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from ninja import Router, Form
from ninja.errors import ValidationError


router = Router(tags=['Todos'])

@router.get('/todos/', response=list[TodoSchema])
def get_todos(request: HttpRequest):
    if request.user.is_authenticated:
        todos = Todo.objects.filter(author=request.user)
        return todos
    else:
        raise ValidationError('User is not authenticated or registeres')

@router.post('/todos/', response=TodoSchema)
def post_todo(request: HttpRequest, todo_data: Form[TodoCreateSchema]):
    if request.user.is_authenticated:
        todo_text = todo_data.dict().get('text')
        todo = Todo.objects.create(text=todo_text, author=request.user)
        return todo
    else:
        raise ValidationError('User is not authenticated or registeres')

@router.patch('/todos/update/{todo_id}/', response=TodoSchema)
def update_todo(request: HttpRequest, todo_id: int, todo_data: TodoUpdateSchema):
    todo = get_object_or_404(Todo, pk=todo_id)

    for key, value in todo_data.dict().items():
        if value is None:
            current_value = getattr(todo, key)
            print(current_value)
            setattr(todo, key, current_value)
        else:
            setattr(todo, key, value)
    todo.save()
    return todo

@router.delete('/todos/delete/{todo_id}/', response=TodoDeleteSchema)
def delete_todo(request: HttpRequest, todo_id: int):
    todo = get_object_or_404(Todo, pk=todo_id)
    todo.delete()
    return {'is_deleted': True}