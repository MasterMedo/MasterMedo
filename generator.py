"""Generates the README.md file from the badges.csv file.
The csv file must contain the following columns:
    - title         text that gets shown as a tooltip (plain text e.g. docker)
    - name          text that is show on the badge (plain text e.g. sqlite)
    - color         color of the badge (hex color e.g. F7AC00)
    - logo          name of the logo icon (plain text e.g. html5)
    - link          href for the action tag (valid url e.g. https://github.com)
    - logo_color    color of the logo (plain text e.g. black)

Find logo icons here:
https://github.com/simple-icons/simple-icons/blob/develop/slugs.md
"""
import csv


header = """\
### [Hi there 👋](https://mislav.dev)

<details>
  <summary align="center" style="color:gray;font-weight:900;align-items:center;display:flex">unlock hidden insights</summary>
  <p align="center">
    <img src="https://github-profile-trophy.vercel.app/?username=MasterMedo&row=1" alt="github stats">
  </p>
</details>
"""

action_tag = """\
<a href="{link}" target="_blank" title="{title}">
    {img}
</a>\
"""

img_tag = """\
<img src="https://img.shields.io/badge/{name}-{color}?style=for-the-badge&logo={logo}&logoColor={logo_color}" alt="{title}"/>\
"""

with open("badges.csv", "r") as f, open("README.md", "w") as g:
    print(header, file=g)
    print('<p align="center">', file=g)
    for row in csv.DictReader(f):
        img = img_tag.format_map(row)
        if row["link"]:
            img = action_tag.format_map({"img": img} | row)

        print(img, file=g, end="\n\n")
    print("</p>", file=g)
