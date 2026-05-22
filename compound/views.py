from django.shortcuts import render

def calculate(request):
    context = {}

    if request.method == 'POST':
        try:
            P = float(request.POST.get('principal'))
            r = float(request.POST.get('rate')) / 100
            t = float(request.POST.get('years'))
            n = int(request.POST.get('frequency'))

            A = P * (1 + r / n) ** (n * t)
            interests = A - P

            context = {
                'principal': P,
                'rate': request.POST.get('rate'),
                'years': t,
                'frequency': n,
                'final_amount': round(A, 2),
                'interests': round(interests, 2),
            }
        except (ValueError, TypeError):
            context['error'] = "Veuillez entrer des valeurs numériques valides."

    return render(request, 'result.html', context)