# -*- coding: utf-8 -*-
#A1b: The program must then navigate through all the resources (identified by URIs or Blank nodes) in the model. If the type (rdf:type) of the resource is not known, add an asserted statement to the model (in memory) that declares that the type of the resource is LocallyUnknownType (suggest proper URI etc.). (1 point)
#For each statement, check which URIRefs and BNodes appear in each statement. For those resources x (i.e. URIRefs and BNodes) for which there is no asserted statement about their type (i.e. something like (x, rdf:type, y)), add a new statement (x, rdf:type : LocallyUnknownType). How to do this in practice, check section 3 and RDFLib examples in Moodle Lecture Material section, or browse RDFLIb documentation.

import rdflib
import logging
from rdflib import RDF, Graph, URIRef
from pprint import pprint
from rdflib.parser import Parser

# In order to get error messages straight from rdflib...
logging.basicConfig()

# Creating the graph with parser
g = rdflib.Graph()
g.open("store", create=True)
result = g.parse("http://data.linked-open-science.org/semantic-dogfood/eswc-2013-complete.rdf", format='application/rdf+xml')

#Go through the graph and place LocallyUnknownType if URIRef is unknown
for s,p,o in g:
    if not type(s) is rdflib.URIRef:
        nt=(s,rdflib.RDFS.__class__LocallyUnknownType,o)
        g.add(nt)
