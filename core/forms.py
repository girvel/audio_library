from django.forms import ModelForm
from .models import Track


class TrackForm(ModelForm):
    class Meta:
        model = Track
        fields = ['file']

    def save(self, commit=True):
        instance = super(TrackForm, self).save(commit=False)
        instance.author, full_name \
            = self.cleaned_data['file'].name.split(' - ')
        instance.name = '.'.join(full_name.split('.')[:-1])

        if commit:
            instance.save()
        return instance
