from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, NumberRange


class AddPetForm(FlaskForm):
    """Form for adding pets"""

    name = StringField("Name", validators=[InputRequired()])
    species = SelectField("Species", choices=     
                        [('cat', 'CAT'), ('dog', 'DOG'), ('porcupine', 'PORCUPINE')],
                        validators=[InputRequired()])
                    
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])   
    age = IntegerField("Age", validators=[InputRequired(), NumberRange(min=0, max=30)])   
    notes = TextAreaField("Notes", validators=[Optional()])
      

class EditPetForm(FlaskForm):
    """Form for editing pets"""

    name = StringField("Name", validators=[InputRequired()])
    species = SelectField("Species", choices=[('cat', 'CAT'), ('dog', 'DOG'),
                                              ('porcupine', 'PORCUPINE')],
                          validators=[InputRequired()])

    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = IntegerField("Age", validators=[InputRequired(), NumberRange(min=0, max=30)])
    notes = TextAreaField("Notes", validators=[Optional()])
    available = BooleanField("Available", validators=[Optional()])
