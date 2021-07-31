import csv


entry = """\
<a href="{link}" target="_blank" title="{title}">
    <img
        src="https://img.shields.io/badge/{name}-{color}?style=for-the-badge&logo={logo}&logoColor=white"
        alt="{title}"
    />
</a>
"""

with open("badges.csv") as f, open("README.md", 'a') as g:
    for row in csv.reader(f):
        print(
            entry.format_map(
                {
                    "title": row[0],
                    "name": row[1],
                    "color": row[2],
                    "logo": row[3],
                    "link": row[4],
                }
            ),
            file=g,
        )
