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
![Homepage Mobile](screenshots/homepagemobile.png)  
Responsive version of the homepage, optimized for mobile users.

### 🔐 Login Page
![Login](screenshots/loginpage.png)  
Secure login form for returning users.

### 📝 Signup Page
![Signup](screenshots/signuppage.png)  
User registration form with validation and error handling.

### 🍳 Post a Recipe
![Post Recipe](screenshots/postrecipe.png)  
Form to add a new recipe with title, summary, ingredients, and method.

### 📖 Recipe Detail
![Recipe Detail](screenshots/recipedetail.png)  
Full view of a recipe including ingredients, method, and interaction buttons.

### 🧑‍💼 Edit Profile
![Edit Profile](screenshots/editprofile.png)  
Allows users to update their bio

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
Displays likes and comments for recipe interactions.

![Comment Responses](screenshots/commentpageresponse.png)  

![Like Responses](screenshots/likepageresponse.png)  
Alert to show succesfully submitted a comment and a like

---

## 👥 User Stories

- As a new user, I want to register so I can create and save recipes.
- As a returning user, I want to log in securely to access my content.
- As a user, I want to post recipes so I can share my dishes.
- As a user, I want to edit or delete my recipes so I can manage my collection.
- As a user, I want to browse and search recipes so I can discover new ideas.
- As a user, I want to like and comment on recipes so I can interact with others.
- As a user, I want to save recipes to my profile so I can revisit them later.
- As a user, I want the site to work on mobile so I can use it easily.

---
## 🗂️ Project Planning

This project was managed using a GitHub Project Board to organize tasks and track progress. Tasks were prioritized using the **MoSCoW method**, which helped guide development from MVP to feature-rich experience. Project Board Link - https://github.com/users/khizermalik1/projects/6/views/1

### MoSCoW Prioritization

**Must Have**
- User registration to create and save recipes  
- Secure login for returning users  
- Ability to post recipes with title, ingredients, and instructions  
- Edit and delete recipes to manage personal collection  

**Should Have**
- Browse and search recipes by keyword or category  
- Responsive design for mobile and tablet use  
- Save recipes to user profile for later access  

**Could Have**
- Like and comment on recipes to encourage interaction and feedback  

Each user story was mapped to specific tasks in the project board to ensure development stayed focused on user needs and goals.

## 🧪 Testing

- Manual testing across Chrome, Firefox, Safari, and mobile browsers (Can be seen VIA Screenshots above of web app)
- Form validation using Django’s built-in tools
- CSRF protection enabled on all forms
- CRUD operations tested for expected behavior (Can be seen VIA Screenshots above of web app)
- Authentication tested (register, login, logout)
- Responsive layout verified using browser dev tools
The Lighthouse audit shows a high-performing mobile experience  
![Lighthouse Mobile Audit](screenshots/lighthousemobile.png)

## 🪞 Reflection
This project was a deep dive into building a full-stack web application with performance, accessibility, and maintainability in mind. From setting up the backend with Django to deploying on Heroku, every step challenged me to think critically about structure, speed, and user experience. Going forward, I plan to replace inline styles with consistent, modular CSS to improve maintainability and scalability. Building this app helped me balance speed, structure, and usability.


## 📄 Credits

- Developed by Khizer Malik  
- Hosted on Heroku  
- Database powered by PostgreSQL

---

## 🤖 AI Assistance

This project was developed with support from Microsoft Copilot for setup, configuration, and documentation.
