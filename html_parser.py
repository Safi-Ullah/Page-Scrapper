import re
import urllib2
from HTMLParser import HTMLParser

invert_index = {}

class MyHTMLParser(HTMLParser):
    read_paragraph = False
    paragraph_no = 0
    print_paragraph = False

    def __retrieve_href_links(self, attrs):
        for attr, value in attrs:
            if attr == 'href':
                links = re.findall(r'http[s]?://[a-zA-Z0-9_\-\./]*', value)
                if len(links) > 0:
                    with open("links.txt", 'a') as file:
                        for link in links:
                            file.write(link + '\n')

    def __retrieve_image_links(self, attrs):
        for attr, value in attrs:
            if attr == 'src':
                links = re.findall(r'http[s]?://[a-zA-Z0-9_\-\./]*', value)
                if len(links) > 0:
                    with open("links.txt", 'a') as file:
                        for link in links:
                            file.write(link + '\n')

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            self.__retrieve_href_links(attrs)
        if tag == 'img':
            self.__retrieve_image_links(attrs)
        if tag == 'p':
            self.read_paragraph = True
            self.paragraph_no += 1

    def handle_endtag(self, tag):
        if tag == 'p' and self.read_paragraph == True:
            self.read_paragraph = False

    def handle_data(self, data):
        if self.read_paragraph == True:
            word_pos = 0
            for word in data.split():
                # if (word == "Python"):
                #     import pdb; pdb.set_trace()
                word_pos += 1
                if word not in invert_index:
                    invert_index[word] = {}
                if self.paragraph_no not in invert_index[word]:
                    # invert_index[word][self.paragraph_no] = []
                    invert_index[word][data] = []

                invert_index[word][data].append(word_pos)
