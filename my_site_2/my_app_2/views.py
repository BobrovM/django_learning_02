from django.shortcuts import render


def example_view(request):
    # my_app_2/templates/my_app_2/example.html
    return render(request, 'my_app_2/example.html')


def variable_view(request):
    var = {'name': 'joe', 'surname': 'franklin', 'list': [1, 2, 3], 'user_logged_in': True}
    return render(request, 'my_app_2/variable.html', context=var)
