# Run this project
Run this project by running the `requirements.txt` folder:
```python
pip install -r requirements.txt
```
Please make sure you have the proper environment variables in place, you will need a MongoDB connection string and a Voyage AI API Key. 

To run the Dublin City Center Pub Finder please make sure you're in the correct folder in your directory and run this command:
```python
python manage.py runserver
```



# Django MongoDB Backend - Project Template

This is a Django project starter template for the Django MongoDB Backend.
In order to use it with your version of Django: 

- Find your Django version. To do so from the command line, make sure you
  have Django installed and run:

```bash
django-admin --version
>> 5.0
```

## Create the Django project

From your shell, run the following command to create a new Django project
replacing the `{{ project_name }}` and `{{ version }}` sections. 

```bash
django-admin startproject {{ project_name }} --template https://github.com/mongodb-labs/django-mongodb-project/archive/refs/heads/{{ version }}.x.zip
```

For a project named `5_0_example` that runs on `django==5.0.*`
the command would look like this:

```bash
django-admin startproject 5_0_example --template https://github.com/mongodb-labs/django-mongodb-project/archive/refs/heads/5.0.x.zip
```
