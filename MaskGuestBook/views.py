from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from .forms import GuestBookForm
from .models import GuestBook
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def postGuestBook(request):
    if request.method == 'POST':
        form = GuestBookForm(request.POST)
        if form.is_valid():
            form.save()
            # return render(
            #     request,
            #     'MaskGuestBook/index.html',
            #     {'form': form}
            # )
            return redirect('index')
    else:
        form = GuestBookForm()
        return render(
            request,
            'MaskGuestBook/GuestBook.html',
            {'form': form}
        )

def index(request):
    guests = {'guests':GuestBook.objects.all()}
    return render(request, 'MaskGuestBook/list.html', guests)
    # return render(
    #     request,
    #     'MaskGuestBook/index.html',
    #     {}
    # )
    # return HttpResponse(str)

def keyboard(request):
    return JsonResponse(
        {
            'type': 'text'
        }
    )

@csrf_exempt
def message(request):
    answer = ((request.body).decode('utf8'))
    return_json_str = json.loads(answer)
    return_str = return_json_str['userRequest']['utterance']

    if return_str == '테스트':
        return JsonResponse({
            'version':"2.0",
            'template':{
                'outputs':[{
                    'simpleText': {
                        'text': '테스트 성공'
                    }
                }],
                'quickReplies':[{
                    'label': 'first',
                    'action': 'message',
                    'messageText': '처음으로'
                }]
            }
        })


