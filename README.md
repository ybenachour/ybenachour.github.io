# Yassine Benachour — academic website

A complete static website for GitHub Pages. No database, login, server or JavaScript build step is needed.

## Publish

1. Create the public repository `ybenachour.github.io` at https://github.com/new?name=ybenachour.github.io&visibility=public
2. Upload the **contents** of this folder to the root of the `main` branch. `index.html` must be at the root, not inside another folder.
3. Open repository **Settings → Pages**.
4. Under **Build and deployment**, select **Deploy from a branch**, branch **main**, folder **/ (root)**, then Save.
5. Wait for GitHub's deployment to finish. The expected address is https://ybenachour.github.io/ . It is only live after successful deployment.

## Included

- Responsive academic home page, research programmes, teaching, textbook, career timeline and contact.
- Searchable publications: 16 published papers and 12 accepted conference papers.
- Public academic CV PDF, with personal identifiers and reference contacts omitted.
- DOI links, Google Scholar, ORCID, GitHub and downloadable source bibliography.
- Accessible navigation, keyboard focus, reduced-motion support, search labels and no-JavaScript publication access.

## Edit

To edit the page directly, change `index.html`, `styles.css` and `script.js`.
For regeneration, edit `template.html` and `content.json`, then run `python3 build.py` (requires ReportLab). This rebuilds `index.html` and `Yassine_Benachour_CV.pdf`; direct changes to either output will be overwritten. The source bibliography is maintained separately and is a July 2026 snapshot, not a complete export of the later conference tracker.

The website works without external JavaScript. Google Fonts are optional; local font fallbacks are defined. No analytics, cookies or form backend is included. Email uses a normal `mailto:` link.

## Content sources and status

Primary academic source: September 2026 academic CV, read from the user's Dropbox. Publication metadata: July 2026 `myResearch.bib` plus the CV. Accepted conference papers: September 2026 EDAS tracker. Website prepared October 2026.

The tracker labels one bearing-fault paper accepted while its detailed note says an acceptance notification was not found. That record is omitted from the public list. Accepted records are not represented as published proceedings. The skin-health work describes predictive associations, not demonstrated causal effects. No citation metrics are presented as current.

The public CV is a reformatted edition based on the academic source with the updated curated publication list. It is not the original CV file. Referee contact details, telephone numbers, nationality and visa information are omitted. No private Dropbox links or research manuscripts are distributed.

## Verification

Static checks validate local asset links, section anchors, publication counts, DOI syntax and JavaScript syntax. The generated CV is rendered and visually inspected. Browser layout QA has not been run in this environment; check the page on desktop and mobile after deployment.
