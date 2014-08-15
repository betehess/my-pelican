#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'betehess'
SITENAME = u"Alexandre Bertails' blog"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'EST'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MD_EXTENSIONS = ['codehilite(css_class=codehilite code)','extra','headerid']

DESCRIPTION = 'My blog and stuff ...@@@@'

# bootstrap built-texts BT3-Flat Responsive-Pelican
THEME = 'themes/betehess'

GITHUB_URL = "https://github.com/betehess"

TWITTER_USERNAME = 'bertails'

SOCIAL = (('twitter', 'http://twitter.com/ametaireau'),
          ('lastfm', 'http://lastfm.com/user/akounet'),
          ('github', 'http://github.com/ametaireau'),)

#SITEURL = 'http://bertails.org/blog'

#FILENAME_METADATA = '(?P<slug>.*)'  # use markdown file name as the slug meta
#USE_FOLDER_AS_CATEGORY = True       # use folder name as posts' category


ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_LANG_URL = '{date:%Y}/{date:%m}/{slug}-{lang}'
ARTICLE_LANG_SAVE_AS = '{date:%Y}/{date:%m}/{slug}-{lang}.html'

DRAFT_URL = 'drafts/{slug}.html'
DRAFT_SAVE_AS = 'drafts/{slug}.html'
DRAFT_LANG_URL = 'drafts/{slug}-{lang}.html'
DRAFT_LANG_SAVE_AS = 'drafts/{slug}-{lang}.html'

CATEGORY_URL = ''
CATEGORY_SAVE_AS = ''

TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}.html'

AUTHOR_URL = ''
AUTHOR_SAVE_AS = ''

YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/index.html'
