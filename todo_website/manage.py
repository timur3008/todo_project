#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo_website.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()


# TODO: работа с git
# .gitignore - файл в котором описывается то что мы не должны заливать на github

# инициализация git в проекте
# git init - инициализирует пустой git репозиторий в папке проекта
# git status - проверяет добавляемые папки/файлы в репозиторий
# git add <file_name> or . - добавляет все измененные или новые папки и файлы для просмотра
# git commit -m <comment>

# настройка профиля отправляющего изменения в репозиторий
# git config user.name '<account_username>' - указываем username аккаунта который отправляет данные
# git config user.email '<account_email>' - указываем email аккаунта который отправляет данные
# git branch -M main - создаёт главную ветку 
# git remote add origin <https://github.com/timur3008/django-ninja-blog.git>
# git push origin main - отправляем изменения на репозиторий впервые
# git push - отправляем изменения на репозиторий
# git clone <project_path> - скачивание проекта с github