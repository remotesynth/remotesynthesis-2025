---
title: Lifting Off with Astro 🚀
tags:
    - web development
    - javascript
description: Let's take a look at how Astro can help you build apps with less JavaScript and better performance.
pubDatetime: 2023-08-07T10:23:31.210Z
---

[Astro](https://astro.build) is still a relatively new JavaScript framework, having been around since 2021, but, in my opinion, it addresses two major issues that face developers doing full stack JavaScript: the cost of that JavaScript and the forces of inertia. Let's discuss the problems first and then look at how Astro addresses them. Finally, we'll explore an example of an Astro application to help you get started using it.

## The Cost of JavaScript

Every year since 2018, Addy Osman writes or speaks about [The Cost of JavaScript](https://www.youtube.com/watch?v=ZKH3DLT4BKw). JavaScript remains the most expensive resource on your site and has been the same since he first talked about it in 2018. That's because it's not just about the weight of the resources, which continues to grow, but also the time it takes to process it.

This past year saw a smaller than usual increase in the size of JavaScript, but it was still up 10% according to the Web Almanac.

> **From 2021 to 2022, an increase of 8% [in the amount of JavaScript shipped to browsers] for mobile devices was observed, whereas desktop devices saw an increase of 10%.** ...The fact remains that **more JavaScript equates to more strain on a device’s resources**.
> [Web Almanac](https://almanac.httparchive.org/en/2022/javascript)

The raw numbers can be shocking, with sites at p90 loading about 1.5MB of JavaScript. I'll hazard a guess that these same sites will have lots of blocking scripts, meaning the site is unusable while the user waits for the JavaScript to process. But, even worse, much of this JavaScript is unused.

![Unused JavaScript according to the Web Almanac](/images/posts/lifting-off-astro/unused-js.png)

### Unnecessary JavaScript

Unused JavaScript is obviously wasteful, and should be addressed, but, in my view, nearly as wasteful is a category of JavaScript that I am calling "unnecessary JavaScript". This is JavaScript that is used but ultimately isn't needed because it does things that could have been done without JavaScript by just using the web platform.

The rise of unnecessary JavaScript is related to the fact that at some point we also started using tools like React, that were meant to solve problems of complex and interactive application development, to build everything including sites that were heavy on content or basic application functionality with limited interactivity.

For example, let's imagine a SaaS company site. There is probably a public facing portion of the site that is mostly marketing with perhaps some forms and simple interactions. Meanwhile there is likely a console of some sort that is fairly complex and represents the core of how the customer interacts with the SaaS application. The needs of the console probably make the cost, in terms of JavaScript, necessary enough to warrant a framework like React. The needs of the public facing site...yeah, not so much.

![are you sure these are the right tools for the job](/images/posts/lifting-off-astro/wrong-tool.jpg)

I think a big reason why developers continue to load on more JavaScript and use frameworks like React for things the framework isn't really designed for is because we've built up years of dependency that makes it increasingly difficult to move without staring down a steep learning curve and/or starting from scratch.

But the good news is that new tools, like Astro are beginning to address these issues.

> New front-end frameworks like Solid and Qwik are suggesting that **React might not have all the answers after all**, and on the server **Astro**, Remix and Next.js (among others) are **making us reconsider how much code we really need to ship to the client**.
> [State of JavaScript 2022](https://2022.stateofjs.com/en-US/)

## The Benefits of Astro

Astro addresses the two big issues I talked about above: unnecessary JavaScript; and the difficulty of transitioning. Let's explore how by first diving into how it deals with unnecessary JavaScript.

### Islands

By default, Astro delivers 0kb of JavaScript to the client. Of course, very few sites today can function with zero JavaScript, but Astro helps you eliminate unnecessary JavaScript via something called the "islands architecture."

First coined by Etsy's frontend architect Katie Sylor-Miller in 2019 as the "Component Islands" pattern, the idea behind an islands architecture is to only send the JavaScript for components that require client-side hydration or interactivity. Here's how it is described from the canonical article on it by Jason Miller:

> The general idea of an “Islands” architecture is deceptively simple: **render HTML pages on the server, and inject placeholders or slots around highly dynamic regions.** These placeholders/slots contain the server-rendered HTML output from their corresponding widget. They denote regions that can then be "hydrated" on the client into small self-contained widgets, reusing their server-rendered initial HTML.
> 
> [Islands Architecture](https://jasonformat.com/islands-architecture/) by Jason Miller

This leads to a page that might look like the below diagram wherein the header and image carousel require JavaScript but the remainder of the page does not. The typical single page application (SPA) architecture would hydrate the entire page using JavaScript. But the islands architecture proposes that by sending only the JavaScript required for rendering these components, we can ultimately minimize the amount of JavaScript necessary on the client.

![islands architecture diagram](/images/posts/lifting-off-astro/islands.png)

#### How islands work in Astro

So how does this work? In the below example (borrowed from the Astro docs), the Astro component (don't worry, we'll talk about the different types of components in a bit) requires no JavaScript to render but the React component does and thus has the directive for `client: load`.

```html
---
// Example: Use a dynamic React component on the page.
import MyAstroComponent from '../components/MyAstroComponent.astro';
import MyReactComponent from '../components/MyReactComponent.jsx';
---
<!-- This component is now interactive on the page! -->
<MyReactComponent client:load />
<!-- This component loads zero js --->
<MyAstroComponent />
```
Astro actually offers a ton of flexibility with its hydration directives that allow you to set the appropriate priority for each component all the way to forcing full client-side rendering where necessary.

* **load** – high priority. Elements that will be immediately visible on the page.
* **idle** – medium priority. Elements that do not need to be immediately interactive.
* **visible** – low priority. Typically below the fold elements that become active when in the viewport.
* **media** – low priority. Elements that might only be visible on certain screen sizes.
* **only** – skip server rendering entirely and only render on the client.

So to summarize, Astro will send zero JavaScript by default but allows you to designate a component "island" that requires JavaScript to render or otherwise enable interactivity. However, you have fine-grained control over how that JavaScript is loaded to help ensure the best performance for your users.

### Components in Astro

So we've talked about how Astro reduces JavaScript, but how does it ease transitioning from an existing SPA architecture? It does this by supporting a variety types of components, including components built in other frameworks like React, Vue, Svelte and more. This eases the learning curve but also means that developers don't necessarily need to toss all of their existing code as components can be reused or shared within the Astro site.

You can even mix and match components from different frameworks. I'm not sure I'd recommend this but you can do it.

```html
---
// Example: Mixing multiple framework components on the same page.
import MyReactComponent from '../components/MyReactComponent.jsx';
import MySvelteComponent from '../components/MySvelteComponent.svelte';
import MyVueComponent from '../components/MyVueComponent.vue';
---
<div>
  <MySvelteComponent />
  <MyReactComponent />
  <MyVueComponent />
</div>
```

But Astro also offers their own component syntax for an Astro component (`.astro`). These are HTML only components on the client, though you can include JavaScript via `<script>` tags or run JavaScript on the server. As we'll see, you can still even build full sites and even simple web applications using just Astro components.

## When to use Astro

All of the above may sound amazing and you may be feeling like, "Build all the things with Astro!" But, in truth, Astro isn't designed to be the solution to everything. Their docs make this clear:

> **Astro was designed for building content-rich websites.** This includes most marketing sites, publishing sites, documentation sites, blogs, portfolios, and some ecommerce sites.
> 
> By contrast, most modern web frameworks are designed for building web applications.
> 
> [Why Astro?](https://docs.astro.build/en/concepts/why-astro/)

This makes sense but I'll admit that the dividing line is fuzzy. Can you build applications using Astro? Most definitely. Just as you could build a blog with Next.js (something it feels like serious overkill for), you could likely build (to use my prior example) a SaaS application dashboard with Astro, but it wouldn't be the best tool for the job.

Ultimately, that dividing line is up to you but it is worth pointing out that it's not all or nothing. You could move the more content-focused aspects of your site to Astro and leave the rest to something like Next.js. This would help you only use the necessary JavaScript.

## Building an Example Astro Application

Let's explore an example I built using Astro. As someone who speaks frequently at conferences, I usually do a fairly poor job of tracking both the content of my CFP submissions and where I submitted them to. The application I built is fairly simple one that allows me to save my CFP titles and abstracts as well as which conferences I have submitted them to and whether they were accepted or not.

You can find the [repo here on GitHub](https://github.com/remotesynth/astro-cfp-tracker). It currently doesn't support multiple users or any advanced functionality (plans for the future!) but it will help us cover the basics of getting started building apps with Astro. The backend uses [AppWrite Cloud](https://appwrite.io/) but I did do another version porting the data portion to Postgres that you can [find here](https://github.com/remotesynth/astro-demo-postgres).

![the example app](/images/posts/lifting-off-astro/example-app.png)

This application uses no JavaScript, but still allows for dynamic output. It's a great example that, while React/Vue/Svelte components have their place, you can do a lot using just Astro components. Let's go through some of the basics.

### Getting Started

The easiest way to get started is via some of the templates on [Astro.new](https://astro.new). In this case, I used the [Tailwind template](https://astro.new/with-tailwindcss?on=github) which, as the name implies, integrates Tailwind. In Astro [integrations](https://astro.build/integrations/) are handled like plugins that you install separately. This even includes things like adding support for deployment options like [Netlify](https://docs.astro.build/en/guides/integrations-guide/netlify/) for example.

To generate a site using the Tailwind template, I just used the command line:

```bash
npm create astro@latest -- --template with-tailwindcss
```
This will walk you through a command line based wizard that ultimately generates a set of project files using the default Astro folder structure. It will also, if you choose, install all the necessary dependencies.

The key thing to note first is the Astro configuration file, `astro.config.mjs`. Let's look at mine because I made a couple small tweaks to the one that was generated.

```javascript
import { defineConfig } from "astro/config";
import tailwind from "@astrojs/tailwind";

// https://astro.build/config
export default defineConfig({
  integrations: [tailwind()],
  output: "server",
});
```

First off, I have removed the MDX plugin as my application doesn't use MDX, so the only integration is the Tailwind one. Second, I added the `output: server` because my application is fully server-side rendered. By default, Astro outputs as static files but it also supports two other rendering modes:

* `server` which is fully server side rendered. Since my application, as it currently exists, isn't designed to pregenerate any pages as static (it's all effectively user generated content), SSR was the right choice.
* `hybrid` which is a combination of server-side rendering and static rendering. This probably suits most sites as it allows pages like your about page, for example, or even static blog posts to opt-out of server-side rendering and be pre-rendered for even better performance.

### Creating Layouts

Layouts are typically placed in a `/src/layouts` folder, but that's a convention not a requirement. Since my app doesn't have many different views, I only created one layout, `main.astro`, which just serves as the shell of the application.

The two key things to point out in the code below (note that for brevity I will be removing the Tailwind classes) is that you can pass props into an Astro component (in this case I am just passing an HTML title) and that you use the `<slot />` tag to indicate where the generated content should be output.

You should also note that the JavaScript that runs on the server, either at build time for static rendering or runtime for SSR, is placed at the top of the file bracketed by `---` as you might typical frontmatter.

```html
---
const { title } = Astro.props;
---

<html lang="en">
	<head>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width" />
		<link rel="icon" type="image/svg+xml" href="/favicon.svg" />
		<title>{title}</title>
	</head>
	<body>
		<section>
			<div>
				<div>
		<slot />
				</div>
			</div>
		</section>
	</body>
</html>
```
I can then import and use a layout anywhere in my application or, in the case of Markdown or MDX, specify a layout to use in the frontmatter. You can also nest layouts, for example if I had this shell as the base and sub-layouts for different sections of my site.

### Components

As the UI is fairly simple, the sample application only uses a couple of simple Astro components. Let's look at the component that renders a session in the list page. It is very similar to the layout above in that it can do imports and run JavaScript on the server in the block at the top of the page. I am passing in the session as a prop which is then used to render the output between `{` and `}`. Notice that I can run arbitrary JavaScript within these as I do in the date formatting.

```html
---
import Button from '../components/Button.astro';

const {session} = Astro.props;
---
<div>
    <h2>
        <a href=`/sessions/${session['$id']}`>{session.Title}</a></h2>
    <div>
        <a>
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16">
                <path d="..." />
            </svg>Created: {new Date(session['$createdAt']).toDateString()}
        </a>
        <a>
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16">
                <path d="..." />
            </svg>Updated: {new Date(session['$updatedAt']).toDateString()}
        </a>
    </div>
    <p>{session.Abstract}</p>
    <div>
        <Button url={`/addSession?sessionID=${session['$id']}`}>
            Edit
        </Button>
        <Button url={`/addCFP?sessionID=${session['$id']}`}>
            Add a CFP
        </Button>
    </div>
</div>
```

Using the layout and component in a page works just as you would expect. You simply import them at the top of the file. You can pass in props via attributes to the tag. Notice that you can do things like output a list using `map()` as you typically would in a React component. Also note that the server-side JavaScript supports top-level `await`.

```html
---
import BaseLayout from '../layouts/main.astro';
import CFPCard from '../components/CFPCard.astro';
import Button from '../components/Button.astro';
import {getSessions} from '../lib/AppWrite.js';

const sessions = await getSessions();
---

<BaseLayout title="My CFP Submissions">
	<div class="w-36 m-4 float-right">
		<Button url="/addSession">New Session</Button>
	</div>
	<h2
		class="mb-4 text-3xl font-bold leading-tight tracking-tighter text-gray-700 md:text-5xl dark:text-gray-300">
		Current Sessions</h2>
	{
		sessions.map((session) => (<CFPCard session={session} />))
	}
</BaseLayout>
```

### Routing

As is a common convention in full-stack JavaScript frameworks, Astro supports file based routing but routing is different than you may be used to because Astro is what's now commonly referred to as an MPA or multi-page application. Essentially, instead of loading an app shell and then rehydrating the shell based upon the route, Astro renders a new page with a full request/response – just like we did in the old days (except back then they were just web sites and not MPAs). You can read more about [MPAs vs SPAs](https://docs.astro.build/en/concepts/mpa-vs-spa/) in Astro's docs.

The routing is based off the structure within the `/pages` directory. This means that if there is an `/src/pages/about.astro` that will resolve to route of `/about.html`. Again, this doesn't cause the app to rehydrate but will do a full server request and response, whether or not that route is statically rendered or server-side rendered.

Astro also supports dynamic routes as well as things like catchall routes. Here's some examples:

```javascript
/pages/about.md // renders /about
/pages/blog/[post].astro // renders /blog/post1 and /blog/post2
/pages/api/[version]/posts.json.js // renders /api/v2/posts.json
/pages/[...path].astro // renders /about and /about/team
```

If you are statically rendering a dynamic route, you do need to supply predefined paths for a route via a `getStaticPaths()` method in the file. If you are server side rendering as I am, this isn't required. However, this means that someone could hit a route that doesn't exist, in which case you'll need to handle that.

In the example app, I have one dynamic route that renders a page for any of the sessions that I submit. Because this is server side rendered, I do not need to predefine the paths, but I am returning a 404 response if the path doesn't exist (I could alternately use `Astro.redirect()` to redirect them to a page instead).

You'll also note that I am using a URL variable to update a CFP as accepted. This is possible because this page is server side rendered. Otherwise I would have to have used client-side JavaScript to manage the request and updating the page HTML to reflect the change.

```javascript
---
import BaseLayout from '../../layouts/main.astro';
import Button from '../../components/button.astro';
import { getSession, getCFPs, acceptCFP } from '../../lib/AppWrite.js';

const currentPath = Astro.url.pathname;
const { id } = Astro.params;
const cfpid = Astro.url.searchParams.get('cfp');

// if the URL variable for a CFP ID is present, we're accepting that session
if (cfpid) {
    acceptCFP(cfpid);
}

const session = await getSession(id);
if (!session) {
    return new Response(null, {
        status: 404,
        statusText: 'Not found'
    });
}
const cfps = await getCFPs(id);
---

<BaseLayout title={`Session: ${session.Title}`}>
    <div>
        <h2>{session.Title}</h2>
        <div>
            <p>Created: {new Date(session['$createdAt']).toDateString()}</p>
            <p>Updated: {new Date(session['$updatedAt']).toDateString()}</p>
        </div>
    </div>
    <div>
        <div>{session.Abstract}</div>
            <h2>Submissions</h2>
        <ol>
            {
                cfps.map((cfp) => {
                    let acceptLink = `<a href="${currentPath}?cfp=${cfp['$id']}">Accepted?</a>`;
                    return (<li>{ cfp.Conference} | Submitted on: {new Date(cfp.SubmissionDate).toDateString()} | { cfp.Accepted ? "Accepted" : <span set:html={acceptLink}></span> }</li>)
                })}
        </ol>
        <Button url="/">
            Back Home
        </Button>
    </div>
</BaseLayout>
```

### Handling form submissions

The only other thing I want to point out in this demo app is that it's pretty easy to handle form submissions via standard HTML and server-side JavaScript using an Astro component. For example, let's look at the page that handles the form for adding a new session title and abstract.

The form submission is handled by looking for the POST method and then getting the values from the submitted form data. The same form is used for updating an existing session by looking for an URL variable and populating the form values. If the form submission is successful, I am redirecting back to the session list on the home page using `Astro.redirect()`.

One thing worth noting is that there is no real error handling on the server side in this example. The form does use basic HTML form validation, but an improvement would be to ensure that there is some degree of server-side error handling as well. In addition, the `alert()` method where I dump the error message if there is one is a server-side alert rather than a client-side one, so, as it exists today, the user wouldn't know if the server submission failed.

```javascript
---
import BaseLayout from '../layouts/main.astro';
import { createSession, getSession, updateSession } from '../lib/AppWrite.js';

// handle the form submission
if (Astro.request.method === "POST") {
  try {
    const data = await Astro.request.formData();
    const sessionID = data.get("sessionID");
    const title = data.get("title");
    const abstract = data.get("abstract");

    if (sessionID)
        await updateSession(sessionID, title, abstract);
    else
        await createSession(title, abstract);
    return Astro.redirect('/')
  } catch (error) {
    if (error instanceof Error) {
      alert(error.message);
    }
  }
}

// if a URL variable is present, we are editing an existing session
// we can handle URL variables on the server because this is SSR
const sessionID = Astro.url.searchParams.get('sessionID');
let title;
let abstract;

if (sessionID) {
  const session = await getSession(sessionID);
  if (session) {
    title = session.Title;
    abstract = session.Abstract;
  }
}
---

<BaseLayout title="Add/Edit a Session Abstract">
    <div>
        <h2>
            Add/Edit Session Abstract
        </h2>
    </div>
    <form method="POST">
    <input type="hidden" name="sessionID" value={ sessionID }>
    <div>
        <div>
            <div>
                <div>
                    <p>
                        Session Title
                    </p>
                </div>
                <div>
                    <input name="title" required
                        type="text" placeholder="title" value={title}>
                </div>
            </div>
        </div>
    </div>
    <div>
        <div>
            <div>
                <div>
                    <p>Abstract</p>
                </div>
                <div>
                    <textarea name="abstract" rows="4" placeholder="your text here.." required>{abstract}</textarea>
                </div>
            </div>
        </div>
    </div>
    <div>
        <div>
            <a href="/">
                <p>Cancel</p>
            </a>
        </div>
        <div class="w-full md:w-auto p-1.5">
            <button>
                <p>Save</p>
            </button>
        </div>
    </div>
    </form>
</BaseLayout>
```

## Prepare for your launch! 🚀

I hope that this has given you all the foundations you need to get started with Astro and you are ready to take off! As I noted, the key benefits Astro offers of reduced JavaScript and better performance are going to be increasingly important as we try to deal with the JavaScript bloat that the SPA era has left behind. But Astro's support of existing framework components and relatively gentle learning curve will help you make the transition from a SPA framework. So, give Astro a try by going to [Astro.new](https://astro.new) and starting a new project or digging into their extensive and well-written [documentation](https://docs.astro.build/en/getting-started/).