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
[[https://lunar-comet-587724.postman.co/workspace/New-Team-Workspace~c87efc13-c3a4-4743-92e4-e07aeeba18de/collection/17595448-e040c467-22a1-48b7-be52-afb0a46440d5?action=share&creator=17595448](https://lunar-comet-587724.postman.co/workspace/New-Team-Workspace~c87efc13-c3a4-4743-92e4-e07aeeba18de/collection/17595448-e040c467-22a1-48b7-be52-afb0a46440d5?action=share&creator=17595448)https://lunar-comet-587724.postman.co/workspace/New-Team-Workspace~c87efc13-c3a4-4743-92e4-e07aeeba18de/collection/17595448-e040c467-22a1-48b7-be52-afb0a46440d5?action=share&creator=17595448](https://lunar-comet-587724.postman.co/workspace/New-Team-Workspace~c87efc13-c3a4-4743-92e4-e07aeeba18de/collection/17595448-e040c467-22a1-48b7-be52-afb0a46440d5?action=share&creator=17595448)

# Database Schema

### User Table
+-----------------+ 
| id: int (PK)     | 
| username: str    | 
| email: str       | 
| password_hash:   | 
|    str           | 
| role: str        | 
+-----------------+

### Book Table
+---------------+       
| id: int (PK)  |       
| title: str    |       
| author: str   |       
| genre: str    |       
| pub_year: int |       
+---------------+

### Review Table
+------------------+       
| id: int (PK)     |       
| rating: int      |       
| text: str        |       
| user_id: int (FK)|       
| book_id: int (FK)|       
+------------------+







