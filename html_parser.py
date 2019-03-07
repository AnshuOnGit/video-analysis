from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def error(self, message):
        pass

    def __init__(self):
        HTMLParser.__init__(self)
        self.extracting = False
        self.data = ""
        self.data_dic = {}

    def handle_starttag(self, tag, attrs):
        if tag == "td":
            self.extracting = True
        if self.extracting and tag == "a":
            # print(attrs[5][1])
            self.data = attrs[5][1]

    def handle_endtag(self, tag):
        if tag == "td":
            self.extracting = False

    def handle_data(self, data):
        if self.extracting and len(data.strip(" \n\t")) != 0:
            key = data.strip(" \n\t")
            # print(data.strip(" \n\t"))
            self.data_dic[key] = self.data

    def get_data_set(self):
        return self.data_dic


parser = MyHTMLParser()

with open("test.html", "r") as file:
    parser.feed(file.read())

print(parser.get_data_set())

print(type({'hello': "hiu"}))
