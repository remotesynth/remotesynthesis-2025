---
title: Moving from Jekyll to Astro
description: After many years it's time to move to a new site generator.
tags:
  - web development
pubDatetime: 2023-01-03T10:23:31.210Z
---

I started the last iteration of this blog [back in July of 2014](https://remotesynthesis.com/blog/starting-anew/) when I jettisoned my ColdFusion-based blog (and all of the old content) for Jekyll. It's difficult to imagine, but in 2014, Jekyll felt new and fresh. And, to be honest, it still worked but it was showing it's age. For instance, I had not bothered to go through the pain of getting it running locally in years.

None of this mattered too much since I rarely posted (it's been a year since my last post). With everything that happened last year though – especially around Twitter – I thought it was finally time to make a change. This time, I chose [Astro](https://astro.build).

## Why Astro?

For the most part, blogs are simple and should be built for simplicity. Astro is one of a number of new frameworks that aims to deliver less JavaScript to the client. There are only a handful of features that a typical blog requires that might need JavaScript (site search perhaps), and a full framework like React feels like overkill for delivering static content.

Speaking of static, there's very little reason that I can see for rendering most blog content as static. Luckily, Astro also makes that easy.

Ultimately, Astro allows me to make this site as simple as it should be while leaving me room to add more complexity if it becomes necessary in the future.

## Making the Transition

The toughest part of any new site for me is design. I lack any real design skill, so I tend to search for free or paid templates. This can be a real rabbit hole. Ultimately, I decided to move forward with [Astro Ink](https://github.com/one-aalam/astro-ink). There are a number of things about the design that I would like to change, but I chose to no longer allow the design to prevent me from moving forward.

Astro Ink comes ready for a Markdown-based blog, so the next challenge was converting all of my old posts to work with it. I was fortunate in that I had not used the default Jekyll URLs that placed posts in subdirectories by date (i.e. `:year/:month/:day`). All of my posts were under the `/blog` directory with just the slug. However, the files were still named as `:year-:month-:day-this-is-my-slug.md`. So I needed to fix those.

Ultimately, I went with a simple Node script to rename all the files, removing the date. Keep in mind that this script actually does not maintain the original, so I used it on a copy of the files.

```javascript
const fs = require("fs");
const files = fs.readdirSync(__dirname);

for (const file of files) {
  if (file.endsWith(".md")) {
    let newName = file.substring(11, file.length);
    fs.renameSync(
      __dirname + "/" + file,
      __dirname + "/renamed" + "/" + newName,
      (err) => {
        console.log(err);
      }
    );
  }
}
```

Next I had to convert the code coloring. Jekyll had, many years ago, used a code coloring format that looked like this:

```liquid
{% highlight html %}
{%raw%}
{% include banner.html %}
<ul class="ArticleList">
  {% for post in site.categories[categoryname] %}
	<li>
        <h4><a href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a></h4>
    </li>
  {% endfor %}
</ul>
{%endraw%}
{% endhighlight %}
```

Unfortuantely, I didn't have an easy way to convert these, so this was a manual process. Fortunately, I didn't have a more than a half-dozen or so pages wit code samples formatted in this manner.

The next step was to fix the frontmatter. The new template required some additional fields, my date formats needed to be updated, and the tagging needed to be cleaned up. Again, this was a manual process and by far the most painful part of the process.

The final step was converting the data pages for my publications and presentations. Honestly, those pages need to be improved but for now I just converted the YAML to JSON using an online converter and displayed them more or less as they were on the previous site.

Once these changes were done, getting a static Astro site up on Netlify was a breeze.

## Current Issues

There were some issues with the template along the way that were relatively easy to fix (for instance the date sort was not set up properly). There are still some issues with the site. Performance of the site is great, but a lot of the issues are accessibility related.

* The color contrast of certain text and links is super low, which is an accessibility issue.
* Some text does not change color when dark mode is turned on
* Some buttons need to have accessibility labels added.

These seem easier to fix than they are as I am digging through the code to find where some of these things are set (it's not as obvious as it should be). If you notice any other issues, please reach out to me (the best way is [via Mastodon](https://mastodon.xyz/@remotesynth)).