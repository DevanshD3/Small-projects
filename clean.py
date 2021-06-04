from io import StringIO
from html.parser import HTMLParser
import csv
import re
import json

# Opening JSON file
f = open(r'C:\Users\devan\OneDrive\Desktop\cv data.json', encoding="utf8")

# returns JSON object as
# a dictionary
data = json.load(f)


class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs = True
        self.text = StringIO()

    def handle_data(self, d):
        self.text.write(d)

    def get_data(self):
        return self.text.getvalue()


def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()


f = open(r'C:\Users\devan\OneDrive\Desktop\cv data - Copy.json','w', encoding="utf8")
li = []
for j in range(len(data)):
    
    if data[j]["description"] == "" or data[j]["description"] == None:
        li.append(data[j])
    else:
        data[j]["description"] = strip_tags(data[j]["description"])
        # data[j]["description"] = data[j]["description"].encode('ascii', errors='ignore')
        li.append(data[j])

json.dump(li, f, ensure_ascii=True, indent=2)
