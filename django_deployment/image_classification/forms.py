from django import forms
from .models import UploadImage

class UploadImageForm(forms.ModelForm):
    class Meta:
        model =UploadImage
        fields = ['image'] 
    
    def clean_image(self):
        img = self.cleaned_data.get('image')
        if img.image.format in ['JPG', 'JPEG']:
            return img
        else:
            raise forms.ValidationError('Upload a jpg image.')
