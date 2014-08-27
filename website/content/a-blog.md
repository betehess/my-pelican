Title: Finally my own blog
Date: 2014-08-28
Slug: a-blog

I have finally found the time and the motivation to put together my own blog \o/ I had actually planned to do so for about 10 years, basically since I own `bertails.org`...

Sooo, how does this work? I wanted something as easy to use as possible. So I have settled on [Pelican](http://docs.getpelican.com/). As I don't want to pollute my environment with Python dependencies, I am using [Docker](https://www.docker.com/) to generate the static version of this website. The [project](https://github.com/betehess/my-pelican/) started as a clone of [https://github.com/jderuere/docker-pelican](https://github.com/jderuere/docker-pelican) but I quickly regenerated everything, including the [Dockerfile](https://github.com/betehess/my-pelican/blob/master/Dockerfile). I run Pelican within the container but against the mounted `content` directory, and I propagate my user from the host to avoid right issues (Docker uses root by default).

The theme is directly based on [Paul Rouget's website](http://paulrouget.com/), with few adaptations. Most important ones are the fixed font ([Ubuntu Mono](https://www.google.com/fonts/specimen/Ubuntu+Mono)) and the greenish colour for the links. I only use 2 templates from Pelican: `index.html` and `article.html`. The blog now becomes the main entry point for [http://bertails.org](http://bertails.org). The previous index page was moved to [http://bertails.org/alex](http://bertails.org/alex) as I intend to use [http://bertails.org/alex#me](http://bertails.org/alex#me) as my [WebID](http://www.w3.org/wiki/WebID).

My mugshot [was taken by](https://www.flickr.com/photos/amyvdh/5837280596/) my friend and ex [W3C](http://www.w3.org) colleague [Amy van der Hiel](https://twitter.com/amyvdh). There are very few pictures of me on the Web :-) I cannot remember where the font icons are coming from though :-/

I couldn't figure out how to use the code highlighter from Pelican. So I took the first one I could find that could run in the browser: [highlight.js](https://highlightjs.org/). I am not super happy with the results so that will probably change in the future:

```scala
case class Foo private (s: String, i: Int, f: Float)
```

What will you find on this blog? Mainly articles about [Scala](http://www.scala-lang.org/) and [Linked Data](http://en.wikipedia.org/wiki/Linked_data). I will maintain RSS feeds for those subjects when the time comes.

Stay tuned!