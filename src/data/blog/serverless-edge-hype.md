---
title: Does the Serverless Edge Live Up to the Hype?
description: A lot of promises have been made about the serverless edge. Does it meet them?
tags:
  - serverless
pubDatetime: 2023-01-09T10:23:31.210Z
---

As developers, we've become accustomed to broken promises. The more hype that surrounds a technology, the more likely we are to find the end result doesn't quite live up to its initial promises. And, let's be honest, serverless edge technologies have gotten a lot of hype lately. Here's just a sampling.

![serverless edge headlines](/images/posts/edge-hype.png)

I wouldn't blame you for being skeptical of these claims, as serverless arguably has a history of broken promises. Corey Quinn, a very well known expert on AWS and serverless, [wrote in November 2021](https://www.lastweekinaws.com/blog/the-unfulfilled-promise-of-serverless/):

> Say what you will about serverless, it’s failed to live up to its promise and hasn’t proved to be particularly lucrative for anybody.

He went on to illustrate three key areas where serverless has failed to meet lofty expectations. Personally, while I'm a big believer in serverless in general, I won't argue that in many cases it hasn't lived up to the hype.

## Jamstack gets edgy

CDNs (Content Delivery Networks) have been around for a long time, but the first time I personally encountered the concept of deploying an actual application to a CDN was via the Jamstack. The idea was that each user would get the static assets for the site from the CDN closest to them, reducing latency and making your app faster.

