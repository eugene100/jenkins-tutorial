# Jenkins Best Practices

ToDo:

- [x] Create sample application
- [ ] Develop script for creating repositories and push the sample code there
- [ ] Simple way to setup Jenkins as a container
- [ ] Apply organization plugin to GitHub. Test CI.
- [ ] Deployment with multienvironment ability. Based on environment repository.

## Need to be installed

- Python3
- AWS account. Free tier would be cool.
- Postman

## Sample application

Requirements:

- Simple resful
- Rest API
- One parameter on a build stage, second on runtime stage

Manual run:

```
$ virtualenv venv
$ source venv/bin/activate
$ pip install flask-restful
$ pip freeze > requirements.txt

$ pip install -r requirements.txt
```

`$ deactivate` for exit venv