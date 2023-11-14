import os



def parser_link(link: str):
    tokens = link.split("\\")
    res = []
    for token in tokens:
        if token[0:2] == "{{":
            token = os.getenv(token[2:-2])
        res.append(token)
    return "\\".join(res)


if __name__ == '__main__':
    link = r"{{appdata}}\div\ini.ini"
    print("даю ", link)
    print("получаю ", parser_link(link))
