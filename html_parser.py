import re
import urllib2
from HTMLParser import HTMLParser


class MyHTMLParser(HTMLParser):
    read_paragraph = False
    paragraph_no = 0
    print_paragraph = False
    invert_index = {}

    def __print_links(self, links):
        links = re.findall(r'http[s]?://[a-zA-Z0-9_\-\./]*', links)
        if links:
            with open("links.txt", 'a') as file:
                for link in links:
                    file.write(link + '\n')

    def __retrieve_href_links(self, attrs):
        links = dict(attrs)['href']
        self.__print_links(links)

    def __retrieve_image_links(self, attrs):
        links = dict(attrs)['src']
        self.__print_links(links)

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            self.__retrieve_href_links(attrs)
        if tag == 'img':
            self.__retrieve_image_links(attrs)
        if tag == 'p':
            self.read_paragraph = True
            self.paragraph_no += 1

    def handle_endtag(self, tag):
        if tag == 'p' and self.read_paragraph:
            self.read_paragraph = False

    def handle_data(self, data):
        if self.read_paragraph:
            word_pos = 0
            for word in data.split():
                # if (word == "Python"):
                #     import pdb; pdb.set_trace()
                word_pos += 1
                if word not in self.invert_index:
                    self.invert_index[word] = {}
                if data not in self.invert_index[word]:
                    # self.invert_index[word][self.paragraph_no] = []
                    self.invert_index[word][data] = []

                self.invert_index[word][data].append(word_pos)
