from django import forms
from Publicacio.models import *


class TestForm (forms.ModelForm):
    class Meta:
        models = Test
        fields = "__all__"
