from django import forms

class LoginForm(forms.Form):

          username = forms.CharField(label="  Nom utilisateur  " ,widget=forms.TextInput(attrs={'class':'form-control'}))
          pwd = forms.CharField(label="  Mot de passe  ", widget=forms.PasswordInput(attrs={'class':'form-control'}))

class RegisterForm(forms.Form):
          
          username = forms.CharField(label="Nom utilisateur  ", widget=forms.TextInput(attrs={'class':'form-control'}))
          pwd = forms.CharField(label="  Mot de passe  ",widget=forms.PasswordInput(attrs={'class':'form-control'}))
          pwd_confirm = forms.CharField(label="  Mot de passe de confirmation  ",widget=forms.PasswordInput(attrs={'class':'form-control'}))


       