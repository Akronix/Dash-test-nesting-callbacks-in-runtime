#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   factory_runtime_elements.py

   Descp:

   Created on: 18-feb-2019

   Copyright 2019 Abel 'Akronix' Serrano Juste <akronix5@gmail.com>
"""

import type1
import type2

def factory_runtime_elements(selection, app):
   if selection == 'one':
      type1.bind_callbacks2(app)
      return type1.get_html()
   else:
      type2.bind_callbacks2(app)
      return type2.get_html()


