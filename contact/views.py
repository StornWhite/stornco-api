from django.http import HttpResponse


def index(request):
    """
    Renders the contact page index.

    :param request: HttpRequest object
    :return: HttpResponse object
    """
    return HttpResponse("Hello, world. You're at the contact index.")
