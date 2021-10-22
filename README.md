<div align="center">

# **FIT BEAST - Milestone Project 04**

<img src="https://i.ibb.co/YkKYXjD/mp4.png">

An e commerce site for Health product and Gym instruments.

Visit [FIT BEAST](https://milestone-project-04.herokuapp.com/)
</div>

## **Table of Contents:**

- [Site Owner Goals](#site-owner-goals)
- [User Experience (UX)](#user-experience-ux)
  - [User Stories](#user-stories)
  - [Design](#Design)
    - [Imagery](#imagery)
    - [Colours Used](#colours-used)
    - [Typography](#typography) 
    - [Layout](#layout)
        - [Accessible to all users via the navbar](#Accessible-to-all-users-via-the-navbar)
        - [Accessible to logged in regisered users via the Navbar](#Accessible-to-logged-in-regisered-users-via-the-Navbar)
        - [Accessible only to Superusers(Admin) via the navbar](#Accessible-only-to-Superusers(Admin)-via-the-navbar)
        - [Accessible to all users via the Footer](#Accessible-to-all-users-via-the-Footer)
        - [Accessible to all users on the Products page](#Accessible-to-all-users-on-the-Products-page)
        - [Accessible to Superusers(Admin) on the Products page](#Accessible-to-Superusers(Admin)-on-the-Products-page)
        - [Accessible to Superusers(Admin) on the Product Detail page](#Accessible-to-Superusers(Admin)-on-the-Product-Detail-page)
        - [Accessible to Superusers(Admin) on the reviews page](#Accessible-to-Superusers(Admin)-on-the-reviews-page)
        - [Error Pages](#Error-Pages)
    - [Wireframes](#wireframes)
  - [Features](#features)
    - [Interactive Features](#Interactive-Features)
    - [Future Features](#future-features)
- [Technologies Used](#technologies-used)
  - [Languages Used](#languages-used)
  - [Frameworks, Libraries and Other Sources Used](#frameworks,-libraries-and-other-sources-used)
- [Information Architecture](#information-architecture)
    - [Database Choice](#database-choice)
    - [Data Modeling](#Data-Modeling)
- [Testing](#testing)
- [Deployment](#deployment)
  - [Heroku Deployment with AWS](#github-pages)
  - [Amazon Web Services](#forking-the-repository)
  - [Making A Local Clone](#making-a-local-clone)
- [Credits](#credits)

# UX:

## Site Owner Goals:

The Fit4Life website is a real world application, designed for the selling of fitness clothing and equipment.

1. The site owner's primary goal is to sell their products to new and returning customers.
2. The secondary goal is to showcase new products that are available to new and returning customers. 

## User Stories:

<img src="https://i.ibb.co/YWj1v1B/us1.png">
<img src="https://i.ibb.co/ZSWZ9cH/us2.png">
<img src="https://i.ibb.co/LhFfygM/us3.png">
<img src="https://i.ibb.co/8shLGjx/us4.png">
<img src="https://i.ibb.co/9VSPbD6/us5.png">

## Design:

### Imagery:

- On the landing page, the Hero image represents 'FIT BEAST' in the name of the company. As image is about fitness and toughness which represents Beast in fitness world. It was downloaded from [pixabay](https://pixabay.com/)

![FIT BEAST Hero Image](media/homepage_background.jpg)

- The origin of all other images is detailed in the [Credits](#Credits) section,

### Colours Used:

- Black (#000) was chosen as the background colour for the navbar and footer.

- Sky Blue (#87ceeb) was used for all buttons, discount banner and footer social media logos that are on the black background as it goes well with the hero image, as well as making a good contrast 
with the black background.

- White (#fff) was used as the backgorund, and black (#000) was used for the text on all pages other than the landing page so that the background and text do not detract from the products displayed.

- Balloon Blue (#2B60DE) was used for Logo of the website/company.


### Typography:

- 'Chakra Petch' was chosen for all logo elements and page titles as it is striking, and appropriate for a logo as well text.
- 'sans-serif' was chosen as fallback font.

### Layout: 

#### Accessible to all users via the navbar:

- All Pages:
- **About** dropdown with the following options:
    - **About**: A short biography of the company.
    - **Contact**: Contact the business owner via a contact form.
- **My Account**: 
    - **Login**: Login for existing users.
    - **Register**: Register as a user.
- **Shopping Basket**:
    - **Shopping Basket Icon**: Click here to navigate to the shopping basket page.
- **Search**: Search the site using key words.
- **All Products** dropdown with the following options:
    - **By Price**: Display items by price.
    - **By Ratings**: Display items by ratings.
    - **By Categories**: Display items by categories.
    - **All Products**: Display all products.
- **Fitness Equipment** dropdown with the following product options:
    - **Cardio**: Show a selection of cardio.
    - **Weights**: Show a selection of weights.
    - **Exercise Classes**: Show a selection of essential equipments.
    -**All Gym Items**: Show all Gym items.
- **Fitness Clothing** dropdown with the following options:
    - **Stringers**: Show all bar & snacks products.
    - **Shirts**: Show all proteins products.
    - **Shorts**: Show all weight loss products.
    - **All Fitness Clothing**: Show all suppliment products.

#### Accessible to logged in regisered users via the Navbar:

-**My Account**:
    - **My Profile**: Navigate to the session user's profile page.
    - **Logout**: Log out of the site.

#### Accessible only to Superusers(Admin) via the navbar:

-**Product Management**: Add products to the site.

#### Accessible to all users via the Footer:

- **Social Media** links to the following social media sites:
    - **Facebook**
    - **Twitter**
    - **Instagram**
    - **GIT Hub**
- **Email**: Icon Link to available for contact business owner.

#### Accessible to all users on the Products page:

-**Sort Box**: Allows the user to sort the items by price, rating, name and category.

#### Accessible to Superusers(Admin) on the Products page:

-**Edit**: Allows a superuser to edit a product.
-**Delete**: ALlows a superuser to delete a product.

#### Accessible to Superusers(Admin) on the Product Detail page:

-**Edit**: Allows a superuser to edit a product.
-**Delete**: Allows a superuser to delete a product.

#### Accessible to Superusers(Admin) on the Reviews page:

-**Delete**: Allows a superuser to delete a review by user.

### Error Pages:

-**404 Error Page**: A custom 404 error page was designed to redirect users back to the site in the event of a 404 error.

-**500 Error Page**: A custom 505 error page was designed to redirect users back to the site in the event of a 500 error.


### Wireframes:

- The Desktop and Mobile screen wireframes <a href="" target="_blank">here.</a>


### Features:

#### Interactive Features:

The Fit4Life website has been built around the principles of CRUD (Create, Read, Update, Delete), and all of these actions can be taken on 
the site:

- **Register**: The site visitor can add their details to open an account on the site.
- **Login**: The site visitor can login to the site if they are an existing user.
- **Contact**: Any User can contact the site owner by email.
- **Sort**: Any user can sort the products by price, name or category.
- **Search**: Any user can search the site using keywords.
- **Checkout**: Any user can make a secure purchase using Stripe.
- **Add Product**: The superuser (Admin) can add products to the database.
- **Edit Product**: The superuser (Admin) can edit products that are already in the database.
- **Delete Product**: The superuser (Admin) can delete products that are already in the database.
- **Add Review**: A logged in and registered user can add a review.
- **Delete Review**: The superuser (Admin) can delete a review.

#### Future Features:

In future I would like to add the following features:

- **Verified Purchases**: I would like to allow only customers who have bought an item to be able to leave a review for it.
- **Wishlist**: I would like users to be able to create a wishlist.
- **Delivery Address**: I would like users to be able to specify different billing and delivery addresses.
- **Paypal**: I would like users to be able to pay for their items using Paypal.
- **Apple Pay**: I would like users to be able to pay for their items using Apple Pay.
- **Documentation**: More photos will be added to the documentaion, in order to make explanations more explicit.

## Technologies used:

### languages Used:

- HTML5
- CSS3
- Javascript
- Python

### Frameworks, Libraries and Other Sources Used:

- [Django](https://www.djangoproject.com/) was used as the principal framework for the project.
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) was used for all forms on the site.
- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/) was used for user authentication on the site.
- [Stripe](https://stripe.com/) was used to handle payments on the site.
- [Bootstrap4](https://getbootstrap.com/) was used to aid reponsive design.
- [Amazon Web Services](https://aws.amazon.com/) S3 was used to store all static CSS and Javascript files, and images.
- [SQLite3](https://www.sqlite.org/index.html) is the database that was used in production.
- [PostgreSQL](https://www.postgresql.org/) is the database used by the deployed site.
- [Heroku](https://www.heroku.com/) hosts the Milestone Project 04 website.
- [JQuery](https://jquery.com/) was used extensively throughout the site, in order to provide functionality for Bootstrap elements, and for Stripe. 
- [GitPod](https://gitpod.io/) was used as an IDE for this project. 
- [GitHub](https://github.com/) is where the Milestone Project 04's repository is stored. Regular commits were made throughout, and code was pushed to GitHub from GitPod.
- [Font Awesome](https://fontawesome.com/) was used for icons on the site.

## Information Architechture:

### Database Choice:

- SQLight was used in development, as it comes pre-installed with Django.
- PostgreSQL was used for the deployed site, as it is offered as an optional add-on by Heroku.

### Data Modeling:

- The image below was produced using the [dbdiagram.io](https://dbdiagram.io/)

<img src="https://i.ibb.co/rfL9MKM/db-schema.jpg">

## Accessibility:

### Alt Tags:

In order to ensure that all images are accessible for those using a screen reader, I have ensured that all images used 
throughout the site include alt tags.

## Testing:

 - There are dead links on the footer on Social media Icons (Facebook, Instagram and Twitter).
 - There are no errors and warnings in the Developer console
 - Tested using lighthouse and it passes the result
 - The page is fully responsive and has been tested using the Developer console.
 - Tested about, bag, check out, contact, home, review and products pages in all devices. All working fine.
 - There is no error in python codes as it passes through Pep8 online check.
 - There is no error in javascript codes as it passes through JsHint.
 - There is no error in CSS and HTML as it passes through W3C validators.
 - All the codes were formatted using git pod buit-in document formatter.
 - Tested every functionality like Stripe, add/edit/delete products, email, contact, check out, and confirmation email. All working fine.
 - Tested modal functionalities and it works fine.

## Following device used for testing:

 #### Mobile:
  - Pixel 2
  - Pixel 2 XL
  - iPhone 6, 7 and 8
  - iPhone 6, 7 and 8 Plus (real device)
  - iPhone X

#### Tablet:
  - iPad
  - iPad pro

#### Laptop:
  - Macbook

#### Browser:
  - Chome
  - Safari
  - Firefox
  - Opera
  - Microsoft Edge

## Deployment:

### Heroku deployment with AWS:

- The Fit4Life website was deployed to [Heroku](https://www.heroku.com/) using the following steps:

1. Install gunicorn, psycopg2-binary and dj-database-url using the ```PIP Install``` command.
2. Freeze all the requirements for the project into a requirements.txt file using the ```pip3 freeze > requirements.txt``` command.
3. Create a procfile, with the following inside it: ```web: gunicorn MS4.wsgi:application```.
4. Push these changes to GitHub, using ```git add .```, ```git commit -m``` and ```git push``` commands.
5. Navigate to [Heroku](https://www.heroku.com/), and login or create an account.
6. Once logged in, click on 'resources'.
7. From the add-ons search bar, add the Heroku Postgres DB, select the free account, and then submit order form to add it to the project.
8. From the app's dashboard, click on 'settings', and then 'reveal config vars' in order to set the necessary configuration variables for the project. 
It should look like this: 

| Key                   | Value                      |
|-----------------------|----------------------------|
| AWS_ACCESS_KEY_ID     | Your AWS Access Key        |
| AWS_SECRET_ACCESS_KEY | Your AWS Secret Access Key |
| DATABASE_URL          | Your Database URL          |
| EMAIL_HOST_PASS       | Your Email Password        |
| EMAIL_HOST_USER       | Your Email Address         |
| SECRET_KEY            | Your Secret Key            |
| STRIPE_PUBLIC_KEY     | Your Stripe Public Key     |
| STRIPE_SECRET_KEY     | Your Stripe Secret Key     |
| STRIPE_WH_SECRET      | Your Stripe WH Key         |
| USE_AWS               | TRUE                       |

9. Back on the main dashboard, click on 'deploy', and then under the 'Deployment' method section, select GitHub and 'Automatic Deploys'.
10. Ensure that in settings.py, the following code is commented out:
```
Database
 https://docs.djangoproject.com/en/3.1/ref/settings/#databases
```
and the at the following code is added:
```
DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
```
11. Make migrations using the following command:
```
python3 manage.py makemigrations
```
and migrate the database models to the Postgres database using the following command:
```
python3 manage.py migrate
```
12. Load the fixtures from the 'product_types.json' file and then from the 'products.json' file - which are contained in the 'fixtures' folder into the database. 
This is done by using the following command:
```
python3 manage.py loaddata <file name>
```
13. Create a new superuser with the following command:
```
python3 manage.py createsuperuser
```
and then enter chosen email, username and password.
14. In settings.py, contain the previously entered database setting in an if statement, and add an else condition, so that different databases are 
used depending on the environment.
```
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
```
15. Disable 'COLLECTSTATIC' with the fillowing code: ``` heroku config:set DISABLE_COLLECTSTATIC=1 ``` 
so that Heroku doesn't attempt to collect the static files.
16. Add ```ALLOWED_HOSTS = ['milestone-project-04.herokuapp.com', 'localhost']``` to settings.py.
17. Add Stripe environment variables to settings.py.
18. Push to Heroku using the following command:
```git push heroku main```

### Amazon Web Services:

All Static and media files for the deployed version of the site are hosted in a Amazon Web Services(AWS) S3 bucket. 
In order to create your own bucket, please follow the instructions on the AWS website 
[Here](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html)

1. In the gitpod terminal, install boto3 and django-storages using the following commands:
```pip3 install boto3 ``` and ```pip3 install django-storages```
2. Freeze the new requirements into the 'requirements.txt' file using the ```pip3 freeze > requirements.txt``` command
3. Add 'storages' to INSTALLED_APPS in settings.py.
4. Add the following code to settings.py in order to link the AWS bucket to the website:
```
if 'USE_AWS' in os.environ:
    # Cache control
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }

    # Bucket Config
    AWS_STORAGE_BUCKET_NAME = 'milestone-project-04'
    AWS_S3_REGION_NAME = 'eu-west-1'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
```
5. Create a custom_storages.py file in the root level of the project. Inside it, include the locations of the Static Storage and Media Storage.
6. Delete DISABLE_COLLECTSTATIC from the Heroku Config Variables.
7. Finally, push to GitHub, and all changes should be automatically pushed to Heroku too.

### Making a Local Clone:
In order to make a local clone of the FIT BEAST website, enter ```git clone https://github.com/atiqbeenrahim/milestone-project-04.git``` into the terminal. 


Next, create an .env.py file in the root directory of the project, and add it to the .gitignore file. 
The following code needs to be added to the .env.py file:
```
import os  
os.environ["DEVELOPMENT"] = "True"    
os.environ["SECRET_KEY"] = "<Your Secret Key>"
os.environ["STRIPE_PUBLIC_KEY"] = "<Your Stripe Public Key>"    
os.environ["STRIPE_SECRET_KEY"] = "<Your Stripe Secret Key>"    
os.environ["STRIPE_WH_SECRET"] = "<Your Stripe WH Secret Key>"   
```

Then make sure that the required packages are installed by running the following command: 
```pip install -r requirements.txt```

Make migrations and then migrate in order to create a database, by running the following commands:
```python3 manage.py makemigrations``` and ```python3 manage.py migrate```.

Load the fixtures from the 'product_types.json' file and then from the 'products.json' file - which are contained in the 'fixtures' folder into the database. 
This is done by using the following command:
```
    python3 manage.py loaddata <file name> 
```

Create a superuser with the following command: ```python3 manage.py runserver``` and entering your credentials.

Run the app by entering the following command:
```python3 manage.py runserver```

## Credits:

### Code:

- **Code Institute Boutique Ado Project**: Much of this project was copied and adapted from the Code Institute 'Boutique Ado' project. Comments stating this have been added to the top
of files that have been copied and adapted in this way, as well as to views, as it was felt that by commenting on every piece of copied code 
would mean that the comments would detract from the code. If there is additional code that has been copied from Boutique Ado and NOT acknowledged in 
the corresponding file, then it is in error, and should have been acknowledged. 

- **Code Institute Slack Channels**: Slack was used extensively for debugging, and to bounce ideas off other students and CI staff members.

-**W3 Schools**: W3 Schools was referenced for debugging purposes.

### Images: 

- All product images are the property of fitnessequipmentireland.ie, and were taken from their website.

- The background image on the homepage is from [pixabay](https://pixabay.com/)

- The favicon image, is from [Icons8](https://icons8.com/)


### Content:

- All content on the site was either taken from the Boutique Ado project, fitnessireland, or written by the developer.

## Acknowledgements:

- **My Mentor** Akshat Garg, for help and guidance on this project.
- **My Friends and Family** for constant support, and feedback on the content and functionality.
- **Code Institute Slack Channel** for help answering my many questions.
- **Code Institute Tutor Support** for helping me work out why things weren't working how they should.
