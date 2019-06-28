from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SelectField
from wtforms.validators import InputRequired, Optional, URL, NumberRange


class AddPetForm(FlaskForm):
    """Form for adding pets"""

    name = StringField("Name", validators=[InputRequired()])
    species = SelectField("Species", choices=       
                    [('cat', 'CAT'), ('dog', 'DOG'), ('porcupine', 'PORCUPINE')],
                    validators=[InputRequired()])
                    
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])   
    age = IntegerField("Age", validators=[InputRequired(), NumberRange(0, 30)])   
    notes = TextAreaField("Notes", validators=[Optional()])
      

