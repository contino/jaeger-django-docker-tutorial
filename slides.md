---
title: "Plugging Performance Holes with Distributed Tracing"
separator: <!--s-->
verticalSeparator: <!--v-->
---

### Plugging Performance Holes with Distributed Tracing

**Carlos Nunez**

*2019 April 3*

---

## Web app hotspots are hard

<!-- .slide: data-background=./assets/images/traffic.jpg -->

Note: You have a web application that _mostly_ performs well. When it doesn't perform well,
however, you're not sure where to begin. You have a bunch of logs from your web server and backing
services and a lot of data points to reference, but finding hotspots is still difficult.


<!--s-->

<!-- .slide: data-background=./assets/images/tracks.png -->

## Tracing finds hotspots.

Note: Tracing helps here. Much like how system administrators would find slow syscalls with `strace`,
tracing platforms plug into running services and collect information about how long _things_ take
over time. This way, you can find and alert on interesting slowdowns as they occur.

<!--s-->

## Talk Goals

![](./assets/images/goals.png)

* What's Tracing?
* How does it work?
* What's Jaeger?
* How does Jaeger work?
* Demo
* Questions

<!--s-->

# What's Tracing?

From [the OpenTracing project](https://opentracing.io/docs/overview/what-is-tracing/)

> Distributed tracing, also called distributed request tracing, is a method used to profile and
> monitor applications, especially those built using a microservices architecture. Distributed
> tracing helps pinpoint where failures occur and what causes poor performance.

Notes: There is a lot going on in a single webapp. There is even more going on with a distributed
system of web applications. Tracing helps by profiling interesting characteristics behind various
network calls such as request times and timestamps.

<!--s-->

# What Tracing *Is Not*

* Tracing is *not* logging (though it can supplement interesting logs)
* Tracing is *not* performance monitoring (though it helps)
* Tracing is *not* monitoring (though it's a component of it)

<!--s-->

# Spans

A _span_ is a unit of work done, i.e. a "thing"

<!--s-->

# Traces

Traces are collections of _spans_ that describe an event within the life of a system.

<!--s-->

# A General Example

![](./assets/span-vs-trace.png)

Note: This graph is interesting. Notice how individual events (A through E) are spans, i.e, things
that happened. The entire duration of an event that A through E were a part of is the _trace_.

<!--s-->

# A More Realistic Example

![](./assets/zipkin-example.png)

# Other Terminology

- *Logs*: Key-value pairs that are associated with spans to help tell more of a story.
- *Tags*: Attributes that are associated with spans that help describe them.

<!--s-->

# What's Jaeger

![](./assets/jaeger-logo.png)

Jaeger is an implementation of OpenTracing from Uber that provides a system for collecting, reporting and
exporting traces for distributed applications.

# How Does Jaeger Work?

![](./assets/jaeger-architecture.png)

Note: Things to keep note of:

- *jaeger-agent*: Runs alongside your application. This is what your code talks to so that it can
  collect traces.
- *jaeger-collector*: Collects Jaeger spans and traces from various `jaeger-agents`. It uses the
  Thrift protocol to do this, but it supports others. It also uses Cassandra as a backing store, but
  it can use others.
- *jaeger-client*: These are the libraries that are used to create and send spans to the
  `jaeger-agent`.
- *jaeger-query*: Processes queries performed on the Jaeger frontend.

<!--s-->

# Demo

![](./assets/absolutely-nothing-will-go-wrong.png)

<!--s-->

# Questions?

<!--s-->

# Thanks!
