When building django application it is a best practice to run it on **virtual environment** so that there are no conflicts between code sharing between projects

Python already has a built in **venv** virtual environment module that can be used .

### Django  Project Creation
1. Create a django specific directory
2. termianl onto the above directory andrun this command `python -m venv <env_name>`
3. New folder under the name <env_name> will be created and then you need to activate it.
    Run this command `source <env_name>/Scripts/activate`
4. After running this command a (<venv_name>) will appear next to terminal title which means our enivormant activation is succesful.
5. Install django on the same directory by performing  `pip install django`
6. Optionally you may check your django version by `python3 -m django version`
7. Create a new project by using the  `django-admin startproject <project_name>`
8. If we open our newly created project directory you see a manage.py file which is equivalent to django-admin