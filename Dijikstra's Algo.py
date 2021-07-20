import pygame as pg
from queue import PriorityQueue

pg.init()

clock = pg.time.Clock()

screen  = pg.display.set_mode((900,900))

pg.display.set_caption('Algo Visualizer')

loop = True

eventsDone = 0

Xstart = 0
Ystart = 0
Xend = 0
Yend = 0
w = 150
h = 150
mousedown = 0
miniDist = [[1000000 for x in range(w)] for y in range(h)]
prevNode = [[(-1,-1) for x in range(w)]for y in range(h)]
Done = [[0 for x in range(w)] for y in range(h)]
Dist = PriorityQueue()
walls = []
pg.font.init()

font = pg.font.Font('freesansbold.ttf',20)

def colorTheBoxes():
    for x in color:
        pg.draw.rect(screen,(0,0,255),(x[0]*6,x[1]*6,6,6),0)

def check(x,y):
    for i in walls:
        if(i[0] == x and i[1] == y):
            return False
    return True
def DijikstraAlgo(loop):
    for x in range(150):
        for y in range(150):
          if(check(x,y)):
            Dist.put((miniDist[x][y],(x,y)))
    done = 0
    while done < 22500:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                loop = False
                break
        if not(loop):
            return loop
        temp = Dist.get()
        i = temp[1][0]
        j = temp[1][1]
        if (i == Xend and j == Yend):
            while (not(prevNode[i][j] == (-1,-1))):
                if(i == Xstart and j == Ystart):
                    eventsDone = 0
                    pg.draw.rect(screen, (0, 0, 0), (prevNode[i][j][0] * 6, 6 * prevNode[i][j][1], 6, 6), 0)
                    pg.display.update()
                    break
                pg.draw.rect(screen, (255, 255, 0), (prevNode[i][j][0] * 6, 6 * prevNode[i][j][1], 6, 6), 0)
                x = prevNode[i][j][0]
                y = prevNode[i][j][1]
                i = x
                j = y
                pg.display.update()
            break
        if(Done[i][j] == 0):
            Done[i][j] = 1
            done += 1
        else:
            continue
        if (i - 1 >= 0 and check(i - 1,j)):
            if (miniDist[i - 1][j] > miniDist[i][j] + 1):
                miniDist[i - 1][j] = miniDist[i][j] + 1
                Dist.put((miniDist[i - 1][j],(i - 1, j)))
                prevNode[i - 1][j] = (i, j)
        if (i + 1 < 150 and check(i + 1,j)):
            if (miniDist[i + 1][j] > miniDist[i][j] + 1):
                miniDist[i + 1][j] = miniDist[i][j] + 1
                Dist.put((miniDist[i + 1][j],(i + 1, j)))
                prevNode[i + 1][j] = (i, j)
        if (j + 1 < 150 and check(i,j + 1)):
            if (miniDist[i][j + 1] > miniDist[i][j] + 1):
                miniDist[i][j + 1] = miniDist[i][j] + 1
                Dist.put((miniDist[i][j + 1],(i,j + 1)))
                prevNode[i][j + 1] = (i, j)
        if (j - 1 >= 0 and check(i,j - 1)):
            if (miniDist[i][j - 1] > miniDist[i][j] + 1):
                miniDist[i][j - 1] = miniDist[i][j] + 1
                Dist.put((miniDist[i][j - 1],(i, j-1)))
                prevNode[i][j - 1] = (i, j)
        pg.draw.rect(screen, (0, 0, 255), (i * 6, 6 * j, 6, 6), 0)
        drawBoxes()
        #drawLines()
        pg.display.update()
    return True
def drawLines():
    for i in range(1,150):
        pg.draw.line(screen,(0,0,0),(6*i - 1,0),(6*i - 1,900),1)
        pg.draw.line(screen,(0,0,0),(0,6*i - 1),(900,6*i - 1),1)

screen.fill((255,255,255))

