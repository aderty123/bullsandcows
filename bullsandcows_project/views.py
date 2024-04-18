from django.shortcuts import render
from .logic import Check

# Это ваша главная страница
def index(request):
    return render(request, 'index.html')

# Представление для обработки хода игры
def play(request):
    if request.method == 'POST':
        secret_numbers = [int(num) for num in request.POST.getlist('secret_number')]
        guess_numbers = [int(num) for num in request.POST.getlist('guess_number')]
        
        checker = Check()
        result = checker.guess_numbers(secret_numbers, guess_numbers)
        
        return render(request, 'result.html', {'result': result})
    else:
        return render(request, 'play.html')

# Другие представления, если нужно
