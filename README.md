# Book_Review_Platform
Welcome to the Book Review Platform, a web application that allows users to review and rate books. This platform provides a simple and intuitive interface for managing books, user accounts, and reviews.


## Features
User Authentication: Secure user authentication system to ensure privacy and access control.
Book Management: Add, update, and delete books with details such as title, author, genre, and publication year.
User Reviews: Users can rate and review books, contributing to a community-driven feedback system.
Role-Based Access Control: Admin users have additional privileges, ensuring proper control over platform features.
RESTful API: The platform exposes a RESTful API, allowing developers to integrate and extend its functionality.


Getting Started
Follow these steps to set up the Book Review Platform locally:

Clone this repository:
git clone https://github.com/your-username/Book_Review_Platform.git

Install dependencies:
pip install -r requirements.txt

Configure the environment:
  Set up your database configuration in config.py.
  Define your JWT secret key in the create_app function in __init__.py.
Run the application:
  flask run
  The application will be accessible at http://127.0.0.1:5000.

#### API Documentation

Explore the API endpoints using the provided Postman collection here .
Postman Collection: https://bit.ly/47cYD7y

# Database Schema

## User Table
| Field           | Type       |
| --------------- | ---------- |
| id (PK)         | int        |
| username        | str        |
| email           | str        |
| password_hash   | str        |
| role            | str        |

## Book Table
| Field           | Type       |
| --------------- | ---------- |
| id (PK)         | int        |
| title           | str        |
| author          | str        |
| genre           | str        |
| pub_year        | int        |

## Review Table
| Field           | Type       |
| --------------- | ---------- |
| id (PK)         | int        |
| rating          | int        |
| text            | str        |
| user_id (FK)    | int        |
| book_id (FK)    | int        |








