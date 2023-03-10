from gendiff.formaters.json import format_json
from gendiff.formaters.stylish import format_stylish
from gendiff.formaters.plain import format_plain
from gendiff.formaters.formats import JSON, STYLISH, PLAIN


def format_diff(diff, formatter):
    """Checks the file format for compliance with the formats available
    in the utility and runs the format set for this file format."""
    if formatter == STYLISH:
        return format_stylish(diff)
    if formatter == JSON:
        return format_json(diff)
    if formatter == PLAIN:
        return format_plain(diff)
