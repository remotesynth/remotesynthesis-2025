---
title: "Full-stack Web Apps Without React"
tags:
    - web development
description: There are a ton of options for full stack web frameworks that don't use React. Let's explore some of them and why they are each unique.
pubDatetime: 2023-04-17T10:23:31.210Z
---

As I discussed in [my last post](https://remotesynthesis.com/blog/the-price-of-developer-tools/), change can be difficult but it is often good to expand your horizons. If you've been thnking of exploring. the good news is that the past couple years have seen an explosion of tools that offer full-stack capabilities similar to Next.js or even Gatsby including server-side rendering and, in some cases, static site generation, but without relying on (or at least not entirely on) React, Vue or Angular. In this post, I want to look at a few options and what makes each of their approaches unique.

## Astro

[Astro](https://astro.build/) is a full-stack JavaScript framework for building sites that supports both static generation and server-side rendering. It hit [version 2](https://astro.build/blog/astro-2/) back in January.

### What Makes It Unique

One of the things that makes Astro unique and particularly useful for someone looking to explore beyond React is that it supports components from almost any framework including React, Preact, Svelte, Vue, SolidJS, AlpineJS or Lit as well as it's own component format. This means that if you are transitioning an existing project you can reuse your components, or, if you just don't want to learn a new component structure, you don't have to.

Astro also emphasizes the performance of its web applications compared to alternatives like Gatsby, Next and Nuxt. The way that it aims to achieve this performance is via an "[islands architecture](https://jasonformat.com/islands-architecture/)," which they call [Astro Islands](https://docs.astro.build/en/concepts/islands/). This means that, by default, Astro will ship no JavaScript, even where a framework component is used. However, when a component is designated as requiring interactivity and Astro will ship the necessary JavaScript to make that component work.

### How Do I Get Started

```bash
npm create astro@latest
```

## Eleventy

[Eleventy](https://www.11ty.dev) is a wiely JavaScript-based static site generator that has a very active user base and lots of integrations and plugins to support things like server-side rendering or even edge rendering. It released [version 2.0](https://www.11ty.dev/blog/eleventy-v2/) back in February. 

### What Makes It Unique

Eleventy's core is deceptively simple, but it functions almost like a workshop, allowing you to assemble the tools you need to build the site however you like. For example, you can pick and choose from a multitude of [templating language options](https://www.11ty.dev/docs/languages/). Want to use server-side rendering, install the [serverless plugin](https://www.11ty.dev/docs/plugins/serverless/). Want to add support for edge functions, install the [Eleventy Edge plugin](https://www.11ty.dev/docs/plugins/edge/). Want to use components in a web component format, install the [webc plugin](https://www.11ty.dev/docs/languages/webc/). It's impossible to cover the number of options here.

While you can pull all these options as needed, under the covers Eleventy gives you the tools like layouts, collections, data files and more to pull all the pieces together.

### How Do I Get Started

```bash
npm install @11ty/eleventy --save-dev
```

## Enhance

[Enhance](https://enhance.dev/) is relatively new, even compared to some of the newer tools we're talking about in this post, having been released [in August 2022](https://begin.com/blog/posts/2022-08-31-new-begin-and-enhance-html-framework). It is an application framework that supports server-side rendering via Lambda functions.

### What Makes It Unique

Enhance focuses on being an HTML-first library that doesn't require JavaScript when not needed, but also relies on web standards like web components and progressive enhancement to make the site fully interactive. Enhance provides tools like single-file components with styling, routing for page and API routes that get rendered server-side, and tools for maintaining state client-side. When you are ready to deploy, Enhance offers inegrations that make it easy to deploy the application to AWS.

### How Do I Get Started

```bash
npx "@enhance/create@latest" ./myproject -y
```

Or check out their new [blog template](https://begin.com/blog/posts/2023-03-17-introducing-the-enhance-blog-template).

## Fresh

[Fresh](https://fresh.deno.dev/) is a full-stack framework created by Deno that also ships no JavaScript to the client by default (a theme across all the tools so far) that supports server-side rendering. It released [version 1.1](https://deno.com/blog/fresh-1.1) back in September.

### What Makes It Unique

Fresh relies on an islands architecture (like Astro) that enables shipping minimal (or no) JavaScript to the client while allowing you to create interactive components, using Preact and JSX, that are rendered both server-side and client-side using JavaScript as needed. In addition, there is no build step to Fresh, meaning the code you write is the code that runs, which can make iteration on a project faster and, potentially, makes debugging easier. Finally, while Fresh can be deployed to any Deno server, it is designed to utilize rendering on the edge (deployed to Deno Deploy of course).

### How Do I Get Started

```bash
deno run -A -r https://fresh.deno.dev my-project
```

## Other Options

This isn't a comprehensive list of course. There are frameworks like [SolidJS](https://remotesynthesis.com/blog/the-price-of-developer-tools/), which offers a lot of React capabilities but without requiring a virtual DOM, [SvelteKit](https://kit.svelte.dev/), which is similar to NextJS but relying on Svelte, or [Qwik](https://qwik.builder.io/), which does SSR and SSG but without hydration, relying instead on what they call "JavaScript Streaming." I'm sure there are others I've missed as well, but the point is, there are lots of options and, because each takes a unique approach to solving similar problems, we can learn a lot by exploring them.