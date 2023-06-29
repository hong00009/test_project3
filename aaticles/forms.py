from django import forms
from .models import AAticle

class AAticleForm(forms.ModelForm):
    class Meta:
        model = AAticle
        fields = '__all__'