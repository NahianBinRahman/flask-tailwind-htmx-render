from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length

# Define the ContactForm class
class ContactForm(FlaskForm):
    # StringField is for short text inputs (like name)
    # validators check the data (DataRequired means it can't be empty)
    name = StringField('Full Name', validators=[DataRequired(), Length(min=2, max=50)])
    
    # Email field ensures the input looks like an email
    email = StringField('Email Address', validators=[DataRequired(), Email()])
    
    # TextAreaField is for long text (like the message)
    message = TextAreaField('Message', validators=[DataRequired(), Length(max=500)])
    
    # SubmitField creates the submit button
    submit = SubmitField('Send Message')