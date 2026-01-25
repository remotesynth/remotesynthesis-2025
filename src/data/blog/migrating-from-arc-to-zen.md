---
title:  "Tips on Migrating from Arc to Zen"
tags:
    - general
description: I'm switching browsers due to The Browser Company's recently announced change in direction. Here's some migration tips I encountered switching from Arc to Zen.
pubDatetime: 2025-06-22T10:23:31.210Z
---

I was a fairly early adopter of the Arc browser shortly after it was released in 2022. I was initially drawn in by some of the extremely simple conveniences like the simplified tab maintenance and easy URL copy shortcuts. Many of these were minor improvements but, considering how much time I spend in the browser, they had real quality-of-life type impacts on my day-to-day.

Things like the left-hand tab management took a little adjustment, but now seem like obvious improvements to me. As time went on, Arc added other conveniences that I relied on like split view (which was often particularly helpful when building web apps), little arc (which opened a quick preview rather than a full tab for many activities), live calendars, GitHub live folders and more.

However, it wasn't until I understood the relationship between spaces and profiles that Arc became indispensable to me. This is why I was extremely dismayed at the [recent announcement](https://browsercompany.substack.com/p/letter-to-arc-members-2025) from Arc's CEO that development of Arc is officially over in favor of some (as yet unreleased) AI browsing tool called Dia. While Arc isn't going away immediately, it seemed like an opportune time to explore alternatives (especially since I am not on board for the concept of an AI browsing alternative – you'd think Google's awful foray into AI summaries would have disabused people of this idea).

## The Beauty of Spaces

Like many of you, I maintain multiple email addresses and calendars. I have my personal email address, my work email address and my "[side business](https://cfe.dev)" email address. These aren't just email addresses, but represent parts of my life that, while they at times overlap, are usually independent of each other.

Spaces in Arc allowed me to organize my browsing experience around the way I live.

During the day when I am working, I tend to function primarily in a work space that includes my work email and calendar along with a set of "always on" tabs that are applications I use frequently in a work context, as well as tabs that are related to whatever I might be working on at the moment.

During the evening and weekends, I will primarily use my personal space, which has my personal email and calendar as well as "always on" tabs for things like my social media accounts, financial accounts. I will have additional tabs open for whatever I may be working on in my personal life, like things related to my recent move or vacation planning.

Also during the evening or weekends, I will need to work on the side business (for me, the only dedicated time I have for this is usually Sunday). Again, I have an email and calendar related to this and "always on" tabs for managing the YouTube channel, events in Streamyard and social media accounts.

While these spaces represented distinct parts of my life that are often time-bound as described above, the lines are frequently blurry. At times we all need to check something in our personal space during work hours or our work space off-work hours, for instance. I also had a dedicated demo space for presentations which was usually clean of any tabs, which I'd open as needed for a presentation (which meant that none of my work, side-work or personal stuff accidentally bled into a presentation).

Spaces in Arc can be assigned to a particular profile. There was no blurring of personal email and calendar profiles in my work space and vice versa, for example. I could easily swap between them as needed (usually with the keyboard shortcut of command+option+left/right). 

The combination of complete separation of my profiles combined with quick and easy access as needed is incredibly powerful. Sadly, though, I was apparently in a small minority as Arc claims that only "5.52% of DAUs (daily active users) use more than one Space regularly." This is part of the reason they give for killing the browser effort.

## Moving to Zen

