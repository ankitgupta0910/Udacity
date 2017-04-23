import urllib


def read_text():
    quotes = open("/Users/ankitgupta/PycharmProjects/Udacity/movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    profanity_check(contents_of_file)


def profanity_check(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text_to_check)
    output = connection.read()
    print(output)
    connection.close()

read_text()
