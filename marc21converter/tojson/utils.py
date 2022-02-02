# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
#
# Copyright (C) 2022 Graz University of Technology.
#
# marc21converter is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.


"""Utility functions."""

import codecs
import json
import functools
import warnings
from lxml import etree
from io import StringIO
from collections import OrderedDict


def load(stream):
    """Load JSON from bytestream."""
    reader = codecs.getreader("utf-8")
    return json.load(reader(stream))


def dump(iterator):
    """Dump JSON from iteraror."""
    return json.dumps(list(iterator))


def deprecated(explanation):
    """Decorate as deprecated."""

    def decorator(f):
        @functools.wraps(f)
        def wrapper(self, key, values, **kwargs):
            warnings.warn("{0}: {1}".format(key, explanation), DeprecationWarning)
            return f(self, key, values, **kwargs)

    return decorator


def create_record(marcxml, keep_singletons=False):
    """Create a record object using the LXML parser."""
    if isinstance(marcxml, bytes):
        marcxml = marcxml.decode("utf-8")

    if isinstance(marcxml, str):
        parser = etree.XMLParser(recover=True)
        tree = etree.parse(StringIO(marcxml), parser)
    else:
        tree = marcxml
    record = []

    leader_iterator = tree.iter(tag="{*}leader")
    for leader in leader_iterator:
        text = leader.text or ""
        record.append(("leader", text))

    controlfield_iterator = tree.iter(tag="{*}controlfield")
    control = []
    for controlfield in controlfield_iterator:
        tag = controlfield.attrib.get("tag", "!")
        text = controlfield.text or ""
        if text or keep_singletons:
            control.append((tag, text))
    record.append(("control", OrderedDict(control)))

    datafield_iterator = tree.iter(tag="{*}datafield")
    data = []
    for datafield in datafield_iterator:
        tag = datafield.attrib.get("tag", "!")
        ind1 = datafield.attrib.get("ind1", "!")
        ind2 = datafield.attrib.get("ind2", "!")

        ind1 = ind1.replace(" ", "_")
        ind2 = ind2.replace(" ", "_")

        fields = []
        subfield_iterator = datafield.iter(tag="{*}subfield")
        for subfield in subfield_iterator:
            code = subfield.attrib.get("code", "!")
            text = subfield.text or ""
            if text or keep_singletons:
                fields.append((code, text))

        if fields or keep_singletons:
            key = "{0}{1}{2}".format(tag, ind1, ind2)
            data.append((key, OrderedDict(fields)))
    record.append(("fields", data))
    return OrderedDict(record)
