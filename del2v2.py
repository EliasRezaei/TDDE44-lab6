#!/usr/bin/python3
"""TDDE44 lab6."""

from todolist import *


class TodoApp(object):
    """Klass TodoApp."""

    def __init__(self):
        """Definera instansvaribler till klassen TodoApp."""
        self.tasklist = TaskList()
        self.command = {"?": self.show_commands, "visa": self.show_task,
                        "klar": self.mark_done, "ny": self.new_task}

    def show_commands(self):
        """Skriver ut vilka kommandon som användaren kan välja."""
        print("Kommando: ny, visa, klar, ? ")

    def new_task(self):
        """Frågar användaren vilken uppgift som ska läggas till."""
        while True:
            description = input("Beskriv uppgiften: ")
            user_input = input((
                "Du skrev '{}', är det ok? [j/n] ").format(description))
            if user_input == "j":
                self.tasklist.create_task(description)
                break
            elif user_input == "n":
                break
            elif user_input != "n" or "j":
                print("ogilitg kommando")
                break

    def show_task(self):
        """Printar alla tasks som lagts till, både klar och oklar."""
        self.tasklist.__str__()

    def mark_done(self):
        """Skriv ut de som finns och kör mark_done på den utpekade."""
        length = len(self.tasklist.task_list)
        while True:
            user_input = input(
                "Vilken uppgifte ska markeras som klar? ")
            if user_input == "q":
                break
            if user_input == "-0":
                print("Angivet index är ogiltig ")
                break
            try:
                if int(user_input) < length and int(user_input) >= 0:
                    self.tasklist.mark_done(int(user_input))
                    break
                else:
                    print("Detta finns inte i listan. ")
                    break
            except ValueError:
                print("Angivet index är ogiltig ")

    def main(self):
        """Interakteras med användaren."""
        while True:
            message = input("Ange kommando (q=Avsluta, ?=hjälp): ")
            if message == "q":
                break
            try:
                self.command[message]()
            except KeyError:
                print("Kommande är ogilitug")


def Main():
    """kör programmet."""
    if __name__ == "__main__":
        app = TodoApp()
        app.main()


Main()
