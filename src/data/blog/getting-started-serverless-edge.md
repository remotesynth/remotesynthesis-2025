---
title: "Getting Started with Serverless Edge - Exploring the Options"
tags:
    - serverless
description: There are a lot of options when it comes to edge functions, let's explore what they are and how they are different.
pubDatetime: 2023-01-23T10:23:31.210Z
---

There are a lot of options for serverless edge functions and services – and the list seems to get longer every day. It can be difficult to judge them too, because often you aren't comparing apples to apples. You might be comparing an offering that actually sits on top of another companies infrastructure with the offering from the infrastructure provider or even just a framework that makes it easy to deploy edge functions.

It can be confusing. In this post, I hope to help you get an overview of the various offerings and how they compare. There are a couple of caveats to get out of the way first:

* This is not a comprehensive list. I have tried to include the major offerings but I definitely have not included everything.
* This is not a ranking. I have not used all of these services, so I am not in a position to evaluate and rank all of them.
* I am looking at these services purely from the perspective of a web/front-end developer. Edge functions have uses beyond the web but that sits outside my own areas of expertise.

> Check out my [last post](https://remotesynthesis.com/blog/serverless-edge-hype/) where I discussed the promise of edge serverless as well as potential use cases.

## Categories of Edge Serverless

As I mentioned, part of the problem of evaluating edge serverless offerings is that you are often comparing two very different things that are labeled the same. To help clarify, I've created categories that I think best describe these offerings. They are:

### Core Edge Serverless

These are the companies (mostly CDN companies) who have compute offerings like serverless edge functions, databases and more. While they have their own offerings, they also own the infrastructure upon which the other categories rely.

These include the following:

- [Cloudflare Workers](https://workers.cloudflare.com/)
- [Deno Deploy](https://deno.com/deploy)
- AWS ([Lambda@Edge](https://aws.amazon.com/lambda/edge/), [Cloudfront Functions](https://aws.amazon.com/blogs/aws/introducing-cloudfront-functions-run-your-code-at-the-edge-with-low-latency-at-any-scale/))
- [Fastly Compute@Edge](https://www.fastly.com/products/edge-compute)
- [Akamai EdgeWorkers](https://www.akamai.com/products/serverless-computing-edgeworkers)
- [Stackpath](https://www.stackpath.com/)
- [Azion](https://www.azion.com/en)

### Edge Platforms

These are services that offer things like edge functions that are built on top of the core edge serverless offerings. The goal of these is usually to improve the developer experience of building edge serverless through continuous deployment while also integrating it with your broader projects, like adding edge functions into your web site codebase or your database.

Here are some examples of edge platforms with the core edge serverless offering they are built upon listed in parentheses.

* [Netlify Edge Functions](https://www.netlify.com/products/#netlify-edge-functions) (Deno)
* [Vercel Edge Functions](https://vercel.com/features/edge-functions) (Cloudflare)
* [Supabase Edge Functions](https://supabase.com/docs/guides/functions) (Deno)
* [Cloudflare Pages Functions](https://developers.cloudflare.com/pages/platform/functions/) (Workers)

### Edge-enabled Frameworks

These are full-stack web frameworks that enable you to automatically deploy edge functions as part of your web application code.

* [Next.js](https://nextjs.org/docs/api-reference/edge-runtime)
* [Astro](https://astro.build/) (Example the [Netlify SSR Integration](https://docs.astro.build/en/guides/deploy/netlify/#adapter-for-ssredge))
* [SvelteKit](https://kit.svelte.dev/) (See examples from [Vercel](https://vercel.com/templates/svelte/sveltekit-edge-functions) and [Netlify](https://www.netlify.com/blog/sveltekit-with-netlify-edge-functions/))
* [Eleventy](https://www.11ty.dev/) (Using the [Eleventy Edge plugin](https://www.11ty.dev/docs/plugins/edge/) that is Netlify only)
* [Remix](https://remix.run/) (Using [adapters](https://remix.run/docs/en/v1/other-api/adapter))
* [Fresh](https://fresh.deno.dev/) (Built by Deno)

### Edge Databases

This is a relatively new category, but these are databases that replicate to the edge (note that I am not including data stores, though some of the prior core and platform offerings do offer a means of storing key/value or cached data at the edge). As I mentioned in the [prior post](https://remotesynthesis.com/blog/serverless-edge-hype/), where your data lives is a core consideration when choosing to use an edge function.

* [Fauna](https://fauna.com/) – A serverless database with built in global replication and strong consistency.
* [Planetscale Portals](https://planetscale.com/blog/introducing-planetscale-portals-read-only-regions) (public beta) – A serverless MySQL database with support for replicating to read-only regions.
* [Cloudflare D1](https://blog.cloudflare.com/whats-new-with-d1/) (still in private beta) – A SQLite based relational database that has globally replicated reads.
* [DGraph](https://dgraph.io/) – A distributed GraphQL database with a graph backend.

## Which Option Should You Choose?

Of course, it depends.

If you are already tied to an existing CDN provider like Fastly, Akamai or Cloudflare for your existing infrastructure, then choosing their offerings may offer the easiest runway to get going. Edge platforms offer an easy option for those who have a greenfield project or are already deploying to these services and want an easy way to get started integrating edge functions while integrating them into new/existing web applications codebases.

If you are using an edge platform, you may also want to consider integrating an edge-enabled framework. This can greatly improve the developer experience of integrating edge functions into you web project.

In all cases, if your edge function(s) will be calling some form of data, you need to consider where that data will live. You don't want to move a function to the edge that relies on data that potentially comes from across the globe, thereby negating some/all of the benefit of moving to the edge. In some cases, an integrated K/V or cache will suffice, but if you need a full database, these services are worth exploring.

In the next post in this series, I will explore a few of the options that I listed a little bit deeper.