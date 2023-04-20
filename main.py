import pygame
from Quantum_TTT import classical_move,quantum_move,mark
from Error_display import Error,guideline
        
pygame.init()
clicked=False
clicked_side=False
running = True
i=0
j=0
marked=False
classical=False
quantum=False
entangle=False
ct = False
tg = False
guidelines=False
qt=0
xo='' 
background_colour = (0,0,0)
black = (0,0,0)
white = (255,255,255)
moves=['O','X']
game_moves=[]
purple=(160,32,240)
cell_number=0
cell_list=[]
quantum_set=set()
control=set()
target=set()
pturn = set()

Win_moves=[[0,1,2],[3,4,5],[6,7,8],
            [0,3,6],[1,4,7],[2,5,8],
            [0,4,8],[2,4,6]]

cell_dict={'tl':1,'tm':2,'tr':3,
           'ml':4,'mm':5,'mr':6,
           'bl':7,'bm':8,'br':9}

win_dict= {'tl':1,'tm':2,'tr':3,
           'ml':4,'mm':5,'mr':6,
           'bl':7,'bm':8,'br':9}

yolist=['tl','tm','tr',
        'ml','mm','mr',
        'bl','bm','br']

def evaluate():
    draw_count=0
    for list in Win_moves:
        a,b,c=list
        if win_dict[yolist[a]] == win_dict[yolist[b]] == win_dict[yolist[c]]=='X':
            return 'Player X won !!!'
            
        elif win_dict[yolist[a]] == win_dict[yolist[b]] == win_dict[yolist[c]]=='O':
            return 'Player O won !!!'
        
        elif win_dict[yolist[a]] in moves and win_dict[yolist[b]] in moves and win_dict[yolist[c]] in moves:
            draw_count+=1
        
        if draw_count==8:
            return 'Draw'

screen = pygame.display.set_mode((900, 650))
pygame.display.set_caption('Quantum tic tac toe')
screen.fill(background_colour)

