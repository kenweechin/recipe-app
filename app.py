import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_recipes")
def get_recipes():
    recipes = mongo.db.recipes.find()
    return render_template("index.html", recipes=recipes)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one({"username": request.form.get("username").lower()})

        if existing_user:
            flash("This username is already registered")
            return redirect(url_for("register"))
        
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("Registration Completed!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one({
            "username": request.form.get("username").lower()})

        if existing_user: 
            if check_password_hash(existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for("profile", username=session["user"]))
            else:
                flash("You've entered an invalid username and/or password")
                return redirect(url_for("login"))
        
        else:
            flash("Sorry, incorrect username and/or password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    username = mongo.db.users.find_one({"username": session["user"]})["username"]
    if session["user"]:
        recipes = list(mongo.db.recipes.find({"created_by": username}))
        my_recipes = mongo.db.recipes.find({"created_by": username})
        num_of_rec = my_recipes.count()
        return render_template("profile.html", username=username, recipes=recipes, my_recipes=my_recipes, num_of_rec=num_of_rec)
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    flash("You've have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():

    if request.method == "POST":
        recipe = {
            "recipe_name": request.form.get("recipe_name"),
            "recipe_description": request.form.get("recipe_description"),
            "category_name": request.form.get("category_name"),
            "diet_type": request.form.get("diet_type"),
            "recipe_serving": request.form.get("recipe_serving"),
            "recipe_preparation_time": request.form.get("recipe_preparation_time"),
            "recipe_cooking_time": request.form.get("recipe_cooking_time"),
            "recipe_ingredients": request.form.getlist("recipe_ingredients"),
            "recipe_method": request.form.getlist("recipe_method"),
            "image_url": request.form.get("image_url"),
            "created_by": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Successfully Added")
        return redirect(url_for("profile", username=session["user"]))

    categories = mongo.db.categories.find().sort("category_name", 1)
    dietery = mongo.db.dietery.find().sort("diet_type", 1)
    return render_template("add_recipe.html", categories=categories, dietery=dietery)


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        submit = {
            "recipe_name": request.form.get("recipe_name"),
            "recipe_description": request.form.get("recipe_description"),
            "category_name": request.form.get("category_name"),
            "diet_type": request.form.get("diet_type"),
            "recipe_serving": request.form.get("recipe_serving"),
            "recipe_preparation_time": request.form.get("recipe_preparation_time"),
            "recipe_cooking_time": request.form.get("recipe_cooking_time"),
            "recipe_ingredients": request.form.get("recipe_ingredients"),
            "recipe_method": request.form.get("recipe_method"),
            "image_url": request.form.get("image_url"),
            "created_by": session["user"]
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)},submit)
        flash("Recipe Successfully Updated")
        return redirect(url_for("recipe_details", recipe_id=recipe_id))

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    dietery = mongo.db.dietery.find().sort("diet_type", 1)
    return render_template("edit_recipe.html", recipe=recipe, categories=categories, dietery=dietery)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted")
    return redirect(url_for("get_recipes"))


@app.route('/recipe_details/<recipe_id>')
def recipe_details(recipe_id):
    selected_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("recipe_details.html", selected_recipe=selected_recipe)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)