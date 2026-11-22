"""Check that internal links resolve to files in the generated Pages site."""

import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import quote, unquote, urljoin, urlsplit


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            self.hrefs.extend(value for name, value in attrs if name == "href" and value)


def check_links(site, site_url):
    site = site.resolve()
    base_url = site_url.rstrip("/") + "/"
    base = urlsplit(base_url)
    base_path = unquote(base.path)
    if not (site / "index.html").is_file():
        return [f"{site}: missing generated index.html"]

    failures = []
    for page in sorted(site.rglob("*.html")):
        relative_path = page.relative_to(site).as_posix()
        public_path = relative_path
        if page.name == "index.html":
            public_path = public_path.removesuffix("index.html")
        page_url = urljoin(base_url, quote(public_path))
        parser = Links()
        parser.feed(page.read_text(encoding="utf-8"))
        for href in dict.fromkeys(parser.hrefs):
            target = urlsplit(urljoin(page_url, href))
            if (target.scheme, target.netloc) != (base.scheme, base.netloc):
                continue

            path = unquote(target.path)
            if path == base_path.rstrip("/"):
                path = base_path
            if path.startswith(base_path):
                candidate = (site / path.removeprefix(base_path)).resolve()
                if candidate.is_relative_to(site) and (
                    (not path.endswith("/") and candidate.is_file()) or (candidate / "index.html").is_file()
                ):
                    continue

            failures.append(f"{relative_path}: {href} → {path} does not exist")
    return failures


if __name__ == "__main__":
    failures = check_links(Path(sys.argv[1]), sys.argv[2])
    if failures:
        print("\n".join(failures), file=sys.stderr)
    sys.exit(bool(failures))
