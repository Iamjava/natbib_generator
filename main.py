

def start():
    txt = input("Möchtest du ein article (a) oder buch (b) ")
    if txt == "a":
        paper()
    else:
        book()


def maybe_safe(s, t):
    if s != 'n':
        with open("literature.bib", "a") as myfile:
            myfile.write(t + "\n")
        print("---------SAVED--------------")

def paper():
    print("paper/article")
    tag = input("Der tag zum zitieren im LATEX Dokument:")
    aut = input("Autor:")
    jur = input("Journal:")
    tit = input("Title:")
    dat = input("Year:")
    volume = input("Volume:")
    doi = input("<Optional>DOI:")
    t = f'@Article{{ {tag},author={{ {aut} }},title={{ {tit} }},journal={{ {jur} }}, doi = {{ {doi}  }},year={{ {dat} }},volume={{ {volume} }}}}'
    print(t)
    s = input("SAVE (y/n):")[0]
    maybe_safe(s, t)
    start()

def book():
    print("book")
    tag = input("Der tag zum zitieren im LATEX Dokument:")
    aut = input("Autor:")
    tit = input("Title:")
    dat = input("Year:")
    pub = input("Publisher:")
    isbn = input("<Optional>ISBN:")
    page = input("<Optional>Page:")
    t = f'@book{{ {tag},title={{ {tit} }},author={{ {aut} }},page = {{ {page} }}, isbn = {{ {isbn}  }},year={{ {dat} }},publisher={{ {pub} }}}}'
    s = input("SAVE (y/n):")[0]
    print(s)
    maybe_safe(s, t)
    start()


if __name__ == '__main__':
    start()


