#!/usr/bin/python
# -*- coding: utf-8 -*-

# === About ============================================================================================================

"""
 __init__.py

Copyright © 2017 Yuto Mizutani.
This software is released under the MIT License.

Version: 1.0.0

TranslateAuthors: Yuto Mizutani
E-mail: yuto.mizutani.dev@gmail.com
Website: http://operantroom.com

Created: 2017/12/09
Device: MacBook Pro (Retina, 13-inch, Mid 2015)
OS: macOS Serria version 10.12.6
IDE: PyCharm Community Edition 2017.2.4
Python: 3.6.1
"""

# --- References ---
"""
https://www.slideshare.net/kei10in/python-package-constructure
"""
# --- notes ---
# --- Information ---
# --- Circumstances ---

# === import ===========================================================================================================

""" Standard library """
# from .core import hmm
import sys
import os
""" Third party library """
""" Local library """
from getdoi.reader.readEnteredText import ReadEnteredTextImpl
from getdoi.reader.readTextFile import ReadTextFile
from getdoi.translator.translateEscapeSequence import TranslateEscapeSequence

# === CONSTANTS ========================================================================================================

# === User Parameters ==================================================================================================

# === variables ========================================================================================================
__version__ = '0.1.0'
__all__ = ['']

# ======================================================================================================================
