from django import forms
from stories.models import Contact
from stories.validators import validate_gmail_account

class ContactForm(forms.ModelForm):
    email = forms.EmailField(validators=[validate_gmail_account, ], max_length=40, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your Email'
    }))
    # name = forms.CharField(widget=)
    # message = forms.CharField(widget=)

    # def clean(self):
    #     cleaned_data = self.cleaned_data
    #     if not cleaned_data['email'].endswith('@gmail.com'):
    #         raise forms.ValidationError('Email gmail account olmalidir')
    #     return super().clean()
    
    # def clean_email(self):
    #     cleaned_data = self.cleaned_data
    #     if not cleaned_data['email'].endswith('@gmail.com'):
    #         raise forms.ValidationError('Email gmail account olmalidir')
    #     return True


    class Meta:
        model = Contact
        fields = (
            'name',
            'email',
            'subject',
            'message'
        )
        widgets = {
            'name': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Your name'
            }),
            'message': forms.Textarea(attrs={
                'rows': 10,
                'class': 'form-control',
                'placeholder': 'Message'
            }),
            'subject': forms.Select(attrs={
                'class': 'form-control',
            })
        }