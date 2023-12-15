import turtle
import time
import tkinter as tk

def desenhar_haste(x, y, altura):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(altura)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(altura)
    turtle.left(90)
    turtle.forward(10)

def desenhar_disco(x, y, largura, altura):
    turtle.penup()
    turtle.goto(x - largura / 2, y)
    turtle.pendown()
    turtle.fillcolor("blue")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(largura)
        turtle.left(90)
        turtle.forward(altura)
        turtle.left(90)
    turtle.end_fill()

def mover_disco(origem, destino):
    disco = hastes[origem].pop()
    hastes[destino].append(disco)
    x, y = coordenadas_disco(destino, len(hastes[destino]))
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.clear()
    desenhar_torre()

def coordenadas_disco(haste, nivel):
    x = haste * 150 - 150
    y = nivel * 20
    return x, y

def resolver_hanoi(n, origem, destino, auxiliar):
    if n > 0:
        resolver_hanoi(n - 1, origem, auxiliar, destino)
        time.sleep(0.5)  # Aguarda 0.5 segundos entre os movimentos
        mover_disco(origem, destino)
        resolver_hanoi(n - 1, auxiliar, destino, origem)

def desenhar_torre():
    for i in range(3):
        desenhar_haste(i * 150 - 150, 0, 200)
        for j in range(len(hastes[i])):
            x, y = coordenadas_disco(i, j + 1)
            largura = hastes[i][j] * 20
            desenhar_disco(x, y, largura, 20)

if __name__ == "__main__":
    
    
   

    root = tk.Tk()
    root.withdraw()



    
    
    turtle.speed(0)
    turtle.hideturtle()

    num_discos = int(turtle.numinput("Quantidade de Discos", "Digite a quantidade de discos:", default=3, minval=1))
    hastes = [list(range(num_discos, 0, -1)), [], []]  # Configuração inicial com 'num_discos' discos na haste A

    desenhar_torre()
    resolver_hanoi(num_discos, 0, 2, 1)  # Resolve a Torre de Hanói com a quantidade especificada de discos

    turtle.done()
