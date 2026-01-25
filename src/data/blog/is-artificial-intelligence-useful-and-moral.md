---
title: Is Generative Artificial Intelligence Useful? And Moral?
description: There are a ton of difficult questions to answer around generative AI. Is it useful and how useful is it? And is it moral both in the way it is built and the way it is used? Let's dig in.
tags:
  - ai
pubDatetime: 2025-04-13T10:23:31.210Z
---

There is no shortage of opinions on AI – so much so, that sharing another set of opinions seems like throwing a penny into a fountain filled with coins: it's a fleeting gesture soon to be rendered meaningless by others doing the same and burying yours.

It doesn't help matters that AI is a bit of a moving target. Your opinion might seem prescient today and shortsighted tomorrow. It's not even that the technology is changing quickly (which it is), but that we don't clearly understand all of the impacts yet. This is why I've struggled with defining my perspective on AI even for myself (this post is, in part, an attempt to gather my own thoughts).

We could categorize our ever changing understanding of the impacts of AI into two areas:

1. Technological impact: This is basically questions around is this useful, if so, how useful is it and how will it impact the way we do our jobs?
2. Moral and ethical impact: Is this the right thing to do? Do the negative impacts of this technology outweigh its potential benefit? Is there the potential for abuse and misuse?

Often debates around AI seem to focus on one or the other of these categories at a time, but sometimes these streams cross. That was the case with the popularity of the [Ghibli-styled images](https://www.forbes.com/sites/danidiplacido/2025/03/27/the-ai-generated-studio-ghibli-trend-explained/) that seemingly took over social media for a week in late March. We were suddenly faced with a seemingly much-improved AI image generation that created images which, to an untrained eye, recreated a particular art style that was indistinguishable from an original. We were also faced with questions of the morality of creating these images, especially in the face of [well-known opposition to AI-generated art](https://www.youtube.com/watch?v=ngZ0K3lWKRc) from Studio Ghibli's cofounder, Hayao Miyazaki.

Since whether a belief that AI is useful or not directly affects any judgements around whether it is moral, I'll tackle that question first.
## Is It Useful?

The answer to this question, especially for the type of person who would be reading this post on my blog, may seem obvious. If you are a developer, there's a solid chance that you use AI-based tools regularly. And, if you use something regularly, then it must be useful. However contradictory it may seem though, the use of something is not proof of its usefulness. Something can be both *usable* and not *useful*, especially since usefulness is generally about the value of its use and typically measured in aggregate.

Let me give an example. Blockchain and, in particular, cryptocurrency is something that is usable. Blockchain and cryptocurrency have been around since 2009 – so over 15 year – and are still in use today. They are not useful though. Blockchain has found no widespread use case beyond cryptocurrency and cryptocurrency has proven no actual usefulness beyond money laundering, tax evasion and pump-and-dump schemes. The promises that blockchain and crypto would revolutionize industries and money have long since been given up even by their loudest cheerleaders.

The point is that, at least to me, being usable for certain niche use cases is not the same as being broadly useful. So is AI broadly useful? Let's look at first whether they are using it, why they are using it and the outcomes of its use.
### Are People Using it? And Why?

Developers have been at the forefront of AI _usage_ since the beginning. Coding assistants were among the earliest productized uses of AI in commercial tools (GitHub Copilot, for instance, launched in 2021). A recent [Wired Survey](https://www.wired.com/story/how-software-engineers-coders-actually-use-ai/) found that about 75% of developers had already used AI and a majority of them used it at least every week.

Interestingly, this same survey showed some unusual signs about its usage that may indicate this is not entirely driven from the bottoms up (by that I mean that developers are using it, finding it valuable and thus pushing for adoption). The strong adoption seems to be, in part at least, driven by a fear of being left behind as in this quote from a respondent:

> It's all they talk about. You have to get with AI if you want to move up.

This is a fear being reinforced by leadership that is pushing [AI mandates](https://www.fastcompany.com/91312832/shopify-ceo-tobi-lutke-ai-is-now-a-fundamental-expectation-for-employees). But using AI doesn't seem to be changing many minds among developers, with only 35% of Wired respondents calling themselves AI optimists while 38% being pessimists (the rest being agnostic). Another way to put that is that, of the 75% of developers that use AI, fully 40% of them (more than half), aren't convinced of its usefulness. If I am launching a product and more than half of the people who try it tell me it isn't useful, there may be a fundamental issue with what I'm trying to sell.

This plays out in other data as well. Developers are using the tools because they feel they have no choice but aren't finding them particularly useful. Let's take [another recent survey](https://leaddev.com/culture/ai-coding-mandates-are-driving-developers-to-the-brink) which found:

>While 75% of company leaders thought their AI rollout over the past 12 months has been successful, only 45% of employees said the same.

As that same article notes, growing usage (driven by management and/or FOMO) has actually led to *declining* perceptions of AI.
### Explaining the Disconnect

What's driving this disconnect of growing usage and declining perceptions? As [Charity Majors explained](https://stackoverflow.blog/2024/12/31/generative-ai-is-not-going-to-build-your-engineering-team-for-you/), it's that it turns out that writing code is the easy part of our jobs:

>People act like writing code is the hard part of software. It is not. It never has been, it never will be. **Writing code is the easiest part of software engineering**, and it’s getting easier by the day. The hard parts are what you do with that code—operating it, understanding it, extending it, and governing it over its entire lifecycle.

Any experienced developer understands this. When you first learn to code as a junior developer, it feels incredibly powerful. It takes years of experience to recognize the complexities and limitations. AI is both incapable of doing that and prone to producing code with errors, often that seem correct to an untrained eye. That's because generative AI, like a junior dev high on their newfound ability to code, [doesn't know what it doesn't know](https://blog.scottlogic.com/2025/03/06/llms-dont-know-what-they-dont-know-and-thats-a-problem.html).

> All LLM-based tools that I have used seem to lack an understanding of their own limitations. If you ask them to undertake a task that is far beyond their capabilities, they will valiantly give it a try, and utterly fail!
### Frustrating Outcomes

As we'll discuss further, generative AI is built upon grandiose promises – promises that much of the tech leadership has fully bought into for their own reasons. This is driving developers to use AI more broadly out of fear of being left behind or by outright management mandates. But that usage is leading, in many cases, to lower quality outcomes including [lower code quality and increased technical debt](https://leaddev.com/software-quality/how-ai-generated-code-accelerates-technical-debt) (they even outright [invent package names](https://www.theregister.com/2025/04/12/ai_code_suggestions_sabotage_supply_chain/) in a way that can compromise security) and [frustratingly poor products](https://amp.cnn.com/cnn/2025/03/27/tech/apple-ai-artificial-intelligence) even from big name players.

I think this ultimately leads to a bit of a disappointingly mushy answer to whether AI is useful. It seems pretty accepted that it allows us to accomplish some tasks faster. For example, developers (myself included) seem generally to accept that AI is good at [repetitive coding tasks (tests, boilerplate, algorithms)](https://thenewstack.io/ai-coding-assistants-are-reshaping-engineering-not-replacing-engineers/) but not good at large scale coding tasks (at least not in a way that they would ever be production-ready).

This has led to creating some mental frameworks for how we think about AI's usage, at least in a software development context. I personally found the framework lightly outlined by Annie Vella in [The Software Engineering Identity Crisis](https://annievella.com/posts/the-software-engineering-identity-crisis/) to be useful. Here's my slight variation of her framework:
* Some projects can be fully AI generated/vide-coded (prototypes, demos and proof of concepts) because long-term code quality is generally not an issue in these as they are short-lived by design.
* Some projects AI can be used to assist with those repetitive code tasks, but the majority of the work should is done by developers and AI-coding-tasks are heavily supervised by experienced developers to ensure accuracy and maintainability.
* Some projects should not use AI on any level because of either their complexity or their security requirements.
I use AI regularly, but that makes sense since most of my work falls into the first bucket and a portion in the second, with none in the third.

So, to finally answer the question, is it useful? Yes, but not nearly as useful as promised nor as useful as many tech leaders, with their mandates, seem to believe. It can speed up some development tasks and assist with learning but it doesn't even replace a junior level developer because it is unable to learn and improve. For most use cases (i.e. not demos and proof-of-concepts), it is forever a junior developer in their first month of employment, performing menial tasks fairly reliably (though sometimes imperfectly) in a way that is helpful but not irreplaceable. 
## Is it moral?

Comedian Steven Wright had a [famous joke](https://www.youtube.com/watch?v=oBOSUyJETfg):

> “Last night somebody broke into my apartment and replaced everything with exact duplicates... When I pointed it out to my roommate, he said, "Do I know you?”  

Part of the humor here is that the initial scenario is both morally and experientially meaningless. If every individual thing is an exact replica, was it really stolen? That situation takes a meaningful and humorous turn when it turns out that the roommate is an exact replica too – except the replica of a person doesn't include their memories and experiences.

Why do I bring this up? AI is a tool for making exact replicas of everything in our apartment. This seems harmless until it has the potential to make a replica of us – to replace us with something less meaningful. This is the essence of Hayao Miyazaki's quote that was frequently cited when referencing the AI-generated art, "Whoever creates this stuff has no idea what pain is."

AI is a replication machine and the [mashups](https://en.wikipedia.org/wiki/Mashup_(music)) it creates can sometimes be mistaken for original creativity, but are, in reality, nothing more than complex combinations of replicas. Yes, the creative process is often informed by what has come before but creation is forward looking, creating something that is unique beyond just combining past influences.

### The Morality of Training

This is the problem that I have with moral justifications for AI that are based upon some envisioned future where [AI enables some sort of "super science"](https://www.robinsloan.com/lab/is-it-okay/) leading to potential cures for cancer. This argument justifies the consumption and even replications of other people's work based upon a theoretical future wherein LLMs bring about major improvements in life-saving science, but as [Baldur Bjarnason points out](https://www.baldurbjarnason.com/notes/2025/now-im-disappointed/):

>Saying “we will probably get super-scientist AI” in 2025 is, unlike a 2019 statement on fluent chatbots, not a reasonable speculation to make based on current scientific and academic research.

The current LLM-based generative AI is inherently backwards looking, which, for example, is why it tends to excel at summarization . It can only perform based upon what it is trained on, which is why AI companies have become so greedy in their thirst for training data. It's ability to create soulless replicas – or ["pale imitations" of authentic thoughts and creativity](https://thehistoryoftheweb.com/what-happens-to-what-weve-already-created/) – depends on consuming all the work ever created.

This goes beyond reasonable arguments that it relies on the "theft" of original work. AI crawlers are also already straining the web's resources, testing the capacity even of sites run by Wikimedia, for instance, which have seen increases to upwards of [65% of their resource-consuming traffic coming from bots](https://www.techdirt.com/2025/04/10/ai-crawlers-are-harming-wikimedia-bringing-open-source-sites-to-their-knees-and-putting-the-open-web-at-risk/). Forcing companies to rely on [deploying AI labyrinths](https://blog.cloudflare.com/ai-labyrinth/) to restrain costs and maintain performance for ttheir actual human customers (while also hoping to protect their intellectual property).

When companies like OpenAI promote Ghibli-style art creation, they are both flouting that theft but also trying to present the resistance of people like Hayao Miyazaki as a lost cause. This has personal implications too, as AI agents on your devices have the potential to [train on and even leak personal information](https://www.techdirt.com/2025/04/08/if-ai-agents-catch-on-expect-the-legacy-copyright-industry-to-turn-them-against-you/). 
### The Morality of Consumption

There are two parts to this question. The first is purely financial. Generative AI, as an industry, openly celebrates its consumption of never-before-seen amounts of capital. The combination of venture capital money and spend by just Microsoft, Alphabet, Amazon, and Meta amounted to nearly a [half-a-trillion dollars in 2024](https://prospect.org/power/2025-03-25-bubble-trouble-ai-threat/). OpenAI's ([very suspicious](https://www.wheresyoured.at/power-cut/#:~:text=OpenAI%20does%20not,of%20the%20capital.)) last funding round valued the company at [$300 billion based on a $40 billion dollar round](https://www.marketwatch.com/story/openais-now-worth-more-than-chevron-after-300-billion-valuation-9a3fa6d1). As that article points out, it puts it above Chevron in terms of market cap. Chevron earned $18 billion last year while OpenAI has said that they expect their annual losses to be $14 billion by 2026 (in 2024 they [lost about $5 billion on $4 billion of revenue](https://www.lesswrong.com/posts/CCQsQnCMWhJcCFY9x/openai-lost-usd5-billion-in-2024-and-its-losses-are)).

All of this money might make sense if we are developing a cure for cancer, but, as noted in the "Is it useful?" section, we're currently talking about mostly incremental improvements to mundane tasks. There's really no argument that spending well over a half-a-trillion dollars to automate copy-pasting cost from StackOverflow is morally defensible. Yet, that's basically where we are with little actual evidence that the breakthrough benefits are even achievable, never mind just around the corner.

That doesn't even take into account the impact on people's livelihoods, as [Tressie McMillan Cottom points out](https://www.nytimes.com/2025/03/29/opinion/ai-tech-innovation.html?unlocked_article_code=1.7k4.oG8D.H6ureDIHnmAO&smid=url-share):

> But A.I. is a parasite. It attaches itself to a robust learning ecosystem and speeds up some parts of the decision process. The parasite and the host can peacefully coexist as long as the parasite does not starve its host. The political problem with A.I.’s hype is that its most compelling use case is starving the host — fewer teachers, fewer degrees, fewer workers, fewer healthy information environments.

As she notes, that's based upon the bast case scenario where AI becomes capable of replacing these jobs – something that it ultimately does not seem close to doing. Nonetheless, we've already seen waves of [AI related layoffs](https://www.forbes.com/sites/jasonsnyder/2025/02/12/ai-reset-layoffs-rto-and-the-new-realities-of-work/) from well-known companies, while others attempt to offset the heavy cost of AI-investments with workforce reductions.

And we also can't ignore the [environmental impact of AI's consumption](https://news.mit.edu/2025/explained-generative-ai-environmental-impact-0117) which can require "a staggering amount of electricity" that increases pollution while requiring enough water (to cool hardware) so as to "strain municipal water supplies and disrupt local ecosystems."
### The Morality of Misuse

The last moral issue with AI is one of potential abuse and misuse. It's something  the [latest Turing Award winners (among others) have warned against](https://www.theverge.com/news/624485/turing-award-andrew-barto-richard-sutton-ai-dangers):

> “Releasing software to millions of people without safeguards is not good engineering practice,” Barto told _The Financial Times_. “Engineering practice has evolved to try to mitigate the negative consequences of technology, and I don’t see that being practiced by the companies that are developing.”

It's one thing to over-rely on AI in your software project causing potential downtime or maintenance nightmares. It's another to rely on it in [mistake strewn legal submissions](https://www.reuters.com/technology/artificial-intelligence/ai-hallucinations-court-papers-spell-trouble-lawyers-2025-02-18/). It's an entirely different and more dangerous thing when AI leads to [amateurish mistakes in policy decisions that cause a global market meltdown](https://x.com/krishnanrohit/status/1907587352157106292) or to [spy on the federal workforce](https://www.reuters.com/technology/artificial-intelligence/musks-doge-using-ai-snoop-us-federal-workers-sources-say-2025-04-08/).

Safeguards aren't necessary because AI might become self-aware and super-intelligent. They are necessary because we know generative AI is deeply flawed in a way that only expert human intervention can mitigate. It's necessary because humans can and will misuse it for both potentially innocent or definitely nefarious purposes. There are no such safeguards in the current generation of generative AI tools in part because the funding for these companies relies on the grandiose promises of a utopian AI future, one that cannot admit the limits of the technology or the flawed (if still sometimes useful) nature of the what it produces.
## Summing Up

Eesh. I know that was a lot of words. If you made it this far, I am both deeply grateful and somewhat concerned for your mental health. 😂 To boil down my current thinking around generative, it's this:

* Generative AI is useful for automating or assisting with mundane tasks in code and in other areas. It can help an experienced developer write code faster or a writer generate the outline of a project, for instance.
* Generative AI is not useful for large scale production-ready projects (outside of perhaps some of the mundane and repetitive tasks above) because it is too prone to mistakes. It should also not be used (or used exceedingly sparingly) in projects with strict security requirements – both of the data within the project development itself (ex. proprietary information) or of the data that the software might inadvertently expose (ex. PII).
* Generative AI does not live up to the grandiose promises that supports the industries valuations or the promises of the tech executives who champion it.
* The moral costs of generative AI currently significantly outweigh the benefit. It's training, consumption and potential for misuse are all serious issues that we have yet to resolve.

All that being said, generative AI isn't going away. It's *far* more useful and potentially beneficial than crypto/blockchain, and we can't even get rid of that. So expecting some kind of grassroots campaign to deter AI is unrealistic. Instead we, both as individuals and as an industry, need to find a way to utilize it in those areas where it can have a positive impact, understand its limits to avoid misuse and mitigate as many of its negative impacts (both professionally in our workplace and a politically in our society) as we can. 