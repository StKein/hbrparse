# Description:
Django REST application that parses daily top posts from Habr
# Installation:
0. Install python
1. Clone repository
2. Open terminal, cd into directory you cloned repository to
3. (preferably) Make virtual environment, activate it
4. Type following:
> pip install -r requirements.txt
# Running:
0. Open terminal in cloned repository directory
1. (if venv was added) Activate venv
2. Run server:
> python manage.py runserver
3. Now you can browse API via browser or requests (Postman, curl, ...)
# Parsing:
0. Open terminal in cloned repository directory, activate venv if it was added
1. Run app in shell:
> python manage.py shell
2. Run parser script:
> from prser.tasks import parseHabr
> parseHabr()
# API URLs:
- Posts list: /api/posts/
- Single post: /api/posts/<int>
  > /api/posts/13
  > /api/posts/6
Each post in posts list contains API link to it, no need to guess