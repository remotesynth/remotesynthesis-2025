---
title: Is "GraphQL Mesh" the Next Big Thing?
description: GraphQL Mesh is a concept that consolidates the many sources of data an application consumes. Do recent acqisitions mean it's about to take off?
tags:
  - general
pubDatetime: 2023-02-13T10:23:31.210Z
---

The human brain excels at pattern recognition. In fact, our ability to detect patterns is so strong that it often happens without our conscious awareness. However, this also means that sometimes we can be quick to see patterns where they may not exist.

Let's take two recent acquisitions, [Netlify's acquisition of Gatsby](https://www.netlify.com/press/netlify-acquires-gatsby-inc-to-accelerate-adoption-of-composable-web-architectures/) and [IBM's acquisition of StepZen](https://techcrunch.com/2023/02/08/ibm-graphql/). Both companies focus on allowing companies to bring together a variety of data sources under a single umbrella via GraphQL  (Gatsby via their Valhalla product, which [I argue](https://remotesynthesis.com/blog/gatsby-plus-netlify/) was the real motivation behind the acquisition).

Is this the beginning of a pattern? Does this mean that GraphQL mesh might be the next big thing? Let's look at what GraphQL mesh is and I'll share my thoughts on where it might be headed.

_For full transparency, I worked for StepZen for a year from 2021 to 2022, but I did not and do not have any financial stake in the company._

## What the heck is a GraphQL mesh?

Let's be clear that "GraphQL mesh" isn't a common industry term. You could argue that I made it up, though [TakeShape](https://www.takeshape.io/), another company in this space, calls it a "GraphQL API Mesh" (not coincidentally, Netlify also invested in TakeShape via their [Jamstack fund](https://www.netlify.com/jamstack-fund/)). So what do I mean by GraphQL mesh?

In modern application development, most companies deal with a lot of data coming from a variety of sources. These may include APIs, both internal and external, as well as databases (cloud-based and/or on-premise) or other third party sources of data. This can add a lot of complexity to your application code.

For example, I might have some business logic that first needs to get user details out of a database, then use that to call an API to get their account status (perhaps whether their account subscription is still active) and then a subsequent API call to get their personalized content. This isn't even a particularly complicated example, but, not only is this a potential bottleneck in your code, it's also complex and fragile.

A GraphQL mesh consumes all of these sources of data and puts them behind a single GraphQL API. This means that my application only needs to know about a single endpoint to consume data from all of these sources and all of the data from the above example can be retrieved via a single API call. In some cases, a very limited amount of the business logic might be encapsulated in the GraphQL mesh. For instance, the mesh knows how to tie the database and the account details together and that, if the account is inactive, it won't get personalized content.

_As a side note, if you're curious how some of this works, I'm hosting a talk by Alex Patterson of Appwrite on [how to turn your REST APIs into GraphQL](https://cfe.dev/events/better-rest-through-graphql/) tomorrow, February 14, at 1pm ET (GMT -5)._

## Is this the start of a pattern?

So do the two acquisitions, coming so closely together represent a pattern that indicates that GraphQL mesh is something we should really start devoting our attention to? My personal view, having worked in this area, is a bit skeptical. I think a GraphQL mesh can be a valuable tool as part of a larger platform (so acquisitions make perfect sense in this case), but I also see less of a pattern in these acquisitions despite some of the similarities in product and timing.

### Gatsby Valhalla

Gatsby's Valhalla makes a ton of sense as part of a Netlify platform offering. One of the most complex parts of the Jamstack architecture is bringing together data from a potentially wide variety of sources (cloud databases, APIs, headless CMS, user management, etc.). This complexity has led developers towards a "[backend for frontends (BFF)](https://samnewman.io/patterns/architectural/bff/)" pattern, but a GraphQL mesh that consumes all of your data and makes it easily available to your web application eliminates the need to build and maintain a complex BFF implementation. 

Gatsby already had ties to Netlify and had an open source project that was a key piece of the Jamstack ecosystem. Their approach to building a GraphQL mesh makes it almost "plug and play" and the API's structure is largely determined by the tool. It is targeted primarily at web developers, which generally aligns with Netlify's target demographic.

### StepZen

StepZen initially positioned itself towards Jamstack developers (thus my interest there at the time) but eventually pivoted towards enterprises. Even before my departure, they were finding more success marketing their solution towards large enterprises that were trying to consolidate their internal APIs, often developed by disparate teams across the organization, into a single backend.

StepZen's solution used a declarative DSL that was GraphQL compatible to generate the mesh. It has a fairly steep learning curve and implementation can take a good deal of work, but it is extremely flexible, allowing fine-grained control over how the API is constructed, which is perfect for teams tasked with managing a company's APIs. StepZen's CEO was a former IBM fellow and senior executive, so the ties there are deep as well. Given its enterprise target, it makes a lot of sense as an IBM offering.

### Why now?

Both these products are useful to solve issues of complexity in application development and I think can become an important offering in their larger respective platforms – Valhalla for web developers using Jamstack and StepZen for API developers at large enterprises. But I'm going to be brutally honest here. The real pattern is that [VC Funding is drying up](https://www.bloomberg.com/news/articles/2022-12-07/venture-capital-deals-set-for-worst-drop-in-over-two-decades). I suspect both Gatsby and StepZen were at or near the end of their current runways and joining companies with which they had longstanding relationships made sense out of necessity. In that sense, I do think we'll see more consolidation of startups in the near future, but not necessarily specific to areas around GraphQL mesh.