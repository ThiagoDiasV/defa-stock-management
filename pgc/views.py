from django.shortcuts import render


def pgc(request):
    return render(request, "pgc/pgc.html")
