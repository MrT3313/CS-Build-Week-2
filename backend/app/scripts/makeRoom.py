# IMPORTS
import os 
import django

import resuests
import json

# ??
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')
django.setup()

# MODELS
from  ..models import Room

# == === == == == == == == == == == == == == == == #
# == === == == == == == == == == == == == == == == #

# def makeRoom():
#     print(f'- + -You are making a room - + -')

#     newRoom = Room()