#!/usr/bin/python
# -*- coding: utf-8 -*-

import falcon
import random
import json
from translate import Translator


class HelloWorld:

    def on_get(self, req, resp):
        '''
        * Handles GET request, calls get_hello with params to
        * get appropriate hello world
        '''

        params = req.params  # Get parameters
        hello = self.get_hello(params)  # Get appropriate hello
        resp.body = json.dumps(hello)  # Dump into body

    def get_hello(self, params):
        '''
        * Takes in params and outputs hello world with correct formatting
        * excited:true -> hello world!
        * comma:true -> hello, world
        * case:title -> Hello World
        * case:lower -> hello world
        * classic:true -> Hello, World!
        * prepend:** -> **hello world
        * append:** -> hello world**
        * multiplier:2 -> hello world\nhello world
        * l33t:true -> h3770 w0r7d
        * translate:fr -> bonjour le monde
        '''

        phrase = 'hello world'
        if 'translate' in params:
            if type(params['translate']) is str:
                translator = Translator(to_lang=params['translate'])
            else:
                translator = Translator(to_lang=params['translate'][0])
            phrase = translator.translate(phrase).lower()
        if 'comma' in params and params['comma'] == 'true':
            phrase = phrase.replace(' ', ', ')
        if 'prepend' in params:
            phrase = params['prepend'] + phrase
        if 'append' in params:
            phrase += params['append']
        if 'excited' in params and params['excited'] == 'true':
            phrase += '!'
        if 'l33t' in params and params['l33t'] == 'true':
            phrase = phrase.translate(str.maketrans('elao', '3740'))
        if 'case' in params:
            if params['case'] == 'title':
                phrase = phrase.title()
            elif params['case'] == 'lower':
                phrase = phrase.lower()
            elif params['case'] == 'upper':
                phrase = phrase.upper()
            elif params['case'] == 'random':
                phrase = ''.join([random.choice([c.upper(), c])
                                 for c in phrase])
        if 'multiplier' in params:
            phrase = (phrase + '\n') * int(params['multiplier'])
        if 'classic' in params and params['classic'] == 'true':
            phrase = 'Hello, World!'
        return phrase


api = falcon.API()
api.add_route('/', HelloWorld())


			