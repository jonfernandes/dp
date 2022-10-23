# https://github.com/facebookresearch/flores/tree/main/flores200#languages-in-flores-200

import re

with open(html_file, 'rt') as file:
    content = file.read()

p = re.findall(r'<p>(.*?)</p>', content)
blockquote = re.findall(r'<blockquote>(.*)</blockquote>', content)

update_html = []

for index, block in enumerate(p):
    if index == 1:
        update_html.append(f'<blockquote>{blockquote[0]}</blockquote>')
    else:
        update_html.append(f'<p>{block}</p>')