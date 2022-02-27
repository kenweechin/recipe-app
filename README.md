![Responsive Mockup](wireframes/mockup.png)

# MEALBOOK
MEALBOOK is a practical Python and Data Centric Development Milestone Project.

This is a Full-Stack MongoDB-based Flask project. The main objective is to create a recipe database which allows users to perform the CRUD functionality (create, read, update, and delete). MEALBOOK offers features of all recipes accessibility to either registered or non registered user. They can browse recipes created by other creators and themselves. Registered users can create, edit, and delete their own recipes. MEALBOOK is aiming to create a food lover community where all the registered and non-registed inspire and get inspired by others.

The website consists of:
* Home Page: Landing image with different varieties of foods as background, different meal types showing different meal varieties created on this website.
* All Recipes Page: Display all recipes that have been created by different users. All the recipes are display as a card structure which showing image(if user uploads their food's image), , meal type, recipe's name, and number of serving. Each page consists of a maximum of eight card recipes, and user can click on the second page to browse more recipes. Search recipe bar is shown on top of the page. The number of recipe created is shown on top of the page highlighted with a red underline. 
* Log In Page: User can log in to their own account.
* Register Page: Non registered user can create an account.
* Profile Page: Display all the recipes created by the user him/herself. The number of recipe created is shown on top of the page highlighted with a red underline. 
* Recipe Detail Page: This page is directed when user/non user click on the recipe card. It displays recipe name, recipe image, meal type, diet type, serving size, prep time, cooking time, author, dish description, ingredients, and methods of cooking.
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
* The purpose of the app is obvious when the user click landed on the main page. 
* Eye-catching landing image and description that suit the theme of the website.
* All recipes created are shown in a page and can be navigated by just one click. The page will show an overview of recipes created.
* The details of the recipe can be viewed by clicking on the recipe card profile. 
* Each specific recipe profile consists of all neccessary data created by the author.
* Registered user can edit or delete their own recipe but not others. 
* Non registered user do not have edit and delete button when browsing the recipe profile. 
* Registered user can add recipes through add recipe link by just one click on the top navigation bar. 
* All navigation links and input in add recipe page have relevant icons right beside it so all users can know what does the link/input do in a glance. 
* All required inputs are marked with an asterisk symbol in red color. 
* Easy navigation between different pages without any broken link or page error.
* Well-structured content created from programming that provides a user-friendly MEABOOK app.
* Utilizing HTML, CSS, Javascript, Python, Flask, Jinga Template, and MongoDB to showcase the coding skill and as the third portfolio.  

### **User Stories**

* View all the recipes without having to register an account.
* View all the recipe details as in recipe image, recipe meal type, recipe name, recipe diet type, recipe serving size, recipe preparation time, recipe cooking time, dish description, ingredients needed, and cooking methods. All of these are shown in an organized layout. All the details have a relevant icon so user can easily know what it is.
* Able to search the keyword by typing keyword into the search bar. 
* A respond message will show if there is no result returned. 
* Register a new account.
* Add a new recipe.
* Edit or delete an existing recipe. 
* View the total recipes created.
* Log out with one click and terminate session.
* Use the website from any device such as desktop, laptop, tablet and mobile.    

### **Design Choices**

* Framework
    * [Materialize](https://materializecss.com/), a front-end framework was utilized for this project. Navbars, recipe cards, forms, and grid was created. 
    * [JQuery](https://jquery.com/) was used to initialize some Materialize elements. 
* Imagery
    * The background image on the home page is using the image with combination of different dishes. This is to demonstrate the main purpose of the website, which act as a representative element of the website is focusing on. This is to attract the user's attention and yield a trust emotion toward the website. The background images on the log in page and register page are food relevant as well to match the website's theme. 
* Color Scheme
    * The main color of the website (except the images) used are generally in white tone. This is because all the images used and will be uploaded by the user to the website are generally rich in colors due to the food content. Hence, the colours of the images themselves are sufficient to yield colours that are able to enrich the website. Furthermore, white color tone does match to the design purpose which is clean and simplicity.
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
    * [FontAwesome](https://fontawesome.com/) and [MaterializeIcon](https://materializecss.com/icons.html) are the main icons library used for this project. Icons are a great in grabbing user's attention. It is user-friendly and absolutely useful for non-native english speakers and the icons stand out their purpose.  

### **Wireframes**

Balsamiq software was used to generate the following wireframes while doing the project planning and scope plan section. Click on the following links to view.

* [Home](wireframes/home.pdf)
* [All Recipe](wireframes/all_recipes.pdf)
* [Log In](wireframes/login.pdf)
* [Register](wireframes/register.pdf)
* [Add/EditRecipe](wireframes/add.edit_recipe.pdf)
* [Recipe Details](wireframes/recipe_details.pdf)

# **Features**

### **Home Navigation Bar**

![Navbar](/static/images/homenavbar.png)

The logo of the website is located at the top left position, whereas the remaining navigation links (Home, All Recipes, Log In, Register) for non-registered user, (Home, All Recipes, Log In, Register, Profile, Add Recipe) for registered user are situated at top right corner. Both MEALBOOK and Home navigation links are redirected to the home page. In a tablet and mobile resolution, the navbar is collapsed into a burger bar icon and a sidenav bar will pop out once clicked.  

### **Home Navigation Bar for non-registered user**

![Non-Registered User](/static/images/nonusernav.png)

* Home
* All Recipes
* Log In
* Register

### **Home Navigation Bar for registered user**

![Registered User](/static/images/usernav.png)

* Home
* All Recipes
* Profile
* Add Recipe
* Log Out

### **Home Page Features**

* Home page consists of a landing image and follow up by a button that redirects the user to the "All Recipe" page which to glance the overview of all the recipes created.

### **All Recipes Page Features**

![All Recipes](/static/images/allrecipes.png)

* The All Recipes page displays all the recipes card profile created by different users. 
* Non-registered and registered user has the accessibility to browse all those recipes. 
* At the top section of the page, there are **Log In** and **Sign Up** links for non-registered user/logged out user. The reason of placing these links at top is to encourage the user to log in to create more recipes, and for non-registered user to sign up an account. 
* Follow up the links are the browse recipe bar section, where all the users can type in the keyword which in turn will return the desire results. Orelse, the message will show no results were found.
* Each of the recipe card is showing the following features:
    * Recipe image
    * Recipe meal type ( Breakfast, Lunch, Dinner, or Dessert)
    * Recipe diet type ( Normal, Vegan, Low Carb, Diary/Lactose Free)
    * Recipe serving size

### **Recipe Details Page**
![Recipe Details](/static/images/recipedetails.png)

* The Recipe Detail page displays the details of the recipe. 
* Recipe name is shown at the top of the page.
* Recipe image and (meal type, diet type, serving size, preparation time, cooking time) are sitting side by side. The reason for this arrangement is that, this will show the overview of a recipe. Furthermore, once the user is landed on this page, either any type of resolution, these section will display to the user first. 
* Then, as the user scrolls down the page, it shows the dish description, ingredients, and cooking methods section. These elements are placing at below the page because those description elements tend to contain larger space for the content. Hence this page arrangement yield an easy following guide for the user to get around. 

### **Login Page**

![Login](/static/images/login.png)

* Log in column section at the top page is styled with white box shadow feature to highlight the purpose of the log in page.
* The log in page consists of the feature for the user to log in by entering correct username and hashed password. 
* Once the user key in the correct input field which matched to the database, it will then redirect the user to the user's profile page, which shows all the recipes created by the user.
* If the user key in the incorrect input for either the username and/or password, the flash message will pop up at the top of the page notifying incorrect username and/or password, and the user will continue to stay on the same page. 
* The log in button is emplaced at the bottom of the user input field section. It is styled with liquid motion feature to make it looks more elegant and visually tempting. 
* A **Register Link** is displayed below the button for the user to create an account.   

### **Registration Page**

![Register](/static/images/register.png)

* Register column section at the top page is styled with white box shadow feature to highlight the purpose of the register page.
* The register page consists of the feature for the user to create their username and password. 
* The register button is styled with liquid motion feature same to the log in button. 
* Once the user created their username and password, it will then redirect the user to the user's profile page, which shows all the recipes created by the user, flash message stating **Registration Completed**, number of recipe created, and a **Add New Recipe** button below. 

### **Log Out**

* Log Out link is located the the top right corner for logged in user.
* Once the user has logged out from the session, it will redirect the user to the log in page and the flash message will pop up to notify the user has been logged out.

### **Profile Page**

![Profile](/static/images/profile.png)

* The profile page shows all the recipes created by the user. 
* User can see the total number of recipes created by themselves.
* User can glance an overview of all those recipes in recipe card profile style. 
* User can click onto the recipe card to view the recipe details. 

### **Add Recipe Page**

![Add Recipe](/static/images/addrecipe.png)

* Logged in and registered user can add a recipe on the add new recipe page. 
* All of the required input fields contain the placeholders to notify the user what kind of data to enter. 
* The required input fields has an red asterisk icon so the user knows it is compulsory to have these input fields to be filled. 
* Each of the input fields is associated with a relevant fontawesome icon. 
* The **Meal Type** and **Dietery** fields have dropdown section where the user can choose an option from the dropdown. 
* If the user doesn't have a recipe image to upload to their page, the recipe image placeholder will show on the recipe detail page.
* The red **CREATE RECIPE** button is located at bottom of the form after the user has filled up the input fields. It will then redirect the user to the user's profile page.      

### **Edit Recipe Feature**

* The recipe edit feature is only accessible for the user who has created their own recipe. Other user would not have the edit feature if they are viewing other's creators recipe. 
* The Edit Recipe page has the same input fields and form layout as to the Add Recipe page but the form is pre-populated with the original recipe's detail. This pre-populated feature enable the user to edit the recipe easily without have to re-enter the details. 
* Once the user clicked on the **DONE** button, the database will get updated and redirect the user back to the edited recipe detail page with a flash message pop up saying the recipe is updated successfully.
* The user can click on the **CANCEL** button if he/she decided not to edit the recipe, and will be redirected back to the same recipe detail page.  

### **Delete Recipe Feature**

* The recipe delete feature is only accessible for the user who has created their own recipe. Other user would not have the delete feature if they are viewing other's creators recipe. 
* User can delete the recipe by clicking on the **DELETE** button and the recipe will be removed from the database and user's recipe profile page. The total number of user's recipe will deduct and update automatically. 

### **Footer Section**

* All pages contain a footer section which shows [Github](https://github.com/), [Facebook](https://www.facebook.com/), [Linkedin](https://www.facebook.com/) and [Youtube](https://www.youtube.com/). 
* Each link clicked will open up a new tab so the existing page will remain which is easy for navigation. 

### **Error 404 and 500 Page**

![Error 404 and 500 Page](/static/images/404.png)

* Error 404 page is shown if page not found or file not found error message. There is a **HOME** link the user can click to redirect back to the home page.
* On the other hand, user can click on any navigation link on the top page.

# **Features Left To Implement**

* Total Views - Allow user to know the total views of a recipe profile.
* Recipe Arrangement Order - Allow the recipes to appear at the top page based on the number of viewing. Highest view will placed at the top page, and following up subsequently.
* Advance search function - Allow the user to search any keyword from the database if the input is in a proper order which the database can filter and look up for it.
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

* [Python](https://www.python.org/) - Progamming used for this back-end project.
* [MongoDB](https://www.mongodb.com/) - NoSQL database program for storing non-relational data.
* [PyMongo](https://pypi.org/project/pymongo/) - Tools for interacting with MongoDB database from Python.
* [Flask](https://flask.palletsprojects.com/en/2.0.x/) - For developing web applications using python, implemented on Werkzeug and Jinja2. 
* [Werkzeug](https://werkzeug.palletsprojects.com/en/0.16.x/) - For password hashing generation and verification.
* [Jinja](https://jinja.palletsprojects.com/en/2.10.x/) - Allow data to be shared and processed before being turned in to content and sent back to the client.
* [Heroku](https://www.heroku.com/) - For hosting project.

### **Libraries**

* [Materialize](https://materializecss.com/) - An open source responsive front-end framework that offers slick material design.
* [Font Awesome](https://fontawesome.com/) - Offer icons for the project.
* [Google Fonts](https://fonts.google.com/) - To import **Playfair Display** font to use for this project
* [JQuery](https://jquery.com/) - For HTML DOM tree traversal and manipulation.

# **Testing**

### **Client Stories Testing Section** 

**All Recipes Page**
    
* Once the "All Recipes" link was clicked and entering the page, all the recipes are shown. A maximum of 8 recipes card profiles are shown with each row contain 4 recipes card profiles in tablet and laptop resolution. Each of the recipe card profiles shows the image, meal type, recipe name, diet type, and quantity of serving. There are no elements that are extending beyond the card profile which can yield an unprofessional sense toward the website. The pagination is shown at the bottom of the page. It will highlight the current page in a light pink color. Clicking on the second and subsequent pages do show the remaining recipe card profiles with all recipe details that are suppose to be shown. All pagination works smoothly without any broken page. The quantity of recipes created which shown in "All Recipes" page are matching to the MongoDB. 

* The "Log In" and "Sign Up" links at the top page is directing the user to the corresponding pages.   

* The search function is filtering the entered keyword and showing the correct result. For example, if "breakfast" is searched, all the recipes where the meal type is "Breakfast" will display to the page, and it does not matter if the keyword entered is in capital letter. Recipe name and diet type shows the corresponding results as well. An irrelevant keyword was entered to test the pop up message of stating "Ops! No results were found" is showing, which it does. User can click on the "All Recipe" navigation link at the top navigation bar to reset the searching.  

* For logged in user, the additional elements displayed are the total recipes quantity is shown at the top page. The button "CLICK ME TO ADD NEW RECIPE" is working which direct the user to "Add Recipe" page. 

**Recipe Details Page**

* The layout of the recipe image and recipe details are align properly. Ingredients and cooking method section contents are display in a list and a proper way. For logged in user, the "Edit" button direct the user to the "Edit Recipe" page, whereas the "Delete" button will delete the recipe. 

**Log In Page**

* Once the "Log In" button on the top navigation bar is clicked, the form is opened up. A valid username and password are entered and it logged the user in successfully and direct the user to their profile page. Further testing was done by entering an invalid either username or password, and log in action can't be performed. The "Register" link below works which direct the guest to the registration page.

**Register Page**

* The first thing to test is by entering the existing username and password which is already created and stored in the database. Once clicked on the sign up button, a flash message popped up stating "This username is already registered" as expected. Whereas, entering a new username and password will direct the new user to their profile page with a flash message showing registration succeed. If the guest entering the username with the character less than 4 and more than 20, the error will show. On the other hand, if the new password entered is less than 6 character and more than 20 character, the error will show. If neither username and password are entered, the error will show as well. The "Sign-In" link below the sign up button is working which direct the guest to the "Log In" page. 

**Profile Page**

* This is shown only for the logged in user. The total recipes quantity is shown at the top page. It shows the number of recipes created by the particular user. Once clicked onto each of the recipe detail pages, all the essential recipes details are shown. Both "Edit" and "Delete" buttons are shown. "CLICK ME TO ADD NEW RECIPE" button is shown on the top recipe page and it can direct the user to "Add Recipe" page to fill up the required recipe forms.   

**Profile Page**

* All the required input fields with empty input will lead to an error and the form won't be able to submit. The image url input is not essential, hence leaving it blank does not generate error. Yet if the user enter an invalid image url, it will display an error to request the user to enter an valid image url. If there is no image url input, the image placeholder will display, which in this case all is working fine. 

**Edit Page**

* Only the author will able to see the "Edit" and "Delete" button. If the link was edited and changed to the other user's username, nothing will show and it remains on the user's own profile page, indicates the defensive design works well. Furthermore, author can see the pre-populated fields on the form and able to apply changes easily. Once every required input fields are edited and submmitted, the recipe details are changed accordingly as well, proving the edit feature works perfectly.

**404 and 500 Errors**

* The url in the browser was changed to a dummy url to get a non-existing page, and the custom page 404 error page shows up. It proves the error-handler function works perfectly. The "Home" link on the page which direct the user back to the home page works as well. 

**Navbar / Footer Section**

* All links are tested to ensure they are pointing to the correct destination. 

**Bugs and Fixes**

* The landing image on the home page will go blank or missing occasionally. Hard reload the page few times will resolve the issue. 
* The ingredients and methods of cooking input field: If the user is copy the content from the other sources and paste to the input field, the result page will show all the text are displaying on the same row. Hence, hitting "enter" button after a sentence or paragraph will show the content in a proper alignment list. 

**Responsiveness**

* All the pages are tested for its responsivess by using Google Chrome's Developer Tools, from mobile resolution to desktop resolution. All the page elements display in a proper manner. The burger bar icon is shown when the website is in mobile and tablet resolution. 

### **Code Validation**

**Python**

* Python file was tested via [PEP8 Online](http://pep8online.com/) validator and the tested python code is PEP8 compliant.

# **Deployment**

### **Local Deployment**

* In order to run this project, the essentials tools stated below are required for installation beforehand:
    * An Integreted Development Environment(IDE)- [Gitpod](https://www.gitpod.io/) was used for this project.
    * [Git](https://git-scm.com/)
    * [MongoDB](https://www.mongodb.com/) (Database creation)
    * [PIP](https://pip.pypa.io/en/stable/installation/)
    * [Python](https://www.python.org/)

