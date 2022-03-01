import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
import math
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


'''
HOME PAGE
'''


@app.route("/")
@app.route("/get_recipes")
def get_recipes():
    recipes = mongo.db.recipes.find()
    return render_template("index.html", recipes=recipes, title="Home")


'''
ROUTES FOR USERS
'''


# Register
@app.route("/register", methods=["GET", "POST"])
def register():
    '''
    Create a new account
    '''
    # check if the username is existing in the database
    if request.method == "POST":
        existing_user = mongo.db.users.find_one({"username":
                                                request.form.get
                                                ("username").lower()})
        # check if the user has already registered
        if existing_user:
            flash("This username is already registered")
            return redirect(url_for("register"))
        # hashing the entered password
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("Registration Completed!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html", title="Register")


# Login
@app.route("/login", methods=["GET", "POST"])
def login():
    '''
    Check if the username and password entered are valid, if so
    it will add the user to the session.
    '''
    if request.method == "POST":
        existing_user = mongo.db.users.find_one({
            "username": request.form.get("username").lower()})
        # Check if the user enters a valid username and the password
        if existing_user:
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                # Add user to session if password is matching to the DB
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for("profile", username=session["user"]))
            else:
                # If user entered an invalid username and/or password
                flash("You've entered an invalid username and/or password")
                return redirect(url_for("login"))
        # If un-registered user entered an invalid username and/or password
        else:
            flash("Sorry, incorrect username and/or password")
            return redirect(url_for("login"))

    return render_template("login.html", title="LogIn")


# Registered User's Profile
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    # Identify the user in session and display the recipes created by the user
    if session["user"]:
        recipes = list(mongo.db.recipes.find({"created_by": username}))
        my_recipes = mongo.db.recipes.find({"created_by": username})
        # Count the number of recipes created by the user
        num_of_rec = my_recipes.count()
        return render_template("profile.html", username=username,
                               recipes=recipes, my_recipes=my_recipes,
                               num_of_rec=num_of_rec, title="Profile")
    return redirect(url_for("login"))


# Logout
@app.route("/logout")
def logout():
    '''
    Log out the user and redirect to the login page.
    '''
    flash("You've have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


'''
ROUTES FOR RECIPES
'''


@app.route("/search", methods=["GET", "POST"])
def search():
    '''
    A function that find the recipes on a query.
    User input is the query.
    User's list of recipes is then rendered on search.html page
    '''
    query = request.form.get("query")
    # find instances of the keyword in recipe_name, category_name, or diet_type
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("all_recipes.html", recipes=recipes, title="Search")


@app.route('/all_recipes')
def all_recipes():
    '''
    Shows all the recipes created by different users.
    This page can be browsed by either registered/logged in
    user or unregistered/logged out user.
    '''
    # CREDITS: the pagination's idea implemented here is derived and modified
    # from Spencer Barriball's project

    # number of recipes show per page
    recipe_per_page = 8
    page = int(request.args.get('page', 1))

    # get total of all the recipes in db
    recipes = mongo.db.recipes.find().skip((
        page - 1)*recipe_per_page).limit(recipe_per_page)
    num_of_all_rec = recipes.count()
    pages = range(1, int(math.ceil(num_of_all_rec / recipe_per_page)) + 1)

    return render_template("all_recipes.html", recipes=recipes,
                           num_of_all_rec=num_of_all_rec,
                           pages=pages, page=page, title="All Recipes")


# Insert Recipe
@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    '''
    Create feature. Logged in user can view and create new recipes form
    '''
    if request.method == "POST":
        # record the recipe forms created by the user
        recipe = {
            "recipe_name": request.form.get("recipe_name"),
            "recipe_description": request.form.get("recipe_description"),
            "category_name": request.form.get("category_name"),
            "diet_type": request.form.get("diet_type"),
            "recipe_serving": request.form.get("recipe_serving"),
            "recipe_preparation_time": request.form.get(
                "recipe_preparation_time"),
            "recipe_cooking_time": request.form.get("recipe_cooking_time"),
            "recipe_ingredients": request.form.getlist("recipe_ingredients"),
            "recipe_method": request.form.getlist("recipe_method"),
            "image_url": request.form.get("image_url"),
            "created_by": session["user"]
        }
        # insert the dictionary into the database
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Successfully Added")
        return redirect(url_for("profile", username=session["user"]))

    categories = mongo.db.categories.find().sort("category_name", 1)
    dietery = mongo.db.dietery.find().sort("diet_type", 1)
    return render_template("add_recipe.html", categories=categories,
                           dietery=dietery, title="Add Recipe")


# Edit Recipe
@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    '''
    Update feature. Allows user to update the existing recipes form.
    '''
    if request.method == "POST":
        submit = {
            "recipe_name": request.form.get("recipe_name"),
            "recipe_description": request.form.get("recipe_description"),
            "category_name": request.form.get("category_name"),
            "diet_type": request.form.get("diet_type"),
            "recipe_serving": request.form.get("recipe_serving"),
            "recipe_preparation_time": request.form.get(
                                        "recipe_preparation_time"),
            "recipe_cooking_time": request.form.get("recipe_cooking_time"),
            "recipe_ingredients": request.form.get("recipe_ingredients"),
            "recipe_method": request.form.get("recipe_method"),
            "image_url": request.form.get("image_url"),
            "created_by": session["user"]
        }
        # update the dictionary in the database
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit)
        flash("Recipe Successfully Updated")
        return redirect(url_for("recipe_details", recipe_id=recipe_id))

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    dietery = mongo.db.dietery.find().sort("diet_type", 1)
    return render_template("edit_recipe.html", recipe=recipe,
                           categories=categories, dietery=dietery,
                           title="Edit Recipe")


# Delete Recipe
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    '''
    Delete feature. Delete the selected recipe from the database.
    '''
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted")
    return redirect(url_for("get_recipes"))


# Page shows the recipe details
@app.route('/recipe_details/<recipe_id>')
def recipe_details(recipe_id):
    selected_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("recipe_details.html",
                           selected_recipe=selected_recipe,
                           title="Recipe Details")


@app.errorhandler(404)
def error_404(error):
    '''
    Handle 404 error
    '''
    return render_template('errors/404.html', error=True,
                           title="Page Not Found"), 404


@app.errorhandler(500)
def error_500(error):
    '''
    Handle internal server error
    '''
    return render_template('errors/500.html', error=True,
                           title="Internal Server Error"), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
