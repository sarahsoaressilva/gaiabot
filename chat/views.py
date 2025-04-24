from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .logic import obter_resposta

@csrf_exempt
def enviar_mensagem(request):
    if request.method == 'POST':
        mensagem = request.POST.get('mensagem')
        if mensagem:
            resposta = obter_resposta(mensagem)
            return JsonResponse({'resposta': resposta})
        else:
            return JsonResponse({'erro': 'Nenhuma mensagem recebida.'}, status=400)
    else:
        return JsonResponse({'erro': 'Método não permitido.'}, status=405)

def chat_view(request):
    return render(request, 'chat.html')