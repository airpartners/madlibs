# imports
from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired

# class for initial form (choosing between wind direction and time of day)
class Entry1Form(FlaskForm):
    entry1 = SelectField('Search by', choices=[('wind', 'wind direction'), ('time', 'time of day')])
    submit = SubmitField('Next')

# class for form when searching by wind direction
class WindForm(FlaskForm):
    entry2 = SelectField('When wind is blowing _____,', choices=[('N', 'N'),
                                                ('NE', 'NE'),
                                                ('E', 'E'),
                                                ('SE', 'SE'),
                                                ('S', 'S'),
                                                ('SW', 'SW'),
                                                ('W', 'W'),
                                                ('NW', 'NW')])
    pollutant = SelectField('the concentration of _____ is...', choices=[('co', 'co'),
                                                ('no', 'no'),
                                                ('no2', 'no2'),
                                                ('o3', 'o3'),
                                                ('pm1', 'pm1'),
                                                ('pm25', 'pm25'),
                                                ('pm10', 'pm10'),
                                                ('co2', 'co2'),
                                                ('bin0', 'bin0'),
                                                ('bin1', 'bin1'),
                                                ('bin2', 'bin2')])
    submit = SubmitField('Search')

# class for form when searching by time of day
class TimeForm(FlaskForm):
    entry2 = SelectField('When time of day is _____,', choices=[('early morning', 'early morning'),
                                                ('morning', 'morning'),
                                                ('midday', 'midday'),
                                                ('afternoon', 'afternoon'),
                                                ('evening', 'evening'),
                                                ('night', 'night'),
                                                ('late night', 'late night')])
    pollutant = SelectField('the concentration of _____ is...', choices=[('co', 'co'),
                                                ('no', 'no'),
                                                ('no2', 'no2'),
                                                ('o3', 'o3'),
                                                ('pm1', 'pm1'),
                                                ('pm25', 'pm25'),
                                                ('pm10', 'pm10'),
                                                ('co2', 'co2'),
                                                ('bin0', 'bin0'),
                                                ('bin1', 'bin1'),
                                                ('bin2', 'bin2')])
    submit = SubmitField('Search')