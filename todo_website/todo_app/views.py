from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from django.views.generic import UpdateView

from .forms import TodoForm, AuthorizationForm, RegistrationForm
from . import models

def render_home_page(request):
    if not request.user.is_authenticated:
        return redirect('authorization')

    todos = models.Todo.objects.filter(author=request.user)

    if request.method == 'POST':
        form = TodoForm(data=request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.save()
            messages.success(request, 'Задача создана успешно!!!')
            return redirect('home')
    else:
        form = TodoForm()

    context = {
        'todos': todos,
        'form': form,
        'action': 'Создать'
    }

    return render(request, 'index.html', context)

def render_filter_page(request, status: str):
    todos = models.Todo.objects.filter(author=request.user)

    if request.method == 'POST':
        form = TodoForm(data=request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.save()
            messages.success(request, message='Задача создана успешно!!!')
            return redirect('home')
    else:
        form = TodoForm()

    if status == 'completed':
        todos = todos.filter(is_completed=True)
    else:
        todos = todos.filter(is_completed=False)

    context = {
        'todos': todos,
        'status': status,
        'form': form,
        'action': 'Создать'
    }

    return render(request, 'index.html', context)

def render_registration_form(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, message='Вы успешно зарегистрировались')
            return redirect('authorization')
    else:
        form = RegistrationForm()

    context = {
        'form': form,
        'action': 'Зарегистрироваться'
    }

    return render(request, 'registration.html', context)

def render_authorization_page(request):
    if request.method == 'POST':
        form = AuthorizationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user is not None:
                login(request, user)
                messages.success(request, message='Вы успешно авторизовались')
                return redirect('home')
            else:
                messages.error(request, message='Такого пользователя не существует')
        else:
            messages.error(request, message='Введены неправильные значения')
    else:
        form = AuthorizationForm()

    context = {
        'form': form,
        'action': 'Авторизоваться'
    }

    return render(request, 'authorization.html', context)

def render_logout_page(request):
    logout(request)
    return redirect('authorization')

def render_update_todo_page(request, todo_id: int, action: str):
    todo = models.Todo.objects.get(pk=todo_id)
    if action == 'CHANGE_STATUS':
        todo.is_completed = not todo.is_completed
        todo.save()
        messages.success(request, message=f'Статус задачи номер: {todo_id} - ОБНОВЛЕН!!!')
    elif action == 'DELETE':
        todo.delete()
        messages.success(request, message=f'Статус задачи номер: {todo_id} - УДАЛЁН!!!')
    
    return redirect('home')

def render_search_page(request):
    query_text = request.GET.get('query')
    todos = models.Todo.objects.filter(text__iregex=query_text)

    context = {
        'query_text': query_text,
        'todos': todos
    }

    return render(request, 'search.html', context)

class UpdateTodo(UpdateView):
    model = models.Todo
    template_name = 'update.html'
    form_class = TodoForm

def render_profile_page(request):
    todos = models.Todo.objects.filter(author=request.user)

    context = {
        'todos': todos,
        'total_todos': todos.count(),
        'total_completed': todos.filter(is_completed=True).count(),
        'total_pending': todos.filter(is_completed=False).count()
    }

    return render(request, 'profile.html', context)