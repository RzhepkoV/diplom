from django.shortcuts import render
from .forms import LinkForm
from .models import Link
from django.contrib import messages


def home(request):
    return render(request, 'sokrat/home.html')


def sokrat(request):
    post = request.POST.copy()
    post['user'] = request.user
    request.POST = post

    form = LinkForm(request.POST)
    all_links = Link.objects.all()
    if form.is_valid():
        link = form.cleaned_data.get('short')
        counts = Link.objects.filter(user=request.user, short=link).count()
        if counts == 0:
            form.save()
            form = LinkForm()
            # messages.success(request, 'Ссылка успешно добавлена')
            return render(request, 'sokrat/sokrat.html', {'form': form, 'links': all_links})
        else:
            form = LinkForm()
            messages.warning(request, 'Такая ссылка уже существует')
            return render(request, 'sokrat/sokrat.html', {'form': form, 'links': all_links})
    else:
        form = LinkForm()
        return render(request, 'sokrat/sokrat.html', {'form': form, 'links': all_links})
