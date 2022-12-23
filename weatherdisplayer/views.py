from django.shortcuts import render
# from bs4 import BeautifulSoup
from django.http import HttpResponse, HttpResponseRedirect



# Create your views here.
def get_html_content(city):
    import requests
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    city = city.replace(' ','+')
    html_content = session.get(f'https://www.google.com/search?q=weather+in+{city}').text
    return html_content

def home(request):
    if 'city' in request.GET:
        city = request.GET.get('city')
        html_content = get_html_content(city)
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')
        result = dict()
        try:
            # extract regionBNeawe s3v9rd AP7Wnd
            result['region'] = soup.find("span", attrs={"class": "BNeawe tAd8D AP7Wnd"}).text
            # extract temperature now
            result['temp_now'] = soup.find("div", attrs={"class": "BNeawe iBp4i AP7Wnd"}).text
            # get the day, hour and actual weather
            result['dayhour'], result['weather_now'] = soup.find("div", attrs={"class": "BNeawe tAd8D AP7Wnd"}).text.split(
                '\n')
            return render(request, 'weatherdisplayer/home.html',{'result': result})
        except:
            return HttpResponse("please check the city name")
    return render(request, 'weatherdisplayer/home.html')
