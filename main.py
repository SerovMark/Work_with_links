def open_file(file_name):
    links = []
    with open(file_name, "r", encoding="utf-8") as f:
        while True:
            line = f.readline()
            line = line.replace("!", "ы")
            if not line:
                break
            links.append(line.strip())
    return links


def compare(file_name):
    with open(file_name, "w", encoding="utf-8") as f:
        for word1 in links1:
            for word2 in links2:
                if word1 == word2:
                    f.write(word2 + "\n")


def no_compare(file_name):
    with open(file_name, "w", encoding="utf-8") as f:
        for word1 in links1:
            for word2 in links2:
                if word1 == word2:
                    break
            else:
                f.write(word1 + "\n")
        for word1 in links2:
            for word2 in links1:
                if word1 == word2:
                    break
            else:
                f.write(word1 + "\n")


links1 = open_file("file_1.txt")
links2 = open_file("file_2.txt")
compare("Совпадающие ссылки.txt")
no_compare("Несовпадающие ссылки.txt")
print(links1)
print(links2)
