# PyGallica
A Python wrapper for the National Library of France's Gallica API.
The package contains basic classes and associated methods for querying the [Search API](http://api.bnf.fr/api-gallica-de-recherche), [Gallica IIIF API](http://api.bnf.fr/api-iiif-de-recuperation-des-images-de-gallica), and the [Document API](http://api.bnf.fr/api-document-de-gallica). No API keys are required.

### Search API

The Search API allows you to perform keyword searches in Gallica's holdings and retrieve xml returned by those searches.

Example usage:
```
>>> from search_api import Search
>>> Search.search('your', 'keywords')
````
This will return the xml associated with your search. The xml file will be saved locally for easy parsing.

### IIIF API

The IIIF API allows you to retrieve images from Gallica's holdings, as well as the .json metadata associated with those images. Gallica, as a participant in the IIIF, offers access to all of the more than 100 million images in its Gallica digital library.

The API takes an Ark ID, region, size, rotation, quality, and format as arguments.

Example usage:
```
>>> from iiif_api import IIIF
>>> IIIF.iiif('12148/btv1b90017179/f15', '0,1900,2400,1200', 'full', '0', 'native', 'jpg'
```
This will save your image in a new folder. To retrieve the metadata for an image, simply input an Ark ID:
```
>>> from iiif_api import IIIF
>>> IIIF.metadata('12148/btv1b90017179/f15')
```

### Document API

The Document API allows you to retrieve metadata about a particular document in Gallica's holdings. There are a number of different methods for retrieving various types of metadata.

Example usage, retrieving OCR from page 10 of the document whose Ark ID is passed:
```
>>> from document_api import Document
>>> Document.ocr('bpt6k5619759j', '10')
```
