from django.shortcuts import render
from django.http import HttpResponse

def main(request):
    '''
    Show 'Hello World!' in the main page
    '''
    return HttpResponse('Hello World!')


