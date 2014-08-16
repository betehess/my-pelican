#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'betehess'
SITENAME = u"Alexandre Bertails"
#SITEURL = 'http://bertails.org'

PATH = 'content'

TIMEZONE = 'EST'

DEFAULT_LANG = u'en'
DELETE_OUTPUT_DIRECTORY = True

#feeds
FEED_ALL_ATOM = 'feeds/all.xml'
FEED_ALL_RSS = 'feeds/all.rss'
CATEGORY_FEED_ATOM = 'feeds/%s.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss'
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS = None
FEED_ATOM = None
FEED_RSS = None

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MD_EXTENSIONS = ['codehilite(css_class=codehilite code)','extra','headerid']

# bootstrap built-texts BT3-Flat Responsive-Pelican
THEME = 'my-theme'
THEME_STATIC_DIR = ''

ARTICLE_URL = '{slug}'
ARTICLE_SAVE_AS = '{slug}.html'
ARTICLE_LANG_URL = '{slug}-{lang}'
ARTICLE_LANG_SAVE_AS = '{slug}-{lang}.html'

DRAFT_URL = 'drafts/{slug}.html'
DRAFT_SAVE_AS = 'drafts/{slug}.html'
DRAFT_LANG_URL = 'drafts/{slug}-{lang}.html'
DRAFT_LANG_SAVE_AS = 'drafts/{slug}-{lang}.html'

CATEGORY_URL = ''
CATEGORY_SAVE_AS = ''

TAG_URL = None
TAG_SAVE_AS = None

AUTHOR_URL = ''
AUTHOR_SAVE_AS = ''

ARCHIVES_SAVE_AS = None
AUTHORS_SAVE_AS = None
CATEGORIES_SAVE_AS = None
TAGS_SAVE_AS = None

#YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
#MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'
