docker-pelican
==============

Dockerize pelican framework

## Installation

First, fork this repo, as it's going to contain your site source code (markdown), and clone it on your docker host:

    git clone git@github.com:USERNAME/docker-pelican
    cd docker-pelican

Build the image manually from the included Dockerfile:

    make docker-build

Then update the following settings inside `website/pelicanconf.py`:
    AUTHOR = u'Author name'
    SITENAME = u'The name of your website'
    TIMEZONE = 'Europe/Paris'
    DEFAULT_LANG = u'en'
    
And inside `Makefile` :
    deploy_repo_url = git@github.com:jderuere/jderuere.github.io.git 

Now, you're ready to use Pelican to build and deploy the HTML!

## Usage

First run the command :

    make docker-run

This wil enable you to have a preview to your website at localhost:8000.

You can now start writing posts into `website/content` (i.e article.md) :

```markdown
---
   Title: My title
   Date: 2010-12-03 10:20
   Modified: 2010-12-05 19:30
   Category: Python
   Tags: pelican, publishing
   Slug: my-super-post
   Authors: jderuere
   Summary: Short version for index and feeds
---
```

Pelican will automatically build the html into `website/output`.

## Stop the container

To stop the container, run the command :

    make docker-kill

## Push on github-page

Work on progress.
