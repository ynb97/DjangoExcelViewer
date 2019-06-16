from django.core.exceptions import ValidationError
from rest_framework import status

def validate_type_excel(value):
	if any(s in value.name for s in ['xlsx','xls']):
		return value
	else:
		raise ValidationError("Only excel files allowed !")