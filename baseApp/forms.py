from django import forms
from .models import Upload_mutiple_files_model
from django.forms import ValidationError
from django.core.exceptions import ValidationError




class upload_file_form(forms.ModelForm):
    # 83886080
    file = forms.FileField(label='')

    def clean_file(self, *args, **kwargs):
        file = self.cleaned_data.get('file')
        limit = 2 * 1024 * 1024
        if file.size > limit:
            raise forms.ValidationError("")
        else:
            return file

    class Meta:
        model = Upload_mutiple_files_model
        fields = "__all__"




# class ContactForm(forms.Form):
#     # Everything as before.
#     ...
#
#     def clean_recipients(self):
#         data = self.cleaned_data['recipients']
#         if "fred@example.com" not in data:
#             raise forms.ValidationError("You have forgotten about Fred!")
#
#         # Always return a value to use as the new cleaned data, even if
#         # this method didn't change it.
#         return data