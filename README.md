# MOVIE CRUD API USING DJANGO REST FRAMEWORK

## Requirements
- Python 3.12
- Django 5.2
- Djangorestframework 3.16

## Installation
Clone this repository using git and cd into the "movies-crud-api-drf" dir by running these commands in the command line terminal
```
git clone https://github.com/Atharva-Bhosale238/movies-crud-api-drf.git
cd movies-crud-api-drf
```
Install virtualenv module if not installed
```
pip install virtualenv
```

Create a virtual env using pip
```
python -m venv env
```
Activate the virtual env

For windows:
```
env\Scripts\activate
```
For Linux
```
source env/bin/activate
```
Install the required dependencies
```
pip install -r requirements.txt
```



## Structure
In a RESTful API, endpoints (URLs) define the structure of the API and how end users access data from our application using the HTTP methods - GET, POST, PUT, DELETE etc. 

In our case, we have one single resource, `movies`, so we will use the following URLS - `/movies/` and `/movies/<id>` for collections and elements, respectively:

Endpoint |HTTP Method | CRUD Method | Result
-- | -- |-- |--
`/movies` | GET | READ | Get all movies
`/movies/{id}/` | GET | READ | Get a single movie 
`/movies`| POST | CREATE | Create a new movie
`/movies/{id}/` | PUT | UPDATE | Update a movie
`/movies/{id}/` | DELETE | DELETE | Delete a movie

## Use
We can test the API using [Postman](https://www.postman.com/) or inbuilt testcases for unit testing

First, we have to start up Django's development server.
```
cd movie_api
python manage.py runserver
```

### Testing the API with Postman

The Base url is 
```
http://127.0.0.1:8000/api/
```
Below are some examples, replace `<id>` with the movie id you want to update/delete/retreive

| Method | URL             | Description                                    | Body (JSON)                                                                                                                |
| ------ | --------------- | ---------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| GET    | `/movies/`      | List all movies                                | N/A                                                                                                                        |
| GET    | `/movies/<id>/` | Retrieve a single movie by ID                  |         N/A                                                                                                            | 
| POST   | `/movies/`      | Create a new movie                             | `{ "title": "Interstellar", "director": "Christopher Nolan", "releaseYear": 2014, "genre": "Sci-Fi", "rating": 10 } ` |
| PUT    | `/movies/<id>/` | Update an existing movie (all fields required) | `{   "title": "Inception Updated","director": "Christopher Nolan","releaseYear": 2010, "genre": "Sci-Fi","rating": 10}`     |
| DELETE | `/movies/<id>/` | Delete a movie                                 | N/A                                                                                                                        |


