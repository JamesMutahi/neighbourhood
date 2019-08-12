from django import forms
from .models import Neighbourhood


class HoodForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Name'].widget = forms.TextInput()
        self.fields['police'].widget = forms.TextInput()
        self.fields['health'].widget = forms.TextInput()

    class Meta:
        model = Neighbourhood
        exclude = ('admin',)
