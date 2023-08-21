# hamllab.github.io

Staging area for HaML Lab website.

## Maintenance

To update the publication list, edit `papers.json` to add entries. Entries must be compatible with CSL. Special fields in each paper entry can be used to support specific features:

-   icon: Path to a PNG file that illustrates some key idea from the paper. Should only include black and transparency, so the icon will appear silhouetted against the background image, `images/logo_background.png`. The image must be 600x600. Resizing can be quickly done using ImageMagick. For example, `convert original_image.png -resize 600x600 resized_image.png`.
-   DOI: Should just include the DOI by itself, not the full URL. Adds a link to the paper entry.
-   link: Indicates a non-DOI persistent URL.
-   PMID: PubMed identifier, used to generate a link to the PubMed version of the article.
-   code: URL of code used in the paper.
-   data: URL of data used in the paper.
-   post: URL of a social media post about the paper.
-   preprint: URL of a preprint of the paper (for Submitted, In revision, and In press articles only).

Articles that have not yet been published can be included by setting the status property to "Submitted", "In revision", or "In press". These articles should only be included if there is a preprint. Indicate a URL to the preprint using the "preprint" property.
