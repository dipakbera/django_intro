# I have created this file -- DIPAK
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
    #return HttpResponse('HOME')

def contact(request):
    params={'contact':'My gmail:ghtyu@gmail.com\nMy phone:0987655432'}
    return render(request,'contact.html',params)

def myinterest(request):
    return HttpResponse('''<h1>Dipak's Favourite</h1>(Django Magic) <br><br>Youtube:<a href="https://www.youtube.com/channel/UCAugp8-22UiWTb_1HqHCCvw?view_as=subscriber">My Youtube Channel</a><br
    >My Facebook Profile:<a href="https://www.facebook.com/profile.php?id=100051050375182">Facebook </a><br
    >My Linked IN:<a href="https://www.linkedin.com/in/dipakapman/">LinkedIN </a><br
    >My Quora:<a href = "https://www.quora.com/profile/Dipak-Bera-13">Quora Log In <a/>''')

def tohome(request):
    return HttpResponse("space remover <a href='/'>back</a>")

def analyze(request):
    analyzed=request.GET.get('text','default')
    raw=analyzed.split('\n')
    removepunc=request.GET.get('removepunc','off')
    capitalizefirst = request.GET.get('capitalizefirst', 'off')
    extraspaceremover= request.GET.get('extraspaceremover', 'off')
    if (removepunc == 'off' and extraspaceremover == 'off' and capitalizefirst == 'off'):
        params = {'purpose': 'Nothing!ERROR!', 'analyzed_text': 'something wrong,please try again.'}
        return render(request, 'analyze.html', params)
    if removepunc=='on':
       bl=''
       punctuations='''!@#$%^&*()_'";:,.<>[]{}\|?/'''
       for char in analyzed:
           if char not in punctuations:
              bl+=char
       analyzed=bl

    if extraspaceremover == 'on':
        l=[]
        for d in analyzed.split('\n'):
          dj = ''
          for i in range(len(d)-1):
            if d[i] != ' ':
                dj += d[i]
            elif d[i] == ' ' and d[i + 1] != ' ':
                dj += d[i]
          if d[-1]!='':
              dj+=d[-1]
          dj=list(dj)
          for char in dj:
              if char==' ':
                 dj.remove(char)
              else:
                  break
          dj=''.join(dj)
          l.append(dj)
        analyzed='\n'.join(l)

    if capitalizefirst == 'on':
        l=[]
        for ele in analyzed.split('\n'):
            cap = ele[0].upper() + ele[1:]
            l.append(cap)
        analyzed='\n'.join(l)

    params = {'purpose': '(after analyzing)-', 'analyzed_text': analyzed}
    return render(request, 'analyze.html', params)



