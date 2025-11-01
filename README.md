# Dish-Diary 🍽️

Dish-Diary is a full-stack Django web application that allows users to create, manage, and explore a personal collection of recipes. It supports secure user authentication, full CRUD functionality, and a responsive design optimized for both desktop and mobile devices. Users can interact with recipes by liking, commenting, and saving them to their profile.

---

## ✨ Features

- Register and log in securely
- Create, edit, and delete recipes
- Upload recipe images and ingredients
- Browse recipes by category or keyword
- Save recipes to your profile
- Like and comment on recipes
- Edit user profile details
- Responsive layout for mobile and desktop

---

## 🛠️ Technologies Used

- Django & Python
- PostgreSQL
- HTML5, CSS3, JavaScript
- Bootstrap 5
- Heroku (deployment)
- Gunicorn & WhiteNoise (production setup)

---

## 🚀 Deployment

Dish-Diary is deployed on Heroku using a PostgreSQL database.  
Sensitive configuration values such as `SECRET_KEY`, `DEBUG`, and `DATABASE_URL` are stored securely in Heroku Config Vars and excluded from version control.

---

## 📸 Screenshots & UI Walkthrough

Below are screenshots taken from the deployed Dish-Diary app, showing key features and user flows:

### 🏠 Homepage (Desktop)
![Homepage](screenshots/homepage.png)  
Displays featured recipes and navigation. Clean layout with category filters.

### 📱 Homepage (Mobile)
![Homepage Mobile](screenshots/homepage-mobile.png)  
Responsive version of the homepage, optimized for mobile users.

### 🔐 Login Page
![Login](screenshots/loginpage.png)  
Secure login form for returning users.

### 📝 Signup Page
![Signup](screenshots/signuppage.png)  
User registration form with validation and error handling.

### 🍳 Post a Recipe
![Post Recipe](screenshots/postrecipe.png)  
Form to add a new recipe with image upload, ingredients, and method.

### 📖 Recipe Detail
![Recipe Detail](screenshots/recipedetail.png)  
Full view of a recipe including image, ingredients, method, and interaction buttons.

### 🧑‍💼 Edit Profile
![Edit Profile](screenshots/editprofile.png)  
Allows users to update their personal details.

### 💾 Saved Recipes
![Saved Recipes](screenshots/savedrecipepage.png)  
Displays recipes saved by the user for future reference.

### 🔍 Search Results
![Search Results](screenshots/searchresults.png)  
Shows filtered recipes based on user search input.

### ❌ Delete Confirmation
![Delete Confirmation](screenshots/deleteconfirmation.png)  
Confirmation prompt before deleting a recipe.

### ❤️ Likes & Comments
![Comment Likes](screenshots/commentlikes.png)  
Displays likes on comments and recipe interactions.

![Comment Responses](screenshots/commentpageresponse.png)  
Threaded responses to recipe comments.

![Like Responses](screenshots/likepageresponse.png)  
Shows who liked a recipe and how users engage with content.

---

## 👥 User Stories

- As a new user, I want to register so I can create and save recipes.
- As a returning user, I want to log in securely to access my content.
- As a user, I want to post recipes with images so I can share my dishes.
- As a user, I want to edit or delete my recipes so I can manage my collection.
- As a user, I want to browse and search recipes so I can discover new ideas.
- As a user, I want to like and comment on recipes so I can interact with others.
- As a user, I want to save recipes to my profile so I can revisit them later.
- As a user, I want the site to work on mobile so I can use it while cooking.

---

## 🧪 Testing

- Manual testing across Chrome, Firefox, Safari, and mobile browsers
- Form validation using Django’s built-in tools
- CSRF protection enabled on all forms
- CRUD operations tested for expected behavior
- Authentication tested (register, login, logout)
- Responsive layout verified using browser dev tools

---

## 📄 Credits

- Developed by Khizer Malik  
- Hosted on Heroku  
- Database powered by PostgreSQL

---

## 🤖 AI Assistance

This project was developed with support from Microsoft Copilot for setup, configuration, and documentation.
