#!/usr/bin/env python
#-*-coding:utf-8-*-
from  wtforms import * 
from  wtforms.validators import *
class UserForm(Form):
    u_id=TextField("u_id")
    user_name=TextField("user_name",validators=[Required()])
    user_password=PasswordField("user_password",validators=[Required()])
    user_desc=TextAreaField('user_desc')
    user_sex=SelectField('user_sex',choices=[('1',unicode('男','utf-8')),('2',unicode('女','utf-8'))])

    
    def __init__(self,operate_type,uid=0,*args,**kwargs):
        Form.__init__(self,*args,**kwargs)
        self.operate_type=operate_type
        self.uid=uid
        
    def validate(self):
        print 'abc'
        if not Form.validate(self):
            return False
        return True

