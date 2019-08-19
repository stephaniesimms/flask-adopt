"""Pet adoption application."""
from flask import Flask, render_template, redirect, flash
import requests
from models import db, connect_db, Pet
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddPetForm, EditPetForm
from secret import TOKEN 


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
    show_pets = Pet.query.order_by("id").all()
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
    """Show page to display pet info"""
    pet = Pet.query.get(pet_id)
    return render_template("pet_info.html", pet=pet)


@app.route("/<int:pet_id>/edit", methods=["GET", "POST"])
def edit_pet_form(pet_id):
    """Edit the pet and update the pet's info"""
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        
        db.session.add(pet)
        db.session.commit()
        
        flash(f"{pet.name} was updated")
        return redirect("/")    
    else:
        return render_template("edit_pet_form.html", form=form)


@app.route("/")
def random_pet():
    """get a random pet from the petfinder API"""
    resp = requests.get("https://api.petfinder.com/v2/animals?type=dog&page=2",
                        headers={"Authorization": f"Bearer {TOKEN}"})
    pet_data = resp.json()['animals'][0]['photos'][0]['full']
    print("PETTTT",pet_data)
    import pdb; pdb.set_trace()
    return render_template("index.html", pet_data=pet_data)
