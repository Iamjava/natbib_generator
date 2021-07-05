
def print_hi():
    txt = input("Möchtest du ein article (a) oder buch (b)")
    if txt == "a":
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
        if s!='n':
            with open("literatur.txt", "a") as myfile:
                myfile.write(t+"\n")
            print("---------SAVED--------------")
        print_hi()
    else:
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
        if s != 'n':
            with open("literatur.txt", "a") as myfile:
                myfile.write(t+"\n")
            print("---------SAVED--------------")
        print_hi()

if __name__ == '__main__':
    print_hi()


