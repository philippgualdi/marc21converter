# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
#
# Copyright (C) 2022 Graz University of Technology.
#
# marc21converter is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

from collections import OrderedDict


class Converter(object):
    def __init__(self):
        pass

    def convert(xml):
        pass

    def do(self, blob):

        output = {}

        leader = blob.get("leader", "")
        output["leader"] = leader

        control = blob.get("control", {})
        items = control.items()

        fields = {}
        for key, value in items:
            fields[key] = value

        data = blob.get("fields", {})
        items = data
        datafields = {}
        for key, value in items:

            tag = key[:3]
            ind1 = key[3:4]
            ind2 = key[4:5]
            datafield = {"indicator1": ind1, "indicator2": ind2}
            subfields = []
            for k, v in value.items():
                subfields.append({k: v})
            datafield.update({"subfields": subfields})
            if tag in datafields.keys() and not isinstance(datafields[tag], list):
                temp = datafields[tag]
                datafields[tag] = [temp]
            if tag in datafields.keys() and isinstance(datafields[tag], list):
                datafields[tag].append(datafield)
            else:
                datafields[tag] = datafield

        fields.update(datafields)
        output["fields"] = fields
        return output

    def elem2dict(self, node):
        """
        Convert an lxml.etree node tree into a dict.
        """

        result = {}

        for element in node.iterchildren():
            # Remove namespace prefix
            key = element.tag.split("}")[1] if "}" in element.tag else element.tag

            # Process element as tree element if the inner XML contains non-whitespace content
            if element.text and element.text.strip():
                value = element.text
            else:
                value = self.elem2dict(element)
            if key in result:

                if type(result[key]) is list:
                    result[key].append(value)
                else:
                    tempvalue = result[key].copy()
                    result[key] = [tempvalue, value]
            else:
                result[key] = value
        return result
