from django import forms


class PostUploadForm(forms.Form):
    title = forms.CharField()
    photo = forms.ImageField()
    content = forms.CharField(widget=forms.Textarea())