# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
#
# Copyright (C) 2022 Graz University of Technology.
#
# marc21converter is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Command-line tools for demo module."""


import click
from .tojson import create_record, Converter


@click.group()
def cli():
    """marc21converter commands."""
    pass


@cli.command("tojson")
@click.option(
    "--file",
    "-f",
    default="data/example-record.xml",
    show_default=True,
    type=click.File("r"),
    help="Relative path to file",
)
def tojson(file):
    """Create number of fake records for demo purposes."""
    click.secho("Converting record...", fg="blue")
    output = Converter().do(create_record(file.read()))

    import json

    print(json.dumps(output, indent=2))
    validate(output)
    click.secho("Successfully converted record!", fg="green")


def validate(input):
    import json
    from jsonschema import validate
    from os.path import join, dirname

    with open(
        join(dirname(__file__), "jsonschemas/marc21-record-1.0.0.json"), "rb"
    ) as fp:
        schema = json.load(fp)
    validate(instance=input, schema=schema)
