from django.forms import Form, FileField, FileInput

class FileUploadForm(Form):
    file = FileField(label='Select a CSV file', widget=FileInput(attrs={'accept': '.csv'}))