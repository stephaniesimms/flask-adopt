"""Adoption application."""
from flask import Flask, request, render_template, redirect, flash
from models import db, connect_db, Pet
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddPetForm

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

debug = DebugToolbarExtension(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()


@app.route("/")
def homepage():
    """List all pets on homepage"""
    show_pets = Pet.query.all()
    print("LOOK HERE", show_pets)
    return render_template("index.html", show_pets=show_pets)


@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Handler to validate add new pet form"""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data 
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data 
        notes = form.notes.data 
        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(pet)
        db.session.commit()
        return redirect("/")

    else:
        return render_template("add_pet_form.html", form=form)

@app.route("/<int:pet_id>")
def show_pet_info(pet_id):
    """Page to display pet info"""

    pet = Pet.query.get(pet_id)
    return render_template("", pet=pet)