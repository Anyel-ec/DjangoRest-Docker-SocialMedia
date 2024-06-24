# **Select Language:** 🌍
- [Español (Spanish)](README-es.md)
- [English](README.md)

# User, Post, and Category Management Project in Django

This Django project is an application for managing users, posts, and categories, utilizing Django's own ORM and a layered architecture.

## RESULTS
## REST CONSUMER
### Core Documentation
![Alt text](api_doc/doc.png)
### Test in Insomio (or Postman)
![Alt text](api_doc/insomia.png)


## Features

- **Users**: Registration, update, deletion, and verification of users.
- **Posts**: Creation, update, deletion, and retrieval of posts.
- **Categories**: Creation, update, deletion, and retrieval of categories.

## Requirements

- Python 3.8+
- Django 3.2+
- Django REST Framework

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Anyel-ec/Django-REST-Py-SocialMedia-ORM
    cd Django-REST-Py-SocialMedia-ORM
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Apply the database migrations:
    ```sh
    python manage.py migrate
    ```

5. Run the development server:
    ```sh
    python manage.py runserver
    ```

## Architecture

The project follows a layered architecture:

1. **Models**: Represent domain entities such as `User`, `Post`, and `Category`.
2. **Repositories**: Manage communication with the database.
3. **Services**: Contain business logic and application rules.
4. **Views**: Handle HTTP requests and return appropriate responses.

## Main Endpoints

### Users

- `POST /users/`: Create a new user.
- `GET /users/`: Retrieve the list of all users.
- `GET /users/{id}/`: Retrieve the details of a specific user.
- `PUT /users/{id}/`: Update a specific user.
- `DELETE /users/{id}/`: Delete a specific user.
- `POST /users/{id}/verify/`: Verify a user's password.
- `POST /users/verify_login/`: Verify login credentials.

### Posts

- `POST /posts/`: Create a new post.
- `GET /posts/`: Retrieve the list of all posts.
- `GET /posts/{id}/`: Retrieve the details of a specific post.
- `PUT /posts/{id}/`: Update a specific post.
- `DELETE /posts/{id}/`: Delete a specific post.
- `GET /posts/by_user/`: Retrieve posts of a specific user.
- `GET /posts/by_email/`: Retrieve posts of a specific user by email.

### Categories

- `POST /categories/`: Create a new category.
- `GET /categories/`: Retrieve the list of all categories.
- `GET /categories/{id}/`: Retrieve the details of a specific category.
- `PUT /categories/{id}/`: Update a specific category.
- `DELETE /categories/{id}/`: Delete a specific category.

## Usage

To test the API, it is recommended to use tools like `Postman` or `curl` to make HTTP requests to the endpoints mentioned above.

## Contributions

Contributions are welcome. Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
