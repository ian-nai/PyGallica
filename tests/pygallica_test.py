import unittest

class TestClient(unittest.TestCase):
    
    def test_search(self):
    
        RECHERCHE_BASEURL = 'http://gallica.bnf.fr/SRU?operation=searchRetrieve&version=1.2&query=(gallica all '
        START_REC = ')&startRecord='
        
        args = 'test 1', 'test 2'
        startRecord = '10'
        expected = 'http://gallica.bnf.fr/SRU?operation=searchRetrieve&version=1.2&query=(gallica all "test 1", "test 2")&startRecord=10'
    
        for arg in args:
            search_string = (', '.join('"' + item + '"' for item in args))
      
        url = "".join([RECHERCHE_BASEURL, search_string, START_REC, startRecord])
        
        self.assertEqual(url, expected,  "Search url is constructed correctly")

    def test_iiif(self):
    
        IIIF_BASEURL = 'http://gallica.bnf.fr/iiif/ark:/'
        
        id = '1'
        region = '2'
        size = '3'
        rotation = '4'
        quality = '5'
        format = 'png'
        expected = 'http://gallica.bnf.fr/iiif/ark:/1/2/3/4/5.png'
        
        url = "".join([IIIF_BASEURL, id, '/', region, '/', size, '/', rotation, '/', quality, '.', format])
        
        self.assertEqual(url, expected,  "IIIF url is constructed correctly")
    
    def test_metadata(self):
    
        METADATA_BASEURL = 'http://gallica.bnf.fr/iiif/ark:/'
        id = 'test'
        expected = 'http://gallica.bnf.fr/iiif/ark:/test/info.json'
        
        req_url = "".join([METADATA_BASEURL, id, '/info.json'])
    
        self.assertEqual(req_url, expected,  "Metadata url is constructed correctly")
        
    def test_issues(self):
    
        ISSUES_BASEURL = 'http://gallica.bnf.fr/services/Issues?ark=ark:/'
        id = 'test'
        expected = 'http://gallica.bnf.fr/services/Issues?ark=ark:/test/date'
    
        url = "".join([ISSUES_BASEURL, id, '/date'])
        
        self.assertEqual(url, expected,  "Issues url is constructed correctly")
        
    def test_issues_date(self):
    
        ISSUESDATE_BASEURL = 'http://gallica.bnf.fr/services/Issues?ark=ark:/'
        id = 'test'
        date = '1979'
        expected = 'http://gallica.bnf.fr/services/Issues?ark=ark:/test/date&date=1979'
      
        url = "".join([ISSUESDATE_BASEURL, id, '/date', '&date=', date])
        
        self.assertEqual(url, expected,  "Issues_date url is constructed correctly")
        
    def test_OAI(self):
    
        OAI_BASEURL = 'http://gallica.bnf.fr/services/OAIRecord?ark=ark:/'
        id = 'test'
        expected = 'http://gallica.bnf.fr/services/OAIRecord?ark=ark:/test'
    
        url = "".join([OAI_BASEURL, id])
        
        self.assertEqual(url, expected,  "OAI url is constructed correctly")
    
    def test_pagination(self):
    
        PAGINATION_BASEURL = 'http://gallica.bnf.fr/services/Pagination?ark=ark:/'
        id = 'test'
        expected = 'http://gallica.bnf.fr/services/Pagination?ark=ark:/test'
    
        url = "".join([PAGINATION_BASEURL, id])
        
        self.assertEqual(url, expected,  "Pagination url is constructed correctly")
    
    def test_simple_images(self):
    
        IMAGES_BASEURL = 'http://gallica.bnf.fr/ark:/'
        id = 'test'
        res='highres'
        expected = 'http://gallica.bnf.fr/ark:/test/highres'
    
        url = "".join([IMAGES_BASEURL, id, '/', res])
        
        self.assertEqual(url, expected,  "Simple_images url is constructed correctly")
    
    def test_content(self):
    
        CONTENT_BASEURL = 'http://gallica.bnf.fr/services/ContentSearch?ark='
        id = 'test'
        query = 'testing'
        expected = 'http://gallica.bnf.fr/services/ContentSearch?ark=test&query=testing'
    
        url = "".join([CONTENT_BASEURL, id, '&query=', query])
        
        self.assertEqual(url, expected,  "Content url is constructed correctly")
        
    def test_content_page(self):
    
        CONTENTPAGE_BASEURL = 'http://gallica.bnf.fr/services/ContentSearch?ark='
        id = 'test'
        query = 'testing'
        page = '10'
        expected = 'http://gallica.bnf.fr/services/ContentSearch?ark=test&query=testing&page=10'
    
        url = "".join([CONTENTPAGE_BASEURL, id, '&query=', query, '&page=', page])
        
        self.assertEqual(url, expected,  "Content_page url is constructed correctly")
        
    def test_toc(self):
    
        TOC_BASEURL = 'http://gallica.bnf.fr/services/Toc?ark='
        id = 'test/test'
        expected = 'http://gallica.bnf.fr/services/Toc?ark=test/test'
    
        url = "".join([TOC_BASEURL, id])
        
        self.assertEqual(url, expected,  "TOC url is constructed correctly")
    
    def test_texte_brut(self):
     
        TEXTEBRUT_BASEURL = 'http://gallica.bnf.fr/ark:/'
        id = 'test'
        expected = 'http://gallica.bnf.fr/ark:/test.texteBrut'
    
        url = "".join([TEXTEBRUT_BASEURL, id, '.texteBrut'])
        
        self.assertEqual(url, expected,  "Texte_brut url is constructed correctly")
    
    def test_ocr(self):
     
        OCR_BASEURL = 'http://gallica.bnf.fr/RequestDigitalElement?O='
        id = 'test'
        page = '10'
        expected = 'http://gallica.bnf.fr/RequestDigitalElement?O=test&E=ALTO&Deb=10'
    
        url = "".join([OCR_BASEURL, id, '&E=ALTO&Deb=', page])
        
        self.assertEqual(url, expected,  "OCR url is constructed correctly")
    
if __name__ == '__main__':
    unittest.main()
