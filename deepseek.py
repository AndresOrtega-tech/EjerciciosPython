import tkinter as tk

def draw_board():
    canvas = tk.Canvas(width=300, height=300)
    canvas.pack()
    
    squares = []
    for i in range(3):
        for j in range(3):
            x = (i + 1) * 100
            y = (j + 1) * 100
            square = tk.Canvas(canvas, width=100, height=100)
            square.pack(anchor='ne', padx=5, pady=5)
            squares.append(square)
    
    return squares

def write_text(text, font=('Arial', 24)):
    label = tk.Label(text=text, font=font, anchor='center')
    label.pack()

def draw_square(squares, is_even=True):
    if not is_even:
        return
    x_coord = []
    y_coord = []
    
    for i in range(3):
        for j in range(3):
            square = squares[i][j]
            # Cambiar el fondo de los cuadros a gris
            square_bg = square.bgconfig['bg']
            if not square_bg:
                square_bg.set('#e0e0e0')
            
            # Obtener las coordenadas para el click
            x = (i + 1) * 100
            y = (j + 1) * 100
            square.x = x
            square.y = y
            
    if is_even:
        write_text("X", font=('Arial', 24, 'bold'))
    else:
        write_text("O", font=('Arial', 24, 'bold'))

def handle_click(event, row, col):
    current_square = event.widget
    squares = draw_board()  # Actualizar las listas de cuadros
    
    if (current_square.x is None or 
        current_square.y is None or
        int(current_square.x) < 0 or
        int(current_square.y) < 0 or
        int(current_square.x) > 299 or
        int(current_square.y) > 299):
        return
    
    if squares[row][col] != draw_square[0].bg:
        # Cambiar el fondo de los cuadros
        for i in range(3):
            for j in range(3):
                squares[i][j].bg = '#fff'
                
        x = int(current_square.x)
        y = int(current_square.y)
        
        if 5 <= x <= 295 and 5 <= y <= 295:
            square = squares[1][1]
            square_bg = square.bg
            square_bg.set('#e0e0e0')
            
            for i in range(3):
                for j in range(3):
                    if (i == row and j == col) or (i, j) == (1, 1):
                        squares[i][j] = draw_square[0].bg
                        
        else:
            square = squares[row][col]
            square_bg = square.bg
            square_bg.set('#e0e0e0')
            
            for i in range(3):
                if i != row or j == col:
                    squares[i][col] = draw_square[0].bg

squares = None  # Variable global para almacenar las listas de cuadros

def reset_game():
    global squares
    squares = []
    for i in range(3):
        for j in range(3):
            square = tk.Canvas(tk.Tk(), width=100, height=100)
            square.pack(anchor='ne', padx=5, pady=5)
            squares.append([square, square.x, square.y])

root = tk.Tk()

def main():
    draw_board()
    
    def handle_square_click(event):
        current_square = event.widget
        row = int(current_square.y // 100) - 1
        col = int(current_square.x // 100) - 1
        
        if row >= 0 and row < 3 and col >= 0 and col < 3:
            handle_click(None, row, col)
    
    for i in range(3):
        for j in range(3):
            squares[i][j].bind('<Button-1>', lambda e=j, i=i, j=j: handle_square_click(e))
    
    root.mainloop()

if __name__ == "__main__":
    main()