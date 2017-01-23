from django.http import HttpResponse


def home(request):
    """
    Homepage for storn.co.

    :param request: HttpRequest object
    :return: HttpResonse object
    """
    return HttpResponse("Welcome to StornCo.  Get Some! Storn loves Karen!")
