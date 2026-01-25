---
title: Navigating the Buzzwords of Frontend Development
description: A guide to commonly used jargon in the frontend and full-stack development world.
tags:
  - jamstack
  - webdev
  - javascript
pubDatetime: 2024-04-30T10:23:31.210Z
---

Technical concepts are, by nature, complex and difficult to describe. While developer love to hate buzzwords or jargon, they can serve as very useful shorthand for people "in the know" that simplifies discussing complex concepts by encapsulating them into a single term. They can even help us organize and categorize concepts.

Let's take a quick example. Imagine I am trying to discuss compute that runs in the cloud and typically scales up or down depending on the needs of the application at any given moment and, though it runs on servers, the developer coding for it doesn't need to worry about the servers. That's a lot of words. You'd be forgiven if you got lost in the middle of them. Many of you may already know the term that I am describing though: serverless. Is the jargon imperfect? Yes, but it's a heck of a lot easier to use than the alternative.

## We Love To Hate Jargon

On the other hand, jargon's bad rep is not entirely undeserved. It can be:
* **Exclusionary** – If you don't already know what it means you can easily get left out or confused by discussions that could be relevant to you. Oftentimes, this is combined with a complete lack of explanation of the underlying terms and can even bring embarrassment or ridicule for those not "in the know".
* **Ambiguous** – In many cases, terms start out clearly defined and, as the technology matures and companies and developers pile into trends, they become blurred and amorphous.
* **Appropriated** – The more companies jump on the bandwagon, the more a term can seem like a marketing tool.

Developers and companies often throw out buzzwords and jargon simply assuming you know what it means. This is frequently done in a way that can even folks feel "stupid" for not immediately knowing terms – especially new developers. Heck, I've been in this industry for over 25 years and I still encounter situations where I am left feeling this way. I'm hoping that this guide helps folks feel a bit more confident in understanding some of the jargon they'll frequently hear as a frontend developer.

## Frontend and Full-stack Development is Full of Jargon

We use a lot of buzzwords in frontend development. I'm not even sure that any article could cover them all. Here's the ones I plan to talk about:

* Jamstack
* Composable
* MACH
* Decoupling
* Headless
* Pre-rendering
* SSR, SSG, CSR, ISR, etc.
* Edge
* Middleware
* Islands

I'm going to spend a bit more time on Jamstack because it ends up being relevant, in my opinion, to many of the others.

## Jamstack

Once upon a time, we had static sites. Tools like Jekyll and GitHub Pages helped popularize the concept back in 2008.

![static sites circa 2008](/images/posts/buzzwords/static-sites.png)

But static sounded old fashioned and limiting. I know as I tried (unsuccessfully) to convince my company to adopt them for our company blog and talked about them extensively at various events around this time.

