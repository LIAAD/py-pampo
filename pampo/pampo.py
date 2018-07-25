# -*- coding: utf-8 -*-

import click
from .ner import *

@click.command()
@click.argument('input', type=click.File('rb'))
def main(input):
    """Console script for Pampo. Inform an input file and it returns detected entities."""

    content = ''
    while True:
        chunk = input.read(1024)
        if not chunk:
            break

        content += chunk.decode("utf-8") 

    entities = extract_entities(content)
    for entity in entities:
        print(entity)

if __name__ == "__main__":
    main()
