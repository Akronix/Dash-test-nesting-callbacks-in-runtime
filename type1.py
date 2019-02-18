#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   type.py

   Descp:

   Created on: 18-feb-2019

   Copyright 2019 Abel 'Akronix' Serrano Juste <akronix5@gmail.com>
"""

import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State


def get_html():
   print('f Returning html for type1')
   return html.Div([
            html.Button(
               'Button to be bound',
               id='bt2',
            ),
            html.P(id='result2')
         ])


def bind_callbacks2(app):

   @app.callback(
      Output('result2', 'children'),
      [Input('bt2', 'n_clicks')]
   )
   def press_bt1(click):
      if click and click % 2 == 1:
         print('BT2 click')
         return 'Pressed bt2'

      return None


