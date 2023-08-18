"""Generate HTML for a publications list."""

import json
from collections import defaultdict
from pathlib import Path
from PIL import Image
import numpy as np
from citeproc import CitationStylesStyle, CitationStylesBibliography
from citeproc import Citation, CitationItem
from citeproc import formatter
from citeproc.source.json import CiteProcJSON


def gen_publications(json_file, csl_file, icon_background, icon_default):
    """Generate a publications list with icons and links."""
    bib_style = CitationStylesStyle(csl_file)
    with open(json_file) as f:
        bib_data = json.load(f)
    bib_source = CiteProcJSON(bib_data)
    
    # reverse chronological sort
    bib_sort_keys = {}
    for key, val in bib_source.items():
        if "issued" not in val:
            bib_sort_keys[key] = (0, 0, 0)
        else:
            dates = defaultdict(lambda: 0, val["issued"])
            bib_sort_keys[key] = (dates["year"], dates["month"], dates["day"])
    bib_sorted = {
        key: bib_source[key] for key, _ in sorted(bib_sort_keys.items(), key=lambda x: x[1], reverse=True)
    }
    
    year = None
    for key, val in bib_sorted.items():
        if "issued" in val and "year" in val["issued"]:
            new_year = val["issued"]["year"]
            if year != new_year:
                year = new_year
                print(f'# {year}')
        
        citation = Citation([CitationItem(key)])
        bibliography = CitationStylesBibliography(bib_style, bib_source, formatter.html)
        bibliography.register(citation)
        for item in bibliography.bibliography():
            if "icon" in val:
                icon_path = Path(str(val["icon"]))
                comb_name = str(icon_path.stem) + "_combined" + icon_path.suffix
                comb_path = icon_path.parent / comb_name
                img1 = Image.open(icon_background)
                img2 = Image.open(icon_path)
                box = (np.array(img1.size) - np.array(img2.size)) / 2
                img1.paste(img2, tuple(box.astype(int)), mask=img2)
                img1.save(comb_path)
                pic_file = str(comb_path)
            else:
                pic_file = icon_default
            
            print(f'<div class="container"><img class="icon" src="{pic_file}"></img><p class="bib-entry">{str(item)}', end='')
            
            if "DOI" in val:
                doi = val["DOI"]
                print(f' <a href="http://doi.org/{doi}">DOI</a>', end='')
            if "link" in val:
                link = val["link"]
                print(f' <a href="{link}">Link</a>', end='')
            if "PMID" in val:
                pmid = val["PMID"]
                print(f' <a href="https://pubmed.ncbi.nlm.nih.gov/{pmid}">PubMed</a>', end='')
            if "code" in val:
                link = val["code"]
                print(f' <a href="{link}">Code</a>', end='')
            if "data" in val:
                link = val["data"]
                print(f' <a href="{link}">Data</a>', end='')
            if "post" in val:
                link = val["post"]
                print(f' <a href="{link}">Post</a>', end='')
            
            print('</p></div>\n\n')
