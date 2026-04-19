---
title: "Announcing DevRel(ish) – A Free Site for Running IRL Tech Communities"
tags:
  - devrel
description: Announcing a new, free and open source site for hosting in-real-life gatherings for niche tech communities.
pubDatetime: 2026-04-19T10:23:31.210Z
---

It feels like it's becoming ever more difficult to make real connections in our industry. Most of us have very little, if any, budget for attending conferences, and many community-focused events have called it quits. Some local gatherings still exist, but many have shuttered. What remains of both conferences and gatherings seems dominated by branded events focused on pushing the narrative of a big tech corporation.

On top of all of that, our platforms have failed us. Meetup.com is emblematic of "enshittification". The service has become expensive and worse. The "improvements" that get made feel designed purely to force you to pay more rather than to address the real difficulties of running local gatherings. Lu.ma is much more reasonably priced (in some cases even free) but is focused on events rather than communities. Informal means of organizing for free via Slack or Discord can be difficult.

These are some of the pains that led me to create a new site called [DevRel(ish)](https://devrelish.tech). It's a free site for running your own niche communities, whether based on topic or location, and organizing in-real-life (IRL) gatherings.

## What's DevRel(ish)?

DevRel(ish) is not a full replacement for Meetup.com or Lu.ma. It is intentionally designed to be simple and fit the needs of smaller, more niche communities to meet in person, whether they are a local gathering for people interested in web development or a topic-focused gathering for underrepresented folks in tech who meet at conferences not bound to a single city.

> Side note: For those of you who may recognize the name, yes, I took it from the name of a podcast Erin Mikail Staples and I ran about working DevRel and related roles. The original version of the site was aimed at running DevRel communities, but I expanded it as I think the need is broader.

Here are the key features for attendees and organizers:

- **It's incredibly easy to RSVP – no registration required.** Just fill out the RSVP form with your basic information, and that's it. The site will not send you engagement or marketing emails. Your email is only shared with the organizer for the purposes of running their group. You can, if you choose, follow a group's postings using either email or RSS so that you are notified if new events are posted.
- **Organizers own their group – not the site.** DevRel(ish) aims to make it simple to create your group (requires admin approval), organize, and share gatherings. RSVPs are shared only with the organizers. The site does not control your communication with your attendees. Instead, you can download RSVP lists and are free to use whatever tools you want to communicate with your group about this gathering or announce any upcoming ones.

Plus, I aim to keep the site free for both attendees and organizers, though, at the moment, it runs on some services that may eventually incur costs, especially around email sending and the database. This is part of what drove the design of the site as well as the decision to limit it to specific categories of gatherings for the tech community.

Plus, it's [open source](https://github.com/remotesynth/DevRel-ish-). Want to take it and modify it to run your own communities? Go for it. The readme contains all the details you should need to stand this up on your own.

## How DevRel(ish) was built?

Yes, DevRel(ish) was built by AI using a combination of Claude Code and Cursor. I used an approach I've been refining recently that has worked well for me in my own tests. This tries to limit the decisions of the LLM by dictating not just the specs but the tools.

Left to its own devices, tools like Claude Code and Cursor [gravitate towards certain solutions](https://amplifying.ai/research/claude-code-picks). Instead, I did the research and largely instructed what tools we'd use. For instance:

- **Astro 6 and SSR.** Rather than the default of building a React app, I forced the LLM to choose Astro and SSR. This is beneficial both in terms of how I wanted the site to be architected, but also because I am very comfortable in Astro and thus can easily validate and hand-edit the output code. I chose AstroDB for development while production data was pushed to Turso, which has a generous free tier.
- **Run on Netlify**. Netlify has a generous free tier, but my status as a "netlifriend" also gives me some additional leeway to provide this free to the community before necessitating a paid tier.
- **Emails with Resend**. Resend offers a generous free tier as well, which enabled me to implement the limited email communications the site requires. This is most likely where costs will be incurred first, but the types of email communications the site sends are intentionally limited.

Again, it's [open source](https://github.com/remotesynth/DevRel-ish-), so I welcome contributions or forks.

## Give DevRel(ish) a try!

Got a community you've been wanting to start? Please, give it a go and let me know your feedback. Keep in mind, this is still an early beta release and, while I've done my best to test it, there will surely be some bugs. However, I am hopeful that this can become a useful tool in helping connect people all across the tech community and build lasting friendships and valuable professional connections.
