from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, Optional

# Form for adding/editing members
class MemberForm(FlaskForm):
    # Personal Details
    first_names = StringField('First Names', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    id_number = StringField('ID Number', validators=[DataRequired(), Length(min=13, max=13)])
    gender = SelectField('Gender', choices=[('Male', 'Male'), ('Female', 'Female')], validators=[DataRequired()])
    language = SelectField('Language', choices=[('English', 'English'), ('Afrikaans', 'Afrikaans'), ('IsiZulu', 'IsiZulu'), ('isiXhosa', 'isiXhosa')], validators=[DataRequired()])

    # Contact Details
    mobile_number = StringField('Mobile Number', validators=[DataRequired(), Length(min=10, max=10)])
    alternative_number = StringField('Alternative Number', validators=[Length(min=10, max=10)])

    # Address Details
    ward = StringField('Ward', validators=[DataRequired(), Length(min=1, max=3)])
    region = StringField('Region', validators=[DataRequired()])
    municipality = StringField('Municipality', validators=[DataRequired()])
    house_number = IntegerField('House Number', validators=[DataRequired()])
    street_address = StringField('Street Address', validators=[DataRequired()])
    suburb = StringField('Suburb', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    province = StringField('Province', validators=[DataRequired()])
    postal_code = StringField('Postal Code', validators=[DataRequired(), Length(min=4, max=4)])

    # Voting Details
    iec_registered = SelectField('IEC Registered', choices=[('Yes', 'Yes'), ('No', 'No')], validators=[DataRequired()])
    pat_no = StringField('PAT No')
    voting_district = StringField('Voting District', validators=[DataRequired()])

    # Submit Button
    submit = SubmitField('Submit')

# Form for searching members by ID Number or PAT Number
class SearchForm(FlaskForm):
    id_number = StringField('ID Number', validators=[Optional(), Length(min=13, max=13)])
    pat_no = StringField('PAT No', validators=[Optional()])
    submit = SubmitField('Search')