In the hopes of bringing the concept to a broader audience, Matt Biilmann, cofounder and CEO of Netlify, coined the term Jamstack in 2015. This gained a lot of attention when he presented to [Smashing Conference in 2016](https://vimeo.com/163522126).

The original definition emphasized the speed and security that aligned with static sites sprinkled with client-side JavaScript:
>Jamstack is an architecture designed to make the web faster, more secure, and easier to scale. It builds on many of the tools and workflows which developers love, and which bring maximum productivity.
>
>The core principles of [pre-rendering](https://web.archive.org/web/20220718111936/https://jamstack.org/glossary/pre-render), and [decoupling](https://web.archive.org/web/20220718111936/https://jamstack.org/glossary/decoupling), enable sites and applications to be delivered with greater confidence and resilience than ever before.

Conceptually, to me, it was like "static sites++". You'd use a static site generator (Jekyll, Hugo, Middleman were the popular options at the time, though Gatsby had just been released) and you'd enhance them with client-side JavaScript for interactivity and some data loading.

As tools (and Netlify) evolved though, so did the [official definition](https://www.netlify.com/blog/the-jamstack-definition-evolved/) in 2022 ([more details here](https://www.smashingmagazine.com/2021/05/evolution-jamstack/)). The new definition got much more ambiguous because it attempted to incorporate things like server rendering, serverless, headless and a bunch of other terms we'll discuss here:
> Jamstack is an architectural approach that decouples the web experience layer from data and business logic, improving flexibility, scalability, performance, and maintainability.
>
> Jamstack removes the need for business logic to dictate the web experience. It enables a composable architecture for the web where custom logic and 3rd party services are consumed through APIs.

The biggest change was the removal of pre-rendering from the description. This is what I said in [my newsletter](https://jamstack.email) at the time:

> Let's explore a question that we've never explored before: what is Jamstack? !🤣 Of course I kid as we, as a community, have perhaps explored this to death lately. However, it is prescient to talk about it again since Netlify has officially [revamped the definition](https://jamstack.email/link/126499/39ee9d46c5) on Jamstack.org.
>
> The biggest change is that the definition is now the first thing you see on the site. At first glance you may not even notice any dramatic changes in the text but look closer you'll notice **a primary emphasis on decoupling** with _no mention of pre-rendering_, which was a core tenet of the prior definition (so much so, it was called out with its own subsection). I suspect the trend towards hybrid SSG/SSR or even pure SSR frameworks is driving this change in order to keep Jamstack (and the companies that identify with it) relevant as developer tools evolve.

As you may have noticed from both these definitions though, that Jamstack is very focused on the *how* you build your web application, from the tools you use to how you retrieve data to the type of output or rendering you choose. It's an umbrella term that encompasses a ton of other terminology (aka jargon).

![Jamstack is an umbrella term](/images/posts/buzzwords/umbrella.png)

It's worth noting that, though the current usage of Jamstack encompasses all these concepts, they are all separate terms that you can use outside the scope of Jamstack. For example, a site can use SSR that isn't in any way Jamstack. With that being said, let's dig into some of these terms. In fact, while the Jamstack term is still in use, you'll more frequently hear the terms under the umbrella than Jamstack itself.

### What is "decoupling"?

Decoupling is one of those terms that is defined mostly by what it isn't. So, to understand decoupling, I think it's easiest to start with understanding the alternative because it's simpler conceptually.

**Monolithic Architecture** – The frontend and the backend are combined and inseparable.  For example, you can think a more traditional WordPress or Drupal site where all the aspects of the application are lumped together into a single entity. Making changes to the backend requires changes and redeployment of the frontend and vice-vera. Thus the frontend and backend are considered "tightly coupled". 

**Decoupled Architecture** – Decoupling is essentially the opposite of this wherein the frontend and backend are independent of each other. The frontend generally gets data from the backend via APIs. This communication is generally isolated into microservices, meaning that, even when a backend change might require a frontend update, the scope of the changes is typically limited. In addition, an update to the backend can be made without requiring a build and redeploy of the frontend and vice-versa.

### What is headless?

Headless tools often play an important role in a decoupled architecture. A headless tool is one where only the backend exists and any frontend (web, mobile, etc.) can access the data via an API. These tools largely came about to solve the problem of maintaining multiple backends to support both web and mobile apps. The term headless is used to distinguish the tool from alternatives that have traditionally been monolithic such as:

* Headless CMS (ex. Contentful, Sanity, AgilityCMS)
* Headless Commerce (ex. headless versions of Shopify, BigCommerce)

[![headless CMS versus traditional CMS](/images/posts/buzzwords/headless-cms.png)](https://agilitycms.com/resources/guide/what-is-a-headless-cms)

_Source: ["What is a headless CMS?" by Agility CMS](https://agilitycms.com/resources/guide/what-is-a-headless-cms)_

Because of the focus on decoupling, headless tools were commonly considered a core piece of the Jamstack ecosystem.

### What is "pre-rendering"?

Pre-rendering is just a fancy way of saying static, but, in my opinion, it is more accurate.

![I like big words](/images/posts/buzzwords/big-words.jpg)

I could grab Notepad and create a "static site". On the other hand,  pre-rendering is functionally the same as server-side rendering (SSR) but, instead of happening at request time, it happens at build time. Unlike plain static HTML, this is done by running the output of the page template/components and data and generating the assets as part of the build in the same way as any other server rendered page. The only difference is that this happens at build time, so everyone will receive the same rendered output.

### What are CSR, SSG, SSR, etc?

So I mentioned rendering and specifically server-side rendering (SSR). Nowadays, there seems to be a new rendering acronym every month. Below are the ones you are most likely to hear about. It is worth noting that these are the very basic definitions that leave out the nuances to how every front-end framework implements each.

**CSR (client-side rendering)** – Rendering happens in the browser client. This is the way that single-page applications (SPAs) like React, Angular and Vue rendered pages prior to the advent of things like server components. A shell application is loaded and populated with data/content (usually in the form of JSON) that is used to "hydrate" the pages/views. Changing views doesn't reload the whole page, but gets new content/data and updates the rendered output on the client.

**SSR (server side rendering)** – What's old is new again. Once upon a time this was the only rendering available (it's how I started my career building in ColdFusion). Every request by every user is sent to the server where the output is rendered and the returned to the client (i.e. browser). There are definitely differences between how modern frameworks handle this versus my ColdFusion days, but it's conceptually the same thing.

**SSG (static site generation)** – The is the pre-rendering I spoke about earlier. It's a form of server-side rendering done at build time where data and templates are combined to generate static output (primarily HTML, CSS and JavaScript) that can be deployed to the server/CDN as files.

**Incremental Static Regeneration (ISR), Distributed Persistent Rendering (DPR) and Deferred Static Generation (DSG)** – These are various implementations of the same general concept (yes, there are slight differences in implementation that aren't worth going into detail here). Basically, think of this as "deferred rendering", which is like if SSR and SSG had a baby. The request is rendered upon the initial request on the server as static and subsequent requests get the static response (similar to a long-term or persistent cache). It is generally a way to reduce the build times of large sites but still maintain most of the speed benefits of pre-rendering.

## Composable

Developers sometimes complain that the only distinction between Jamstack and composable is that the latter is more "enterprisey". This isn't entirely wrong, as the marketing for Jamstack tools tended to be very bottoms-up (i.e. targeting developers directly), while composable solutions are usually more expensive enterprise solutions.

However, there is more to the distinction.

The term composable is primarily concerned with the backend of your application than either how you build that application or even what type of application it is. Jamstack, as we noted, is more about how you build the frontend of specifically web applications. Composable is about creating a backend that can serve all the various frontends your company may support.

Composable architectures address a problem that arises when you adopt decoupling and headless. That problem is that suddenly you are combining data from a wide variety of sources. Take for instance the diagram shown below wherein an e-commerce site has product data, payment APIs, customer data, inventory APIS and much more.

[![Composable architecture](/images/posts/buzzwords/composable.png)](https://commercetools.com/blog/how-do-composable-headless-and-mach-compare-the-key-differences-explained)

_Source: ["How do composable, headless and MACH compare? The key differences explained" by CommerceTools](https://commercetools.com/blog/how-do-composable-headless-and-mach-compare-the-key-differences-explained)_

Composable tools tend to target enterprises because they tend to feel this problem more acutely, relying on many sources for their data (internal APIs, external APIs, databases, third-party services, etc.). The concept of composable architecture combines all of these sources into a single, consolidated backend API (often using GraphQL). This can greatly simplify the code and architecture of an application because the decoupled frontend doesn't need to concern itself with all the various data sources – it only needs to access the composed data layer. It also makes the backend more "plug and play" in the sense that you can choose the right tool for each job and plug them into the backend.

### So... Jamstack + Composable?

Yep. A composed backend API can be a part of a Jamstack application architecture. The two terms are not mutually exclusive.

### What about MACH?

MACH stands for:

- **M**icroservices 
- **A**PI-first 
- **C**loud-native SaaS
- **H**eadless

This is somewhat interchangeable with composable (and, in fact, composability is one of the core tenets) but a bit more specific in terms of the nature of the stack. The concept is pushed by the [MACH Alliance](https://machalliance.org/), a non-profit industry group supported by a number of companies within the stack.

## Edge

To understand the edge, you have to understand what a Content Delivery Network (CDN) is.

**CDN** – A CDN is a globally distributed group of servers that allows you to serve content closer to the user's geographic location. This was traditionally just static assets (ex. you might have an image CDN) but it played an important role the origin of Jamstack. The static assets that are generated as part of your web app such as Netlify, Vercel or Cloudflare are deployed across their CDN network. It's part of what made Jamstack fast.

The common usage of the term edge nowadays is generally referring to compute (think serverless functions) that runs at the CDN level ("at the edge"), close to the users. This can reduce the latency running compute compared to calling a typical serverless function deployed to a single region, but that is far from universal and edge compute can even cause additional latency in some cases (though that's an article in itself).

There is also a lot of variance across providers in terms of the number and geographic distribution of edge nodes/regions. Some vendors have hundreds of edge nodes while others have maybe a dozen. The importance of this really depends on the type of application that you are building and the type of compute you are running at the edge.

### Middleware

![middleware](/images/posts/buzzwords/middleware.png)

One of the interesting capabilities of edge functions beyond the potential for reduced latency is that they can intercept a user's request and response. This allows them to modify or redirect either, opening up a ton of use cases that can be done without less performant client-side or server-side solutions. Middleware is a term most often used to describe a capability within a full-stack framework that intercepts the request and/or response to the server using edge compute.

## Islands

Islands is a term that has only more recently gained a lot of attention. It's a web architecture that aims to address the problem of ever increasing JavaScript bundle sizes for applications, particularly the single-page applications (SPAs) built using frameworks like React, though it tends to be targeted more at content-focused web apps. It's become popular via newer web application frameworks, notably Astro.

In a SPA, the entire page is interactive and loaded via JavaScript, regardless of whether what it is displaying requires the interactivity. However a typical page is generally some combination of static content and interactive elements. Your site's home page, using Jason Miller's canonical example shown below, may have an interactive navigation and image carousel, but the other aspects do not require interactivity.

[![islands architecture diagram](/images/posts/buzzwords/islands-architecture.png)](https://jasonformat.com/islands-architecture/)

_Source: [Islands Architecture by Jason Miller](https://jasonformat.com/islands-architecture/)_

In an islands architecture, only those interactive elements get the necessary JavaScript to run rather than the entire page. This can potentially reduce the JavaScript bundle by a substantial amount depending on the nature of the page.

## But, wait, there's more...

Ultimately, this was always going to be a very incomplete list. There are plenty of buzzwords I didn't have time to cover and plenty more I may not even know myself. Plus, new ones are created all the time, so keeping up can be difficult. Still, I hope that this has been helpful to at least give you a foundation in some of the terms you may have been unfamiliar with.