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
from jinja2 import Environment, FileSystemLoader, select_autoescape


def gen_publications(json_file, csl_file, icon_background, icon_default):
    """Generate a publications list with icons and links."""
    # get citation style and bibliography
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
    
    # set up templating engine
    env = Environment(
        loader=FileSystemLoader("templates"),
        autoescape=select_autoescape(),
    )
    template = env.get_template("bib_entry.html")
    
    # generate bibliography
    year = None
    for key, val in bib_sorted.items():
        if "issued" in val and "year" in val["issued"]:
            new_year = val["issued"]["year"]
            if year != new_year:
                year = new_year
                print(f'# {year}')
        
        # generate one-item bibliography for this entry
        citation = Citation([CitationItem(key)])
        bibliography = CitationStylesBibliography(bib_style, bib_source, formatter.html)
        bibliography.register(citation)
        for item in bibliography.bibliography():
            reference = str(item)
          
            if "icon" in val:
                # generate custom icon
                icon_path = Path(str(val["icon"]))
                comb_name = str(icon_path.stem) + "_combined" + icon_path.suffix
                comb_path = icon_path.parent / comb_name
                img1 = Image.open(icon_background)
                img2 = Image.open(icon_path)
                box = (np.array(img1.size) - np.array(img2.size)) / 2
                img1.paste(img2, tuple(box.astype(int)), mask=img2)
                img1.save(comb_path)
                icon = str(comb_path)
            else:
                # use generic icon
                icon = icon_default
            
            # prepare links
            links = {}
            if "DOI" in val:
                doi = val["DOI"]
                links["DOI"] = f"http://doi.org/{doi}"
            if "link" in val:
                links["Link"] = val["link"]
            if "PMID" in val:
                pmid = val["PMID"]
                links["PubMed"] = f"https://pubmed.ncbi.nlm.nih.gov/{pmid}"
            if "code" in val:
                links["Code"] = val["code"]
            if "data" in val:
                links["Data"] = val["data"]
            if "post" in val:
                links["Overview"] = val["post"]
            
            # generate entry from template
            entry = {"icon": icon, "reference": reference, "links": links}
            print(template.render(entry=entry))
