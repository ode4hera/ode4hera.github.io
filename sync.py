# -*- coding: utf-8 -*-
#
# Author: Francesco Torrigiani, francesco.torrigiani@dlr.de
#
# Copyright (c) 2023, (DLR)
# All rights reserved.
#
# http://www.dlr.de/sl/
#
from pathlib import Path
from utils import (
    shield_human_file,
    update_onto_date,
    change_serialization,
    rdf_to_htmldoc,
)

filedir = Path(__file__).parent
ONTO_TAGS = [
    'Bibliography',
    'Glossary'
]
URI_ROOT = "https://w3id.org/CA-ODE4HERA/"

#################################################################
# SYNCHRONIZATION
#   Reference file: .ttl
#   Synchronized files: .owl (xml), html
##################################################################

for onto_tag in ONTO_TAGS:
    onto_folder = filedir / onto_tag
    onto_doc_folder = onto_folder / '{}Doc'.format(onto_tag.lower())
    ttl_file = onto_folder / 'ode4hera_{}.ttl'.format(onto_tag.lower())
    owl_file = onto_folder / 'ode4hera_{}.owl'.format(onto_tag.lower())
    html_file = onto_doc_folder / 'index.html'.format(onto_tag.lower())

    ttl_h_file = onto_folder / 'ode4hera_h_{}.ttl'.format(onto_tag.lower())
    ttl_data_file = onto_folder / 'ode4hera_{}_data.ttl'.format(onto_tag.lower())
    onto_uri = URI_ROOT + onto_tag
    shield_human_file(ttl_h_file, ttl_file)
    update_onto_date(ttl_file, onto_uri, rdf_format='ttl')
    change_serialization(ttl_file, in_format='ttl', out_format='xml', out_extension='.owl')
    rdf_to_htmldoc(ttl_file, html_file=html_file)
