import os

os.environ['DATABASE_URL'] = 'postgres://postgres:23.Howard@localhost:5432/dish_diary'
os.environ['DEBUG'] = 'True'
os.environ['SECRET_KEY'] = 'django-insecure-4z@1!x7^g$8n#k3&b!9r2@+m%qv$1=5z@u3z@6z@v8z@3z@x9z'
os.environ['ALLOWED_HOSTS'] = 'localhost,127.0.0.1'