Thankfully, [Zen Browser](https://zen-browser.app/), an open source alternative to Arc based on the Gecko rendering engine that powers Firefox (Arc is based on Chromium), also offers spaces that can be tied to profiles. They call them "workspaces" rather than "spaces", but the concept is the same.

In addition, Zen includes many of the other conveniences that I'd become adjusted to from Arc. Things like a the left hand tab management, quick URL copy shortcut, a lightweight preview tab for quick tasks, split view and more all exist, though with (mostly) small differences. It's these differences that can actually make the transition tougher than expected, so let's go through them.
### Favorites vs. Essentials

Both Arc and Zen have the concept of frequently used tabs that exist across workspaces. These tabs sessions generally remain open and are at the top of the left-hand tab management for quick access, regardless of what workspace you are in.

![Essentials in Zen persist across workspaces](/images/posts/arc-to-zen/Favorites-Essentials.png)

A key difference (and one of my biggest early stumbling blocks) is that in Arc these could change per profile and use the accounts associated with that space's profile, while in Zen they do not. This meant that in Arc I could keep things like my email and calendar in the favorites while in Zen I cannot (thus why Newsblur and GitHub are there in the screenshot above). In addition, in Zen the essentials persist across all workspaces, meaning you can't have an essential in your personal workspace that isn't in your work workspace (something Arc does allow).
#### Alternative Solution

What I've done instead is to move things like email and calendar into the pinned tabs section as shown int he screenshot below. The pinned tabs are the items above the horizontal rule break (just below the Buffer tab in my screenshot).

![Pinned tabs for email and calendar in Zen](/images/posts/arc-to-zen/pinned-tabs.png)

These tabs still maintain their open sessions (meaning you don't have to re-log in or renavigate to a sub-page every time), but you do lose features of Arc like the live calendar, which was useful for quick access to an upcoming meeting.

### Extensions

I'll be honest, I don't use a lot of extensions, but you may need to change some of the ones you rely on as Arc and Zen rely on different extension libraries (i.e. Chrome versus Firefox). Nonetheless, the one extension I use most (1Password), I use frequently throughout the day. The good news is that Zen supports Firefox extensions, so 1Password exists, but it works slightly differently. In fact, there's a dedicated page to deal with issues in [supporting 1Password](https://docs.zen-browser.app/guides/1password).

I did not face any significant roadblocks other than minor UX confusions. In Arc, I'd usually enable the plugin via biometric authentication that would be opened automatically when trying to access login information on a page. In Zen, I've so far had to enable this by clicking the small extensions icon in the upper left-hand corner of the browser (looks like a puzzle piece), then clicking 1Password and finally logging in with my password. This flow also seems to repeat far more often (i.e. needing to authenticate 1Password) than I recall it happening in Arc.

To get biometric authentication to work, you need to enable Zen as a trusted browser in 1Password as laid out in the instructions linked above (it is not a default trusted browser) which makes the workflow just like Arc.

### Keyboard Shortcuts

I am also not a heavy user of keyboard shortcuts for everything but there were a few that I relied on heavily in Arc:

* *Command+Option+left/right arrow* for moving between spaces.
* *Command+Shift+C* for copying the current URL.

Zen supports both functionalities, but the default shortcuts are different. Thankfully, Zen offers a wide array of configuration on keyboard shortcuts (far beyond my own needs), so fixing this was super easy. Just open the settings menu, navigate to "Keyboard shortcuts", click into the one you'd like to adjust (ex. Forward Workspace) and then hit the shortcut you'd like to use (you'll need to do this twice to confirm and save it).

That's it. Now my Zen behaves exactly like Arc for the keyboard shortcuts I use regularly without the need to relearn new ones, though I did notice some unusual behaviors of the copy URL shortcut on GitHub (in some cases it literally copied the markdown of the readme rather than the page URL).

### Little Arc vs. Glance

Both Little Arc and Glance achieve the same result for Arc and Zen respectively, which is to open a quick, lightweight tab that overlays your current tab without losing the context of the current tab. This can be very useful when you want to quickly check a link from your current tab (example, read a blog post or quickly review a search result link). The big benefit is that you don't fully switch to the new tab or open a bunch of trivial tabs for things that should be short-lived.

There are just some small differences between how they work across the browsers. Arc will open up a Little Arc window when you click a browser link from another desktop application, Zen does not. Instead Zen opens a Glance when you click a link within a pinned tab (something Arc also did via what they called "previews"). Links from other desktop applications open in a full tab in Zen.

In addition, I got so used to the UX of Little Arc that I initially struggled to find how to expand or close a Glance. These controls are on the left hand side hovering over the parent tab, which, for some reason, made them nearly invisible to my eye.

![Glance in Zen](/images/posts/arc-to-zen/glance.png)

### Stuff You'll Just Have to Live Without (for now)

There are some Arc features that, while useful, weren't game changers to me that I would love to have but can accept living without.

* **Air traffic control** – This allowed you to set rules about which space a tab opened within. For instance, I only use Notion at work so I directed all my Notion tabs to my work space, where I am already logged in.
* **Instant dev tools** – This feature added quick links to dev tools on top of any localhost URL, which was actually very handy but dev tools are just a quick keyboard shortcut away anyway.
* **Live calendar** – This would show a quick link to an upcoming meeting for calendar items when the meeting time was close, which was handy both as a visual reminder and as quick access.
* **GitHub live folders** – This shows open PRs underneath a GitHub pinned tab, giving you quick access to review and approve PRs.
* **Previews** – This would show a quick preview of unread emails, recent Notion pages and upcoming meeting just by hovering over a tab.

These were all great features and hopefully Zen will "borrow" some of these ideas. For now, I am ok working without them.

## It's Still Early But the Transition Has Been Smooth

I've only really just committed to Zen, which I define as switching my default browser. So far, the only stumbling block was the way workspaces behaved versus spaces, and that had a fairly simple workaround. Zen works similarly enough that the transition has been smoother than other times I've switched browsers (which, admittedly, is very infrequent). I do like that Zen is open source, actively releasing new features and, importantly, aren't trying to move into AI browsing features that I do not want – and I am willing to forgo some niceties that Arc had to get that.