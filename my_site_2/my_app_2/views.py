from django.shortcuts import render


def example_view(request):
    # my_app_2/templates/my_app_2/example.html
    return render(request, 'my_app_2/example.html')


def variable_view(request):
    var = {'name': 'joe', 'surname': 'franklin', 'list': [1, 2, 3], 'dict': {'inside_key': 'inside_value'}}
    return render(request, 'my_app_2/variable.html', context=var)
