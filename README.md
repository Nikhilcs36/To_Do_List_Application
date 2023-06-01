# To_Do_List_Application

This is a Django-based Todo application that allows users to create, read, update, and delete todo items. The application provides a RESTful API for managing todo items and uses Django's built-in models, views, serializers, and the Django REST framework.

## Features

* Create a new todo item with a title, description, due date, tags, and status
* Retrieve a specific todo item by its ID.
* Retrieve all todo items.
* Update an existing todo item.
* Delete a todo item. 

## Installation

1. Clone the repository:
  git clone https://github.com/Nikhilcs36/To_Do_List_Application.git

  cd To_Do_List_Application

2. Install the required dependencies:
  pip install -r requirements.txt

3. Run database migrations:
  python manage.py migrate

4. Start the development server:
  python manage.py runserver

## API Endpoints

The following API endpoints are available:

* Create Todo Item: POST /api/create/
Create a new todo item by providing the necessary data in the request body.

* Read Todo Item: GET /api/read/<int:pk>/
Retrieve a specific todo item by its ID. Replace <int:pk> with the actual ID of the todo item.

* Read All Todo Items: GET /api/read_all/
Retrieve all todo items.

* Update Todo Item: PUT /api/update/<int:pk>/
Update an existing todo item by providing the updated data in the request body. Replace <int:pk> with the actual ID of the todo item.

* Delete Todo Item: DELETE /api/delete/<int:pk>/
Delete a todo item by its ID. Replace <int:pk> with the actual ID of the todo item.

## Usage

1. Access the application by visiting http://localhost:8000 in your web browser.

2. Use the provided API endpoints to interact with the todo items programmatically.

## Customization

You can customize the application by modifying the following files:

* models.py: Contains the database models for the TodoItem and Tag entities.
* views.py: Defines the views for creating, reading, updating, and deleting todo items.
* serializer.py: Handles the serialization and deserialization of todo item and tag data.
* urls.py: Contains the URL patterns for the API endpoints.
* admin.py: Configures the admin interface for managing TodoItem and Tag entities.

Feel free to explore and extend the functionality according to your project requirements.

## Admin Interface

The application provides an admin interface for managing todo items and tags. To access the admin interface, follow these steps:

1. Create a superuser account:
python manage.py createsuperuser

2. Start the development server:
python manage.py runserver

3. Access the admin interface by visiting http://localhost:8000/admin in your web browser.

## License

[MIT](https://choosealicense.com/licenses/mit/)



