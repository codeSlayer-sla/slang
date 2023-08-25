"""



    Dictionary from: https://es.wiktionary.org/wiki/Wikcionario:Jerga_paname%C3%B1a

"""

import sqlite3



class Slang:

    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning



lb = "\n\n"
t = "\t\t"
lb_t = "\n\t\t"
lb_t2 = f"{lb_t}{t}"



conn = sqlite3.connect("slang.db")
cursor = conn.cursor()



try:
    cursor.execute("CREATE TABLE SlangPanameno(word text, meaning text)")
except sqlite3.OperationalError:
    pass



def insert_record(slang):
    with conn:
        cursor.execute("INSERT INTO SlangPanameno VALUES (:word, :meaning)",
                       {'word': slang.word, 'meaning': slang.meaning})



def edit_record(word_request, new_word, new_meaning):
    with conn:
        cursor.execute("UPDATE SlangPanameno SET word=:new_word, meaning=:new_meaning WHERE word = :word_request",
                       {'word_request': word_request, 'new_meaning': new_meaning, 'new_word': new_word})



def del_record(word):
    with conn:
        cursor.execute("DELETE FROM SlangPanameno WHERE word=:word", {'word': word})



def get_records():
    with conn:
        cursor.execute("SELECT * FROM SlangPanameno")
        results = cursor.fetchall()
        return results



def get_meaning_by_word(word):
    cursor.execute("SELECT * FROM SlangPanameno WHERE word=:word", {'word': word})
    result = cursor.fetchone()
    return result

def add_word():
    word = input(f"{lb_t2}Ingresa la palabra: ")
    meaning = input(f"{lb_t2}Ingresa el significado: ")
    new_word = Slang(word, meaning)
    insert_record(new_word)
    print(f"{lb_t2}¡Palabra guardada!")



def edit_word():
    word_request = input(f"{lb_t2}Ingrese palabra a editar: ")
    new_word = input(f"{lb_t2}Ingrese nueva palabra: ")
    new_meaning = input(f"{lb_t2}Ingrese el significado: ")
    edit_record(word_request, new_word, new_meaning)
    print(f"{lb_t2}¡Palabra editada!")


def del_word():
    word = input(f"{lb_t2}Ingresa palabra para eliminar: ")
    del_record(word)
    print(f"{lb_t2}¡Palabra eliminada!")


def see_words():
    print(f"{lb_t2}\tP A L A B R A{t}{t}S I G N I F I C A D O")
    for x in get_records():
        print(f"{lb_t2}{x[0]}{t}{t}{x[1]}")


def get_meaning():
    word = input(f"{lb_t}{t}Ingresa la palabra a buscar: ")
    try:
        x = get_meaning_by_word(word)
        print(f"{lb_t2}{x[0]}, significa: {x[1]}")
    except TypeError:
        print(f"{lb_t2}ERROR - Palabra no encontrada")




print(f"{lb}BIENVENIDO AL DICCIONARIO DE SLANG PANAMEÑO")


menu = """

        
        1) Agregar nueva palabra
        2) Editar palabra
        3) Eliminar palabra 
        4) Ver palabras
        5) Buscar significado de palabra
        6) Salir
        """



end = False
len(menu)
while not end:
    try:
        print(menu)
        option = int(input(f"{lb_t}Ingresa una opcion: "))
        match option:
            case 1:
                add_word()
            case 2:
                edit_word()
            case 3:
                del_word()
            case 4:
                see_words()
            case 5:
                get_meaning()
            case 6:
                exit(0)
    except ValueError:
        print(f"{lb_t}ERROR - Ingrese una opcion correcta")
#


conn.close()
