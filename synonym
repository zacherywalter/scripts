#!/usr/bin/env python3
import sys, re, urllib.request, html

if len(sys.argv) < 2:
    print("Usage: syn <word>")
    sys.exit(1)

word = sys.argv[1].lower().replace(" ", "_")
url  = f"https://www.wordhippo.com/what-is/another-word-for/{word}.html"

request  = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
raw_html = urllib.request.urlopen(request).read().decode("utf-8")

def strip_tags(text):
    text = re.sub(r'<[^>]+>', '', text)
    return html.unescape(text).strip()

# Split the page into sections at each wordtype div
sections = re.split(r'<div class="wordtype"[^>]*>', raw_html)[1:]

for section in sections:
    part_of_speech = strip_tags(re.search(r'^([^<]+)', section).group(1))

    description_match = re.search(r'<div class="tabdesc">(.*?)</div>', section)
    description = strip_tags(description_match.group(1)) if description_match else ""

    example_match = re.search(r'<div class="tabexample">(.*?)</div>', section)
    example = strip_tags(example_match.group(1)) if example_match else ""

    # Only grab words that appear before the "show more" button
    visible_words_html = section.split('morewordsblock')[0]
    words = re.findall(r'<a href="[^"]+\.html">([^<]+)</a>', visible_words_html)

    print(f"\n{part_of_speech} — {description}")
    if example:
        print(f'{example}')
    for word in words[:12]:
        print(f"    {word}")
