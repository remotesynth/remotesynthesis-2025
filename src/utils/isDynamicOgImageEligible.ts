import { SITE } from "@/config";

/** Whether a post should get a generated per-post OG image. */
export function isDynamicOgImageEligible(pubDatetime: Date): boolean {
  if (!SITE.dynamicOgImage) return false;

  const cutoff = new Date();
  cutoff.setFullYear(cutoff.getFullYear() - SITE.dynamicOgImageYears);
  return pubDatetime >= cutoff;
}
