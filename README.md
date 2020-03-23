# receipt_sharing

## Setup environment
### 1. Create MySQL container
```
docker pull mysql:5.7
docker run -d -it --name mysql --env="MYSQL_ROOT_PASSWORD=xxxx" -p 3306:33060 mysql:5.7
```
check port mapping status:
```
$ docker port mysql
3306/tcp -> 0.0.0.0:33060
```
check MySQL container IP:
```
$ docker inspect mysql | grep IPAddress                        
    "SecondaryIPAddresses": null,
    "IPAddress": "172.17.0.2",
            "IPAddress": "172.17.0.2",
```
Create MySQL db user and password
```
mysql> GRANT ALL ON *.* to whole_recipes@'%' IDENTIFIED BY 'XXX';
```

### 2. Create app environment (ubuntu container)
```
$ docker pull ubuntu:18.04
$ pwd
/home/mguo/repos/recipes_sharing
$ docker run -d -it --name myapp -p 8000:80 -v <your-local-code-folder>:/opt/recipes_sharing ubuntu:18.04
```
#### 2.1 Install python3.7 in container
refer: http://ubuntuhandbook.org/index.php/2019/02/install-python-3-7-ubuntu-18-04/
```
$ apt update
$ apt install software-properties-common -y
$ add-apt-repository ppa:deadsnakes/ppa
$ apt install python3.7 -y
$ rm /usr/bin/python3
$ ln -s python3.6 /usr/bin/python3
$ update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 1
$ update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.7 2
$ update-alternatives --config python3
$ apt install python3-pip -y
```
#### 2.2 Install Django in container
```
$ pip3 install Django
```
#### 2.3 Build our own base docker image (contains Python-3.7 and Django-3.0.4)
```
$ docker commit myapp recipes_sharing:latest
```
---
## Create project
Go into `myapp` container, go to directory `/opt/recipes_sharing`, execute following command:
```
django-admin startproject whole_recipes
```
At this time, we can see a new folder has been created at current directory. Code structure of our project was initialized by `startproject` command, the starting project structure will be like this:
```
root@e8892c405253:/opt/recipes_sharing# tree whole_recipes/
whole_recipes/
|-- manage.py
`-- whole_recipes
    |-- __init__.py
    |-- asgi.py
    |-- settings.py
    |-- urls.py
    `-- wsgi.py

1 directory, 6 files
```




