# App Form
# Flask From which holds contains the data.
# @author: Dr. Benjamin M. Abdel-Karim
# @since: 2022-01-09
# @version: 2021-01-09

from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TextAreaField, SelectField
from wtforms.validators import InputRequired, Email, Length
from flask_wtf.file import FileField, FileAllowed, FileRequired


class CForm_upload(FlaskForm):
    # Upload File
    upload = FileField('Deine Daten (Format: .jpeg)', validators=[InputRequired()])

