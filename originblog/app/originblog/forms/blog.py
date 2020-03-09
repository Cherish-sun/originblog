from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, \
    HiddenField
from wtforms.validators import DataRequired, Length, Email, URL, Optional


class CommentForm(FlaskForm):
    """定义评论表单"""
    author = StringField('姓名', validators=[DataRequired(), Length(1, 30)])
    email = StringField('邮箱', validators=[DataRequired(), Email(), Length(1, 254)])
    homepage = StringField('个人主页', validators=[Optional(), URL(), Length(0, 255)])
    content = TextAreaField('<span class="badge badge-info">markdown</span>',
                            validators=[DataRequired()])
    submit = SubmitField('提交')


class UserCommentForm(FlaskForm):
    """定义已登录用户的评论表单"""
    author = HiddenField('姓名', validators=[DataRequired(), Length(1, 30)])
    email = HiddenField('邮箱号', validators=[DataRequired(), Email(), Length(1, 254)])
    homepage = HiddenField('个人主页', validators=[Optional(), URL(), Length(0, 255)])
    content = TextAreaField('<small><span class="badge badge-info">markdown</span></small>',
                            validators=[DataRequired()])
    submit = SubmitField('提交')
