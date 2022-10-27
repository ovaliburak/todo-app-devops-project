# React-Node-Django DevOps Project

## General Info 
The application is a simple to-do application. This app is used for my Devops learning process.

React and Nginx are used on the frontend.

Django Rest Framework-Gunicorn and Node are used on the backend. Since I do not have much knowledge on the node side, I cannot give a detailed explanation.

Postgresql is preferred as database.

## Usage

I'm trying to combine what I've learned for the CI-CD process. I will advance this project using different devops tools. Minicube and docker-compose are used under this single repo. Its purpose is to run the project locally. Each service is kept under different repo for a complete CI-CD process. Links to other repos will be shared.

### Running application with docker-compose

Make sure these ports are empty as they are used on the Nginx and Postgresql default ports (80 and 5432).

```
git clone https://github.com/ovaliburak/todo-app-devops-project.git
cd todo-app-devops-project/
docker-compose up -d --build
```

We can now access the application from local. It is running on Node 5000 port, Django running on 8000 port. React is served by Nginx with port 80.