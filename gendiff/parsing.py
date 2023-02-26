#!/usr/bin/env python
import json
import yaml
import os


def parse(data, format_):
    """Parses data"""
    if format_ == 'json':
        return json.loads(data)
    if format_ == 'yaml':
        return yaml.safe_load(data)


def read_file(filepath):
    """Reads data from a file"""
    with open(filepath, 'r') as file:
        return file.read()


def get_format(filepath):
    """Gets the file format"""
    root, ext = os.path.splitext(filepath)
    if ext == '.yaml' or ext == '.yml':
        return 'yaml'
    elif ext == '.json':
        return 'json'
    raise TypeError("Can't read because input data type is not supported")
