---
title: I Totally Misunderstood ATProto
description: I thought I knew what AT Protocol was about. It was for Bluesky and Bluesky-like sites and maybe auth. I wasn't entirely wrong but I was also way off the mark.
tags:
  - ATproto
pubDatetime: 2026-08-05T10:23:31.210Z
---

You may be hearing a lot about AT Protocol or ATproto, as it's often referred to for short, or maybe even heard of the Atmosphere. You may have some sense that it is an open standard that is somehow tied to Bluesky. So you suspect it somehow is connected to social media, maybe. Perhaps, you are particularly interested in open standards and especially how they may assist us in countering some of the ill effects and misaligned incentive structures of "big tech" social networks.

That's where I was only a few weeks ago. I'd been saving some links and following some folks around ATproto, because it seemed to be something of particular interest to me personally. This is especially true because, as someone who has been developing for the web professionally for 30 years, I have major concerns over the current state of the open web.

At the time, in my spare time, I was building a site called [DevRel(ish)](https://devrelish.tech) that was aimed at offering free and open tools for folks in tech who were organizing in-person events and gatherings. I _thought_ ATproto was mostly some kind of identity/auth standard tied to BlueSky. I knew that there was some part of the standard that allowed posts on BlueSky to be interoperable with other ATproto-based social media sites like [BlackSky](https://blacksky.community/) or [Mu Social](https://mu.social/), but, since I was building an event-focused site, that didn't seem super relevant.

I'll build the site, I thought, and then focus on how to integrate ATproto as an alternative sign-in option afterwards. I wasn't wrong that this was _a possible_ use of ATproto, but I had thoroughly misunderstood what ATproto was really about and the opportunity it offered to radically rethink my application if I built around it rather than treating it as simply an auth option.

I'll note ahead of time that I am still learning about this stuff. So I am sharing what I have learned so far in the hopes that it helps _but_ my knowledge on this topic is still new and limited, and I will be simplifying some explanations for the sake of making this all easier to comprehend (i.e., forgive me if any explanations gloss over some technical details).

## Clarifying the Terminology

For me, part of the trouble was that I didn't quite understand any of the terminology that tends to fly around about ATproto.

### What is ATproto and how's that different from the Atmosphere?

First, [**AT Protocol**](https://atproto.com/) is the standard. It stands for authenticated transfer protocol. It is the standard that was designed by the team around Bluesky. As [this excellent history of how the protocol came to be](https://pfrazee.leaflet.pub/3mrpsdizmus2h) notes, "Bluesky was founded to produce a protocol which Twitter could adopt." Honestly, having known about its origins for years, this may be where some of my own confusion about ATproto stemmed from, but the team had bigger dreams of being the protocol for far more than just the Twitter use case – and so it is.

One of these big ideas was around data sovereignty, which is basically the idea that you own your data and can take your account and your data to another site if you choose, thereby disrupting the whole misaligned incentive structure in social media (if you're interested, you can dig more into this specific aspect around incentive structures and data sovereignty in ATproto [in this post](https://blog.joebasser.com/3m52tr7s75c2a)). We'll dive into how that works a bit more later.

The **Atmosphere** is a network of sites that all use ATproto under the hood. Basically, if you have an account with one of them, you can use all of them. Do I mean a Bluesky account? Yes and no. A Bluesky account is an Atmosphere account and can be used to log in to other Atmosphere apps, but it is not the only way to establish an account on the Atmosphere. The idea here, remember, is about data sovereignty, so locking you in to a single identity provider wouldn't make much sense. (Side note: if you want to learn more about what the Atmosphere is, read [this post](https://lab.leaflet.pub/3mrq6ma5dgs2x).)

### How does ATproto ensure data sovereignty and avoid lock-in?

But how exactly does that work? It's one thing to be able to switch your account over, but how can you take your data too? That's where a **[PDS (personal data server)](https://atproto.com/guides/the-at-stack#pds)** comes in. You may have heard that data in ATproto is "federated," meaning it's spread across many servers, and that's where PDSs come in. Your application data is written to a PDS. From there, it's syndicated out over [sync](https://atproto.com/specs/sync) streams to "interested applications" across the Atmosphere. Yes, Bluesky operates PDSs, but "there are now over 3,000 PDS operators in production" today ([source](https://pfrazee.leaflet.pub/3mrpsdizmus2h)).

Your data on a PDS can be migrated to a different PDS, but it is not synced across PDSs. This is a key difference to Mastodon/ActivityPub. This ability to easily migrate to a different PDS but retain your data solves the data sovereignty aspect, though, to be clear, that data is all public, so you do not control who gets to see it (at least, not yet).

Data on the PDS is (at the moment) all open, which means that ATproto isn't exactly a workable solution for data that, while tied to a user, needs to be private. In fact, you can go see my PDS data (or that of anyone else on the Atmosphere) [here](https://atproto.at/uri/at://did:plc:56ek3ps3dttt2ui3cwdmmuxe#constellation).

![Viewing my ATproto PDS contents](/images/posts/atproto-collections.jpg)

You may notice that while Bluesky is one of my apps with multiple collections, my account is not a Bluesky-specific account, and there are collections for other apps. This works because, even though I originally established my ATproto ID on Bluesky, my account is associated with a **DID (decentralized identifier)**. DIDs are effectively a pointer that indicates where my PDS resides. Using this DID, apps across the Atmosphere can access the data in my collections. So the data doesn't sit in a proprietary format only available to Bluesky's, but is accessible to any ATproto site via my associated ID.

Each of those **collections** contains data. For example, you can actually click through to `app.bsky.feed.post` to see all of the data behind my Bluesky posts. This data will conform to the shape of a **[lexicon](https://atproto.com/specs/lexicon)**. A lexicon is the schema that defines the shape of data, such as posts, likes, and follows.

Lexicons are also a key to what makes this data interoperable and not locked to a single provider. For example, if I were to make a Bluesky clone, I can conform to the standard lexicon for posts, likes, and follows. Since the data is open and our data both conform to the standard lexicon shape, I can read from Bluesky posts, likes and follows data in the collection on the user's PDS repository or, if the user grants access, I can even write to the same collection.

Dan Abramov described all this as a "[social filesystem](https://overreacted.io/a-social-filesystem/)." I recommend reading his post for a far better and more accurate description of how this all works.

## How Is Any of This Useful to Me?

The implications of ATproto were not immediately obvious to me at first. I saw it as limited to Bluesky or Bluesky-like social media. I thought maybe it might be useful for auth/login for a subset of users who used Bluesky or similar sites. I did not get how the Atmosphere related at all.

But once you start to dig around the ecosystem, you can start to see how it can serve as the backbone of a huge number of applications beyond text-based social media. Here are just some examples:

- [Leaflet](https://leaflet.pub/): a blog and newsletter hosting site that offers free and paid features for content creators that (in my opinion) has long-term potential as a Substack replacement.
- [Tangled](https://tangled.org/): a code hosting and collaboration application that is similar to a GitHub.
- [Spark](https://sprk.so/): a short-form video platform that is similar to TikTok (or I think so since I have literally never used TikTok).
- [atmo.rsvp](https://atmo.rsvp/) and [OpenMeet](https://platform.openmeet.net/): event hosting/RSVP platforms similar to lu.ma or Meetup (or similar to [DevRel(ish)](https://devrelish.tech) , which I am also in the midst of transitioning to ATproto).

These are just a handful of examples. I also foresee a future where ATproto sites expand well beyond use cases that are "similar to" existing social tools. I know there are examples out there, but I expect this to grow as more folks become aware of the capabilities. Personally, I can't wait to continue learning about it and using it.
