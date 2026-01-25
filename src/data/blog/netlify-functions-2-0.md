---
title: Updating Your Netlify Functions to 2.0
description: Netlify Functions 2.0 offer some important improvements, but, to take advantage of them, you'll need to make some simple updates.
tags:
  - web development
  - jamstack
pubDatetime: 2023-11-26T10:23:31.210Z
---

Netlify recently announced their [Netlify Functions 2.0](https://www.netlify.com/blog/introducing-netlify-functions-2-0/), which offer a new functions API more in line with web standards, custom endpoints, advanced routing and more. However, if you built your site for the previous version of Netlify Functions, you'll need to make some updates to take advantage of these features.

I recently updated the functions that run for [CFE.dev](https://cfe.dev) and will share the steps I made to update them. Don't worry, it's really straightforward.

## Convert the file to an ESModule

My old functions were written CommonJS format with a `.js` extension. The first thing you need to do is rename the file with a `.mjs` extension which is for the ESModule format that newer functions use. Since my site's functions were _really old_, I also moved them from their prior folder structure, to the new default location of `/netlify/functions`. This last part isn't necessary but got my site structure in line with Netlify's more recent standards.

### Change requires to imports

ESModule format uses the `import` syntax rather than the `require()` one. This means you'll need to update all of your imports from:

```javascript
const Mailjet = require("node-mailjet");
```

To:

```javascript
import Mailjet from "node-mailjet";
```

### Update the handler syntax

The old handler looked like this:

```javascript
exports.handler = async (event, context, callback) => {
	...
}
```

The updated handler uses just a slightly different syntax:

```javascript
export default async (req, context) => {
	...
}
```

### Return Response objects

The other changes were extremely simple, but this one can require a little more work. The new functions require that you return a [Response object](https://developer.mozilla.org/en-US/docs/Web/API/Response) while the old ones did not. You'll need to make sure that anywhere that you are passing back a response from the handler, that it returns a response object.

For example, my old returns looked like this:

```javascript
if (!email) {
  return {
    statusCode: 500,
    body: "email query parameter required",
  };
}
// do stuff
const response = { msg: "Good news! You've been added." };
return {
  statusCode: 200,
  body: JSON.stringify(response),
};
```

The updated responses now look like this:

```javascript
if (!email) {
  return new Response("email and list query parameters are required", {
    status: 500,
  });
}
// do stuff
const response = { msg: "Good news! You've been added." };
return new Response(JSON.stringify(response), {
  status: 200,
});
```

It's not difficult but, depending on your code, may require a little time and effort.

### Add a custom path

This isn't required, but, now that you're using the 2.0 syntax, you might as well use a custom path. This means that instead of the `/.netlify/functions/<function name>`, I can tell Netlify what URL I want the API to use. It's super easy. Just add a config export to the end of the function.

```javascript
export const config = {
  path: "/api/mailjet",
};
```

In this example, the function that used to be at `/.netlify/functions/mailjet` is now available at `/api/mailjet`. Since my API isn't for external consumption, there's no real benefit to my application here other than it is a cleaner and shorter URL.

## Welcome to 2.0

That's all you really need to do. At this point, the function isn't taking advantage of the new 2.0 features other than the custom API path, but it's ready to when I want to.
