import xmltodict as xmltodict
from django.http import JsonResponse
from django.shortcuts import render


def upload_page(request):
    if request.method == 'POST':
        # Converting the submitted XML file into a JSON object.
        data_dict = xmltodict.parse(request.FILES['file'].read())
        return JsonResponse(data_dict)

    return render(request, "upload_page.html")
