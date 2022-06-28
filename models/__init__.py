#!/usr/bin/python3

"""
Create a unique Filestorage instance for your the app.
"""

from imp import reload
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
