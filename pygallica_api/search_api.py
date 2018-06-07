import urllib
import xmltodict

# Full documentation for this API can be found on Gallica's site: http://api.bnf.fr/api-gallica-de-recherche


class Search(object):
    
    @staticmethod
    def search(startRecord, *args):
    
    #This function passes your queries, separated by commas, in addition to the record you'd like to start with. 
    
        RECHERCHE_BASEURL = 'http://gallica.bnf.fr/SRU?operation=searchRetrieve&version=1.2&query=(gallica all '
        START_REC = ')&startRecord='
    
        for arg in args:
            search_string = (', '.join('"' + item + '"' for item in args))
      
        url = "".join([RECHERCHE_BASEURL, search_string, START_REC, startRecord])
        print url

        s = urllib.urlopen(url)
        contents = s.read()
        file = open('gallica.xml', 'w')
        file.write(contents)
        file.close()
        with open('gallica.xml') as xml:
            doc = xmltodict.parse(xml.read())
            return doc
import urllib
import xmltodict

# Full documentation for this API can be found on Gallica's site: http://api.bnf.fr/api-gallica-de-recherche


class Search(object):
    
    @staticmethod
    def search(startRecord, *args):
    
    #This function passes your queries, separated by commas, in addition to the record you'd like to start with. 
    
        RECHERCHE_BASEURL = 'http://gallica.bnf.fr/SRU?operation=searchRetrieve&version=1.2&query=(gallica all '
        START_REC = ')&startRecord='
    
        for arg in args:
            search_string = (', '.join('"' + item + '"' for item in args))
      
        url = "".join([RECHERCHE_BASEURL, search_string, START_REC, startRecord])
        print url

        s = urllib.urlopen(url)
        contents = s.read()
        file = open('gallica.xml', 'w')
        file.write(contents)
        file.close()
        with open('gallica.xml') as xml:
            doc = xmltodict.parse(xml.read())
            return doc
