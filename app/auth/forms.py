from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired,Length,Email,Regexp,EqualTo
from wtforms import ValidationError
from ..models import User

class LoginForm(FlaskForm):
    email = StringField('电子邮箱',validators=[DataRequired(),Length(1,64),Email()])
    password = PasswordField('密码',validators=[DataRequired()])
    remember_me = BooleanField('记住我')
    submit = SubmitField('登入')

class RegistrationForm(FlaskForm):
    email = StringField('电子邮箱',validators=[DataRequired(),Length(1,64),Email()])
    username = StringField('用户名',validators=[DataRequired(),Length(1,64),
                                             Regexp('^[A-Za-z][A-Za-z0-9_.]*$',0,
                                                    '用户名须以字母开头且只包含数字、字母、下划线')])
    password = PasswordField('用户密码',validators=[DataRequired(),EqualTo('password2',message='两次密码必须输入相同')])
    password2 = PasswordField('再次输入密码',validators=[DataRequired()])
    submit = SubmitField('注册')

    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已经注册过了')

    def validate_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名已存在')


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('旧密码',validators=[DataRequired()])
    password = PasswordField('新密码',validators=[DataRequired(),EqualTo('password2',message='两次密码输入必须一致')])
    password2 = PasswordField('确认密码',validators=[DataRequired()])
    submit = SubmitField('更新密码')

class PasswordResetRequestForm(FlaskForm):
    email = StringField('邮箱',validators=[DataRequired(),Length(1,64),Email()])
    submit = SubmitField('重置密码')

class PasswordResetForm(FlaskForm):
    password = PasswordField('新密码',validators=[DataRequired(),EqualTo('password2',message='前后密码输入需一致')])
    password2 = PasswordField('确认密码',validators=[DataRequired()])
    submit = SubmitField('重置密码')

class ChangeEmailForm(FlaskForm):
    email = StringField('新邮箱', validators=[DataRequired(), Length(1, 64),
                                                 Email()])
    password = PasswordField('密码', validators=[DataRequired()])
    submit = SubmitField('更新邮箱')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data.lower()).first():
            raise ValidationError('邮箱已注册.')