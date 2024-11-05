from wtforms import StringField,Form,validators,IntegerRangeField,PasswordField

class InputForm(Form):
    Username = StringField(label="Username: ",
        default='',
        validators=[validators.InputRequired()])
    Password = StringField(label="Password: ",
        default='',
        validators=[validators.InputRequired()])
    Client_ID = StringField(label="Client ID: ",
        default='',
        validators=[validators.InputRequired()])
    Client_Secret = StringField(label="Client Secret: ",
        default='',
        validators=[validators.InputRequired()])
    Query = StringField(label="Query: ",
        default='',
        validators=[validators.InputRequired()])
    NoOfQuery = IntegerRangeField(label="No. of Queries (max=100): ",
        default='',
        validators=[validators.InputRequired(),])