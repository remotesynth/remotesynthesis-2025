---
title: "When You Build the Wrong Thing"
tags:
    - ai
description: AI makes it almost too simple to release stuff, which can, as in my case, lead to not enough preparation.
pubDatetime: 2026-07-24T10:23:31.210Z
---

For developers, AI has made it easy to build and release new projects. The code part, which, even when it wasn't difficult, was at least time-consuming, is now easy and relatively quick. This has led to a boom of micro-SaaS apps as the barriers for developers releasing their side projects have dramatically lowered.

As Allen Helton recently noted:

> Specifically coding agents removed barriers preventing us from launching products in our free time. The time it would have taken to research, build, tinker, polish, rebuild, and polish some more has been replaced with a plain-text “_Make it do this_” and walking away from our laptops (or cell phones 🤯).
> 
> Source: PSA: [That probably doesn’t need to be SaaS](https://www.readysetcloud.io/blog/allen.helton/that-probably-doesnt-need-to-be-saas/)

Lowering the burden of building these apps in many ways reduces risk, because the cost of failure is just a bit of time and tokens. Cory Doctorow talks about this very issue in his new book "[The Reverse Centaur's Guide to Life After AI](The Reverse Centaur's Guide to Life After AI](https://us.macmillan.com/books/9780374621568/thereversecentaursguidetolifeafterai/)" as it relates to recommendation letters for law schools:

> The fact that a professor sat down and wrote their own paragraphs of stilted puffery on behalf of a student used to convey something about the prof's estimation of the candidate, because no one would do such tedious work for a bad student.

But, just as with software development, removing the tediousness can easily lead to carelessness, which, in the case of recommendation letters, led to an explosion of meaningless AI-generated letters.

This lower investment required also leads to asking too few questions and doing too little due diligence. It's so easy to get an idea and be like, "Screw it...I'll just build it!" While there's nothing inherently wrong with that (it can be a lot of fun), it can easily lead to building the wrong thing – or even the right thing in the wrong way.

I ran headlong into this problem myself recently, and I learned two lessons:

1. Being able to build quickly, cheaply, and easily doesn't inoculate us from having to ask the hard questions about why we're building this, who needs it, and how best to meet those needs.
2. Aligning with open standards wherever available can help diminish the risk of each micro-SaaS app existing in a silo while potentially increasing chances of success or at least reducing the sting of failure.

## "Let Us Discuss Your Failures"

Or, more accurately, my failures (side note: I am a big Overwatch fan and "Let us discuss your failures" is one of my favorite Symmetra voice lines).

I spent a few weekends building and launching a site for managing local, in-person gatherings (a la Meetup) called [DevRel(ish)](https://devrelish.tech). It seemed like a slam dunk win to me.

For one, Meetup.com is, in my opinion, a case study in "enshittification." The site has gotten progressively more expensive even as the service it provides has either gotten worse or, in many cases, is basically the same as it was a decade ago. The burden of this additional cost has fallen on organizers who are already overburdened, with high demands on their time and often on their wallets (many meetup organizers I know foot all or part of the bill for things like food and drink).

Second, sites like Eventbrite and Luma are focused on _events_ rather than _groups_, which makes them workable for the meetup-like gatherings but not ideal, in my view. The "lock in" of Meetup – what allowed it to enshittify – is that your group has followers who are notified of activity in your group, including any new events. The other sites do let you follow an organizer but not a specific group. It seems like a small distinction, but it's an important one (to me at least). 

Third, unlike many sites, my site would allow you to RSVP for an event and even to follow a group without requiring registration.

Plus, the aim for the site was to be open source and free. Win, win, win, win...right?!

Wrong. A couple of months after launch, my new site had all of 3 groups hosted and no actual events (I think perhaps one was posted during that period and only briefly, with no RSVPs). Sure, there was likely an issue of awareness, but it quickly became clear that either I wasn't solving a real problem or I was solving it incorrectly.

## Rethinking the Approach

### Developing with AI Requires More Research and Planning, Not Less

AI makes coding "cheap" (yes, AI has many costs, but here I am specifically referring to the time and expense of the developer), but it doesn't absolve us from doing our due diligence. The time between thinking up an idea and having a working version built can be extremely small, but that actually puts _more_ burden on thinking through the problem you are trying to solve.

Think about it this way:

In a traditional development scenario, building my side project might have taken months. During that time, I would have had time to dig deeper into research, get reactions on initial work, and adjust my strategy as necessary. When the development time is compressed into hours or days, there is little time or opportunity for rethinking or adjustment, so all of that needs to be part of the pre-development work you do before setting your agent to code.

For DevRel(ish), I did research on how I wanted to build the app and the tools I wanted my agent to use, but not enough research into competition, what gaps existed, what needs I intended to fulfill, etc. I wasn't building this project for my own use. It was for the community, and I failed to explore deeply enough how best to meet their needs, which led me to entirely miss the existing work being done in ATProto around events on sites like [Smoke Signal](https://smokesignal.events/), [atmo.rsvp](https://atmo.rsvp/) and [OpenMeet](https://platform.openmeet.net/) (side note: since I started writing this Smoke Signal has closed posting events and only lists events listed on ATProto).
### Developing with Open Standards Can Reduce The Risk of Failure

When creating a project like this, there are two sets of risks:

1. The risk that I invest time, money, and effort into something that no one uses.
2. The risk for users of the site that they invest in a platform that fails.

By not aligning to open standards, I increased both risks because they are inherently tied together. Regardless of it being free, users may feel less inclined to take a risk on a platform that is proprietary. This is especially true for the audience I was targeting, who put a lot of their own blood, sweat, and tears into running local community gatherings. It's tough risking that on a closed and untested platform. This, in turn, means that my time, money, and effort are more likely to be wasted.

By swapping to an open standard like ATProto, I hope to reduce the risk to the end user and thereby reduce my own risk. By using an open standard:

* The end user feels less risk of losing their data should the site fail because they own their data via ATProto.
* Because I aligned to existing [lexicons](https://atproto.com/guides/lexicon) in ATProto, the site becomes interoperable with other existing sites serving similar purposes. This can bring more awareness, reduce the risk of lock-in, and make the open source project more useful – someone could stand up their own version of DevRel(ish), and it would be interoperable both with *my* existing site and other existing sites serving similar purposes.
* I feel that my own risk of failure is lower, both because of the two items above but also because the data and success aren't tied to my specific implementation.
The benefits aren't _just_ tied to ATProto. The site is built using open source tooling wherever possible (in some cases, there are no free and open source tools to do what the site needs to do), which makes it easier for others to take it and run with it. This means that, even if my version dies, it has a better chance to still be valuable as an open source project that can be iterated and improved.

## I'm Not Saying I Got the Formula Right, Just Better

I haven't even officially re-launched DevRel(ish), so who knows if this new direction will ultimately work better than the last one. But I already _feel_ better about it. I spent more time investigating to ensure it fills a need and does so in a way that is tied to open standards. In doing so, I learned a ton about ATProto, which was something I'd hoped to learn (and clearly misunderstood), so this additional work benefited me. Any community that posts on DevRel(ish) won't be locked in, and their community will be interoperable with existing sites. Finally, I feel that the [open source project](https://github.com/remotesynth/DevRel-ish-) has far more value for the community, even if my own version doesn't take off.