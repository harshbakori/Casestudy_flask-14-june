from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,TextAreaField,SelectField,SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError,NumberRange
# from application.models import User

class RegisterForm(FlaskForm):

    state_pairs=[("New York","New York"),("Texas","Texas"),("Utah","Utah"),("Virginia","Virginia"),("Missouri","Missouri"),("Vermont","Vermont")]
    city_pairs=[("New York","New York"),("Texas","Texas"),("Utah","Utah"),("Virginia","Virginia"),("Missouri","Missouri"),("Vermont","Vermont")]

    SSN_ID = StringField("SSN ID", validators=[DataRequired(),Length(min=2,max=55)])
    Cust_Name = StringField("Customer Name", validators=[DataRequired(),Length(min=2,max=55)])
    Cust_Age = IntegerField("Customer Age",validators=[DataRequired(),NumberRange(min=18, max=80)])
    address = TextAreaField("Address", validators=[DataRequired(),Length(min=2,max=55)])
    State = SelectField("State",validators=[DataRequired()],choices=state_pairs)
    City = SelectField("State",validators=[DataRequired()],choices=city_pairs)
    submit = SubmitField("Submit")
    
class DeleteAccount(FlaskForm):
    
    Account_ID = StringField("Account Id", validators=[DataRequired(),Length(min=2,max=55)])
    ACC_Type = StringField("Account Type", validators=[DataRequired(),Length(min=2,max=55)])
    submit = SubmitField("Delete Account")
    
