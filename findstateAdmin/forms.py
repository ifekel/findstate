from django import forms
from app.models import Property

class AgentForm(forms.ModelForm):
    name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'name'}))
    image = forms.ImageField(required=True, widget=forms.FileInput(attrs={'class': 'form-control', 'id': 'image'}))
    properties = forms.ModelMultipleChoiceField(queryset=Property.objects.all(), widget=forms.CheckboxSelectMultiple(attrs={'id': 'properties'}))

    class Meta:
        model = Property
        fields = ['name', 'image', 'properties']