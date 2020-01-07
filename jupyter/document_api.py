import shutil
import requests
import xmltodict
from bs4 import BeautifulSoup
from xml.etree import ElementTree as ET

# Full documentation for this API can be found on Gallica's site: http://api.bnf.fr/api-document-de-gallica

class Document(object):

    @staticmethod
    def issues(id):
    
        ISSUES_BASEURL = 'https://gallica.bnf.fr/services/Issues?ark=ark:/'
    
        url = "".join([ISSUES_BASEURL, id, '/date'])
        print(url)
    
        s = requests.get(url, stream=True)
        soup = BeautifulSoup(s.content,"lxml-xml")
        print(soup)
       
            
    @staticmethod
    def issues_date(id, date):
    
        ISSUESDATE_BASEURL = 'https://gallica.bnf.fr/services/Issues?ark=ark:/'
      
        url = "".join([ISSUESDATE_BASEURL, id, '/date', '&date=', date])
        print(url)
    
        s = requests.get(url, stream=True)
        soup = BeautifulSoup(s.content,"lxml-xml")
        print(soup)
        
            
    @staticmethod
    def OAI(id):
    
        OAI_BASEURL = 'https://gallica.bnf.fr/services/OAIRecord?ark=ark:/'
    
        url = "".join([OAI_BASEURL, id])
        print(url)
    
        s = requests.get(url, stream=True)
        soup = BeautifulSoup(s.content,"lxml-xml")
        print(soup)
            
    @staticmethod
    def pagination(id):
    
        PAGINATION_BASEURL = 'https://gallica.bnf.fr/services/Pagination?ark=ark:/'
    
        url = "".join([PAGINATION_BASEURL, id])
        print(url)
    
        s = requests.get(url, stream=True)
        soup = BeautifulSoup(s.content,"lxml-xml")
        print(soup)
            
    @staticmethod
    def simple_images(id, res):
    
        IMAGES_BASEURL = 'https://gallica.bnf.fr/ark:/'
    
        url = "".join([IMAGES_BASEURL, id, '/', res])
        print(url)
    
        response = requests.get(url, stream=True)
        with open('simple_image.jpg', 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
            del response
    
    @staticmethod
    def content(id, query):
    
        CONTENT_BASEURL = 'https://gallica.bnf.fr/services/ContentSearch?ark='
    
        url = "".join([CONTENT_BASEURL, id, '&query=', query])
        print(url)
    
        s = requests.get(url, stream=True)
        soup = BeautifulSoup(s.content,"lxml-xml")
        print(soup)
    
    @staticmethod
    def content_page(id, query, page):
    
        CONTENTPAGE_BASEURL = 'https://gallica.bnf.fr/services/ContentSearch?ark='
    
        url = "".join([CONTENTPAGE_BASEURL, id, '&query=', query, '&page=', page])
        print(url)
    
        s = requests.get(url, stream=True)
        soup = BeautifulSoup(s.content,"lxml-xml")
        print(soup)
            
    @staticmethod
    def toc(id):
    
        TOC_BASEURL = 'https://gallica.bnf.fr/services/Toc?ark='
    
        url = "".join([TOC_BASEURL, id])
        print(url)
    
        s = requests.get(url, stream=True)
        soup = BeautifulSoup(s.content,"lxml-xml")
        print(soup)
            
    @staticmethod
    def texte_brut(id):
        TEXTEBRUT_BASEURL = 'https://gallica.bnf.fr/ark:/'
    
        url = "".join([TEXTEBRUT_BASEURL, id, '.texteBrut'])
        print(url)
    
        s = requests.get(url, stream=True)
        soup = BeautifulSoup(s.content,"lxml-xml")
        print(soup)
            
    @staticmethod
    def ocr(id, page):
        OCR_BASEURL = 'https://gallica.bnf.fr/RequestDigitalElement?O='
    
        url = "".join([OCR_BASEURL, id, '&E=ALTO&Deb=', page])
        print(url)
    
        s = requests.get(url, stream=True)
        soup = BeautifulSoup(s.content,"lxml-xml")
        print(soup)
        