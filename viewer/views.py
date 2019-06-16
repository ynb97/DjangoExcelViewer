from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from .models import ExcelFile
from rest_framework.response import Response
from django.core.exceptions import ValidationError

@csrf_exempt
@api_view(['GET'])
def get_file_by_name(request,):
    if request.method == 'GET':
        _file_name = request.GET.get('name')
        _type = request.GET.get('type')
        print(_type)
        file_instance = ExcelFile.objects.get(file_name=_file_name)
        if _type == "dict":
            return Response(file_instance.file_data_as_dict)
        elif _type == "html":
            return Response(file_instance.file_data_as_html)


@csrf_exempt
@api_view(['POST'])
def send_file(request):
    if request.method == 'POST':
        file_obj = request.data['file']
        instance = ExcelFile(file_name=file_obj.name, file_data=file_obj)
        try:
            instance.full_clean()
        except ValidationError as e:
            return Response(e)
        else:
            instance.save()
            return Response({'status': 'success', 'detail':'File sent to server successfully.'})