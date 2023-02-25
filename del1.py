#!/usr/bin/python3
"""TDDE44, lab6, Del1."""


class Text(object):
    """Hela texen ska undersökas.

    value är imorterade text
    """

    def __init__(self, value):
        """Definera instansvariabler."""
        self.text = value
        self.text_splitter = value.split("\n")
        self.create_list_sentence()

    def create_list_sentence(self):
        """En lista med alla meninagar i filen lorem.txt skapas."""
        self.list_sentence = []
        for sentence in self.text_splitter:
            if sentence != "":
                self.list_sentence.append(Sentence(sentence))

    def count_nr_sentences(self):
        """Få antal meningar i texten."""
        return (len(self.list_sentence))

    def __str__(self):
        """Utskrivning av resultatet."""
        word = 0
        chars = 0
        sentence = self.count_nr_sentences()
        for index in self.list_sentence:
            word += index.count_nr_word()
            chars += index.count_nr_chars()
        TXT = "Texten innehåller {} meningar.\nTexten innehåller {} " \
            "ord/skiljetecken.\nTexten innehåller {} tecken."
        return TXT.format(sentence, word, chars)


class Sentence(object):
    """Undersökning av meninagr.

    value är en mening
    """

    def __init__(self, value):
        """Definera Instanser."""
        self.word_list = []
        words = value.split(" ")
        for word in words:
            # skciaks vidare till Token
            #  klassen för vidatre undersökning av antal word/skilkjetecken
            self.word_list.append(Token(word))

    def count_nr_word(self):
        """Räknar antal word i en mening."""
        return len(self.word_list)

    def count_nr_chars(self):
        """Räknar atnal chars i en mening."""
        chars = 0
        for index in self.word_list:
            chars += index.count_num_chars()  # index är en ett word vilket
            # skickas till
            # nr_tecken() i class token och
            # undersöker hur många chars det innehåller.
        return chars


class Token(object):
    """Summary.

    value är antingen ett word eller en skiljetcken
    """

    def __init__(self, value):
        """Definera insatansvariabler."""
        self.value = value

    def count_num_chars(self):  # get_num_chars
        """Räknar antal chars i ett word."""
        return (len(self.value))


def Main():
    """Importerar filen och kör det."""
    if __name__ == "__main__":
        file1 = open(
            "/courses/TDDE44/kursmaterial/laboration6/del1/lorem.txt", "r")
        file = file1.read()
        file1.close()
        text = Text(file)
        print(text)


Main()
