# To_Do_List_Application (Token And Email Authentication)

This is a Django-based Todo application that allows users to create, read, update, and delete todo items. The application provides a RESTful API for managing todo items and uses Django's built-in models, views, serializers, and the Django REST framework.

The app includes the following validations to ensure data integrity and enforce business logic:

* Timestamp: A timestamp is automatically set when creating a new todo item. It cannot be edited by the user.

* Title: The title of a todo item is limited to a maximum of 100 characters and is a mandatory field. It must be at least 2 characters long and must start with a capital letter.

* Description: The description of a todo item is limited to a maximum of 1000 characters and is a mandatory field. It must be at least 2  characters long.

* Due Date: The due date of a todo item is an optional field. If provided, it must be later than the timestamp created.

* Tag: Tags can be added to a todo item, allowing users to categorize their tasks. Multiple tags can be added to the same item, and  duplicate tags with the same value are saved only once.

* Status: The status of a task can be one of the following values: OPEN (default), WORKING, DONE, or OVERDUE. The status field is a  mandatory field and helps track the progress of a task.

The Django admin interface is enabled for easy management of todo items, providing appropriate validation checks for the fields mentioned above. The interface includes a changelist view with filters for efficient browsing and proper fieldsets for clear organization.

Token authentication is enabled for all the REST APIs, ensuring secure access to the application's functionalities.

In addition to the mentioned validations, the code includes a custom save method in the TodoItem model. This method checks if the due_date exists and if it has passed the current date. If the due_date is in the past, the status of the todo item is automatically updated to 'OVERDUE' before saving.

Overall, the To_Do_List_Application incorporates robust validations to maintain data consistency and enforce logical constraints, providing users with an efficient and reliable todo management system.

## Features

Todo :

* Create a new todo item with a title, description, due date, tags, and status
* Retrieve a specific todo item by its ID.
* Retrieve all todo items.
* Update an existing todo item.
* Delete a todo item. 

Tag:

* Retrieve a specific tag item by its ID.
* Retrieve all tag items.
* Update an existing tag item.
* Delete a tag item. 

Progress Note:

* Retrieve a specific Progress Note item by its ID.
* Retrieve all Progress Note items.
* Update an existing Progress Note.
* Delete a Progress Note item. 

Account:

* login 
* logout
* register
* request_reset_email
* set_new_password
* activate_account


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

URL for published documentation
https://documenter.getpostman.com/view/27765893/2s9XxsWH2x


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
