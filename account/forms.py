from django import forms




class login_form(forms.Form):
    username = forms.CharField(max_length=50, required=True,label='Username', widget= forms.TextInput({"placeholder":"Username daxil edin..."}))
    password = forms.CharField(max_length=50, required=True, label='Password', widget=forms.PasswordInput({"placeholder":"Password daxil edin..."}))