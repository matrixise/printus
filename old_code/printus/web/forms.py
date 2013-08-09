from flask.ext.babel import _, lazy_gettext

from flask.ext.wtf import (Form, 
                           TextField, 
                           BooleanField,
                           IntegerField,
                           HiddenField,
                           Length,
                           Email,
                           SelectField,
                           DateField,
                           DateTimeField,
                           SubmitField,
                           PasswordField,
                           EqualTo,
                           FileField,
                           Required, 
                           TextAreaField)

class UserForm(Form):
    name = TextField(lazy_gettext(u'Full name'), validators=[Required(), Length(min=4, max=80)])

    username = TextField(lazy_gettext(u'Username'),
                         validators=[Required(),
                                     Length(min=4, max=32)])
    password = PasswordField(lazy_gettext(u'Password'),
                             validators=[Required(), Length(min=5, max=64)])
    # password_confirmation = PasswordField(lazy_gettext(u'Confirm Password'),
    #                                       validators=[
    #                                           Required(),
    #                                           EqualTo('password', message=_(u'The password must match'))
    #                                       ])
    email = TextField(lazy_gettext(u'Email'),
                      validators=[
                          Required(),
                          Email(),
                          Length(min=6, max=128),
                      ])
    # email_confirmation = TextField(lazy_gettext(u'Confirm Email'),
    #                                validators=[
    #                                    Required(),
    #                                    Email(),
    #                                    EqualTo('email', message=_(u'The email must match')),
    #                                ])
    next = HiddenField()
    submit = SubmitField(lazy_gettext(u'Join !'))

class ContactForm(Form):
    title = TextField(lazy_gettext(u'Subject'), validators=[Required(), Length(max=128)])
    description = TextAreaField(lazy_gettext(u'Description'), validators=[Required()])
    submit = SubmitField(lazy_gettext(u'Send !'))


class SignupForm(Form):
    name = TextField(lazy_gettext(u'Full name'), validators=[Required(), Length(min=4, max=80)])
    password = PasswordField(lazy_gettext(u'Password'), validators=[Required(), Length(min=5, max=64)])
    email = TextField(lazy_gettext(u'Email'), validators=[Required(),Email(),Length(min=6, max=128),])
    next = HiddenField()
    submit = SubmitField(lazy_gettext(u'Subscribe to PrintUs'))

class LoginForm(Form):
  username = TextField(lazy_gettext(u'Username'),validators=[Required(), Length(min=4, max=32)])
  password = PasswordField(lazy_gettext(u'Password'), validators=[Required(), Length(min=5, max=64)])

  next = HiddenField()
  submit = SubmitField(lazy_gettext(u'Login'))

class ReportForm(Form):
    name = TextField(lazy_gettext(u'Name'),
                     validators=[
                         Required(),
                         Length(min=4, max=32)
                     ])
    description = TextAreaField(lazy_gettext(u'Description'))
    report_file = FileField(lazy_gettext(u'File'))
    submit = SubmitField(lazy_gettext(u'Submit'))

