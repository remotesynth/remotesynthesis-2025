---
title: Building a (Virtual) Events Site
description: What does it take to build and run a site that hosts virtual events? Let's dig into how mine is set up.
tags:
  - general
  - jamstack
pubDatetime: 2023-11-21T08:23:31.210Z
---

Back in the summer of 2017, I embarked on creating a site to host events. The site was called Certified Fresh Events, which, for simplicity's sake, I eventually shortened to [cfe.dev](https://cfe.dev) Honestly, the plan wasn't to host only virtual events, but that is what it's been for 6 1/2 years. In this post, I will talk about how the site is built – what technologies it uses under the covers, what services it relies on and what supporting tools I use.

Ultimately the structure has been flexible enough to expand from smaller "meetup" style virtual events, to full virtual conferences, to handling live streams and interview style shows. And, the costs are (relatively) low, meaning I don't go broke running it. You can actually check out the [source code on GitHub](https://github.com/remotesynth/certifiedfreshevents).

Now, let's dive into the details.

## Building the Actual Site

The first thing to know about the site is that it is actually pretty large, with 1253 pages as of today, but also fully static. That doesn't mean it isn't "dynamic" from a user perspective.

### Hugo

The site has been built with the [Hugo static site generator](https://gohugo.io) since day one. Back in 2017, when I was originally building the site, I was a big fan of Hugo for its flexibility and speed. Hugo, which is built in Go, is known for extremely fast build times (for example, my 1200+ pages generate in about 7 seconds). This wasn't important when I built it, but it has been beneficial as the site grew large. And, while a lot has changed in the web development framework world since 2017, Hugo still does what I need it to.

Hugo is very good at handling content, so there are some built in tools that have come in handy over the years. For example, building related content can be difficult and often requires either a manual association or building some kind of algorithm to score related content. In Hugo, this is built in.

First, I add some details to the Hugo configuration file to tell it how to score related content. In this case, I am giving the highest weight to categories and tags and a slight weight to date adjacency. This isn't a perfect scoring algorithm (it probably needs more thought) since either a category or a tag will put it over the scoring threshold, but it works well enough for my needs.

```yaml
related:
  threshold: 80
  includeNewer: true
  toLower: true
  indices:
    - name: categories
      weight: 100
    - name: tags
      weight: 100
    - name: date
      weight: 10
```

Next, I can query the related pages for any page. The following line pulls only related content from the sessions section of my content. Yes, the syntax in Hugo can be a little awkward at first (or, at least, it was for me).

```handlebars
{{ $related := where (.Site.RegularPages.Related . ) "Section" "sessions" }}
```

Another thing that has been useful over the years has been Hugo's asset pipeline. This lets me combine JavaScript and CSS files as well as do things like resize images into multiple sizes at build time. I know this isn't unique to Hugo as most SSGs have it, but it is useful nonetheless. The early iteration of this site required me to manually export image sizes, which was laborious. I will admit, I am still not using this feature to its full capabilities.

The first step is to put assets in the assets folder. Right now this includes my JavaScript, CSS and images. To use CSS, I need to get the assets and then display them (JavaScript works similarly):

```html
{{ $styles := resources.Get "css/styles.css" | postCSS (dict "config"
"./assets/css/postcss.config.js") }}
<link rel="stylesheet" href="{{ $styles.RelPermalink }}" />
```

For images, I pull the media from the page metadata in this case, resize it and then display the resized image:

```html
{{- $src := resources.Get (print "img/banners/" .Params.homepage_banner) -}} {{-
$src := $src.Resize "608x" }}
<img
  src="{{ $src.RelPermalink }}"
  loading="lazy"
  alt="Banner for {{ .Title }}"
  aria-hidden="true"
/>
```

One of the other quirky things about the way I set up my site is that an event (which I define as the live, virtual meetup or conference) is made up of one or more sessions and those sessions are made up of one or more speakers. Rather than maintain all of this metadata and content in a single file, I assemble it at build time, which also lets me reuse the session and speaker info (side note, there are also transcripts which are also in a different set of files but are never output independently)

This means that assembling the event page, for instance, is combining the metadata and content from three files. I make use the the `scratch` feature repeatedly to avoid scoping issues (yes, there are likely better ways to do that) and the `GetPage` function let's me pull the contents of another file.

```html
<div class="flex items-center font-medium leading-tight avatar-list">
  {{ if ne .Params.sessions nil }} {{ range $session := .Params.sessions }} {{
  with site.GetPage (print "/sessions/" $session) }} {{ $.Scratch.Set "speakers"
  .Params.speakers }} {{ end }} {{ $speakers := $.Scratch.Get "speakers" }} {{
  range $speaker := $speakers }} {{ with site.GetPage (print "/speakers/"
  $speaker) }}
  <img
    src="/img/speakers/{{ .Params.speaker_image }}"
    alt="Avatar for {{ .Title }}"
    class="inline-block w-12 h-12 border-2 border-white rounded-full"
    width="140"
    height="140"
    title="{{ .Title }}"
  />
  {{ end }} {{ end }} {{ end }}

  <span class="max-w-xs ml-2">
    {{ range $session := .Params.sessions }} {{ with site.GetPage (print
    "/sessions/" $session) }} {{ $.Scratch.Set "speakers" .Params.speakers }} {{
    end }} {{ $speakers := $.Scratch.Get "speakers" }} {{ range $speaker :=
    $speakers }} {{ with site.GetPage (print "/speakers/" $speaker) }} {{ .Title
    }}
    <span class="delimiter">&amp;</span>
    {{ end }} {{ end }} {{ end }}
  </span>
  {{ end }}
</div>
```

There's obviously a lot more to the site than what I cover here so I encourage you, if you are curious, to explore the [repo](https://github.com/remotesynth/certifiedfreshevents).

_As an aside, if I were to build it today, I would probably use [Astro](https://astro.build/), but there's really no specific issue with Hugo, I just am more comfortable in Astro nowadays. That being said, there's no compelling reason to change (other than it might be fun)._

The site is deployed to [Netlify](https://netlify.com). There's really nothing special to share about that since Netlify makes the deployment super easy. A quirk of Hugo on Netlify means that I do need to specify the Hugo version as an environment variable but otherwise the deployment just works. One specific requirement of my site is to override the default Hugo build method to include the `-F` or `--buildFuture` flag because my events are future dated and, by default, Hugo ignores them. This flag means it will build items with dates in the future. I do also use some additional Netlify services, which I'll discuss.

### Dynamic Functionality with Netlify Functions

Many of the sites dynamic functionalities come from some of the embedded services, which I'll discuss more below. However, there are a few elements that require the use of a backend serverless functions via [Netlify functions](https://www.netlify.com/platform/core/functions/). All of mine are pretty simple, sign up for the mailing list, perform a search or sign up for an event via a signup form.

All three of these are essentially performing a backend API call to external services (which I will discuss in more detail later). Netlify functions just make it easy for me to include the code within my web site's repo and they get deployed as serverless functions for me. For example, here is the Mailjet function code that uses the Node Mailjet SDK to post a new contact to the list.

```javascript
const Mailjet = require("node-mailjet");

const mailjet = new Mailjet({
  apiKey: process.env.MAILJET_API_KEY,
  apiSecret: process.env.MAILJET_SECRET_KEY,
});
const listID = 10244548;

exports.handler = async (event, context, callback) => {
  try {
    if (!event.body) {
      return {
        statusCode: 500,
        body: "email query parameter required",
      };
    }
    const body = JSON.parse(event.body);
    const email = body.email;
    const firstName = body.firstName ? body.firstName : "";
    const lastName = body.lastName ? body.lastName : "";
    if (!email) {
      return {
        statusCode: 500,
        body: "email query parameter required",
      };
    }

    return mailjet
      .post("contact")
      .request({
        Email: email,
        IsExcludedFromCampaigns: false,
        Name: firstName + " " + lastName,
      })
      .then(async (res) => {
        const addedToList = mailjet
          .post("contact")
          .id(res.body.Data[0].ID)
          .action("managecontactslists")
          .request({
            ContactsLists: [
              {
                ListID: listID,
                Action: "addnoforce",
              },
            ],
          });
        const response = { msg: "Good news! You've been added." };
        return {
          statusCode: 200,
          body: JSON.stringify(response),
        };
      })
      .catch((err) => {
        console.log(err);
        const response = { errorMsg: err.response.statusText };
        return {
          statusCode: 200,
          body: JSON.stringify(response),
        };
      });
  } catch (err) {
    console.log(err);
    return { statusCode: 500, body: err.toString() };
  }
};
```

I'll dig into the search one in a moment, but the sign up for an event form doesn't interact directly with event service that I use as it doesn't have an API. However it does have a Zapier integration so I am posting to a Zapier webhook which then manages the post to Crowdcast (my event service).

### Implementing Search with Algolia

Search is an important (if underused) aspect of a site that contains about [300 free archive recordings](https://cfe.dev/sessions/). To implement search, I use [Algolia](https://www.algolia.com/) which makes the search effective and easy. There are three aspects to the search implementation given that this is a static site. The first is posting new items as they are created.

The posting of new events is handled through an npm package that is old but still works (I've been using it for years) called [Algolia Atomic](https://www.npmjs.com/package/atomic-algolia). It handles batching the requests so that you use the smallest number of operations against your Algolia account (honestly, Algolia's free plan is very generous in my opinion).

To make this work with Hugo, I need to create a JSON file that lists all my sessions (currently, the search searches sessions and talk shows and not the upcoming events). First, I need to add an output to my Hugo config.

```yaml
outputs:
  home:
    - HTML
    - RSS
    - Algolia
```

Then I need to define the output format as JSON.

```yaml
outputFormats:
  Algolia:
    baseName: algolia
    isPlainText: true
    mediaType: application/json
    notAlternative: true
```

Finally, in my default layouts I include a `list.algolia.json` template that outputs the JSON necessary for this to work. It's kind of complicated to parse because it needs to pull all the pieces together from the multiple page parts we discussed above but it works.

```handlebars
{{/* Generates a valid Algolia search index */}}
{{- $.Scratch.Add "index" slice -}}
{{- range where (where .Site.RegularPages "Section" "in" (slice "sessions" "talkshows")) ".Params.recordings" "!=" nil -}}
  {{- if (and (not .Draft) (not .Params.private)) -}}
  {{- if isset .Params "speakers" -}}
    {{- $event := "" -}}
    {{- $eventArr := slice .Page.File.TranslationBaseName -}}
    {{- $events := where .Site.RegularPages ".Params.sessions" "intersect" $eventArr -}}
    {{- $event = (index $events 0) -}}
    {{- $eventdate := .Date.Format "Jan 2, 2006" }}
    {{- $speakerPage := index (first 1 .Params.speakers) 0 -}}
    {{- $speaker := site.GetPage (print "/speakers/" $speakerPage) -}}
    {{- $homepageBanner := "" -}}
    {{- if isset .Params "homepage_banner" -}}
      {{- $homepageBanner = .Params.homepage_banner -}}
    {{- else -}}
      {{- $homepageBanner = $event.Params.Homepage_banner -}}
    {{- end -}}
    {{- $.Scratch.Add "index" (dict "objectID" .File.UniqueID "date" $eventdate "dir" .File.Dir "expirydate" .ExpiryDate.UTC.Unix "fuzzywordcount" .FuzzyWordCount "keywords" .Keywords "kind" .Kind "lang" .Lang "lastmod" .Lastmod.UTC.Unix "permalink" .Permalink "publishdate" .PublishDate "readingtime" .ReadingTime "relpermalink" .RelPermalink "summary" .Summary "title" .Title "type" .Type "url" .Permalink "section" .Section "categories" .Params.Categories "banner" $homepageBanner "speaker" $speaker.Title )}}
  {{- end -}}
  {{- end -}}
{{- end -}}
{{- $.Scratch.Get "index" | jsonify -}}
```

To use this, there are two simple steps. First I run a local build of the site with the flag to build future dated posts and then I run the Algolia Atomic command.

```bash
hugo -F
npm run algolia
```

The latter command just aliases the `atomic-algolia` call.

## Streaming the Events

We've mostly hit the part of this post where we leave code behind. A lot of CFE.dev runs on external services, the most important being the ones that run our live events. For that we use two services: [Crowdcast](https://www.crowdcast.io/) and YouTube.

_As an aside, we used to use Vimeo rather than YouTube because it made it easy to make my videos only accessible on my own site. This was back when I had implemented a sign up for the site. The plan was maybe to try some subscription and/or drive more mailing list subscriptions, but ultimately I gave up on the sign ups and made everything free and open and, thus, dropped Vimeo._

All of our major events (meetups and conferences) are done via Crowdcast. I originally chose this because it made it extremely easy to potentially charge for events without needing to code a registration and payment process. Nowadays, I don't charge for any of the events, but Crowdcast still works well for my purposes, with Q&A, chat, and other integrated features. I also use the embed to allow easy registration on my event pages.

![Crowdcast interface](/images/posts/virtualevents/crowdcast.png)

Why use Crowdcast at all and why not move entirely to YouTube? The mailing list. Crowdcast lets me collect emails of registrants and add them to my mailing list whereas YouTube offers no such ability (afaik). And the mailing list drives a significant portion of my future registrations.

The talk shows and live coding shows ([DevRel(ish)](https://cfe.dev/talkshow/devrelish/), [2 Full 2 Stack](https://cfe.dev/talkshow/2full2stack/)) all run just on YouTube. The live stream is embedded in the site.

The embed URLs for Crowdcast and/or YouTube (Crowdcast videos are eventually posted to YouTube as well) are just included as part of the page front matter.

```yaml
recordings:
  crowdcast:
    url: https://crowdcast.io/c/building-an-api
    start_time: "04:47"
  youtube:
    url: https://youtu.be/6kpvLQmDZls
    length: "57:30"
```

## Supporting Tools

There are a number of additional supporting tools and services that make the site run (if you're wondering, yes, it all adds up 💰💰).

### Triggering Actions with Zapier

The primary need for [Zapier](https://zapier.com/app/dashboard) on this site is because Crowdcast does not currently provide an API. In order to sign folks up for the mailing list when they register for an event, I use a zap that passes the registration information to Mailjet.

However, I also have a few other zaps. One I mentioned earlier is a webhook to post registrations from a form to Crowdcast. Another posts new events from my [RSS feed](https://cfe.dev/rss.xml) to our [Discord](https://discord.gg/jthCg8DHSg). Finally, because events are very date-based, I have a Zap which triggers a daily Netlify rebuild to refresh dates and lists of upcoming events. This last one I could do with Netlify's [scheduled functions](https://docs.netlify.com/functions/scheduled-functions/), but that wasn't available when I built the site.

### Managing Mailing Lists with Mailjet

[MailJet](https://mailjet.com/) is a recent addition to the site. Mailing lists can get _very_ expensive. In fact, the mailing list was by far the single most expensive item on this list but Mailjet helped with that. I started with Mailchimp, but they made pricing changes that made it incredibly expensive (for example, charging you for folks you can't communicate with because they unsubscribed). I then went to ActiveCampaign, which I used for years. As my mailing list grew though, the price became unsustainable for me. It includes a ton of automation and CRM-type features that I never used anyway.

Mailjet is, in my opinion, a more stripped down emailing service, but it does everything I need it to do and saved me upwards of $200/mo ($50/mo vs $250+/mo).

### Streaming via Streamyard

I originally signed up for [Streamyard](https://streamyard.com/) because the streaming options in Crowdcast v1's built in streaming were very limited. This has since improved enormously, but Streamyard has a number of other features that make it useful to me. The ability to do multi-streams is helpful as we've started streaming to both YouTube and Crowdcast at the same time. The customizable displays and branding are useful too. I'm sure I could do all this via OBS but I've often found it difficult and the benefit of Streamyard is that it makes it incredibly easy. I've also almost never had any technical issues with guests or screen sharing despite years of use and hundreds of guests.

### Transcriptions with Otter

[Otter](https://otter.ai/) isn't entirely designed for what I use it for, which is to generate transcripts of sessions that are then posted to the site. It's really intended for transcribing work meetings live. It does not have a way (that I am aware of) to hook into Streamyard or Crowdcast, so I use it very manually. I download the audio from Streamyard of each event (it can handle video but audio-only makes the whole process faster to upload and transcribe).

I then manually go through and make corrections and label speakers (it can auto-detect speakers who you've transcribed before but my speakers tend to be new each time). The good news is that it is pretty accurate, but this is still a time consuming process. I then export the transcript as text to the clipboard, paste it into a file in my transcripts folder in my Hugo site (I name the file the same as the session it transcribed to make it easy to find and combine). Finally, I make some Markdown formatting to make it easier to read (mostly just bolding names).

Is this a lot of work for what is probably a lightly used feature? Yes. I think it can be valuable to some people and make the site more accessible but my hope is that it also helps with SEO (though I can't back that up with data).

### Creating Shorts with Opus Clip

This is another recent addition to my toolset. I have been toying with reusing the content on my site by creating short clips of the live episodes to reuse as YouTube Shorts and hopefully build my audience. The problem is that generating those 60 second clips is an extremely time-consuming process when done manually. Luckily, [Opus Clip](https://www.opus.pro/) does this all via artificial intelligence.

The nice things about Opus Clip versus competitors that I looked into were that it allowed you to edit the generated video and that it gave you a ton of videos each with an explanation as to why it thinks they might drive views (and scores them to help you decide).

![Opus Clip](/images/posts/virtualevents/opus-clip.png)

Has this driven YouTube subscriptions? I don't think so honestly. This could be that I haven't used it consistently enough. Some of the videos have gotten views but few have driven subs.

### Payments via Stripe

All of the above costs money. Once upon a time, I lost money every month keeping this site going. Thankfully sponsors have stepped in to help defray the costs of the site and allow me not only to keep creating content on there but to make all of it free. To handle invoicing for sponsors, I use Stripe. There's really nothing special to how I use it since all the invoicing is manually set up in the Stripe dashboard, but it's still a critical part of the services I use.

## Whew! 😅

Having written all of this out, there's _a lot_ to the site. It's not complicated, just a lot of small pieces. Are there places where I could improve things or consolidate services? My assumption is yes, but the least available resource this site has isn't money but time. Keeping the site running and creating new content is extremely time consuming to the point that updates to the site tend to fall behind schedule. I do my best. 🤷
