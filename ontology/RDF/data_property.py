from rdflib import URIRef
from .prefix import dc, pp

title = URIRef(dc + 'title')
description = URIRef(dc + 'description')
code = URIRef(pp + 'code')
