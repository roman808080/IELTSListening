import pyttsx3
from random import randint


ALPHABET = '1234567890' \
           'abcdefghijklmnopqrstuvwxyz'

MIN_LENGTH = 4
MAX_LENGTH = 5

ENGINE = pyttsx3.init()


def generate_exercise():
    letters_amount = randint(MIN_LENGTH, MAX_LENGTH - 1)
    result = ''

    for _ in range(0, letters_amount):
        letter_shift = randint(0, len(ALPHABET) - 1)
        result += ALPHABET[letter_shift]

    return result


def add_commas(string):
    return ', '.join(string)


def play(exercise):
    ENGINE.say(add_commas(exercise))
    ENGINE.runAndWait()


def main():

    while True:
        exercise = generate_exercise()

        stop = False
        while not stop:
            play(exercise)
            was_written = input()

            if was_written == '/r':
                continue

            is_correct = 'correct' if was_written == exercise else 'incorrect'
            print(f"Was written {was_written}, the original phrase {exercise}. It was {is_correct}")
            stop = True

        input("Press Enter to continue...")


if __name__ == '__main__':
    main()
