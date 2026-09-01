ignore = list()
titles = list()

reading_titles = False

while True:
    try:
        line = input()
    except EOFError:
        break

    if line == "::":
        reading_titles = True
        continue

    if reading_titles:
        titles.append(line)
    else:
        ignore.append(line.lower())

result = list()

for t in titles:
    words = t.split()
    for i in range(len(words)):
        if words[i].lower() in ignore:
            continue

        keyword = words[i].lower()

        new_words = list()

        for w in words:
            new_words.append(w.lower())

        new_words[i] = keyword.upper()
        new_titles = " ".join(new_words)
        result.append((keyword,new_titles))

result.sort(key=lambda x: x[0])

for keyword, title in result:
    print(title)