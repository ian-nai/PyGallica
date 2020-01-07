import requests
import shutil
import os

# Full documentation for this API can be found on Gallica's site: http://api.bnf.fr/api-iiif-de-recuperation-des-images-de-gallica

class IIIF(object):

    @staticmethod
    def iiif(id, region, size, rotation, quality, format):
    
        IIIF_BASEURL = 'https://gallica.bnf.fr/iiif/ark:/'
      
        url = "".join([IIIF_BASEURL, id, '/', region, '/', size, '/', rotation, '/', quality, '.', format])
        print(url)
        filename = "".join([id, '.', format])
        dirname = os.path.dirname(filename)
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        response = requests.get(url, stream=True)
        with open(filename, 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
            del response
            
    @staticmethod
    def metadata(id):
        METADATA_BASEURL = 'https://gallica.bnf.fr/iiif/ark:/'
        req_url = "".join([METADATA_BASEURL, id, '/info.json'])
    
        print(req_url)
    
        r = requests.get(req_url)
        r.raise_for_status()
        return r.json()

