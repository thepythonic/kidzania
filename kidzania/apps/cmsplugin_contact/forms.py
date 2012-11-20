from django import forms
from django.conf import settings
from django.utils.translation import ugettext as _

from cmsplugin_contact.nospam.forms import HoneyPotForm, RecaptchaForm, AkismetForm
  
class ContactForm(forms.Form):
    name = forms.CharField(label= _('Name'), widget=forms.TextInput(attrs={'placeholder': _('Name')}))
    email = forms.EmailField(label= _('Email'), widget=forms.TextInput(attrs={'placeholder': _('Email')}))
    mobile = forms.CharField(label= _('Mobile'), widget=forms.TextInput(attrs={'placeholder': _('Mobile')}))
    subject = forms.ChoiceField(choices=settings.SUBJECT_CHOICHES)
    content = forms.CharField(label= _('Message'), widget=forms.Textarea(attrs={'placeholder': _('Message')}))

  
class HoneyPotContactForm(HoneyPotForm):
    pass

class AkismetContactForm(AkismetForm):
    akismet_fields = {
        'comment_author_email': 'email',
        'comment_content': 'content'
    }
    akismet_api_key = None
    

class RecaptchaContactForm(RecaptchaForm):
    recaptcha_public_key = None
    recaptcha_private_key = None
    recaptcha_theme = None
