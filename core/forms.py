from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=120, widget=forms.TextInput(attrs={'placeholder': 'Your name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Your email'}))
    subject = forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs={'placeholder': 'Subject (optional)'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Type your message here', 'rows': 5}))


class ConsultationForm(forms.Form):
    name = forms.CharField(max_length=120, widget=forms.TextInput(attrs={'placeholder': 'Your name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Your email'}))
    phone = forms.CharField(max_length=30, required=False, widget=forms.TextInput(attrs={'placeholder': 'Phone number'}))
    preferred_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    preferred_time = forms.TimeField(required=False, widget=forms.TimeInput(attrs={'type': 'time'}))
    message = forms.CharField(required=False, widget=forms.Textarea(attrs={'placeholder': 'Tell us what you need', 'rows': 5}))
