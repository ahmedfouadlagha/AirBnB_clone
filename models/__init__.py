#!/usr/bin/python3
"""
__init__ method for models package, or Module for FileStorage autoinit.
__init__ magic method for models directory
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
