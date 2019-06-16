from django.db import models
from django.utils import timezone
from .validators import validate_type_excel
from django.core.validators import FileExtensionValidator
import pandas as pd

class ExcelFile(models.Model):

    file_name = models.TextField(max_length=50, default='file')
    file_data = models.FileField(validators=[validate_type_excel])
    
    @property
    def file_data_as_dict(self):
        file_obj = self.file_data
        file_content = pd.read_excel(file_obj)
        return file_content
    
    @property
    def file_data_as_html(self):
        file_obj = self.file_data
        file_content = pd.read_excel(file_obj)
        df = pd.DataFrame(file_content)
        df = df.replace(r'\n','', regex=True)
        return_file = df.to_html()
        return return_file
    