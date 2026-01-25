import type { Props } from "astro";
import IconMail from "@/assets/icons/IconMail.svg";
import IconGitHub from "@/assets/icons/IconGitHub.svg";
import IconBluesky from "@/assets/icons/IconBluesky.svg";
import IconLinkedin from "@/assets/icons/IconLinkedin.svg";
import IconMastodon from "@/assets/icons/IconMastodon.svg";
import IconTelegram from "@/assets/icons/IconTelegram.svg";
import { SITE } from "@/config";

interface Social {
  name: string;
  href: string;
  linkTitle: string;
  icon: (_props: Props) => Element;
}

export const SOCIALS: Social[] = [
  {
    name: "GitHub",
    href: "https://github.com/remotesynth/",
    linkTitle: `${SITE.title} on GitHub`,
    icon: IconGitHub,
  },
  {
    name: "BlueSky",
    href: "https://bsky.app/profile/remotesynthesis.com",
    linkTitle: `${SITE.title} on BlueSky`,
    icon: IconBluesky,
  },
  {
    name: "LinkedIn",
    href: "https://www.linkedin.com/in/brianrinaldi/",
    linkTitle: `${SITE.title} on LinkedIn`,
    icon: IconLinkedin,
  },
  {
    name: "Mastodon",
    href: "https://mastodon.xyz/@remotesynth",
    linkTitle: `${SITE.title} on Mastodon`,
    icon: IconMastodon,
  },
] as const;

export const SHARE_LINKS: Social[] = [
  {
    name: "Mastodon",
    href: "https://mastodon.xyz/share?text=",
    linkTitle: `Share this post on Mastodon`,
    icon: IconMastodon,
  },
  {
    name: "BlueSky",
    href: "https://bsky.app/intent/compose?text=",
    linkTitle: `Share this post on BlueSky`,
    icon: IconBluesky,
  },
  {
    name: "Telegram",
    href: "https://t.me/share/url?url=",
    linkTitle: `Share this post via Telegram`,
    icon: IconTelegram,
  },
  {
    name: "Mail",
    href: "mailto:?subject=See%20this%20post&body=",
    linkTitle: `Share this post via email`,
    icon: IconMail,
  },
] as const;
