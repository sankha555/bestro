# Bestro
Recruitment task for SSMS Tech Team

This repository contains the source code for "Bestro", and online restaurant which specializes in door-to-door deliveries. The website is made using Django, HTML, CSS and JS. 

A few salient features of the website:
1. Google sign-in for customers (bye bye "Forgot Your Password")
2. Updation of stocks after each order is placed
3. Option for customer feedback and live updation of item ratings based on this feedback
4. Asychrounous item filters
5. Expected Delivery time calculated and shown on the basis of number of active orders, so it's authentic and different for each new order 
6. Email Notifications about new offers
7. Option for staff to view daily sales in the form of downloadable spreadsheets
8. And many more... read below to discover them all!

## Running the Website:
There are two methods to run and test the website:

1. Using the live website on http://bestro.pythonanywhere.com  - click on the link to head over to the webite and start using it
2. Running it on localhost by cloning the repo to your local machine :

   i) Fork the repo
   
   ii) ``git clone https://github.com/{your_username}/bestro.git``
   
   iii) Create a new virtual environment on your local machine by running ``virtualenv myenv --python=python3.6``
   
   iv) Activate the environment by running ``source myenv/bin/activate``
   
   v) ``cd`` into the project folder "bestro"
   
   vi) Run ``pip install -r requirements.txt`` to install all project dependencies
   
   vii) Run ``python manage.py makemigrations`` then ``python manage.py migrate`` to update the database.
   
   viii) Run ``python manage.py runserver`` to launch the server.
   
   ix) Open up ```http://127.0.0.1:8000``` on your browser to open the website.
            
           

## How to use the website?

Please follow the below steps to explore and use the website.

### 1. User registration and login:
  To create an account, click on Sign Up on the navbar. This opens the customer registration page. You can then opt to sign in by providing the necessary details in the form or by using an Google account to sign in. 
  
  After creating an account, you are required to complete your profile. If it's already done - great, let's head to the delicious parts of the website.
  
### 2. View the Menu:

  Click on Menu in the navbar to view the food menu. All items are categorised into 6 categories and displayed under each. You can see the ratings, name, picture, description and price of each item under its category. If an item is purely vegan, it has the green symbol beside its name. You can also filter items on the basis of their category using the checkboxes given on the top of the menu. Mouth-watering? Let's place and order!
  
### 3. Place an Order:

  You can create and order and add food items to it. Click on Place Order in the navbar. A new order is automatically created for you and you will be redirected to the menu.
  
  From the pallette offered on the menu, you can choose any item that you want. Select the quantity of each item from the field under it. After you have selected the quantity of each item, click on Add Items in the side navigation. The selected items will be added to your order and are now visible under the order ID in the side nav. You can then again select more items as per your liking to the order. Once you have selected all items, click on Finalize to confirm your order. 
  
  You'll be taken to the order summary page, showing the items ordered, the grand total and expected delivery time of the order. 
  
  To cancel an order, simply click on Cancel Order while selecting items.
  
### 4. Delivery of order:

  When your order is delivered to your address, click on Order Recieved on the order summary page for the order. 
  
### 5. Feedback:

  After recieving your order, you can give feedback for the items that you ordered. You'll be redirected to the feedback page for the order. 
  For each ordered item, give your rating out of 5 under each item. After clicking submit, your feedback will be processed and you'll be redirected to the home page. 
  
### 6. Viewing Past Order:

  You can see your past orders under the Past Orders option in the nav bar. You'll be shown a list of all your past orders and clicking on each of them takes you to the order summary page of the order.
  
  

## Administrator (Staff) Controls :

The owners of the restaurant have a separate staff account to run the website. The primary staff account has the following credentials: 

      Username : sd
      Pwd : admin
      
A new staff account can only be created by an existing staff user. The steps to do the same are :

  1. Select Register New Employee in the navbar.
  2. Fill out the form for registering the new employee by making credentials like email, password and other personal details.
  3. By submitting, a new employee account is created which can be logged into through the login page.
  
Other Admin Controls:

### 1. Creating and updating items for the menu:

  Head to the menu by clicking the Menu option in the navbar. You will be able to see the option of creating a new Item on the top of the menu. Click on it and fill out the form giving required details to create the new item. To update and item, click on the Update Item button under each item in the menu.
  
### 2. Viewing Sales:
 
 To see category wise page items for each day, head to the Staff Dashboard (Click on your Name in the navbar and click on Update profile in the Profile page to go to the staff dashboard). Click on View Sales button.
 
 A spreadsheet file containing the day's sales will be downloaded to your local machine. 
 
### 3. Publishing New Offers:

  The restaurant can create new offers and notify the customers about the same through email. To create a new offer, click on New Offer in the nav bar. Write about the offer in the form presented and click on Publish. The news about the offer will be mailed to all customers via email. 
  

  
 The backend of the website has been created entirely by me. I have taken templates for the frontend views from "templatemo". Necessary changes have been made by me  to these templates at appropriate places. 
  
Suggestions and feedback about my work is welcome and I would love to hear about it for future improvements! 

---- Sankha Das
  
