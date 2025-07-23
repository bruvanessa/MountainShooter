#!/usr/bin/python
# -*- coding: utf-8 -*-
from pygame import Rect, surface


class Entity:
    def __init__(self):
        self.name: str = None
        self.surf: surface = None
        self.rect: Rect = None

