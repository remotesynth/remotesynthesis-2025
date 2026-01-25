---
title: What is Jamstack in 2023?
description: Yes, it's become extremely vague but the term still retains some value for developers.
tags:
  - jamstack
pubDatetime: 2023-01-16T10:23:31.210Z
---

I've been writing these yearly updates for the past few years, in part because we've seen a lot of dramatic change in what we call Jamstack over those years. Prior to 2020, we were still largely talking about static sites that were decorated with interactivity via client-side JavaScript and APIs. In light of the change over the past few years, the idea of building sites that way can sound quaint.

_If you're into Jamstack, which I'm guessing you are because you are reading this, you'll definitely want to join me (virtually) at [TheJam.dev](https://thejam.dev) on January 25-26. It's 2 days of amazing speakers all about Jamstack and it's completely FREE!_

### A look back

At the [start of 2021](https://remotesynthesis.com/blog/jamstack-in-2021/), we were just beginning to consider the implications of combining SSR and pre-rendering. This came to the forefront largely via Next.js which was becoming increasingly popular. At the time I pushed for thinking about Jamstack as "static-first but not static only," with the idea being that it was ok to allow for SSR into a concept based primarily on pre-rendering, as it broadened the scope of problems the Jamstack could solve.

![I guess SSR is Jamstack now](/images/posts/ssr-meme.jpg)

A [year ago](https://remotesynthesis.com/blog/jamstack-in-2022/), we started talking about islands architectures introduced by both Slinkity and Astro that helped reduce the JavaScript payload to the client. I lamented the growing complexity of Jamstack tools. Many of us were drawn to Jamstack for its simplicity, but the proliferation of rendering methods (ISR, DSG, SSR, SSG, DPR) and integrations had seemed, to me, to cause Jamstack to lose sight of that simplicity.

This continued expansion of what a Jamstack site could be caused many of us to spend an inordinate amount of time debating what the heck Jamstack is anymore. At last year's [TheJam.dev conference](https://cfe.dev/events/the-jam-2022/), Fred K. Schott, creator of Astro, even had [a talk that he called an "intervention"](https://cfe.dev/sessions/jamdev2022-what-is-jamstack/) based on the idea that "no one is on the same page about what Jamstack means today."

Things have not gotten any less confusing.

## What happened in 2022?

![2022 Jamstack timeline](/images/posts/2022-jamstack-timeline.jpg)

Here's a (incomplete) timeline of significant events that occurred in the broader Jamstack ecosystem in 2022:

* Jan 12 – [Astro became a company](https://astro.build/blog/the-astro-technology-company/)
* Jan 9 – [Eleventy hit 1.0](https://github.com/11ty/eleventy/releases/tag/v1.0.0). It gets [funded full time developement](https://www.11ty.dev/blog/eleventy-oss/) via Netlify in Febuary.
* April 19 – [Netlify launches edge functions](https://www.netlify.com/blog/announcing-serverless-compute-with-edge-functions/)
* April 28 – [Redwood V1](https://v1launchweek.redwoodjs.com/)
* May 23 – [SolidJS gets development funding via Netlify](https://dev.to/ryansolid/when-netlify-asks-you-to-full-time-oss-you-say-yes-5ccf)
* June 28 – [Deno releases Fresh 1.0]( https://deno.com/blog/fresh-is-stable)
* July 11 – [Netlify changes the Jamstack definition](https://www.netlify.com/blog/the-jamstack-definition-evolved/)
* Aug 9 – [Astro 1.0](https://astro.build/blog/astro-1/) 
* Aug 9 – [Docusaurus 2.0](https://docusaurus.io/blog/2022/08/01/announcing-docusaurus-2.0)  is finally released as a complete ground up rewrite
* Oct 25 – [Next 13](https://nextjs.org/blog/next-13)
* Oct 31 – [Remix acquired by Shopify](https://remix.run/blog/remixing-shopify)
* Nov 8 – [Gatsby 5](https://www.gatsbyjs.com/blog/gatsby-5/)
* Nov 16 – [Nuxt 3.0 released](https://nuxt.com/v3)
* Nov 17 – [Cloudflare adds Pages Functions](https://blog.cloudflare.com/pages-full-stack-frameworks/)
* Dec 14 – [SvelteKit 1.0](https://svelte.dev/blog/announcing-sveltekit-1.0)
* Dec 15 – [Vercel Edge Functions go GA](https://vercel.com/blog/edge-functions-generally-available)

Let's look at how the definition of Jamstack changed significantly in 2022.

## Jamstack definition changed

In both 2021 and early 2022, we seemed to be inundated with debates about what Jamstack was. So a good place to start is with the revamped definition that Netlify released in July 2022. 

For a refresher, here was the original (all emphasis mine):

> Jamstack is an architecture designed to make the **web faster, more secure**, and easier to scale. It builds on many of the tools and workflows which developers love, and which bring maximum productivity.
>
> The **core principles of pre-rendering**, and decoupling, enable sites and applications to be delivered with greater confidence and resilience than ever before. 

Making the web faster and more secure were two key benefits that have been included since the original definition released in 2015. But these two benefits were tied to the core principle that I highlighted around pre-rendering.

Obviously a pe-rendered site will perform better than a server-rendered site, but Jamstack's frequent dependence on JavaScript frameworks like React had arguably put that benefit into question. Add in the fact that many Jamstack sites now include a heavy dose of server rendering and it's no longer a clear cut case.

The security of Jamstack was also tied to its reliance on pre-rendering. Today's Jamstack sites with SSR, third-party services, cloud databases and so on, are probably no more secure by default than a standard non-Jamstack site.

The [new definition](https://www.netlify.com/blog/the-jamstack-definition-evolved/) that was [announced in July](https://www.netlify.com/blog/the-jamstack-definition-evolved/) removes any mention of pre-rendering and, subsequently, seems to downplay the speed benefits (though it does say it improves performance, that sounds like a less emphatic statement than saying it's faster, at least to my ear) and it removes the security benefits of Jamstack.

> Jamstack is an architectural approach that decouples the web experience layer from data and business logic, improving flexibility, scalability, performance, and maintainability.
>
> Jamstack removes the need for business logic to dictate the web experience. It enables a composable architecture for the web where custom logic and 3rd party services are consumed through APIs.
>
> The best practices for building with the Jamstack evolve alongside modern technologies.

The goal of this definition seems to better fit the broad array of ways people were building and deploying Jamstack apps, from purely static Hugo sites to fully SSR Remix sites, but it did little, in my view, to clarify what makes a site Jamstack beyond decoupling the front-end from the backend.

### What about a different angle?

Laurie Voss and Salma Alam-Naylor took a very different approach in their [Jamstack chapter for the Web Almanac](https://almanac.httparchive.org/en/2022/jamstack) by trying to define Jamstack via the outcomes rather than the tools and technologies. This was dictated somewhat by the kind of data contained in the HTTP Archive, but it also meant that a PHP or .NET site that performed within certain performance criteria would be considered "Jamstack-y" enough to be counted.

In general, I appreciate the the emphasis on outcomes. Over the past few years, Jamstack developers seemed to live under the assumption it was faster. I think a focus on the actual outcomes can hold us all more accountable for our choices. As Zach Leatherman, creator of Eleventy, pointed out in [a recent post](https://www.zachleat.com/web/javascript-community/), despite what may be reported:

>  Remix (67.7 kB compressed) and Next.js (90 kB compressed) have not meaningfully reduced their bundle sizes at all. Measurement reveals that bundles are growing: Next.js was 72.2 kB compressed in 2021.

That being said, purely focusing on outcomes turns Jamstack into more of a broad philosphy than even an "architectural approach."

## So where does that leave us?

If someone new were to ask me how to get started with the Jamstack today, what would I tell them.

1. Start with the tools. In most cases this would be something that falls under the category of static site generator (SSG) but could also include something like Remix which does no actual static generation. Keep in mind that you may not even need a full web framework, so explore tools that can do pure static generation with limited JavaScript like Eleventy, Astro or even Hugo. Personally, I still stick with a "static-first" approach wherever possible.
2. Move on to the services. If this is something other than a personal site, you'll probably need a headless CMS. You may need something for handling authentication like Auth0, Okta, Netlify Identity, etc. and you may need a cloud database like Planetscale, Supabase, Firebase, etc. Obviously, the mix of services depends on the needs of your site. This also includes how I handle some of the additional backend pieces of my site as serverless functions, serverless edge functions, etc.
3. Finally, choose how you will deploy the site. Jamstack sites are typically deployed using a CI/CD process to any number of locations. Ideally this deployment will deploy static assets to a CDN for best performance. In addition, consider your choice on #1 above, as you may need a service that supports your specific choice of tool (i.e. support for server-side logic built into many frameworks for things like SSR or API routes) like Netlify, Vercel, Cloudflare Pages, etc.

There are thousands of permutations of the above and no two sites may have the same stack or architecture, but there are clearly a bunch of overlapping interests for the developers building these sites regardless. For example, you may be using Nuxt while I use Eleventy, but I can still learn about using Supabase from/with you. While I've been unable to find fully reliable data, all indications are that the tools in number 1 and the services in numbers 2 and 3 are only gaining popularity and adoption.

The key thing here is that, while the official definition contains no mention of the tools, but, in my opinion, the reality of how we distinguish between Jamstack and non-Jamstack is in the tools.

# Conclusion

Which leads me to my (perhaps anticlimactic) conclusion. As someone who has worked deeply in and around Jamstack for many years, Jamstack has become more of a "community" than a set of architectural rules.

I don't say that to devalue it.

This community builds things a thousand different ways but each of them have overlapping interests in a common sets of tools, services, strategies and architectures. I can read an article or [book about Jamstack](https://www.manning.com/books/the-jamstack-book), go to a [conference about Jamstack](https://thejam.dev), join a meetup about Jamstack, get a [newsletter about Jamstack](https://jamstack.email) and I know that I will gain information that is applicable to what I am building. There's huge value in that, even if the definition is vague and not prescriptive in any manner.

It's really not all that different than other labels like DevOps, serverless, etc. Are these any less vague? Honestly, I think part of the driver of the issues people have with Jamstack being increasingly nebulous is the term itself and the implications of calling it a "stack" when it clearly never was (even back in the J-A-M days). Yes, we eliminated the JAM and the stack was never really applicable in the truest definition of the word, but, for all its issues, in the years since 2015 when it was introduced, I haven't heard anyone come up with a better term...yet.