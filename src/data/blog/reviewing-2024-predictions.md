---
title: Grading my 2024 Predictions for Developers
tags:
    - general
description: I wasn't bold and nonetheless I didn't do great. Sheesh.
pubDatetime: 2025-01-05T10:23:31.210Z
---

2025 is a hard year to predict. This is partly because 2024 brought a lot of things that made me question my own ability to make predictions. I heard someone say that 2024 was the year that the worst people in the world got everything they ever wanted and boy does that feel accurate.

It is also because predictions are only useful inasmuch as they give you some potential insight that you don't already have. For instance, predicting that AI will continue to have a growing impact on developers in 2025 (for better or worse...probably worse, in my opinion) is both obvious and unhelpful. On the other hand, every corner of technology, both generally and specifically for developers, seems to be converging on AI.

So, while I gather my thoughts on what else besides AI developers (specifically full stack, front-end, serverless and DevRel developers, since that's what I know most about) should know about, let's grade my [last year predictions](https://remotesynthesis.com/blog/2024-predictons-for-developers/). 

I'll start by admitting that, looking back, my predictions weren't particularly bold, so I plan to be tough on myself

## 1. Developers Begin to Flee Complexity: C

This prediction was about developers dropping tools like Next.js and React, which continue to grow ever more complex in my opinion (especially with the move to the app router), and moving to things like Astro or Svelte. While there was a lot of anecdotal evidence I could cite of developer opinions seeming to shift, but that would feel like cherry picking confirmation. Instead, I'll rely on the [State of JavaScript survey](https://2024.stateofjs.com/en-US/). Yes, I'm aware of concerns around the demographics of who answers that survey and I am a skeptic of surveys in general (lol it's fair to say that I am just generally a skeptic), but it's the only recent data we have.

That survey did show [usage drop for React](https://share.stateofjs.com/share/prerendered?localeId=en-US&surveyId=state_of_js&editionId=js2024&blockId=front_end_frameworks_ratios&params=&sectionId=libraries&subSectionId=front_end_frameworks) and [for Next.js](https://share.stateofjs.com/share/prerendered?localeId=en-US&surveyId=state_of_js&editionId=js2024&blockId=meta_frameworks_ratios&params=&sectionId=libraries&subSectionId=meta_frameworks), but only ever so slightly. I'd say, enough to grant me some points but not significant enough to confirm a trend. Astro did continue its rapid climb but everything else was either flat or declining.

I believe this is still a "work in progress." This isn't an easy shift to make. Changing frameworks on an existing project is a massive undertaking, but I think this year may confirm the slow decline we see in last year's data and the anecdotal evidence in blog posts and social media that opinions are shifting.

## 2. AI Becomes Ubiquitous but a Lot of AI Tools Disappear: C-

Even a year ago, the first half of this prediction was probably too obvious but I will grant myself some points in that it wasn't yet so obvious how broadly adopted they would become. There are [numerous](https://github.blog/news-insights/research/survey-reveals-ais-impact-on-the-developer-experience/) [surveys](https://share.stateofjs.com/share/prerendered?localeId=en-US&surveyId=state_of_js&editionId=js2024&blockId=ai_tools&params=&sectionId=other_tools) [that](https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report) show us closing in on near universal adoption of AI tools by developers. Tools like [Cursor](https://www.cursor.com/) exploded this year and with [GitHub Copilot now having a free tier](https://docs.github.com/en/copilot/managing-copilot/managing-copilot-as-an-individual-subscriber/about-github-copilot-free), this will almost definitely continue unabated. In retrospect this all seems super obvious, but a year ago many developers were still feeling cautious about AI tools, so I'll grant myself a few points.

The second part of this prediction was the bolder one, and I don't think I got this right. This was about the costs of AI finally catching up with the growth of AI. When companies need to [buy nuclear power plants](https://www.nbcnews.com/business/business-news/three-mile-island-nuclear-plant-help-power-microsoft-data-center-needs-rcna171958) or admitting that [they need hundreds of billions of dollars to compete](https://futurism.com/the-byte/openai-needs-vastly-more-money), you probably have a sustainability issue. Having been in the industry long enough to see multiple bubbles burst, this feels like a bubble and I'm far from the only one [making this warning](https://www.wheresyoured.at/subprimeai/).

Yes...but...that didn't happen in 2024. Few AI tools disappeared. They proliferated despite the costs. VC money for AI has far from dried up and in fact is likely killing other aspects of technology because funding is drying up elsewhere to free up resources for AI. People are even losing their jobs to help free up money to pay for AI (it's getting tough to argue that the continuing layoffs in tech are motivated by a bad economy or even the pandemic bubble). So points lost and I give myself a barely passing grade for this one.

## 3. More Developer Conferences Shut Down but the Winners Continue to Grow: B

Finally, one I think that I got mostly right. I'll admit that finding data or sources to back this up is tough, but having spoken to many organizers and seen some conferences announce that they won't run again over the course of the year, I think I can safely say that the developer conference business is still a mess (with one major caveat that takes away points that I'll get into momentarily).

Not everyone may remember how many community run conferences we used to have here in the US. Surveying the conferences that are coming again in 2025, many of those appear to be gone. A handful of the larger, community-run conferences like KCDC or All Things Open seem to be growing along with many of the big corporate conferences, but the smaller ones seem to be fading away. I think this is largely being driven by a clawing back of benefits for developers by companies, making time and money for conferences harder to come by.

Here's the thing though, that's only in the US (perhaps in Canada too). By all accounts, the conference scene in Europe is thriving and conferences are packed. My evidence for this is purely anecdotal but has been confirmed by many friends and colleagues there.

2025 will likely continue this trend, especially as visa and travel restrictions are very likely in the US making it even tougher for US-based conferences to draw international attendees. In fact, we may see some of the larger events show some signs of struggle here, while their European counterparts thrive.

## 4. DevRel Adjusts to a New Realities (Show Me the Numbers!): A

If you work in DevRel, you know times are tough. Yes, it's tough across tech, but DevRel seems like it has been hit particularly hard. The layoffs have not stopped and the jobs are relatively thin. Even the jobs that exist are generally paying less (and requiring more).

A lot of this is anecdotal again (based on the folks I know and monitoring discussions on the [DevRel Collective Slack](https://devrelcollective.fun/)), but there are some numbers to back this up. For example, the [State of Developer Relations Report](https://www.stateofdeveloperrelations.com/2024devrelreport) showed:

> Compared to **2023**, **median base salary decreased** from **$175,000 (-14.3%)** and **average base salary decreased** from **$167,088 (-7.0%)**.

And while [layoffs decreased](https://www.stateofdeveloperrelations.com/2024devrelreport) ever so slightly from 2023 (which was a very bad year too) according to this survey, the percentage of respondents working for a company dropped ten points (along with an increase in freelancers and agency workers).

The jobs that do exist seem tougher. Folks in DevRel have to work extra hard to justify their existence right now, and I've heard many stories of new revenue or lead numbers being added to goals.

Early-stage developer tools startups still seem to be opting for hiring DevRel iIn lieu of marketing at first, so there are still some opportunities. I expect the layoffs to slow, as most teams seem pretty lean nowadays, but I don't anticipate a strong increase in hiring in DevRel, unfortunately.

## Final GPA: C+ (2.68)

Not great, but not awful I suppose. Let's see if I can improve for 2025.