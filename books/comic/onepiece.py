#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author: insert0003 <https://github.com/insert0003>
from .cartoonmadbase import CartoonMadBaseBook

def getBook():
    return Onepiece

class Onepiece(CartoonMadBaseBook):
    title               = u'[漫画]海贼王'
    description         = u'日本漫画家尾田荣一郎创作的少年漫画'
    language            = 'zh-tw'
    feed_encoding       = 'big5'
    page_encoding       = 'big5'
    mastheadfile        = 'mh_comic.gif'
    coverfile           = 'cv_onepiece.jpg'
    feeds               = [(u'海贼王', 'http://www.cartoonmad.com/comic/1152.html')]
