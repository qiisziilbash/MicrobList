# MicrobList
This is an open-source project in response to Microsoft taking over Wunderlist

## Description
- Sign up, Sign in, sign out, reset password, forgot password
- See list of 2-layered tasks in a tree style
    - Black (owner and not shared)
    - Blue (owner and shared)
        - Light: View
        - Dark: Edit
    - Green (Collaborator)
        - Light: View
        - Dark: Edit
- Create folders and tasks
- Share folders 
- See log of activities

## How to run
- ``` $ git clone https://github.com/qiisziilbash/MicrobList.git ``` 
- ``` $ virtualenv venv ```
- ``` $ source venv/bin/activate ```
- ``` $ pip install -r requirements.txt ```
- ``` $ python manage.py runserver ```