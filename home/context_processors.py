from .models import GeneralInfo

def general_info(request):
    return {
        'general_info': GeneralInfo.objects.first()
    }