def cell_pos(cell):
    rx=225
    ry=120
    rw=450
    rh=450
    if cell == 'tl':
        return (rx,ry,rw//3,rh//3)
    elif cell == 'tm':
        return (rx+150,ry,rw//3,rh//3)
    elif cell == 'tr':
        return (rx+300,ry,rw//3,rh//3)
    elif cell == 'ml':
        return (rx,ry+150,rw//3,rh//3)
    elif cell == 'mm':
        return (rx+150,ry+150,rw//3,rh//3)
    elif cell == 'mr':
        return (rx+300,ry+150,rw//3,rh//3)
    elif cell == 'bl':
        return (rx,ry+300,rw//3,rh//3)
    elif cell == 'bm':
        return (rx+150,ry+300,rw//3,rh//3)
    elif cell == 'br':
        return (rx+300,ry+300,rw//3,rh//3)
    elif cell == 'sc':
        return (rx,ry,rw,rh)
    elif cell =='cm':
        return (30,320,170,40)
    elif cell == 'cm_ol':
        return (30,320,170,40)
    elif cell =='qm':
        return (705,320,170,40)
    elif cell == 'qm_ol':
        return (705,320,170,40)
    elif cell == 'en':
        return (740,400,110,40)
    elif cell == 'en_ol':
        return (740,400,110,40)
    elif cell == 'gdls':
        return (30,520,130,40)
        
pygame.draw.rect(screen,purple,cell_pos('sc'),2)
tl = pygame.Rect(cell_pos('tl'))
tm = pygame.Rect(cell_pos('tm'))
tr = pygame.Rect(cell_pos('tr'))

ml = pygame.Rect(cell_pos('ml'))
mm = pygame.Rect(cell_pos('mm'))
mr = pygame.Rect(cell_pos('mr'))

bl = pygame.Rect(cell_pos('bl'))
bm = pygame.Rect(cell_pos('bm'))
br = pygame.Rect(cell_pos('br'))

def mark_the_cell(xo,cellp):
    global marked
    rx,ry,rw,rh=cell_pos(cellp)
    font = pygame.font.Font('freesansbold.ttf', 120)
    screen.fill(black, cell_pos(cellp))
    text = font.render(xo, True, white,black)
    screen.blit(text,(rx+35,ry+25,rw,rh))
    marked=True

def choose_player(i):
    global pturn
    if i%2==0:
        plyr='Player X'
        pturn.add('X')
    else:
        plyr='Player O'
        pturn.add('O')
    
    font = font = pygame.font.SysFont("Brush Script MT", 70)
    screen.fill(black, (350,30,200,50))    
    text = font.render(plyr, True, purple,black)
    screen.blit(text, (350,30))

def button(cell,cellp):
    global clicked,classical,i,quantum,control,target,qt,ct,tg,marked,game_moves

    (rx, ry,rw, rh) = cell_pos(cellp)

    if cell.collidepoint(pygame.mouse.get_pos()):
        if pygame.mouse.get_pressed()[0] == 1:
            clicked = True
            pygame.draw.rect(screen,black,cell,2)

        elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
            if classical:
                game_moves.remove('c')
                main_list=get_cell_number(cellp)
                if main_list is not None:
                    for main in main_list:
                        marked=False
                        bit=main[0]
                        mark=main[1]
                        key_list=list(cell_dict.keys())
                        val_list=list(cell_dict.values())
                        vi=val_list.index(bit+1)
                        cell=key_list[vi]
                        win_dict[cell]=mark
                        (rx,ry,rw,rh)=cell_pos(cell)
                        mark_the_cell(mark,cell)
                        cell_list.append(cellp)

                    classical = False
                    choose_player(i)
                    i+=1
            
            elif quantum:
                if qt==0:
                    game_moves.remove('q')
                    ct=False
                    tg=False
                qt+=1
                if qt < 2 and not ct:
                    if cellp in cell_list:
                        qt=0
                        Error('Please select control bit in a quantum cell ')
                        ct=False
                        quantum=False
                    else:
                        control.add(cellp)
                        ct=True
                
                elif qt==2 and ct:
                    if cellp not in cell_list:
                        qt=0
                        tg=False
                        Error('Please select your target bit in classical cell ')
                        quantum=False
                    else:
                        target.add(cellp)
                        tg=True
                        quantum=False

            else:
                Error("Please select a classical or quantum move")
            clicked = False
        else:
            pygame.draw.rect(screen,(56,56,56),cell,1)
    else:
        pygame.draw.rect(screen,white,cell,1)

cm = pygame.Rect(cell_pos('cm'))
qm = pygame.Rect(cell_pos('qm'))
en = pygame.Rect(cell_pos('en'))
gl = pygame.Rect(cell_pos('gdls'))

guideline()

def move_bt(cl,name,color):
    (rx,ry,_,_)=cell_pos(cl)
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render(name, True, color, (0,0,0))
    screen.blit(text, (rx+10,ry+10))

def dsbutton(move,cl,name,cell_ol):
    global clicked_side,classical,quantum,entangle,ct,tg,qt,game_moves,guidelines
    if move.collidepoint(pygame.mouse.get_pos()):
        if pygame.mouse.get_pressed()[0] == 1:
            clicked_side=True
        elif pygame.mouse.get_pressed()[0] == 0 and clicked_side == True:
            if move == cm:
                game_moves.append('c')
                classical=True
                if len(game_moves)>1:
                    if game_moves[-2] =='c':
                        game_moves = list(dict.fromkeys(game_moves))
                        game_moves.remove('c')
                        classical=False

                if quantum:
                    Error('Please select the control and target cell first')
                    classical = False

                elif ct and tg:
                    Error('please entangle the qubits')
                    classical=False

            elif move == qm:
                game_moves.append('q')
                quantum=True
                if qt==0 and ct and tg:
                    Error("Please entangle ")
                    quantum=False
                if classical:
                    Error('Please select the classical cell first')
                    quantum=False
                
                if len(game_moves)>1:
                    if game_moves[-2] =='q':
                        game_moves = list(dict.fromkeys(game_moves))
                        game_moves.remove('q')
                        quantum=False

            elif move == en:
                entangle=True
            elif move == gl:
                guidelines=True
                guideline()

            clicked_side = False
        else:
            pygame.draw.rect(screen,purple,move,2)
    else:
        pygame.draw.rect(screen,black,move,2)
    
    if classical:
        move,cl,name = cm,'cm','Classical Move'
        move_bt(cl,name,purple)
        
    elif quantum:
        move,cl,name = qm,'qm','Quantum Move'
        move_bt(cl,name,purple)

    elif entangle:
        move,cl,name= en,'en','Entangle'
        move_bt(cl,name,purple)
        entangle_cells()
    
    else:
        move_bt(cl,name,white)

    (rx,ry,rw,rh)=cell_pos(cell_ol)
    pygame.draw.line(screen,white,(rx,ry),(rx+rw,ry),2)
    pygame.draw.line(screen,white,(rx,ry),(rx,ry+rh),2)
    pygame.draw.line(screen,purple,(rx,ry+rh),(rx+rw,ry+rh),2)
    pygame.draw.line(screen,purple,(rx+rw,ry),(rx+rw,ry+rh),2)

def get_cell_number(cellp):
    global classical
    if cellp in cell_dict.keys():
        key_list=classical_move(cell_dict[cellp]-1)
        if key_list != 0:
            main_list=mark(key_list)
            return main_list
        else:
            Error('Please select classical move on a quantum cell')
            classical=False

def mark_entangled_cells(c,t):
    global win_dict
    screen.fill(white, cell_pos(c))
    screen.fill(white,cell_pos(t)) 
    pygame.display.update()
    pygame.time.delay(1000)
    screen.fill(black, cell_pos(c))
    mark_the_cell(win_dict[t],t)
    pygame.display.update()
    
def entangle_cells():
    global i,pturn,target,control,ct,tg,qt,entangle
    
    if ct and tg:
        player=pturn.pop()
        t=target.pop()
        c=control.pop()
        mark_entangled_cells(c,t)
        qmove=quantum_move(cell_dict[t]-1,cell_dict[c]-1,player)
        if qmove != 0:
            ct=False
            tg=False
            entangle=False
            choose_player(i)
            i+=1
    else:
        qt=0
        Error("please select the control and target cell")
        entangle=False

def all_button():
    button(tl,'tl')
    button(tm,'tm')
    button(tr,'tr')

    button(ml,'ml')
    button(mm,'mm')
    button(mr,'mr')

    button(bl,'bl')
    button(bm,'bm')
    button(br,'br')

def side_buttons():
    dsbutton(cm,'cm','Classical Move','cm_ol')
    dsbutton(qm,'qm','Quantum Move','qm_ol')
    dsbutton(en,'en','Entangle','en_ol') 
    dsbutton(gl,'gdls','Guidelines','gdls')
    
i=0
choose_player(i)
i+=1
bt = True
while running:  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_button()
    
    if tg:
        qt=0

    if bt:
        side_buttons()
    
    if marked:
        win=evaluate()
        if win:
            font = font = pygame.font.SysFont("Brush Script MT", 70)
            screen.fill(black, (300,30,250,50))    
            text = font.render(win, True, purple,black)
            screen.blit(text, (270,30))
            bt = False

    pygame.display.flip()