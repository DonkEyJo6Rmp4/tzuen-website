# Tzuen Website Agent Notes

## Project Scope

This workspace is for building two related websites:

1. `tzuen.org` - 財團法人佛教慈恩育幼基金 official website.
2. `hongfasi.tzuen.org` - 宏法寺 official website, planned as a subdomain site.

Current priority is the initial `tzuen.org` website. It only needs to be complete enough for Google Workspace for Nonprofits application review, domain credibility, and basic public information. Do not overbuild advanced features unless requested.

## Working Directory

All work for this website project should happen inside:

`Tzuen/Website`

Current source materials:

- Foundation intro: `Tzuen/Website/Tzuen/Tzuen_Intro.md`
- Moodboard: `Tzuen/Website/Tzuen/Tzuen情緒版.png`
- Images and documents: `Tzuen/Website/Tzuen/assets`

Important certificate assets:

- `Tzuen/Website/Tzuen/assets/重要資料_立案證書.jpg`
- `Tzuen/Website/Tzuen/assets/重要資料_法人登記證.jpg`

## Brand Direction

Use the moodboard as the primary visual reference. The site should feel warm, trustworthy, gentle, Buddhist-inspired, child-centered, and nonprofit credible. Avoid generic corporate templates.

Brand colors:

- `#0F2A47` Primary: logo, nav, headings, footer.
- `#7263A8` Secondary: subheadings, feature blocks, card titles, icons.
- `#F2B35B` Accent: key numbers, Buddhist symbols, highlight info.
- `#F27C38` CTA: donation, contact, primary buttons.
- `#FFFDF8` Background: main website background and content areas.
- `#FFE8EE` Soft Accent: children activity, story, warm card backgrounds.
- `#73B17A` Success: success states and completed states only.
- `#8ECFF5` Sky Blue: education, learning, child-related illustrations/icons.

## Required Website Content

Official organization names must always be written in full:

- Chinese: `財團法人佛教慈恩育幼基金`
- English: `Buddhist Tzuen Children’s Welfare Foundation`

The `tzuen.org` initial site needs five pages or five clear sections:

1. Who We Are: short foundation identity, mission, and purpose.
2. What We Do: detailed yearly contributions and activities.
3. Legal Proof: official establishment certificate and legal-person registration certificate.
4. News: for now, show "網站建置中，請耐心等候".
5. Contact: phone, email, Facebook, address, Google Maps embed and direct Maps link.

Required contact data:

- Phone: `+886 07-2365645`
- Email: `tzuen76201061@gmail.com`
- Facebook: `https://www.facebook.com/tzuen.org`
- Address: `800高雄市新興區仁愛一街296號`

Donation content:

- Heading: `成為最溫暖的陽光`
- Postal transfer account: `04771311`
- Account name: `佛教慈恩育幼基金會`
- Donation link: `https://39buy.co/charity/item/44015`
- E-invoice donation code: `728`

Legal registration:

- Establishment number: `高市社福字第81658號`

## Language Requirement

The website must be bilingual:

- Traditional Chinese (`zh-TW`) as the default language.
- English (`en`) selectable by the user.

Do not rely on browser auto-translation. Use explicit bilingual content objects/files so both languages can be reviewed and corrected.

## Deployment Direction

User has already rented `tzuen.org`. Expected workflow:

1. Build website locally.
2. Push source to GitHub.
3. Deploy via GitHub Pages, Cloudflare Pages, Vercel, or similar static hosting.
4. Update DNS records after deployment target is ready.

Do not change DNS or attempt production deployment unless explicitly asked.

## Implementation Preferences

- Keep the first version simple, static, fast, and maintainable.
- Prefer a single modern static frontend project that can host both the main site and future subdomain content.
- Use real local assets from `Tzuen/Website/Tzuen/assets`; do not invent important facts.
- Optimize for nonprofit trust: clear identity, legal proof, contact information, donation transparency.
- Use accessible markup, meaningful alt text, responsive design, and readable typography.
- Preserve image filenames unless there is a strong reason to rename them.

## Important Constraints

- Do not expose private data beyond what the user explicitly provided.
- Do not claim nonprofit approval, Google Workspace approval, government endorsement, or tax status beyond supplied documents.
- If new legal, tax, or official registration wording is needed, ask the user or mark as needing verification.
- If using maps, include both an embedded map view and a direct Google Maps link for mobile app opening.

## Current Status

Initial bilingual static website implemented on 2026-08-02.

- Stack: dependency-free HTML, CSS, and JavaScript.
- Main files: `index.html`, `styles.css`, `app.js`.
- Optimized web assets: `public/images` and `public/documents`; never replace the originals in `Tzuen/assets`.
- Hero slogan: Chinese uses the white horizontal calligraphy image only; English adds `Be the Sunshine That Warms Every Heart.` beneath it.
- All website logos use an optimized WebP derived from `Tzuen/assets/Logo圓型.png`.
- The Hero directly uses `Tzuen/assets/slogan橫式白.svg`; the build copies only this SVG into the deployable `dist/Tzuen/assets` path.
- All seven service cards include approximate dates in both languages.
- Verification: `npm test`, `npm run build`, and Playwright browser checks pass.
- Playwright is isolated in `.venv` with Chromium in `.playwright-browsers`; both are ignored by Git.
- Browser test: `tests/browser_check.py`, covering 1440×1000 desktop and 390×844 mobile layouts, language switching and persistence, mobile navigation, local image loading, horizontal overflow, and runtime errors.
- Remaining: repository selection, deployment platform, and DNS.

Development commands:

- `npm test`: run static content and structure checks.
- `npm run build`: create the deployable site in `dist/`.
