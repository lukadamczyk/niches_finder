from django.shortcuts import render
from .forms import KeywordForm
from lxml import html
import urllib, ssl
from bs4 import BeautifulSoup


import requests


def niches(request):
    form = KeywordForm(request.GET)
    if form.is_valid():
        # headers = {
        #     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
        cd = form.cleaned_data['keyword']
        keywords = cd.replace(' ', '+')
        url = 'https://www.amazon.com/s?k={}&i=stripbooks&ref=nb_sb_noss'.format(keywords)
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        # soup = None
        try:
            html = urllib.request.urlopen(url, context=ctx).read()
            soup = BeautifulSoup(html, 'html.parser')
            html = soup.prettify()
        except Exception as e:
            print(e)
        product_json = {}
        if soup:
            for divs in soup.findAll('div', attrs={'class': 'a-link-normal a-text-normal'}):
                try:
                    product_json['brand'] = divs
                    # soup = BeautifulSoup(page.text, 'html.parser')
                except Exception as e:
                    print(e)
        info = product_json
        # info = html
        return render(request,
                      template_name='niches/home.html',
                      context={'form': form,
                               'info': info})
    info = 'false'
    return render(request,
           template_name='niches/home.html',
           context={'form': form,
                    'info': info})