from django.shortcuts import render, redirect
from .forms import AnketaForm
from .models import Score


def main(request):
    return render(request, 'main/Main.html')


def anketa(request):
    if request.method == 'POST':
        form = AnketaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('test')

    else:
        form = AnketaForm()
        context = {
            'form': form,
        }
        return render(request, 'main/Anketa.html', context)


def test(request):
    return render(request, 'main/Test.html')


def update_counter(request):
    if request.method == 'POST':
        form = Score.objects.get()
        form.PD = request.POST['count1']
        form.AS = request.POST['count2']
        form.SL = request.POST['count3']
        form.NO = request.POST['count4']
        form.K = request.POST['count5']
        form.save()
    return redirect('main')
