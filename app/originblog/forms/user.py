from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Length, Email, URL, Optional, EqualTo
from flask_login import current_user

from originblog.models import User


class ChangePasswordForm(FlaskForm):
    """定义修改密码表单"""
    current_password = PasswordField('旧密码：', validators=[DataRequired(), Length(6, 128)])
    password = PasswordField('新密码：', validators=[DataRequired(), Length(6, 128), EqualTo('password2')])
    password2 = PasswordField('确认密码：', validators=[DataRequired()])
    submit = SubmitField('提交')


class ProfileForm(FlaskForm):
    """定义修改个人资料表单"""
    name = StringField('用户名：', validators=[Length(1, 128)])
    bio = StringField('自我介绍：', validators=[Optional(), Length(0, 200)])
    homepage = StringField('简书：', validators=[Optional(), URL()])
    # weibo = StringField('Weibo', validators=[Optional(), URL()])
    # weixin = StringField('Weixin', validators=[Optional(), URL()])
    github = StringField('GitHub：', validators=[Optional(), URL()])
    submit = SubmitField('提交')


class ChangeEmailForm(FlaskForm):
    email = StringField('新邮箱：', validators=[DataRequired(), Length(1, 254), Email()])
    submit = SubmitField('提交')

    def validate_email(self, field):
        """验证email是否已注新邮箱册"""
        if User.objects.filter(email=field.data.lower()).first():
            raise ValidationError('该邮箱已被注册')


class DeleteAccountForm(FlaskForm):
    username = StringField('用户名：', validators=[DataRequired(), Length(1, 20)],
                           render_kw={'placeholder':'请输入您的用户名来确认.'})
    submit = SubmitField('提交')

    def validate_username(self, field):
        if field.data != current_user.username:
            raise ValidationError('Wrong username.')
