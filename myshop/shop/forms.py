from django import forms


class AddPostEmail(forms.Form):
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    subject = forms.CharField(max_length=150, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 7, 'cols': 30, 'class': 'form-control'}))
