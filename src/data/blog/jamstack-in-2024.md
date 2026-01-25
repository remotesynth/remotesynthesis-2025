---
title: What is Jamstack in 2024?
description: All good things must come to an end and so, most likely, must my annual Jamstack update. But what have we lost in the process?
tags:
  - jamstack
pubDatetime: 2024-01-15T10:23:31.210Z
---

This is my fourth year doing this update. Some of you may be wondering, "But Brian, didn't you already proclaim Jamstack dead?" Back in July, I did write a post titled "[Goodbye Jamstack](https://remotesynthesis.com/blog/goodbye-jamstack/)" in response to the end of the Jamstack Discord Community.

My argument was that, if [last year's update](https://remotesynthesis.com/blog/jamstack-in-2023/) proclaimed "Jamstack has become more of a “community” than a set of architectural rules," what happens when there is no longer a place for the community? What happens when everyone filters off into their tool/framework-specific Discord/Slack and there's no longer opportunities to gather and communicate?

But there was nuance to my conclusion that I felt many follow ups missed (emphasis added).

> The term seems to be dead **but the tools and technologies it encompassed are still very much alive**.

Entering 2024, it still feels like the term is on life support, though there may be a tinge of remorse about that. However, the tools that fell under the Jamstack umbrella continue to grow in adoption.

> Interested in the tools and technologies of Jamstack? Don't miss [TheJam.dev on January 24-25](https://thejam.dev) featuring speakers including Alex Russell, Cassidy Williams, James Q Quick, Matt Biilmann, Zach Leatherman, Salma Alam-Naylor and many more. It's free!

## A Brief 2023 Timeline

First, here's a (very incomplete) list of some of the big announcements in 2023:

**January**

* [First beta of Eleventy 2 release](https://www.11ty.dev/blog/eleventy-v2-beta/)
* [Astro 2.0 adds type-safety for Markdown and MDX](https://astro.build/blog/astro-2/)

**February**

* [Netlify acquires Gatsby](https://thenewstack.io/netlify-acquires-gatsby-its-struggling-jamstack-competitor/)

**March**

* [Eleventy 2.0](https://www.sitepoint.com/eleventy-2/)

**May**

* [Vercel adds storage APIs](https://vercel.com/blog/vercel-storage)

* [Deno adds long-awaited KV stor](https://deno.com/blog/kv)

* [Next 13.4 makes the app router stable](https://nextjs.org/blog/next-13-4)

**June**

* [Lots of big Cloudflare announcements for Workers and Pages](https://blog.cloudflare.com/making-cloudflare-for-web/)

* [Astro 2.5 adds data collections](https://astro.build/blog/astro-250/)

**July**

* [Netlify announces Netlify Connect](https://www.netlify.com/blog/introducing-netlify-connect/)...

* ...[But also announces a major restructuring](https://www.netlify.com/blog/ceo-announcement-to-the-netlify-team/)

**August**

* [Astro announces Starlight for documentation](https://starlight.astro.build/)

**September**

* [Netlify clarifies the future of Gatsby](https://www.netlify.com/blog/gatsby-cloud-evolution/)

* [Astro 3.0 makes view transitions stable](https://astro.build/blog/astro-3/)

* [RedwoodJS goes all in on React Server Components](https://tom.preston-werner.com/2023/05/30/redwoods-next-epoch-all-in-on-rsc.html)

**October**

* [Netlify updates to Functions 2.0](https://www.netlify.com/blog/introducing-netlify-functions-2-0/)

**November**

* [Next.js 14 declares Server Actions stable](https://nextjs.org/blog/next-14)

* [Remix adds Vite support](https://remix.run/blog/remix-heart-vite)

* [Netlify releases an image CDN](https://www.netlify.com/blog/introducing-netlify-image-cdn-beta/)

**December**

* [Astro 4 updates to Vite 5](https://astro.build/blog/astro-4/)

* [Netlify's State of Web Development](https://www.netlify.com/blog/unveiling-the-state-of-web-development-and-predictions-for-2024-and-beyond/)

## The Community Held a Funeral for Jamstack...

In retrospect, trying to convey the nuance between a _term_ being dead and the category of technology it described being dead was always going to be difficult. If it was possible, it appears my post didn't accomplish it because it was shortly followed by a long list of tweets declaring Jamstack dead.

Many folks didn't really seem to see this as a big loss. Tyler from UI.dev declared:

> Even though the term was non-prescriptive and imprecise (and thus mostly unhelpful) from the start, Jamstack *did* help kickstart a movement around modern static sites in the late 2010s. But it was also clearly a marketing term that Netlify overextended to the point where it eventually lost all its original meaning — however nebulous that was to begin with.

Swyx argued that [the community was ambivalent about the term, at best, anyway](https://www.swyx.io/netlify-era-jamstack-end):

> The [rebrand from JAMstack to Jamstack](https://css-tricks.com/jamstack-vs-jamstack/) felt like a distinction without a difference (which is why I continue to capitalize the old way). When the frontend metaframework metagame moved from 100% static rendering to mostly-static to mostly-serverless-and-sometimes-edge, JAMstack’s advocates pivoted adroitly, claiming this fit JAMstack all along, which means it fit nearly everything, which means it stood for nearly nothing. When even a VP is saying ”[Jamstack is a feeling](https://dev.to/ryansolid/when-netlify-asks-you-to-full-time-oss-you-say-yes-5ccf)”, what he doesn’t say is that feeling is most often *ambivalence*.

Jared White agrees, arguing that Jamstack's downfall began when it lost sight of the simplicity it offered in favor of complexity that sold services:

> Along with this “second generation” Jamstack mindset shift came *an order of magnitude* more build complexity. Instead of a straightforward CLI kicking off simple transformations to go from Markdown -> HTML plus concatenate some (S)CSS files together or whatever, you’d get multi-minute long builds and GBs of `node_modules`...

Publicly, Netlify and its employees (summed up nicely [here](https://www.javascriptjam.com/august-1-2023/)) responded with a refrain that argued that Jamstack isn't dead, the term is just not necessary anymore because it won. They compared it to terms like Responsive Web Design that are rarely used anymore because they are so ubiquitous that the term becomes pointless. Here's how [Matt Biilmann put it](https://news.ycombinator.com/item?id=36947761):

> I would actually argue that Jamstack has won to the point of basically just being "Modern Web Development" by now.

He also clarified to [The New Stack](https://thenewstack.io/is-jamstack-toast-some-developers-say-yes-netlify-says-no/):

> Very much not dropping the term or declaring the architecture gone!

But, while Jamstack.org still exists, the term has seen a dramatic decline in usage in the community, and is no longer part of Netlify's core messaging.

## ...But Is the Term Actually Dead?

The term still has strong defenders though, most notably, Zach Leatherman, creator of Eleventy. He started by gathering a number of folks with strong opinions on the topic to discuss it in what he called a [Zhuzh](https://www.zachleat.com/web/jamstack-zhuzh/) and then followed it up with a post on [what the future of Jamstack could look like](https://www.zachleat.com/web/jamstack-future/). His goal?

> To refocus the definition and pull it back from post-pivot silver-bullet marketing, which was arguably an overstep attempt to pull dynamic/SSR/on-request frameworks like (non-static export) Next.js, Remix, Fresh (et al) under the umbrella.

To that end, he and his colleagues at CloudCannon even launched a new site called [The Future of Jamstack](https://thefutureofjamstack.org/). The general idea seems that maybe Jamstack doesn't have to be the solution to everything. Maybe a narrower term closer to its origins can make the distinction of Jamstack versus traditional web development clearer and could revive the community, albeit on a smaller scale.

## So Where Does That Leave Us?

> Don't it always seem to go
> That you don't know what you've got 'til it's gone
>
> [Joni Mitchell, Big Yellow Taxi](https://g.co/kgs/SMMkB9W)

I am fortunate that my job gives me the opportunity to talk to a lot of developers and, when it comes to the Jamstack, I could summarize many recent discussions with: "Maybe Jamstack did describe something after all?"

Web development describes an incredibly and increasingly broad spectrum of tools, techniques and technologies. It could mean building full stack applications in a language like Ruby and Rails. Or full stack JavaScript using a tool like Next.js deployed to Vercel (and AWS, Cloudflare, etc. under the covers). Or maybe it's a static site using Eleventy or Hugo that focuses on content but adds some services for dynamic functionality. Or even a simple marketing site built with Squarespace or Wix.

Sometimes these distinctions aren't relevant but most of the time they are. I don't want to go to a conference, join a community, purchase training, buy a book, etc. only to find out that none of it is relevant to me. Web development is just too big an umbrella.

I also prefer that we all don't just further divide off into ultra-niche communities largely run by for-profit companies to support their framework/tools but, unfortunately, that is where I feel that we are right now. It turns out the term, as amorphous as it was, was a nice shortcut for a range of tools and technologies that spanned companies and projects. Trying to reach to a Jamstack audience without it is just laundry-listing a range of things, as I've largely done when promoting [TheJam.dev](https://thejam.dev) or my [Jamstacked newsletter](https://cfe.dev/newsletters/jamstacked/).

[Every](https://www.netlify.com/blog/unveiling-the-state-of-web-development-and-predictions-for-2024-and-beyond/) [single](https://risingstars.js.org/2023/en#section-ssg) [data point](https://2022.stateofjs.com/en-US) indicates that everything that arguably sat under the Jamstack umbrella continues to grow is adoption and popularity, but I don't foresee anyone turning back the tide for the term itself. So barring dramatic changes in 2024, this will likely be the last of these updates (note that the event and the newsletter will continue, focusing on that laundry list of topics that are still relevant). Perhaps 2024 will bring us new ways (or terms) to talk about how we build web sites.