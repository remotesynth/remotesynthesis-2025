---
title: "Two Ways AI Is Changing the Developer Conference Presentation"
tags:
    - conferences
description: The nature of conference presentations at developer-focused tech conferences seems to be changing in at least two important ways.
pubDatetime: 2026-11-01T10:23:31.210Z
---

The past two years have seen a dramatic shift in how we develop code. It seems straightforward, then, that this would impact how we present developer topics in a session at a conference. Yet, over the past two years or so, I have not had the opportunity to *attend* a developer conference in a while without spending my time at the booth, unable to watch sessions. So attending sessions at Web Unleashed last week seemed like a sudden, dramatic change.

In this post, I want to share two observations I had about the changing nature of the conference presentation at developer conferences. I'll readily admit that both are based on a small sample size, but, given the shift in how we develop software, they both seem to just make sense.

## Teach Concepts, Not Code

For better or worse (and let's be honest, mostly worse), developers are not spending their days writing code any longer. Instead, they are prompting and supervising agents that write most of the code. That's not to say that they are writing no code; it's just a much, much smaller part of their job or may just involve reviewing already written code. 

This isn't just me saying so, but nearly every person I've spoken to at recent events, including this one, barring a handful of folks who are deeply skeptical of AI and still able to survive today's AI mandates and usage tracking.

So it makes sense that there was only minimal exploration of actual code in the presentations I attended. Instead, the sessions were largely around teaching the concepts you'd need to understand to improve the output of agents. Even the one session I attended that explored code, that code was mostly to create something fun, as though the written code part is now a fun hobby for the true code artisan. Yet, even in that presentation, the code took a backseat to teaching concepts.

In a way, this is a welcome change. Oftentimes in the past, the code was the hardest problem to solve, so the concept got short shrift in the session. If I have to spend a lot of time explaining code, then I can't go as deep into the concept as I might otherwise wish I could, given time constraints. It's also, as I mention in [my recent post](https://remotesynthesis.com/posts/the-joy-of-programming/)a bit sad, since solving hard problems in code was one of the joys of being a programmer.

Nonetheless, when your job is mostly about guiding an agent, concepts matter more than the underlying code, and the deeper you can understand a concept, the better. So, it makes sense that today's presentations may lack much actual code.

## Interactivity is the Baseline

Interactive sessions that encourage some kind of audience participation or include interactive on-screen elements can be a lot of fun. In the past, though, I've done them sparingly because they required _a lot_ of up-front work. Developing a presentation (and demo) is already incredibly time-consuming, but developing a presentation with an interactive UI or an audience participation mechanism was much, much more so.

This isn't exactly the case anymore with AI. First of all, your agent doesn't care if you're creating a slide deck in Google Slides/Powerpoint or creating it as a web page. To the agent, both are essentially equivalent effort. So then why make a traditional slide deck at all when a web page can give you the equivalent functionality with the ability to add custom, interactive elements to the slides?

The presentations that stood out to me at Web Unleashed all followed this pattern:

* As part of his presentation, [Simon MacDonald](https://mastodon.online/@macdonst) demonstrated using the Web Audio API to create a drum loop by including a fully interactive sequencer to create and adjust the drum beat on his slides.
* [Carolyn McNeillie](https://www.linkedin.com/in/carolyn-mcneillie/) demonstrated concepts around color theory by including interactive slides where she could demonstrate the concepts via color sliders, which made clear the differences between HSL and OKLCH color models, that may otherwise have seemed too abstract, much more obvious.
* The peak example, though, goes to [Sean C Davis](https://www.seancdavis.com/) who turned his slide deck into an interactive game. Attendees were encouraged to start the game on their phone via a QR code, and then, as the session progressed, so did the levels of the game. Each level of the game made it more complex and aligned with a new concept he was introducing in the slide. The slides even pulled in data from the attendees' usage of the game.

In each case, these weren't slides in a traditional sense; they were a web application that functioned as slides, but allowed for a much richer experience. All of this was obviously possible before AI, but by reducing the effort required to achieve this, AI may be turning interactive presentations into the baseline expectation an audience has. 

While I, being a little rusty myself, having not spoken at an event in a couple of years, brought traditional slides, I don't expect to do so ever again.

## Summing Up

The thing is that, the way I see it, these two observations fit nicely together. If AI has changed the nature of slides, whereby showing code is either no longer necessary or takes a major backseat to going deep on a concept, then interactivity is the way of reinforcing that concept without needing the code. Yesterday, I might have taught a concept and then shown it in code to help it make sense, while tomorrow I will likely go deeper into the concept with minimal or no code and demonstrate it either through interactive slides or audience participation.