This worked great when Jamstack was heavily focused on pre-rendered (i.e. static) assets, but the equation became more complex when your application made a lot of data calls. [As Chris Coyier points out](https://chriscoyier.net/2022/05/04/it-doesnt-much-matter-how-cdny-your-jamstack-site-is-if-everything-important-happens-from-a-single-origin-server-edge-functions-are-probably-part-of-the-solution/), your data is probably still tied to a specific location or region.

> But don’t fool yourself into thinking you’re really a CDN-hosted site and you’re being as fast as you can be worldwide. Your Australian users are still hitting some server in metaphorical-Oregon (US-WEST-2 or whatever) for the data-that-matters and it will be slow.

Chris goes on to talk about how edge functions may help to resolve this problem. It is core to the promise of edge functions, so let's review.

### Edge Function Basics

A typical web application would get deployed to a single server region. For example, in AWS terms, I might choose to deploy my application to us-east-1. Every user that connects to that application would then receive it from that location, regardless of where in the world they are connecting from.

![application deployed to a single region](/images/posts/region.jpg)

Jamstack moved the assets up close to the user at the CDN level, but the serverless functions and data would still typically be deployed to a single server region. In this case, API calls made from the frontend still need to traverse the distance to the server region where the functions and data are deployed. This means that the static assets load fast, but latency still exists populating the page data.

![a typical jamstack site](/images/posts/jamstack.jpg)

Edge functions aim to solve this problem, by bringing some (or all) of the backend processing up to the CDN level in proximity to the user. So it's no longer just static assets on the CDN but actual compute is being performed there as well. In an ideal world, it might look something like this image from the [Remix blog](https://remix.run/blog/remix-and-the-edge), where every user request has static assets fulfilled by the CDN and backend content and data also fulfilled by the CDN via edge functions.

![ideal edge solution architecture](/images/posts/edge-remix.png)

Source: https://remix.run/blog/remix-and-the-edge

## Does the edge live up to its promises?

How does serverless edge live up to this promise of reduced latency? What about other promises about the edge that you may have read? Let's dig into these.

### Promise: Reduced latency

* ✅ Backend calls go to the CDN geographically closest to the user.
* 🤔 Geographic latency may not be the critical issue in your site's performance
* ❌ Your database or other backend APIs may still be region locked

So the biggest selling point of edge functions is that they will automatically improve the performance of your app simply by reducing the latency of any backend API or server-side rendering (SSR) calls. They do actually achieve that promise in terms of the actual function call, which will now hit the CDN closest to the end user rather than a function deployed to a single region that may be across the globe.

The first thing to consider is that, unless you are building games or IoT, latency caused by distance, while not worth ignoring, may not be the critical aspect to improving your site's performance. Things like reducing the JavaScript you send to the client, improving image size and compression or removing third-party scripts are all other optimizations that may gain you more traction.

I'm not trying to dismiss the cost of geographic latency as it can add up. As [this article points out](https://www.snapt.net/blog/how-geographic-distance-affects-latency), data going from US West to Central Asia, for example, could take up to a few seconds. So this is a legitimate selling point that edge functions can live up to *when used properly*.

What do I mean by "used properly"? Well that gets at the biggest potential drawback to edge functions when it comes to reducing latency: if your edge function needs data, that data may still be region locked.

![the edge and your data](/images/posts/batman.png)

For example, if your edge function calls an API or database and that API is region locked, you may not see the performance gains you are expecting. This is why it is critical that, when thinking about what processing you are moving to the edge, you also think about where the data this processing depends on exists. There are some solutions to these (ex. edge KVs, databases and caching), but these may involve larger changes to your application than you anticipated.

Which brings us to promise number two.

### Promise: It's easy

* ✅ It's just JavaScript, so there's a low barrier to entry and lots of framework support
* 🤔 Runtimes are often not Node-based, so you may not have all your favorite tools
* ❌ Every provider is unique and choosing one isn't easy

Another promise you may hear about edge functions is that it's super easy to get started – and there's definitely truth to this. First of all, on nearly every provider, you can just use JavaScript, while some providers support other languages as well. There are also a growing number of frameworks and tools that can help you build for the edge.

You need to be aware that the edge runtimes are mostly not Node-based, so you can't always bring your npm-based tools with you. If you are trying to migrate existing code to the edge and that code relies on npm tooling, this may require a more extensive refactoring than you may have expected. Plus, most providers have different runtimes and APIs, so there's definitely a learning curve as you get aquainted with their offering and quirks. This also means that your code is likely not easily portable across providers.

### Promise: Additional capabilities

* ✅ Edge functions can intercept the request or response 
* 🤔 Um...actually, this is just cool
* ❌ I got nuthin

Where I get more excited about edge functions from a developer standpoint is where it can actually allow me to do things that previously were much more difficult. Edge functions offer the capability of intercepting the request and response, which can be incredibly powerful.

Your edge function - or middleware as some frameworks call it - will be called when the request comes in before it hits the origin server. It can modify that request, redirect it - so no need for slower server-side or client-side redirects or you can even handle access and authentication at this point.

![intercepting the request](/images/posts/edge-functions-request.jpg)

The edge function can even fulfill the response itself. For example, if you have static assets like HTML, CSS, images and more cached on the edge, you can simply respond without hitting the origin server.

![fulfilling the response at the edge](/images/posts/edge-functions-request-response.jpg)

If you haven't redirected or fulfilled the request, it continues to the origin server to be fulfilled.

![request goes to the origin server](/images/posts/edge-functions-origin-server.jpg)

When that response comes back, your edge function can intercept it again. In this case, you can do things like modify the response. For example, you might add headers that have user specific information or, in most cases, you can even modify the HTML of the response.

![intercepting the response](/images/posts/edge-functions-request-completed.jpg)

This enables you to do some really cool things, like make a dynamic, user-specific response based upon a completely static HTML asset or modify the response for A/B testing at the edge with no flash of content. For some examples, check out Salma Alam-Naylor's [post on using Netlify's edge functions to add personalization](https://whitep4nth3r.com/blog/add-personalization-to-static-html-with-edge-functions-no-browser-javascript/). 

## What can I do with edge serverless?

Now that we've covered some of the key benefits and limitations of the edge, here are some of the things you might consider doing using edge functions: 

* **A/B Testing** – You can replace out HTML content for A/B tests without any flash of rendering.
* **Updating/Modifying/Custom HTTP headers** – You can add custom http headers that might be used for adding CORS to certain requests or control access to content.
* **Conditional routing** – You can route user's to a new location for instance if they are not authenticated or route them to the appropriate localized version of the site.
* **SEO** – You can serve a version of the page that is optimized for being read by search crawlers when they are detected.
* **User authentication/authorization** – You can handle validating authentication and authorization at the edge and redirecting or limiting access if necessary.
* **IoT/Gaming** – Latency is critical for IoT or gaming applications, and edge functions can help remove that latency.
* **Personalization** – You can personalize the output of the page based upon user information. For example, you can show the user's login state without any flash of rendering. 
* **Compliance** – You can serve up different versions of the page depending on the user location to meet location specific compliance issues. For example, you can show cookie acceptance to users specifically in the EU.

These are just a handful of ideas. There's plenty more possibilities with serverless edge functions. While I have discussed some areas that edge functions may not live up to the promises that you've been hearing or reading about, I am definitely a believer in their capabilities and think they will become an important part of modern application architecture going forward.

So how can you get started? That'll be the topic for my next post.