from time import sleep

import cowsay

if __name__ == '__main__':
    cowsay.cow('Hello World')
    sleep(2)
    cowsay.fox(
        'Теперь вы можете работать с проектом не только на домашнем компьютере, '
        'но даже с телефона и/или планшета'
    )
