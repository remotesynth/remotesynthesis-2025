---
title: "What Netlify's Acquisition of Gatsby Really Means"
tags:
    - jamstack
description: It's not about the framework. It's about crossing the streams (of data)
pubDatetime: 2023-02-07T10:23:31.210Z
---

Last week, [Netlify announced its acquisition of Gatsby](https://www.netlify.com/press/netlify-acquires-gatsby-inc-to-accelerate-adoption-of-composable-web-architectures/). The news surprised even those of us, like myself, who follow the Jamstack ecosystem closely. The unsurprising part is that it caused [lots of speculation](https://twitter.com/steventey/status/1620867464669310976) as to Netlify's motives. A lot of this seemed to center on a narrative around Netlify aiming to snatch up an open source competitor to Next.js in the React space to better compete with Vercel.

Now, I have no special insider information, but I do follow this topic pretty closely and I am going to argue that this narrative is wrong. In fact, it's partially rebutted by Matt Biilmann's [own interview about the acquisition](https://thenewstack.io/netlify-acquires-gatsby-its-struggling-jamstack-competitor/). So let's look at what I think this acquisition was really about, what that means for the Jamstack ecosystem and the future of Gatsby, the framework.

## What Makes a Gatsby?

Let's start with what Netlify was most interested in. Gatsby, the company, had three main components:

1. **Gatsby Cloud** – This was the primary revenue driver for Gatsby. It promised to offer a Netlify-like development experience that was specifically optimized for Gatsby. It often touted build times for Gatsby products that were dramatically reduced compared to other vendors.
2. **Gatsby framework** – As you probably know, Gatsby is an open source, React-based library for building web sites (often called a static site generator or SSG). While its popularity has waned in recent years in favor of tools like Next.js, Gatsby's recent releases have brought it in line with the capabilities of other frameworks including support for SSR and partial hydration.
3. **Valhalla Content Hub** – This often flew under the radar but Gatsby started marketing their data layer as an independent product called Valhalla. One of the Gatsby framework's biggest innovations was it's data layer that made it relatively easy to consolidate data from disparate APIs into a single, consolidated data source using GraphQL.

By acquiring Gatsby, Netlify did take a competitor off the board with Gatsby Cloud while also adding the potential for improved support for Gatsby customers by now being able to integrate Gatsby's optimized cloud builds into their product. While taking a competitor off the board is valuable (and keeping in mind that we don't know what Netlify paid for Gatsby, as far as I know), Gatsby Cloud was never a serious threat to Netlify and, given that it was entirely dependent on a single framework whose popularity is waning, it was unlikely to emerge as one.

Could Netlify then be looking to turn the Gatsby framework's fortunes around, building a stronger competitor to Next.js? I think this is unlikely. First of all, Netlify has generally eschewed "owning" frameworks and opting instead to support popular frameworks that help build the Jamstack ecosystem. They currently pay both Zach Leatherman and Ryan Carniato to work on open source, including their own projects Eleventy and SolidJS respectively. They sponsor Astro (as does Vercel). They started a [Jamstack Fund](https://www.netlify.com/jamstack-fund/) to invest in companies and tools in the ecosystem including Deno and NuxtLabs, who each have their own frameworks. It would take a lot of money and work to turn Gatsby's popularity around with no guarantee of success and it just doesn't fit with Netlify's MO.

## Crossing the Streams

Which brings us to what this acquisition was most likely really about, Valhalla. It's about consolidating the streams that make up the backend of your web application.

You may be thinking, "But I'd never even heard of Valhalla until now." But it fits neatly into Netlify's other recent investments as well as it's recent reworking of the Jamstack definition with its emphasis on "composable architecture."

Back in 2021, [Netlify announced the acquisition of OneGraph](https://www.netlify.com/blog/2021/11/17/netlify-acquires-onegraph-a-powerful-graphql-platform-for-connecting-apis-and-services/), which became the [Netlify Graph](https://docs.netlify.com/netlify-labs/experimental-features/netlify-graph/). Netlify Graph aimed to make it easy to integrate popular APIs into your web site backend without needing to write API integration code or OAuth authentication.

Netlify Graph appears to have quietly shut itself to new users last December. One of it's limitations was that it required either Netlify or a partner company to build and continuously maintain the API integration. This works if I'm only integrating popular third-party APIs but it is tough to scale up to all the APIs one might use and, even then, it doesn't include my own APIs, which make up a core piece of my application's backend. To quote an [article at the time](https://www.theregister.com/2021/11/19/netlify_onegraph/):

> The reality is that it is early days, and much will depend on third-party support for OneGraph. "It will be important that we can allow external providers to plug into our platform and extend it," Biilmann adds, "to live up to its full potential."

From the same article:

> Future plans are more comprehensive. "What if we could put all the world's APIs and services behind one GraphQL endpoint," Biilmann says, to give teams "one framework for how to talk to them, how to authenticate with them, and how to build with them."

I'm not saying this is why Netlify closed Graph it to new users, but Valhalla definitely doesn't have that limitation. It can potentially pull from any data source and even allow you to consolidate your proprietary backend API with third-party APIs into a single source that can be easily integrated into your frontend applications. Perhaps it could even be combined with some of the existing Graph capabilities as well as Gatsby's extensive plugin ecosystem to make this process even easier.

That's what I think this acquisition is about. But you don't need to believe me. Here's an excerpt from [The New Stack's interview with Matt Biilmann about the acquisition](https://thenewstack.io/netlify-acquires-gatsby-its-struggling-jamstack-competitor/):

> He says there are similar frontend evolutions in content (headless CMS) and in “headless commerce” APIs. So with composable architectures, he argues, businesses can select “best of breed” solutions in all these areas. Where Netlify comes in, he said, is that it “helps companies orchestrate” all these pieces. He mentioned “the web UI layer, tying together build systems, webhooks from different content sources, deployment, edge run times,” and more.

## So what happens to the Gatsby framework?

I don't think the Gatsby framework is going anywhere. Even taking into account its declining popularity, Gatsby was still used in 28% of projects according to the [most recent Jamstack community survey](https://jamstack.org/survey/2022/#frameworks-by-usage-and-satisfaction), behind only Next.js in terms of Jamstack frameworks/SSGs.

In fact, I think this may improve its viability in many ways. I know it became popular to turn popular open-source frameworks into for-profit startups. While Gatsby was among the first that I can recall, it's been followed by many others like NuxtLabs and Astro, for instance. Even Vercel, while not exclusive to Next.js, appears to have its fate tied heavily to the framework it creates (one need only look at the expense and polish in the most recent Next.js Conf to confirm this).

But developer tastes are fickle, as Gatsby knows all too well. What is today's hot tool can become tomorrow's pariah in a short time. So making a company off a framework can be a heavy lift and, from all outward appearance, Gatsby the company's fortunes had turned in line with its framework (which is unsurprising). With Netlify, Gatsby has found a home that definitely appears to be more stable, improving its long term prospects. My guess is that Netlify will set up a situation similar to Eleventy and SolidJS to allow development of the tool to continue, while also not tying it's future to the ability of the framework to generate profitability, which would have been the case had Gatsby remained independent.

All in all, I think this was the best possible landing spot for Gatsby and its users and I expect it'll continue to be a big part of the Jamstack ecosystem going forward.