from django import  forms
from django.contrib.auth.models import User
from account.models import UserProfile,UserInfo

#用户登录表单
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

#用户注册表单
class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "email")
    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password"] != cd["password2"]:
            raise forms.ValidationError("passwords do not match.")
        return cd["password2"]

#员工信息表单
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("employee_num",)

#用户信息表单
class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ("department", "company", "group", "address", "aboutme", 'phone')

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("email",)

