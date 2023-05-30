from django import forms


class EmailForm(forms.Form):
    email = forms.EmailField()
    name = forms.CharField(max_length=40)
    subject = forms.CharField(max_length=40)
    comment = forms.CharField(widget=forms.Textarea())
