#!/usr/vin/env python
# -*- coding:utf-8 -*-
"""
  @date = ''
__author__ = 'magic'
"""
from mongonaut.sites import MongoAdmin

# import your custom models
from polls.models import Poem
# instantiate the MongoAdmin class
# Then attach the mongoadmin to your model
Poem.mongoadmin = MongoAdmin()

