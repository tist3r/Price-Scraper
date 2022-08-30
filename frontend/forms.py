from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField
from wtforms.validators import DataRequired

class ScraperForm(FlaskForm):
    name = StringField('name of scraper', validators=[DataRequired()])
    url = StringField("url", validators=[DataRequired()])
    element = StringField('html tag', validators=[DataRequired()])
    price_limit = DecimalField('Price Limit')
    submit = SubmitField('Submit')