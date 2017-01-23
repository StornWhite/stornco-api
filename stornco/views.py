from django.http import HttpResponse


def home(request):
    """
    Homepage for storn.co.

    :param request: HttpRequest object
    :return: HttpResonse object
    """
    return HttpResponse("<h1>Welcome to StornCo.</h1>Get yourself some Storn!")
