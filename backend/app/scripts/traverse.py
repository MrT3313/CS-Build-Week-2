#  IMPORTS
import os
import django

import requests
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')
django.setup()

# Utils
from ..utils.queue import Queue
from ..utils.stack import Stack
from ..utils.graph import Graph

# q = Queue()
# s = Stack()
# g = Graph()

# print(q)
# print(s)
# print(g)
def traverse_server():
    print(f'is this working')
    return f'success'