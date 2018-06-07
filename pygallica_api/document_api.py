import urllib
import xmltodict
import requests
import shutil


# Full documentation for this API can be found on Gallica's site: http://api.bnf.fr/api-document-de-gallica

class Document(object):

    @staticmethod
    def issues(id):
    
        ISSUES_BASEURL = 'http://gallica.bnf.fr/services/Issues?ark=ark:/'
    
        url = "".join([ISSUES_BASEURL, id, '/date'])
        print url
    
        s = urllib.urlopen(url)
        contents = s.read()
        file = open('issues.xml', 'w')
        file.write(contents)
        file.close()
        with open('issues.xml') as xml:
            doc = xmltodict.parse(xml.read())
            return doc
            
    @staticmethod
    def issues_date(id, date):
    
        ISSUESDATE_BASEURL = 'http://gallica.bnf.fr/services/Issues?ark=ark:/'
      
        url = "".join([ISSUESDATE_BASEURL, id, '/date', '&date=', date])
        print url
    
        s = urllib.urlopen(url)
        contents = s.read()
        file = open('issues_date.xml', 'w')
        file.write(contents)
        file.close()
        with open('issues_date.xml') as xml:
            doc = xmltodict.parse(xml.read())
            return doc
            
    @staticmethod
    def OAI(id):
    
        OAI_BASEURL = 'http://gallica.bnf.fr/services/OAIRecord?ark=ark:/'
    
        url = "".join([OAI_BASEURL, id])
        print url
    
        s = urllib.urlopen(url)
        contents = s.read()
        file = open('oai.xml', 'w')
        file.write(contents)
        file.close()
        with open('oai.xml') as xml:
            doc = xmltodict.parse(xml.read())
            return doc
            
    @staticmethod
    def pagination(id):
    
        PAGINATION_BASEURL = 'http://gallica.bnf.fr/services/Pagination?ark=ark:/'
    
        url = "".join([PAGINATION_BASEURL, id])
        print url
    
        s = urllib.urlopen(url)
        contents = s.read()
        file = open('pagination.xml', 'w')
        file.write(contents)
        file.close()
        with open('pagination.xml') as xml:
            doc = xmltodict.parse(xml.read())
            return doc
            
    @staticmethod
    def simple_images(id, res):
    
        IMAGES_BASEURL = 'http://gallica.bnf.fr/ark:/'
    
        url = "".join([IMAGES_BASEURL, id, '/', res])
        print url
    
        response = requests.get(url, stream=True)
        with open('simple_image.jpg', 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
            del response
    
    @staticmethod
    def content(id, query):
    
        CONTENT_BASEURL = 'http://gallica.bnf.fr/services/ContentSearch?ark='
    
        url = "".join([CONTENT_BASEURL, id, '&query=', query])
        print url
    
        s = urllib.urlopen(url)
        contents = s.read()
        file = open('content.xml', 'w')
        file.write(contents)
        file.close()
        with open('content.xml') as xml:
            doc = xmltodict.parse(xml.read())
            return doc
    
    @staticmethod
    def content_page(id, query, page):
    
        CONTENTPAGE_BASEURL = 'http://gallica.bnf.fr/services/ContentSearch?ark='
    
        url = "".join([CONTENTPAGE_BASEURL, id, '&query=', query, '&page=', page])
        print url
    
        s = urllib.urlopen(url)
        contents = s.read()
        file = open('content_page.xml', 'w')
        file.write(contents)
        file.close()
        with open('content_page.xml') as xml:
            doc = xmltodict.parse(xml.read())
            return doc
            
    @staticmethod
    def toc(id):
    
        TOC_BASEURL = 'http://gallica.bnf.fr/services/Toc?ark='
    
        url = "".join([TOC_BASEURL, id])
        print url
    
        s = urllib.urlopen(url)
        contents = s.read()
        file = open('toc.xml', 'w')
        file.write(contents)
        file.close()
        with open('toc.xml') as xml:
            doc = xmltodict.parse(xml.read())
            return doc
            
    @staticmethod
    def texte_brut(id):
        TEXTEBRUT_BASEURL = 'http://gallica.bnf.fr/ark:/'
    
        url = "".join([TEXTEBRUT_BASEURL, id, '.texteBrut'])
        print url
    
        s = urllib.urlopen(url)
        contents = s.read()
        file = open('textebrut.xml', 'w')
        file.write(contents)
        file.close()
        with open('textebrut.xml') as xml:
            doc = xmltodict.parse(xml.read())
            return doc
            
    @staticmethod
    def ocr(id, page):
        OCR_BASEURL = 'http://gallica.bnf.fr/RequestDigitalElement?O='
    
        url = "".join([OCR_BASEURL, id, '&E=ALTO&Deb=', page])
        print url
    
        s = urllib.urlopen(url)
        contents = s.read()
        file = open('oce.xml', 'w')
        file.write(contents)
        file.close()
        with open('ocr.xml') as xml:
            doc = xmltodict.parse(xml.read())
            return doc