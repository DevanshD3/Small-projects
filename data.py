import json

# Opening JSON file
f = open(r'c:\users\devan\sap1.json')

# returns JSON object as
# a dictionary
data = json.load(f)


# print(data['scopes'])
for j in range(len(data['scopes'])):
    for i in data['scopes'][j]:
        if i == 'Text' or i == 'Output':
            for l in data['scopes'][j][i]:
                print(l['label'])
        print(i)


# print(data['scopes'][0]['Text']['label'])
# Closing file
f.close()
