from .models import *
# from users.models import CustomUser
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Submit, Row, Column
# from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.forms import Select
from django.forms.widgets import Textarea
# import datetime
# from django.db.models.functions import Concat, Substr
# from django.db.models import F, Value, CharField
# from datetime import datetime
# from django.core.validators import FileExtensionValidator

class RegistrationForm(forms.Form):
    type_choices = (('', 'Select'), ('AutoLoan_NOC', 'AutoLoan_NOC'),('AutoLoanManarah_NOC', 'AutoLoanManarah_NOC'),('PersonalLoanManarah_NOC', 'PersonalLoanManarah_NOC'), ('PersonalLoan_NOC', 'PersonalLoan_NOC'),
                    ('AutoLoan_BA', 'AutoLoan_BA'), 
                     ('PersonalLoan_BA', 'PersonalLoan_BA'),('AutoLoanManarah_BA', 'AutoLoanManarah_BA'),('PersonalLoanManarah_BA', 'PersonalLoanManarah_BA'),
                     )
    type = forms.ChoiceField(required=True, choices=type_choices,label='Letter Type')

    date = forms.Date