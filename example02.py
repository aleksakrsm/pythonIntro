# count number of apperances of each word in txt

txt = "hej   OVO ovo Ovo   Ova   ohdhd hakf hakf hakf  ahhd ovo aaa ova  aaa ovo "
mapa = {}
for word in txt.split(" "):
    word = word.strip()

    if word == "":
        continue

    word = word.lower()

    if word in mapa:
        mapa[word] += 1
    else:
        mapa[word] = 1

# sorted_keys_in_list = sorted(mapa.keys(), key=lambda x: mapa.get(x), reverse=True)

sorted_list_of_items = sorted(mapa.items(), key=lambda x: x[1], reverse=True)
sorted_map = dict(sorted_list_of_items)

print(mapa)
print(sorted_map)