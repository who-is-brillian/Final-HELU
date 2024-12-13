from django import forms
from .models import Topic

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['title', 'description', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 50}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image and image.size > 5 * 1024 * 1024:  # Batas ukuran file 5MB
            raise forms.ValidationError("Ukuran gambar tidak boleh lebih dari 5MB.")
        return image
