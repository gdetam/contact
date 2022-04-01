# contact
***

### settings

#### Install dependencies from requirements.txt

```
pip install -r requirements.txt
```

#### Run migrations
```
python manage.py migrate
```

#### Run project
```
python manage.py runserver
```
***
## API

### Create user 
```
/api/clients/create/ 
```

### JWT Token Authorization
```
Authorization: Bearer <token>
```

### Users likes
```
api/clients/<int:id>/match
```
### Filters
```
clients/list

api/list/?first_name=[past here first_name]
api/list/?last_name=[past here last_name]
api/list/?sex=[past here sex]  -  (bool 0 or 1)
api/list/?distance=[past here distance(meters)]

```
***
### Deployed project

#### link

### Authors 👨‍💻

Contributors names and contact info

ex. gdetam  
ex. [@gdetam](https://t.me/onlygdetam)

### License

This project is licensed under the [MIT License](LICENSE.txt)


