import urllib2
from html_parser import MyHTMLParser


class SearchEngine:

    def __init__(self, website):
        openwebsite = urllib2.urlopen(website)
        html = openwebsite.read()
        self.html_parser = MyHTMLParser()
        self.__parse_html(html)

    def __parse_html(self, html):
        # Clearing the contents of the file
        with open('links.txt', 'w'): pass
        # Feeding the Parser
        self.html_parser.feed(html)

    def search(self, query):
        if query in self.html_parser.invert_index:
            for paragraph in self.html_parser.invert_index[query]:
                # print paragraphs
                print ("-" * 80)
                print (paragraph)
                print ("\nPostions in the paragraph :")
                word_pos = self.html_parser.invert_index[query][paragraph]
                print (word_pos)
                # print ("-" * 80)
        else:
            print ("\"" + query + "\" not found")
