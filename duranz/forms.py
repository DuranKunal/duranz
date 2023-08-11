from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email
    
    
class ProjectRequestForm(FlaskForm):
    name = StringField('Enter Your/Company Name', validators=[DataRequired()])
    email = StringField('Enter Email ID', validators=[Email(), DataRequired()])
    project = StringField('Type of Project', validators=[DataRequired()])
    detail = TextAreaField('Details of the Project', validators=[DataRequired()])
    submit = SubmitField('Request')

