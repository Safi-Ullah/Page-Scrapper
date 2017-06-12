import urllib2
# from html_parser import MyHTMLParser
from html_parser import *


def search(search_query):
        for word in invert_index:
            if  search_query.lower() in word.lower():
                print ("'" + word + "' found in paragraphs :")
                for paragraph in sorted(invert_index[word]):
                    print ("-" * 80)
                    print ("\t" + str(paragraph))
                    print ("\nPostions in the paragraph")
                    for word_pos in sorted(invert_index[word][paragraph]):
                        print ("\t\t" + str(word_pos))
                    # print_paragraph(paragraph_no)
                    print ("-" * 80)

if __name__ == "__main__":
    website = "http://python-guide-pt-br.re" \
              "adthedocs.io/en/latest/dev/virtualenvs/"
    openwebsite = urllib2.urlopen(website)
    html = openwebsite.read()

    # Clearing the contents of the file
    with open('links.txt', 'w'): pass

    parser = MyHTMLParser()
    parser.feed(html)

    search("python")
