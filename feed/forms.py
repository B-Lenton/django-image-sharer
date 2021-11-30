from django import forms

# creating a form for users to uploaded images with text
class PostForm(forms.Form):
    image = forms.FileField()
    text = forms.CharField(label="Description")
