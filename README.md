## Todo List Application - Backend

Description:
This repository contains the backend code for a Todo List Application built using Django and Django Rest Framework. The Todo List Application allows users to create, manage, and track their tasks through a user-friendly API. This backend project serves as the foundation for the Todo List Application and handles data storage, retrieval, and manipulation through API endpoints.
## Features

* Todo Items Management: 
Users can create, update, retrieve, and delete individual todo items. Each todo item has a title, description, due date, status, and tags associated with it. The status can be one of "Open," "Working," "Done," or "Overdue."

* Tags: 
Users can create tags and associate them with todo items. Tags help in categorizing and organizing todo items for better management.

* Progress Notes: 
Users can add progress notes to their todo items to keep track of updates and progress. Progress notes are associated with specific todo items.

* Authentication: 
The backend includes user authentication to secure API endpoints. Users need to authenticate themselves to access their todo items, tags and progress notes.

* Custom Permissions:

Custom permission classes are implemented to control access to API views based on user ownership and roles. Users can only view, update, or delete their own todo items and progress notes.

* Pagination:

Custom pagination classes are utilized to manage the number of items displayed per page in the API responses.

* Django Admin Interface:

The backend includes a Django admin interface that allows administrators to manage todo items and tags from a user-friendly web interface. The admin interface is configured to display important fields and allows filtering and searching of todo items and tags.
## Authentication Methods

SMTP Email Token Authentication:

Users can authenticate and access the application using token-based authentication through SMTP email.
An email with an authentication token will be sent to the user's registered email address for secure access.

REST Framework API Token Authentication:

Users can also authenticate using REST Framework API tokens for secure API access.

User Authentication and Account Management:

Users can register and create an account.
User accounts can be activated through an email link sent to the registered email address.
Users can log in and log out from their accounts.
In case of a forgotten password, users can request a reset email with a link to set a new password.
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





  ## Todo App Endpoints:

* Create Todo Item:

Endpoint: todo_app/api/todo_list/
Method: POST
Description: Used to create a new Todo item in the Todo list.

* Read Todo Item:

Endpoint: todo_app/api/todo_detail/22/
Method: GET
Description: Used to read the details of a specific Todo item identified by ID 22.

* Read All Todo Items:

Endpoint: todo_app/api/progress_note_list/51/
Method: GET
Description: Used to read all Todo items in the Todo list. The progress_note_list part in the URL might be a typo, or it's using a different name for the endpoint.

* Update Todo Item:

Endpoint: Not provided
Method: PUT or PATCH
Description: This endpoint is not explicitly mentioned in the list, but there should be an endpoint to update the details of a Todo item.

* Delete Todo Item:

Endpoint: Not provided
Method: DELETE
Description: This endpoint is not explicitly mentioned in the list, but there should be an endpoint to delete a Todo item.

* Progress Note Detail:

Endpoint: todo_app/api/progress_note_detail/49/2/
Method: GET
Description: This endpoint appears to be related to some progress notes. It reads the details of a specific progress note identified by ID 2, which is associated with Todo item 49.

* Tag List:

Endpoint: todo_app/api/tag_list/
Method: GET
Description: Used to retrieve a list of all tags available in the Todo app.

* Tag Detail:

Endpoint: todo_app/api/tag_detail/22/
Method: GET
Description: Used to read the details of a specific tag identified by ID 22.

Account Endpoints:

* Logout User:

Endpoint: account/api/logout_user/
Method: GET
Description: Used to log out the currently authenticated user from the account system.

* Register:

Endpoint: account/api/register/
Method: POST
Description: Used for user registration in the account system.

* Request Reset Email:

Endpoint: account/api/request_reset_email/
Method: GET
Description: Used to request a password reset email in case the user forgets their password.

* Set New Password:

Endpoint: /account/api/set_new_password/NTg/brpn6g-76a5341b21e6fb88d44486854cb8dc8b/
Method: GET
Description: Used to set a new password for the user identified by the token NTg and the token brpn6g-76a5341b21e6fb88d44486854cb8dc8b.

* Activate:

Endpoint: /account/api/activate/NTg/brpmxv-5165cfcf2fb23c3de5cf434712040158/
Method: GET
Description: Used to activate a user account identified by the token NTg and the token brpmxv-5165cfcf2fb23c3de5cf434712040158.

Please note that the methods (e.g., POST, GET, PUT, DELETE) for each endpoint are not explicitly provided in the list, so you may need to refer to the API documentation or code implementation to confirm the correct HTTP methods for each endpoint.

URL for published documentation https://documenter.getpostman.com/view/27765893/2s9Xy3sB74

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

3.Access the admin interface by visiting http://localhost:8000/admin in your web browser.

## License

[MIT](https://choosealicense.com/licenses/mit/)