def drawBoxes():
    if eventsDone == 0:
        pg.draw.rect(screen,(0,200,200),(0,0,900,38),0)
        pg.draw.line(screen,(0,0,0),(0,38),(900,38),2)
        text = font.render('Choose the Starting Point',True,(0,0,0))
        textRect = text.get_rect()
        textRect.center = (300,19)
        screen.blit(text,textRect)
        return
    else:
        if eventsDone >= 1:
            if eventsDone == 1:
                pg.draw.rect(screen, (0, 200, 200), (0, 0, 600, 38), 0)
                pg.draw.line(screen, (0, 0, 0), (0, 38), (600, 38), 2)
                text = font.render('Choose the End Point', True, (0, 0, 0))
                textRect = text.get_rect()
                textRect.center = (300, 19)
                screen.blit(text, textRect)
            pg.draw.rect(screen,(0,0,0),(Xstart*6,Ystart*6,6,6),0)
            if(eventsDone >= 2):
                if(eventsDone == 2):
                    pg.draw.rect(screen, (0, 200, 200), (0, 0, 600, 38), 0)
                    pg.draw.line(screen, (0, 0, 0), (0, 38), (600, 38), 2)
                    pg.draw.line(screen,(0,0,0),(500,0),(500,40))
                    text = font.render('Draw the obstacles or Walls', True, (0, 0, 0))
                    textRect = text.get_rect()
                    textRect.center = (250, 19)
                    screen.blit(text, textRect)
                    text1 = font.render('Skip', True, (0, 0, 0))
                    textRect1 = text1.get_rect()
                    textRect1.center = (550, 19)
                    screen.blit(text1, textRect1)
                pg.draw.rect(screen, (0, 0, 0), (Xend * 6, Yend * 6, 6, 6), 0)
                if(eventsDone == 3):
                    pg.draw.rect(screen, (0, 200, 200), (0, 0, 600, 38), 0)
                    pg.draw.line(screen, (0, 0, 0), (0, 38), (600, 38), 2)
                    text = font.render('To Start,Press this Button', True, (0, 0, 0))
                    textRect = text.get_rect()
                    textRect.center = (300, 19)
                    screen.blit(text, textRect)
                for x in walls:
                    pg.draw.rect(screen,(0,0,0),(x[0]*6,x[1]*6,6,6),0)
while(loop):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            loop = False
        if event.type == pg.MOUSEBUTTONDOWN:
            if pg.mouse.get_pressed() == (1,0,0) and eventsDone <= 3:
                pos = pg.mouse.get_pos()
                if(eventsDone == 0):
                    Xstart = int(pos[0]/6)
                    Ystart = int(pos[1]/6)
                    miniDist[Xstart][Ystart] = 0
                    eventsDone += 1
                else:
                    if(eventsDone == 1):
                        Xend = int(pos[0]/6)
                        Yend = int(pos[1]/6)
                        eventsDone += 1
                    else:
                        if(eventsDone == 2):
                            if(pow((pos[0]-550)*(pos[0] - 550),1/2) <= 50 and pow((pos[1]-19)*(pos[1] - 19),1/2) <= 21):
                                eventsDone += 1
                                break
                            else:
                                mousedown = 1
                        if(eventsDone == 3 and pow((pos[0] - 300)*(pos[0]-300),1/2) <= 300 and pow((pos[1]-19)*(pos[1] - 19),1/2) <= 21):
                            eventsDone += 1
        if event.type == pg.MOUSEBUTTONUP and mousedown:
            mousedown = 0
            eventsDone += 1
    if(eventsDone <= 4):
        screen.fill((255, 255, 255))
        #drawLines()
        if(mousedown):
            pos = pg.mouse.get_pos()
            x = int(pos[0]/6)
            y = int(pos[1]/6)
            walls.append((x,y))
        drawBoxes()
        if(eventsDone == 4):
            loop = DijikstraAlgo(loop)
            pg.time.wait(2000)
            eventsDone = 0
            Xstart = -1
            Ystart = -1
            Xend = -1
            Yend = -1
            walls = []
            for x in range(150):
                for y in range(150):
                    miniDist[x][y] = 1000000
                    prevNode[x][y] = (-1,-1)
                    Done[x][y] = 0
        pg.display.flip()
        clock.tick(60)
pg.quit()Dijik
