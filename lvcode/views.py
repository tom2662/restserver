# views.py
from rest_framework import viewsets
from django.http import JsonResponse
from .serializers import HeroSerializer
from .models import Hero
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer


#logic function
@api_view(['POST','GET'])
@permission_classes([IsAuthenticated])
def lvcalc(request):
    if request.method == 'POST':
        code = request.data.get('code','No Data')

        # options = Options()
        # options.add_argument('--headless')
        # options.add_argument('--disable-gpu') 
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome( '/usr/lib/chromium-browser/chromedriver', options=chrome_options)
        driver.get("https://www.lvcodecalc.com/")
        driver.find_element_by_css_selector("input[type='text']").send_keys(code)
        driver.find_element_by_css_selector("input[type='submit']").click()
        result = driver.find_element_by_css_selector(".result > div:nth-child(1) > p:nth-child(2)").text
        #closedriver
        driver.close()
        driver.quit()
        return JsonResponse(result, safe=False)

    elif request.method == 'GET':
        code = 'Hello World'
        return JsonResponse(code, safe=False)
