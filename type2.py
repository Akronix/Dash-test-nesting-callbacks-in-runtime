#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   type2.py

   Descp:

   Created on: 18-feb-2019

   Copyright 2019 Abel 'Akronix' Serrano Juste <akronix5@gmail.com>
"""

import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State



def get_html():
   return html.Div([
            html.Button(
               'Button 3 to be bound',
               id='bt3',
            ),
            html.P(id='result3')
         ])


def bind_callbacks2(app):

   @app.callback(
      Output('result3', 'children'),
      [Input('bt3', 'n_clicks')]
   )
   def press_bt1(click):
      if click and click % 2 == 1:
         print('BT3 click')
         return 'Pressed bt3'

      return None


