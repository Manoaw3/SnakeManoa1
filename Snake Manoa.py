import tkinter #importation d'une librairie
import random #placer la pomme aléatoirement à chaque fois

ROWS = 25                   #25 lignes
COLS = 25                   #25 colones
TILE_SIZE = 25 #taille de la case 5x5 pixels

WINDOW_WIDTH = TILE_SIZE * ROWS
WINDOW_HEIGHT = TILE_SIZE * COLS

# On initialise nous même, TILE = Case
class Tile : 
    def __init__(self, x, y):
        self.x = x
        self.y = y
    


window = tkinter.Tk()  #fenêtre de jeu
window.title("Snake de Manoa")
window.resizable(False, False)

canvas = tkinter.Canvas(window, bg = "black", width = WINDOW_WIDTH, height = WINDOW_HEIGHT, borderwidth = 0, highlightthickness= 0)
canvas.pack() # ????
window.update()

#centrer la fenêtre
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/2)) #y'a INT dans Python aussi ? 
window_y = int((screen_height/2) - (window_height/2)) #là on alligne la fenêtre au milieu (on la place au milieu)

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}") #ON definit F comme le perimètre =string

#Initialiser le jeu
snake = Tile(5*TILE_SIZE, 5*TILE_SIZE) #Tile = case, 1 seule case : tête du snake
food = Tile(10*TILE_SIZE, 10*TILE_SIZE )
snake_body = [] #multiples cases de serpent
velocityX = 0
velocityY = 0 #par défaut le serpent ne bouge pas
game_over = False
score = 0

def change_direction(e) : #e= event / e est le paramètre de la fonction.
    #print(e)
    print(e.keysym) #enregistre dans la console/terminal la touche préssée
    #keysym = keysymbol
    global velocityX, velocityY, game_over #set les velocités (mouvements) comme variables globales
 
    if (game_over):
        return

    if (e.keysym == "Up" and velocityY !=1): #permet aussi d'éviter qu'on puisse faire demi-tour
        ##Si la touche enregistrée est "Up" alops la vélocité Y fait -1 (on monte)
        velocityX = 0
        velocityY = -1
    elif(e.keysym == "Down"and velocityY !=-1):
        velocityX = 0
        velocityY = 1
    elif(e.keysym == "Left" and velocityX !=1):
        velocityX = -1
        velocityY = 0
    elif(e.keysym == "Right" and velocityX !=-1):
        velocityX = 1
        velocityY = 0

def move():
    global snake, food, snake_body, game_over, score

    if(game_over) :
        return
        
    if (snake.x < 0 or snake.x >= WINDOW_WIDTH or snake.y < 0 or snake.y >= WINDOW_HEIGHT): #si on dépasse les bords de fenêtre
        game_over = True
        return 
    
    for tile in snake_body : #si la tête du serpent touche son corp
            if (snake.x == tile.x and snake.y == tile.y):
                game_over = True
                return

    #collision = verifier si le X et Y du snake == Y de la nourriture
    if (snake.x == food.x and snake.y == food.y):
        snake_body.append(Tile(food.x, food.y)) #La méthode append() permet d'ajouter un élément à la fin d'une liste existante
        food.x = random.randint(0, COLS-1) * TILE_SIZE
        food.y = random.randint(0, ROWS-1) * TILE_SIZE #Replacer le food dans une position X aléatoire
        score += 1

    #update snake body 
    for i in range(len(snake_body)-1,-1, -1 ) : # on se base par rapport a la case suivante
        tile = snake_body[i]
        if (i==0): # si il n'ya rien dans la case ça se déplace
            tile.x = snake.x
            tile.y = snake.y
        else :
            prev_tile = snake_body[i-1]
            tile.x = prev_tile.x
            tile.y = prev_tile.y # code à revoir car je veux mieux comprendre.

        

    snake.x += velocityX * TILE_SIZE
    snake.y += velocityY * TILE_SIZE    #Move one Tile over = move one pixel over

def draw():
    global snake, food, snake_body, game_over, score  #Quand j'utilise la vairable "snake" il saura que je me réfère à la variable snake en "global"
    move() #on execute la fonction move

    canvas.delete("all") #pour effacer chaque frame après le dessin

     #On modelise la nourriture
    canvas.create_rectangle(food.x, food.y, food.x + TILE_SIZE, food.y + TILE_SIZE, fill="red")
     
    #on dessine le snake
    canvas.create_rectangle(snake.x, snake.y, snake.x + TILE_SIZE, snake.y + TILE_SIZE, fill="lime green") #On vient de créer et placer le serpent

    for tile in snake_body :#creation du corps rajouté du serpent par la variable snakebody
        canvas.create_rectangle(tile.x, tile.y, tile.x + TILE_SIZE, tile.y + TILE_SIZE, fill = "lime green")

    if (game_over):
        canvas.create_text(WINDOW_HEIGHT/2, WINDOW_HEIGHT/2, font=("Arial", 20), text=f"Psst ! Je cherche un stage ;) ! Score : {score} !", fill="white")
    else :
        canvas.create_text(30, 20, font = "Arial 10", text = f"Score: {score}", fill = "white")

    window.after(100, draw) #100 ms = 1/10 second, 10fps

    

   
    
draw()

window.bind("<KeyRelease>", change_direction) #si on presse une touche = fonction change_dirrection

window.mainloop() #dans la fenêtre il se passe quoi ? 


