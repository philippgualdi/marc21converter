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


@click.group()
def marc21converter():
    """marc21converter commands."""
    pass


@marc21converter.command("tojson")
@click.option(
    "--file",
    "-f",
    default="data/example-record.xml",
    show_default=True,
    type=str,
    help="Relative path to file",
)
def tojson(file):
    """Create number of fake records for demo purposes."""
    click.secho("Converting record...", fg="blue")

    click.secho("Successfully converted record!", fg="green")
