files = ['Client-server architecture', 'Statelessness', 'Cacheability', 'Layered system', 'Resource identification in requests', 'Resource manipulation through representations', 'Self-descriptive messages', 'HATEOAS Hypermedia as the engine of application state']

fileNames = []

for i in files:
    fileNames.append(i.replace(' ', '-').lower())


for index, file in enumerate(fileNames):
    with open("{}.md".format(file), "w") as f:
        f.write('# ' + files[index])
