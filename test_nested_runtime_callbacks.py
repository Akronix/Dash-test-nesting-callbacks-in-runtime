#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   test_nested_callbacks.py

   Descp:

   Created on: 18-feb-2019

   Copyright 2019 Abel 'Akronix' Serrano Juste <akronix5@gmail.com>
"""

import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State

from factory_runtime_elements import factory_runtime_elements

global app;

app = dash.Dash('test')

app.config['suppress_callback_exceptions'] = True

app.layout = html.Div([
      html.Div([
         html.Div([
            dcc.RadioItems(
               id='checklist',
               options=[
                  {'label': 'One', 'value': 'one'},
                  {'label': 'Two', 'value': 'two'},
               ]
            ),
            html.P(id='result1'),
         ]),
         html.Div(id='output')
      ],
      style={'display': 'flex'}
      )
 ])


@app.callback(
   Output('result1', 'children'),
   [Input('checklist', 'value')]
)
def select1(selection):
   return f'This is the selection: {selection}'


@app.callback(
   Output('output', 'children'),
   [Input('checklist', 'value')]
)
def select2(selection):
   print (f'This is the selection: {selection}')
   if not selection:
      return None

   html = factory_runtime_elements(selection, app)
   print (f'This is the html: {html}')
   return html


app.run_server(debug=True, port=8086)
