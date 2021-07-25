## Description

Here is my small ToDo app for organizing my work in progress.\
The idea behind is to learn how to improve prediction of my work in progress.\
Based on numbers tasks done and their difficulty the App will provide recommendation for future planning.\
For now it's just App where you can do it manually, **but** I'm on my way! 

## The current state

The App consists:
- backlog (list of all active tasks)
- dashboard (list of tasks list)
    - task_list (list of task for a day)
        - task (simple task)

* It automatically creates me list for each day.
* I can add, delete, choose from backlog or update a task in a list page 
* I can plan for some period (usually I prefer create plan for a week). I use backlog for it
* The app shows me task ordered by deadline, so I can concentrate on more (lets say) important tasks. 

I think for now that's all. Maybe I forgot to add something, but you always can check it by yourself ;)

## How to install and run it on your PC or server

I'll give you a setup flow for linux. If you use a Windows OS, I'm sorry. 
Maybe you need to try a Linux at least for coding ;). 
Anyway the flow should be similar to this one, I'm sure you will manage.

1. install the latest [python3](https://www.python.org/downloads/)    
   *if you already have python2 instead of python you should use python3*
2. install python virtual environment 
>$ pip install virtualenv
3. create your venv
>$ python -m venv <your-venv-name>
4. clone my repository to your venv
>$ cd <your-venv-name>
>$ git clone https://github.com/nikitazigman/ToDoPetProject.git
5. activate your venv
>$ source bin/activate
6. enter to my project and install all requirements 
>$ cd todo_list
>$ pip install -r requirements.txt
7. You are almost ready to run it!! Create db
>$ python manage.py makemigrations
>$ python manage.pt migrate
8. Add superuser to your project
>$ python manage.py createsuperuser
9. Yep you did it! run server
>$ python manage.py runserver
10. Enjoy it! 

If you don't like something or, you have some questions, text me what I can improve in my App.
You can find my contacts in github profile. 
