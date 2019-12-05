import requests
import xmltodict
from bs4 import BeautifulSoup
from xml.etree import ElementTree as ET

# Full documentation for this API can be found on Gallica's site: http://api.bnf.fr/api-gallica-de-recherche


class Search(object):
    
    @staticmethod
    def search(*args):
    
    #This function passes your queries, separated by commas, in addition to the record you'd like to start with. 
    
        RECHERCHE_BASEURL = 'https://gallica.bnf.fr/SRU?operation=searchRetrieve&version=1.2&query=(gallica all '
        START_REC = ')&startRecord=1'
    
        for arg in args:
            search_string = (', '.join('"' + item + '"' for item in args))
      
        url = "".join([RECHERCHE_BASEURL, search_string, START_REC])
        print url

        s = requests.get(url, stream=True)
        soup = BeautifulSoup(s.content,"lxml-xml")
        print soup
        #file = open('gallica.xml', 'w')
        #file.write(tree)
        #file.close()
        with open('gallica.xml', 'w') as f:
            f.write(soup.prettify().encode('UTF-8'))
            f.close()
        with open('gallica.xml') as xml:
            doc = xmltodict.parse(xml.read())
            return doc
