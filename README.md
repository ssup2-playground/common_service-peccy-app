# eks-cicd-dr_peccy-app

Peccy service app server.

## CLI Commands

```
# Install packages
$ pip3 install -r requirements.txt

# Local run
$ python3 run.py

# Unit test
$ python3 -m unittest
```

## Main Packages

* API Framework : FastAPI
* Web Server : Uvicorn
* ORM : SQLAlchemy
* DB : MySQL
* Log :loguru

## Reference

* Class : https://stackoverflow.com/questions/63853813/how-to-create-routes-with-fastapi-within-a-class
* Send File : https://stackoverflow.com/questions/55873174/how-do-i-return-an-image-in-fastapi
* CORS : https://fastapi.tiangolo.com/tutorial/cors/
* Logging : https://pawamoy.github.io/posts/unify-logging-for-a-gunicorn-uvicorn-app/#uvicorn-only-version
* FastAPI : https://blog.neonkid.xyz/253