from django.shortcuts import render


def greeting(request):
    context = {}
    context['greeting'] = 'Hiya'
    context['week'] = {'Mon', 'Tue', 'Wed', 'Thurs', 'Fri'}
    return render(request, 'greeting.html', context)
