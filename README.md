# **Documentation for URL Shortener Application**

## Introduction

The URL Shortener application is designed to shorten long URLs into shorter, more manageable links. This documentation provides an overview of the application structure and the functionality of each Python file.

The application consists of the following eight Python files:

- `__init__.py`: Initializes the Flask application and registers necessary extensions and routes.
- `auth.py`: Implements basic authentication functionality for protecting routes.
- `database_setup.py`: Sets up the database and creates the necessary tables.
- `extensions.py`: Defines the SQLAlchemy extension for database operations.
- `models.py`: Defines the Link model for storing original and shortened URLs.
- `routes.py`: Implements the application's routes and their associated functions.
- `settings.py`: Contains configuration settings for the application.
- `run.py`: Creates and runs the Flask application.

## File Descriptions

### `__init__.py`

This file initializes the Flask application, sets up the configuration using the provided `config_file`, initializes the database extension, and registers the `short` blueprint for URL shortening routes.

### `auth.py`

The `auth.py` file provides basic authentication functionality for protecting routes. It includes the following functions:

- `check_auth(username, password)`: Checks if the provided username and password combination is valid.
- `authenticate()`: Sends a 401 response with basic authentication information.
- `requires_auth(f)`: Decorator function that wraps routes and requires authentication.

### `database_setup.py`

This script sets up the database and creates the necessary tables. It imports the `create_app` function from the `scissors` module and initializes the database instance. It also imports the `db` instance and creates the tables using the `db.create_all()` method.

### `extensions.py`

The `extensions.py` file defines the SQLAlchemy extension and creates an instance of the `SQLAlchemy` class. This instance, `db`, is used for database operations throughout the application.

### `models.py`

The `models.py` file defines the `Link` model, which represents a shortened URL entry in the database. It includes the following attributes:

- `id`: The primary key of the link.
- `original_url`: The original URL provided by the user.
- `short_url`: The generated short URL.
- `visits`: The number of visits to the short URL.
- `date_created`: The date and time when the link was created.

The `Link` model also includes a constructor that generates a unique short URL using a combination of digits and letters. It ensures that the generated short URL does not already exist in the database.

### `routes.py`

The `routes.py` file contains the route handlers and associated functions for the URL shortener application. It includes the following routes:

- `/short_url`: Redirects to the original URL associated with the given short URL.
- `/`: Renders the index page for adding and managing links.
- `/add_link`: Handles the submission of a new URL for shortening and adds it to the database.
- `/stats`: Displays statistics about the stored links.
- Error handler for 404 pages.

### `settings.py`

The `settings.py` file contains configuration settings for the application. It includes the following settings:

- `SQLALCHEMY_DATABASE_URI`: The URI for the database connection.
- `SQLALCHEMY_TRACK_MODIFICATIONS`: Whether to track modifications to objects.
- `ADMIN_USERNAME`: The administrator's username (set to "admin").
- `ADMIN_PASSWORD`: The administrator's password (set to "password").

### `run.py`

The `run.py` file creates and runs the Flask application. It imports the `create_app` function from the `scissors` module and creates the application instance. Finally, it starts the application by calling `app.run()`.

## Deployment

The URL Shortener application is deployed on Render and can be accessed at the following website: [https://scissors-zrg3.onrender.com](https://scissors-zrg3.onrender.com).

To access the application, use the following credentials:

- Username: admin
- Password: password

These credentials will allow you to authenticate and access the protected routes of the application.

## Conclusion

This documentation has provided an overview of the URL Shortener application and the functionality of each Python file. By following the instructions and understanding the purpose of each file, you can utilize the URL Shortener application for shortening and managing long URLs effectively.# scissorsss
