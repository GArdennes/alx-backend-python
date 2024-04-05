#!/usr/bin/env python3
"""
main
"""
from utils import access_nested_map


nested_map = {"a": 1}
path = ("a")
value = access_nested_map(nested_map, path)
print(value)
nested_map = {"a": {"b": 2}}
path = ("a",)
value = access_nested_map(nested_map, path)
print(value)
nested_map = {"a": {"b": 2}}
path = ("a", "b")
value = access_nested_map(nested_map, path)
print(value)
try:
    nested_map = {}
    path = ("a",)
    value = access_nested_map(nested_map, path)
    print(value)
    nested_map = {"a": 1}
    path = ("a", "b")
    value = access_nested_map(nested_map, path)
    print(value)
except Exception as error:
    print(error)
