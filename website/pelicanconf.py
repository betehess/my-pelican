#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Alexandre Bertails'
SITENAME = u"You have a link"
SITEURL = u'http://bertails.org'
#RELATIVE_URLS = True

PATH = 'content'

TIMEZONE = 'EST'

DEFAULT_LANG = u'en'
DELETE_OUTPUT_DIRECTORY = True

#feeds
FEED_ALL_ATOM = 'feed/all.xml'
FEED_ALL_RSS = 'feed/all.rss'
CATEGORY_FEED_ATOM = 'feed/%s.xml'
CATEGORY_FEED_RSS = 'feed/%s.rss'
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS = None
FEED_ATOM = None
FEED_RSS = None

DEFAULT_PAGINATION = 10

#MD_EXTENSIONS = ['codehilite(css_class=codehilite code)','extra','headerid']
MD_EXTENSIONS = ['extra','headerid']

THEME = 'my-theme'
THEME_STATIC_DIR = ''

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_LANG_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}-{lang}'
ARTICLE_LANG_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}-{lang}.html'

DRAFT_URL = 'draft/{slug}.html'
DRAFT_SAVE_AS = 'draft/{slug}.html'
DRAFT_LANG_URL = 'draft/{slug}-{lang}.html'
DRAFT_LANG_SAVE_AS = 'draft/{slug}-{lang}.html'

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
