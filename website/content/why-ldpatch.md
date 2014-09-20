Title: Why LD Patch
Date: 2014-09-18
Slug: why-ldpatch

The [LDP Working Group](http://www.w3.org/2012/ldp/) recently published [LD Patch](http://www.w3.org/TR/ldpatch/), <cite>a format for describing changes to apply to Linked Data. It is suitable for use with [HTTP PATCH](http://tools.ietf.org/html/rfc5789), a method to perform partial modifications to Web resources.</cite>

After explaining the need for a PATCH format for Linked Data, I will go through all the [other candidate technologies that the group considered](http://www.w3.org/TR/2014/WD-ldpatch-20140918/#alternative-designs), before explaining the rationale behind LD Patch. It is fair to remind the reader that the group is still eager for feedback, and that **not all the group participants would agree with the views expressed in this post**.


Genesis {id="genesis"}
-------

In this post, I consider Linked Data as the intersection of RDF and HTTP: the RDF resources all live in documents accessible on the Web. The store-oriented view of the world does not apply here and [LDP](http://www.w3.org/TR/ldp/) specifically defines how to interact (read/write) with Linked Data resources in a RESTful way. I encourage you to read the [primer](http://www.w3.org/TR/ldp-primer/) for a good introduction.

Despite strong interest from the group participants in a way to partially update LDP Resources with [HTTP PATCH](http://tools.ietf.org/html/rfc5789), settling on which format to use proved to be more difficult than expected. The group could only agree on standardising the use of PATCH over POST, and decided to wait for concrete proposals while allowing the main specification to reach completion.

Work on a PATCH format for LDP got on a limbo for a while, and concretely resumed during the [5th face-to-face](http://www.w3.org/2012/ldp/wiki/F2F5#Day_3_-_Thursday_April_17), where I presented all the proposals [the group had gathered so far](https://www.w3.org/2012/ldp/wiki/LDP_PATCH_Proposals). I also had complete implementations of both [Eric](http://www.w3.org/People/Eric/)'s [SparqlPatch](http://www.w3.org/2001/sw/wiki/SparqlPatch) and [Pierre-Antoine](http://liris.cnrs.fr/~pchampin/en/)'s [rdfpatch](https://github.com/pchampin/rdfpatch) in [banana-rdf](https://github.com/w3c/banana-rdf). Those two proposals were for me the only two serious challengers. But of course, [SPARQL Update 1.1](http://www.w3.org/TR/sparql11-update/) was really the first thing the group ever considered.

A PATCH format for LDP {id="patch-format"}
----------------------

Enough talking. What do we even mean by a *PATCH format for LDP*? Consider the following RDF graph:

```
$ GET -S -H 'Accept: text/turtle' http://www.w3.org/People/Berners-Lee/card
200 OK
@prefix schema: <http://schema.org/> .
@prefix profile: <http://ogp.me/ns/profile#> .
@prefix ex: <http://example.org/vocab#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .

<http://www.w3.org/People/Berners-Lee/card#i> a schema:Person ;
  schema:alternateName "TimBL" ;
  profile:first_name "Tim" ;
  profile:last_name "Berners-Lee" ;
  schema:workLocation [ schema:name "W3C/MIT" ] ;
  schema:performerIn _:b1, _:b2 ;
  ex:preferredLanguages ( "en" "fr" ).

_:b1 schema:name "F2F5 - Linked Data Platform" ;
  schema:url <https://www.w3.org/2012/ldp/wiki/F2F5> .

_:b2 a schema:Event ;
  schema:name "TED 2009" ;
  schema:startDate "2009-02-04" ;
  schema:url <http://conferences.ted.com/TED2009/> .
```

Even if you are not well-versed in RDF and [Turtle](http://www.w3.org/TR/ldp/), I bet you can understand that this piece of data is about a person named Tim Berners-Lee, identified by the URI `<http://www.w3.org/People/Berners-Lee/card#i>`. Also, TimBL seems to have been a participant in two events, each of them having some data attached to them. Also, do you see how those `_:b1` and `_:b2` identifiers give you more flexibility than plain JSON? They are **local to this graph** and we call them [blank nodes](http://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/#section-blank-nodes). 

@@http://bertails.org/2014/09/rdf-graph.png @@

As a side note, let me bring your attention on the URIs used here: there are all backed by real documents on the Web, including those from [schema.org](https://schema.org/) and Facebook's [Open Graph Protocol](http://ogp.me/), they denote real concepts.

Now, let's imagine that TimBL wants to add some geo coordinates to the TED event.

RDF Patch / TurtlePatch {id="simple-patch"}
-----------------------

Here is what TimBL could do with RDF Patch:

```
Add _:b2  <http://schema.org/location> _:loc .
Add _:loc <http://schema.org/name> "Long Beach, California" .
Add _:loc <http://schema.org/geo> _:geo .
Add _:geo <http://schema.org/latitude> "33.7817" .
Add _:geo <http://schema.org/longitude> "-118.2054" .
```

Well, not exactly.

Remember when we said that the blank node `_:b2` was an **local identifier** for the graph? That means that TimBL **cannot speak directly** about the TED event in the document. That would require for the server and the client to agree on a stable identifier for that blank node. That process is called [skolemization](http://www.w3.org/wiki/BnodeSkolemization). It brings a lot of burden on the server to manage those stable identifiers. Also, while the use of blank nodes is transparent in Turtle and JSON-LD, skolemization would break the syntax.

[TurtlePatch](http://www.w3.org/2001/sw/wiki/TurtlePatch) has similar expressive power than RDF Patch (plus *blank nodes as wildcards* in triple deletion), but it is defined as a subset of SPARQL Update. It also defines [skolemization as part of the protocol](http://www.w3.org/2001/sw/wiki/TurtlePatch#Handling_Blank_Nodes), where the client can ask for a skolemized version of the graph, which would then be required before PATCHing.

[Blank nodes happen are very frequent in the wild](http://www.websemanticsjournal.org/index.php/ps/article/view/365) and skolemization was a no-go for several participants of the group. But the result of a [strawpoll](http://www.w3.org/2013/meeting/ldp/2014-04-17#line0243) was welcomed with surprise:

> I'd rather have a solution that (a) doesn't address certain pathological graphs, or (b) requires the server to maintain Skolemization maps

The group was largely in favor of (a), while (b) had basically no support. Knowing that, the group could now focus on SparqlPatch, and on what would later become LD Patch.


SparqlPatch {id=sparqlpatch}
-----------

[SparqlPatch](http://www.w3.org/2001/sw/wiki/SparqlPatch) was proposed by Eric Prud'hommeaux, an editor for the SPARQL query language. SparqlPatch is a profile for SPARQL Update, as it is defined as a subset of it: a valid SparqlPatch query is always a valid SPARQL Update query, with the same semantics.

Why not full SPARQL Update? Well, SPARQL Update comes with a complex machinery for matching nodes in a graph store. Complexity is never a bad thing when it is justified, which is the case for most SPARQL applications. But it is definitely overkill in the context of LDP, hence this proposal.

With SparqlPatch, TimBL could update his profile with the following query:

```
$ POST

204?

INSERT {
 ?ted  <http://schema.org/location>  _:loc .
 _:loc <http://schema.org/name>      "Long Beach, California" .
 _:loc <http://schema.org/geo>       _:geo .
 _:geo <http://schema.org/latitude>  "33.7817" .
 _:geo <http://schema.org/longitude> "-118.2054" .
}
WHERE {
 ?ted schema:url <http://conferences.ted.com/TED2009/>
}
```

The `WHERE` clause would bind the variable `?ted` to the one node satisfying the `schema:url` constraint, and that variable can be used to add new triples.

This is definitely better and worth considering, as we now have a way to PATCH graphs with blank nodes. But...

The runtime complexity for matching nodes in a graph is known to be extremely bad in some cases. While SparqlPatch is better that SPARQL Update in that regard, there are still some issues, which become apparent only when you start implementing and think about the runtime semantics. The main data structure in the SPARQL semantics is the [Solution Mapping](http://www.w3.org/TR/2013/REC-sparql11-query-20130321/#sparqlSolutions), which keeps track of which concrete nodes from the graphs can be mapped to which variables, and that for each clause in the `WHERE`. So the [semantics of the Basic Graph Pattern](http://www.w3.org/TR/2013/REC-sparql11-query-20130321/#BGPsparql) (ie. all the clauses in the SparqlPatch's `WHERE`) involves a lot of costly cartesian products. Finally, the writer of the query cannot rely on the order for the clauses as they don't matter.

SPARQL Update can also be confusing in that if

Another issue is the semantics of `DELETE`/`INSERT` when binding variables: for example, if a variable is not bound to any variable

Another issue is the semantics of 


```
@@@
```

SPARQL Update seems to do the job, so why not using it as the default PATCH format for LDP? 

In the context of LDP, this complexity was not deemed justified:

* 
* SPARQL is hard to implement completely, correctly, and efficiently
* SPARQL has a pretty bad reputation among developers, because of its *perceived* complexity
* most of the features are totally overkill for the purpose of a PATCH
* and other things, read below :-)

So because having **full** SPARQL Update as a dependency for LDP was not possible, a viable proposal was to consider a profile for SPARQL Update.






Actually, the example above would also be a valid SparqlPatch query.

SparqlPatch





RDF Patch {id="rdf-patch"}
---------

simple, but also requires unusual handling of blank nodes


Blank Nodes {id="bnodes"}
-----------



SPARQL Update {id="sparql-update"}
-------------







restricted to a simple subset of SPARQL 1.1 Update



* motivations for LD Patch / use case

* SPARQL Update

* runtime complexity

* semantics: diff vs update

* rdf:list

* SparqlPatch

sparql update profile

less complexity

semantics

runtime complexity

familiar syntax

* RDF Patch + TurtlePatch

excellent complexity

bnodes

still no lists

* LD Patch

doesn't share the sparql semantics

list






* the false good idea of subset syntax

confusing for json patch people:  if match fails, query should fail

overhead of the superset for newcomers