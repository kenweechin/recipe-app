![Responsive Mockup](/documentation/wireframes/mockup.png)

# MEALBOOK
MEALBOOK is a practical Python and Data-Centric Development Milestone Project.

This is a Full-Stack MongoDB-based Flask project. The main objective is to create a recipe database that allows users to perform the CRUD functionality (create, read, update, and delete). MEALBOOK offers features of all recipes accessibility to either registered or non-registered users. They can browse recipes created by other creators and themselves. Registered users can create, edit, and delete their recipes. MEALBOOK is aiming to create a food lover community where all the registered and non-registered inspire and get inspired by others.

The website consists of:
* Home Page: Landing image with different varieties of foods as background, and an eye-catching button for attracting guests to click for browsing recipe collection.
* All Recipes Page: Display all recipes that have been created by different users. All the recipes are displayed as a card structure that shows the image(if the user uploads their food's image), meal type, recipe's name, and serving size. Each page consists of a maximum of eight card recipes, and users can click on the second page to browse more recipes. The search recipe bar is shown on top of the page. The number of a recipe created is shown on top of the page highlighted with a red underline. 
* Log In Page: Users can log in to their account.
* Register Page: Non registered users can create an account.
* Profile Page: Display all the recipes created by the user him/herself. The number of a recipe created is shown on top of the page highlighted with a red underline. 
* Recipe Detail Page: This page is directed when the user/guest click on the recipe card. It displays recipe name, recipe image, meal-type, diet type, serving size, prep time, cooking time, author, dish description, ingredients, and methods of cooking.
* New Recipe Page: All the essentials input for the user to add in the content related to the recipes attributes. Edit and Delete buttons are shown for further changes.

Non-user page accessibility:
* Home Page
* All Recipes Page
* Log In Page
* Register Page
* Recipe Detail Page 

User page accessibility:
* Home Page
* All Recipes Page
* Log In Page
* Register Page
* Recipe Detail Page 
* Profile Page 
* Add Recipe Page
* Edit Recipe Page

## **User Experience (UX)**

### **Player goals**

* Create a simplistic and visual tempting yet flawless recipe app.
* The purpose of the app is obvious when the user lands on the main page. 
* Eye-catching landing image and description that suit the theme of the website.
* All recipes created are shown on a page and can be navigated with just one click. The page will show an overview of recipes created.
* The details of the recipe can be viewed by clicking on the recipe card profile. 
* Each specific recipe profile consists of all necessary data created by the author.
* Registered users can edit or delete their recipes but not others. 
* Non registered users do not have an edit and delete button when browsing the recipe profile. 
* Registered users can add recipes through add recipe link with just one click on the top navigation bar. 
* All navigation links and input in add recipe page have relevant icons right beside it so all users can know what does the link/input do at a glance. 
* All required inputs are marked with an asterisk symbol in red color. 
* Easy navigation between different pages without any broken link or page error.
* Well-structured content created from programming that provides a user-friendly MEABOOK app.
* Utilizing HTML, CSS, Javascript, Python, Flask, Jinga Template, and MongoDB to showcase the coding skill and as the third portfolio.  

### **User Stories**

* View all the recipes without having to register an account.
* View all the recipe details as in recipe image, recipe meal type, recipe name, recipe diet type, recipe serving size, recipe preparation time, recipe cooking time, dish description, ingredients needed, and cooking methods. All of these are shown in an organized layout. All the details have a relevant icon so the user can easily know what it is.
* Able to search the keyword by typing a keyword into the search bar. 
* A response message will show if there is no result returned. 
* Register a new account.
* Add a new recipe.
* Edit or delete an existing recipe. 
* View the total recipes created.
* Log out with one click and terminate the session.
* Use the website from any device such as desktop, laptop, tablet and mobile.    

### **Design Choices**

* Framework
    * [Materialize](https://materializecss.com/), a front-end framework was utilized for this project. Navbars, recipe cards, forms, and a grid was created. 
    * [JQuery](https://jquery.com/) was used to initialize some Materialize elements. 
* Imagery
    * The background image on the home page is using the image with a combination of different dishes. This is to demonstrate the main purpose of the website, which act as a representative element of the website is focusing on. This is to attract the user's attention and yield a trust emotion toward the website. The background images on the log in page and register page are food relevant as well to match the website's theme. 
* Color Scheme
    * The main color of the website (except the images) used are generally in white tone. This is because all the images used and will be uploaded by the user to the website are generally rich in colors due to the food content. Hence, the colours of the images themselves are sufficient to yield colours that can enrich the website. Furthermore, the white color tone does match the simplicity and clean design purpose.
    * The colors of the website title and other navigation links are set to maroon color to yield contrast with the white background of the website. 
    * Dark grey color is used for the top page of navigation links when the user hovers over the links to present a great contrast to the white tone background and shows to the user that they are currently hovering at that link. 
    * Links are shown in blue color. 
    * Add recipe button and Delete button is shown in red to alert the user. 
    * Edit button is shown in green color.
* Typography
    * Playfair Display font is the main font used throughout the website pages with Sans Serif as the fallback font. 
    * Playfair Display font looks elegant either as a title or the content on a website. It tends to yield a trustable emotion to the user as well which is a vital element for a website. 
* Styling
    * Each of the links/pages has the same navigation menu so the user can direct to the other navigation sites when they are browsing particular links.
    * Recipe cards profile has a rounded border style to look more modern. 
* Icons 
    * [FontAwesome](https://fontawesome.com/) and [MaterializeIcon](https://materializecss.com/icons.html) are the main icons library used for this project. Icons are great in grabbing users' attention. It is user-friendly and absolutely useful for non-native English speakers and the icons stand out their purpose.  

### **Wireframes**

Balsamiq software was used to generate the following wireframes while doing the project planning and scope plan section. Click on the following links to view.

* [Home](/documentation/wireframes/home.pdf)
* [All Recipe](/documentation/wireframes/all_recipes.pdf)
* [Log In](/documentation/wireframes/login.pdf)
* [Register](/documentation/wireframes/register.pdf)
* [Add/EditRecipe](/documentation/wireframes/add.edit_recipe.pdf)
* [Recipe Details](/documentation/wireframes/recipe_details.pdf)

# **Features**

### **Home Navigation Bar**

![Navbar](/documentation/screenshots/homenavbar.png)

The logo of the website is located at the top-left position, whereas the remaining navigation links (Home, All Recipes, Login, Register) for the non-registered user, (Home, All Recipes, Login, Register, Profile, Add Recipe) for the registered user are situated at top right corner. Both MEALBOOK and Home navigation links are redirected to the home page. In a tablet and mobile resolution, the navbar is collapsed into a burger bar icon and a side nav bar will pop out once clicked.  

### **Home Navigation Bar for non-registered user**

![Non-Registered User](/documentation/screenshots/nonusernav.png)

* Home
* All Recipes
* Log In
* Register

### **Home Navigation Bar for registered user**

![Registered User](/documentation/screenshots/usernav.png)

* Home
* All Recipes
* Profile
* Add Recipe
* Log Out

### **Home Page Features**

* Home page consists of a landing image and follow up by a button that redirects the user to the "All Recipe" page which to glance the overview of all the recipes created.

### **All Recipes Page Features**

![All Recipes](/documentation/screenshots/allrecipes.png)

* The All Recipes page displays all the recipes card profiles created by different users. 
* Non-registered and registered user has the accessibility to browse all those recipes. 
* At the top section of the page, there is **Log In** and **Sign Up** links for non-registered user/logged out user. The reason for placing these links at the top is to encourage the user to log in to create more recipes, and for the non-registered user to sign up for an account. 
* Follow up the links are the browse recipe bar section, where all the users can type in the keyword which in turn will return the desired results. Or else, the message will show no results were found.
* Each of the recipe cards is showing the following features:
    * Recipe image
    * Recipe meal type ( Breakfast, Lunch, Dinner, or Dessert)
    * Recipe diet type ( Normal, Vegan, Low Carb, Diary/Lactose Free)
    * Recipe serving size

### **Recipe Details Page**
![Recipe Details](/documentation/screenshots/recipedetails.png)

* The Recipe Detail page displays the details of the recipe. 
* Recipe name is shown at the top of the page.
* Recipe image and (meal type, diet type, serving size, preparation time, cooking time) are sitting side by side. The reason for this arrangement is that this will show the overview of a recipe. Furthermore, once the user is landed on this page, either any type of resolution, this section will display to the user first. 
* Then, as the user scrolls down the page, it shows the dish description, ingredients, and cooking methods section. These elements are placing at below the page because those description elements tend to contain larger space for the content. Hence this page arrangement yields an easy following guide for the user to get around. 

### **Login Page**

![Login](/documentation/screenshots/login.png)

* Log in column section at the top page is styled with a white box shadow feature to highlight the purpose of the login page.
* The login page consists of the feature for the user to log in by entering the correct username and hashed password. 
* Once the user key in the correct input field which matched to the database, it will then redirect the user to the user's profile page, which shows all the recipes created by the user.
* If the user key in the incorrect input for either the username and/or password, the flash message will pop up at the top of the page notifying incorrect username and/or password, and the user will continue to stay on the same page. 
* The log in button is emplaced at the bottom of the user input field section. It is styled with a liquid motion feature to make it looks more elegant and visually tempting. 
* A **Register Link** is displayed below the button for the user to create an account.   

### **Registration Page**

![Register](/documentation/screenshots/register.png)

* Register column section at the top page is styled with a white box shadow feature to highlight the purpose of the register page.
* The register page consists of the feature for the user to create their username and password. 
* The register button is styled with a liquid motion feature same as the login button. 
* Once the user-created their username and password, it will then redirect the user to the user's profile page, which shows all the recipes created by the user, flash message stating **Registration Completed**, number of a recipe created, and a **Add New Recipe** button below. 

### **Log Out**

* Log Out link is located in the top right corner for logged in users.
* Once the user has logged out from the session, it will redirect the user to the login page and the flash message will pop up to notify the user has been logged out.

### **Profile Page**

![Profile](/documentation/screenshots/profile.png)

* The profile page shows all the recipes created by the user. 
* User can see the total number of recipes created by themselves.
* User can glance at an overview of all those recipes in recipe card profile style. 
* User can click onto the recipe card to view the recipe details. 

### **Add Recipe Page**

![Add Recipe](/documentation/screenshots/addrecipe.png)

* Log in and registered users can add a recipe on the add new recipe page. 
* All of the required input fields contain the placeholders to notify the user what kind of data to enter. 
* The required input fields have a red asterisk icon so the user knows it is compulsory to have these input fields to be filled. 
* Each of the input fields is associated with a relevant font awesome icon. 
* The **Meal Type** and **Dietary** fields have a dropdown section where the user can choose an option from the dropdown. 
* If the user doesn't have a recipe image to upload to their page, the recipe image placeholder will show on the recipe detail page.
* The red **CREATE RECIPE** button is located at bottom of the form after the user has filled up the input fields. It will then redirect the user to the user's profile page.      

### **Edit Recipe Feature**

* The recipe edit feature is only accessible for the user who has created their recipe. Other users would not have the edit feature if they are viewing another's creator's recipe. 
* The Edit Recipe page has the same input fields and forms layout as the Add Recipe page but the form is pre-populated with the original recipe's detail. This pre-populated feature enables the user to edit the recipe easily without having to re-enter the details. 
* Once the user clicked on the **DONE** button, the database will get updated and redirect the user back to the edited recipe detail page with a flash message pop up saying the recipe is updated successfully.
* The user can click on the **CANCEL** button if he/she decided not to edit the recipe, and will be redirected back to the same recipe detail page.  

### **Delete Recipe Feature**

* The recipe delete feature is only accessible for the user who has created their recipe. Another user would not have the delete feature if they are viewing another's creator's recipe. 
* User can delete the recipe by clicking on the **DELETE** button and the recipe will be removed from the database and user's recipe profile page. The total number of user's recipes will deduct and update automatically. 

![Delete Modal Confirmation Message](/documentation/screenshots/delete.png)
* The delete modal confirmation message will pop out to confirm if the user is intending to delete the recipe. This defensive design is to ensure the user would not accidentally delete their recipe by misclick. 

### **Footer Section**

* All pages contain a footer section which shows [Github](https://github.com/), [Facebook](https://www.facebook.com/), [Linkedin](https://www.facebook.com/) and [Youtube](https://www.youtube.com/). 
* Each link clicked will open up a new tab so the existing page will remain which is easy for navigation. 

### **Error 404 and 500 Page**

![Error 404 and 500 Page](/documentation/screenshots/404.png)

* Error 404 page is shown if page not found or file not found error message. There is a **HOME** link the user can click to redirect back to the home page.
* On the other hand, the user can click on any navigation link on the top page.

# **Features Left To Implement**

* Total Views - Allow users to know the total views of a recipe profile.
* Recipe Arrangement Order - Allow the recipes to appear at the top page based on the number of viewing. The highest view will be placed at the top page and followed up subsequently.
* Advanced search function - Allow the user to search any keyword from the database if the input is in a proper order which the database can filter and lookup for it.
* User account setting - Allow the user to change their username and/or password. 

# **Technologies Used**

* [Am I Responsive](http://ami.responsivedesign.is/) - For checking page responsiveness and readme content.
* [PIP](https://pip.pypa.io/en/stable/installation/) - For installing essential tools.
* [GitPod](https://www.gitpod.io/) - Online IDE for project development. 
* [Git](https://git-scm.com/) - For version control.
* [GitHub](https://github.com/) - For storing project remotely.
* [ResizeImage](https://resizeimage.net/) - For resizing images.

### **Font-End**

* [HTML](https://developer.mozilla.org/en-US/docs/Glossary/HTML5) - For building the web structure.
* [CSS](https://developer.mozilla.org/en-US/docs/Learn/CSS/First_steps/What_is_CSS) - For specifying how documents are presented to users.

### **Back-End**

* [Python](https://www.python.org/) - Programming used for this back-end project.
* [MongoDB](https://www.mongodb.com/) - NoSQL database program for storing non-relational data.
* [PyMongo](https://pypi.org/project/pymongo/) - Tools for interacting with MongoDB database from Python.
* [Flask](https://flask.palletsprojects.com/en/2.0.x/) - For developing web applications using python, implemented on Werkzeug and Jinja2. 
* [Werkzeug](https://werkzeug.palletsprojects.com/en/0.16.x/) - For password hashing generation and verification.
* [Jinja](https://jinja.palletsprojects.com/en/2.10.x/) - Allow data to be shared and processed before being turned into content and sent back to the client.
* [Heroku](https://www.heroku.com/) - For hosting project.

### **Libraries**

* [Materialize](https://materializecss.com/) - An open source responsive front-end framework that offers slick material design.
* [Font Awesome](https://fontawesome.com/) - Offer icons for the project.
* [Google Fonts](https://fonts.google.com/) - To import **Playfair Display** font to use for this project
* [JQuery](https://jquery.com/) - For HTML DOM tree traversal and manipulation.

# **Testing**

### **User Stories Testing Section** 

**All Recipes Page features are working as in**
* Once the "All Recipes" link was clicked and entering the page, all the recipes are shown. 
* A maximum of 8 recipes card profiles are shown with each row containing 4 recipes card profiles in tablet and laptop resolution. 
* Each of the recipe card profiles shows the image, meal-type, recipe name, diet type, and quantity of serving. 
* There are no elements that are extending beyond the card profile which can yield an unprofessional sense toward the website. 
* The pagination is shown at the bottom of the page. It will highlight the current page in a light pink colour. 
* Clicking on the second and subsequent pages do show the remaining recipe card profiles with all recipe details that are supposed to be shown.
* All pagination works smoothly when navigating to different pages without any broken pages. 
* The number of recipes created which is shown on the "All Recipes" page are matches the MongoDB.
* The "Log In" and "Sign Up" links at the top page once clicked, are directing the user to the corresponding pages.   
* The search function is filtering the entered keyword and shows the correct result. For example, if "breakfast" is searched, all the recipes where the meal type is "Breakfast" will display on the page, and it does not matter if the keyword entered is in capital letter. 
* Recipe name and diet type show the corresponding results as well. 
* An irrelevant keyword was entered to test the pop-up message stating "Ops! No results were found" is showing, which it does. 
* User can click on the "All Recipe" navigation link at the top navigation bar to reset the searching.  
* For logged in users, the additional elements displayed are the total recipe's quantity is shown on the top page. The button "CLICK ME TO ADD NEW RECIPE" is working which direct the user to the "Add Recipe" page. 

**Recipe Details Page features are working as in:**

* The layout of the recipe image and recipe details are aligned properly. 
* Ingredients and cooking method section contents are displayed in a list and a proper way. 
* For logged in user, the "Edit" button directs the user to the "Edit Recipe" page, whereas the "Delete" button will delete the recipe. 

**Log In Page features are working as in:**

* Once the "Log In" button on the top navigation bar is clicked, the form is opened up. 
* A valid username and password are entered and it logged the user in successfully and direct the user to their profile page. 
* Further testing was done by entering an invalid either username or password, and login action can't be performed. 
* The "Register" link below works which direct the guest to the registration page.

**Register Page features are working as in:**

* The first thing to test is by entering the existing username and password which is already created and stored in the database.
* Once clicked on the signup button, a flash message popped up stating "This username is already registered" as expected. 
* Entering a new username and password direct the new user to their profile page with a flash message showing registration success. 
* If the guest enters the username with the character less than 4 and more than 20, the error will show. 
* If the new password entered is less than 6 characters and more than 20 characters, the error will show. 
* If neither username nor password is entered, the error will show as well. 
* The "Sign-In" link below the signup button is working which direct the guest to the "Log In" page. 

**Profile Page features are working as in:**

* This is shown only for the logged-in user. 
* The total recipes quantity is shown at the top page which shows the number of recipes created by the particular user. 
* Once clicked onto each of the recipe detail pages, all the essential recipes details are shown. 
* Both "Edit" and "Delete" buttons are shown. 
* "CLICK ME TO ADD NEW RECIPE" button is shown on the top recipe page and it can direct the user to the "Add Recipe" page to fill up the required recipe forms.   

**Add Recipe Page features are working as in:**

* All the required input fields with empty input will lead to an error and the form won't be able to submit. 
* The image URL input is not essential, hence leaving it blank does not generate an error. 
* Yet if the user enters an invalid image URL, it will display an error to request the user to enter a valid image URL. 
* If there is no image URL input, the image placeholder will display, which in this case all is working fine. 

**Edit Recipe Page features are working as in:**

* Only the author will be able to see the "Edit" and "Delete" buttons. 
* If the link was edited and changed to the other user's username, nothing will show and it remains on the user's profile page, indicating the defensive design works well. 
* Author can see the pre-populated fields on the form and able to apply changes easily. 
* Once every required input field are edited and submitted, the recipe details are changed accordingly as well, proving the edit feature works perfectly.

**Delete Recipe feature is working as in:**

* The selected recipe is removed from the collections in "All Recipes" collections and database. 

**404 and 500 Errors**

* The URL in the browser was changed to a dummy URL to get a non-existing page, and the custom page 404 error page shows up. It proves the error-handler function works perfectly. The "Home" link on the page which direct the user back to the home page works as well. 

**Navbar / Footer Section**

* All links are tested and they are pointing to the correct destination. 

**Bugs and Fixes**

* The landing image on the home page will go blank or missing occasionally. Hard reloading the page a few times will resolve the issue. 
* The ingredients and methods of cooking input field: If the user copies the content from the other sources and paste it to the input field, the result page will show all the text are displaying on the same row. Hence, hitting the "enter" button after a sentence or paragraph will show the content in a proper alignment list. 

**Responsiveness**

* All the pages are tested for their responsiveness by using Google Inspect, from mobile resolution to desktop resolution. All the page elements display properly. The burger bar icon is shown when the website is in mobile and tablet resolution. 
* Quality assurance of the website across multiple browsers had been done by using [Browserstack](https://www.browserstack.com/). The following browsers had been tested for compatibility and all of them passed the test.
    * Edge
    * Firefox
    * Chrome
    * Opera
    * Yandex
    * Safari


### **Code Validation**

**Python**

* Python file was tested through [PEP8 Online](http://pep8online.com/) validator and the tested python code is PEP8 compliant.

**Javascript**

* JS code was tested through [JSHint](https://jshint.com/). The dollar sign "$" was considered as an undefined variable by Jshint, yet, it is essential for jQuery to perform Materialize initialization.

**Html**

* All Html pages were tested through [The W3C Markup Validation Service](https://validator.w3.org/). Errors are shown on the Jinja templating language because it doesn't recognize this language. 

**CSS**

* CSS was tested through [The W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/). No error is shown.


# **Deployment**

### **Local Deployment**

* In order to run this project, the essentials tools stated below are required for installation beforehand:
    * An Integreted Development Environment(IDE)- [Gitpod](https://www.gitpod.io/) was used for this project.
    * [Git](https://git-scm.com/)
    * [MongoDB](https://www.mongodb.com/) (Database creation)
    * [PIP](https://pip.pypa.io/en/stable/installation/)
    * [Python](https://www.python.org/)

**Directions**

There are two ways to use this project. 
* You can clone this repository into your local IDE.
    * Log in to Github and navigate to the GitHub repository: https://github.com/kenweechin/recipe-app
    * Click on the "Code" drop-down button which sits right beside the green "Gitpod" button. You can then select one of the drop-down options.

    **Clone the files using URL**
    * Copy the URL.
    * Create a repository in GitHub and a workspace in your IDE.
    * Open the terminal and type: `$ git clone https://github.com/kenweechin/recipe-app`
    * All the files now should import into your workspace.

    **Download zip files**
    * Create a repository in GitHub and a workspace in your IDE.
    * Unzip the folder.
    * Upload the files into your workspace.

### **Deployment Preparation**
* Get connection string with MongoDB
    * Click on project, then click on connect
    * Select connect your application (check python & version 3.6)
    * Copy link & change database name & password (Use the password for user access and not  login details)

* Set local environment
    * Create env.py file in the route directory by entering touch env.py in your command-line interface
    * Add the following to your env.py:

        import os   
        os.environ.setdefault("IP", "0.0.0.0")    
        os.environ.setdefault("PORT", "5000")   
        os.environ.setdefault("SECRET_KEY", "your_secret_key")   
        os.environ.setdefault("MONGO_URI", "Your_Mongo_connection_string")   
        os.environ.setdefault("MONGO_DBNAME", "Your_DB_Name")

    * Add env.py and ‘pycache/’ directory to .gitignore

* Requirements.txt and Procfile
    * Create a requirements.txt file, which will list all of the Python dependencies by typing the following in the command-line interface:

        $ pip freeze > requirements.txt
    * Create a Procfile, which is a specific type of file that tells Heroku how to run our project by typing the following command-line interface:

        $ echo web: python app.py > Procfile
    
    *Note that you have to write Procfile with a capital P. 
    * Add and commit the requirement.txt and procfile then push to GitHub

### **Deployment on Heroku**
* Log onto Heroku and click the create new app button
* Enter a unique name for your application
* Select the region closest to you
* Set your deployment method to 'GitHub'
* Search for the repository you wish to deploy from
* Enable automatic deploy
* Set environment in Heroku App
    * Go to Settings, then click on reveal config vars
    * Enter your key-value pairs as per your env.py file (without the inverted commas)
    
# **Credits**

### **Media**
* Background Image for Log In page, Register page, and landing image on Home page: [Unsplash](https://unsplash.com/).
* Favicon: [The best Favicon Generator](https://favicon.io/).
* Recipe Placeholder Image: [Google](https://www.google.com/).
* Recipe Image: [BBC Food](https://www.bbc.co.uk/food). 

### **Content**
* The recipe's content (ingredients, methods etc.) were taken from the BBC food website, except for another user who has created for their own.
* The layout of the recipe detail page was inspired by the BBC food website.

### **Website Design Feature**
* The button design feature in the Home page, login page and Register page was derived and edited from https://cssbuttons.io/detail/westitan/mean-falcon-52.

### **Acknowledgement**
* I would like to thank the members of the Student Support and Tutor from Code Institute who had offered advice and help on my coding related issue. Furthermore, I would like to thank my mentor - Mr Spencer for steering my projects in the right direction and Mr Rohit for giving an overall assessment of my project.  










