from rich.console import Console
import os
import time
from win10toast import ToastNotifier


console = Console()

toast = ToastNotifier()

console.print("Hola,", " Empecemos! :smile:", style="bold red")

console.print("Cual es la palabra que deseas memorizar? :smile:", style="bold blue")

word = input()

console.print("Cual es el significado que deseas memorizar? :smile:", style="bold blue")
meaning = input()
 

console.print("Cada cuanto tiempo desea que notifique? (en minutos)", style="bold blue")
minutos = int(input())

console.print("Cuantas veces desea que se le notifique", style="bold yellow")
veces = int(input())


os.system("cls")
console.print("   Palabra  -> ",word, style = "bold")
console.print("Significado -> ",word, style = "bold red")


def notiffication_word():
    toast.show_toast(
        "Palabra",
        f"{word} : {meaning}",
        duration = 20,
        icon_path = "idea-genial.ico",
        threaded = True,
    )

import time
  
  
while(veces>0):
    notiffication_word()
    time.sleep(60*minutos) # 60 * minutos

console.print("Gracias por usarme:raccoon: :thumbs_up:")
