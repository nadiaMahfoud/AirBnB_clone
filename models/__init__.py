#!/usr/bin/python3
""" This module is the ‘__init__’ methods for the models directory"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
