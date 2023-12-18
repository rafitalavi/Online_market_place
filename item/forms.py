from django  import forms

from .models import Item
FORM_INPUT_CLASSES = 'w-full px-5 py-4 rounded-xl border '
class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image', )
        widgets = {
            'category':forms.Select(attrs={'class' :FORM_INPUT_CLASSES}),
            'name':forms.TextInput(attrs={'class' :FORM_INPUT_CLASSES}),
            'description':forms.Textarea(attrs={'class' :FORM_INPUT_CLASSES}),
            'price':forms.TextInput(attrs={'class' :FORM_INPUT_CLASSES}),
            'image':forms.FileInput(attrs={'class' :FORM_INPUT_CLASSES}),
            }