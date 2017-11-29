

class NBATweet:

    def __init__(self, text, date_created):
        self.__text = text
        self.__date_created = date_created

    def get_text(self):
        return self.__text

    def set_text(self, text):
        self.__text = text

    def get_date_created(self):
        return self.__date_created

    def set_date_created(self, date_created):
        self.__date_created = date_created

    def print_text(self):
        print(self.__text)

    def print_date_created(self):
        print(self.__date_created)

    def print_text_date(self):
        print("(%s) %s" % (self.__date_created, self.__text))
