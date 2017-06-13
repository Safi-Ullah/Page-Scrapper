from search_engine import SearchEngine


if __name__ == "__main__":
    website = "http://python-guide-pt-br.re" \
              "adthedocs.io/en/latest/dev/virtualenvs/"
    oogle = SearchEngine(website)

    oogle.search("why")
    oogle.search("Python")
