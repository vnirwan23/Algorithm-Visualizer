
import pygame
import time
start1 = time.time()
#time.sleep(10)
pygame.init()

scr_width = 720
scr_height = 720

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
light_blue = (200, 200, 250)
red = (255, 0, 0)

thin_line_space = scr_width // 9
thick_line_space = scr_width // 3

screen = pygame.display.set_mode((scr_width, scr_height))
done = False

#cnt = 0

pygame.display.set_caption('Sudoku')
screen.fill(white)
font = pygame.font.Font('freesansbold.ttf', 50)

def draw_lines():
    global screen
    #Draw Major Lines
    for x in range(0, scr_width, thin_line_space):  # draw vertical lines
        pygame.draw.line(screen, black, (x, 0), (x, scr_height))

    for x in range(0, scr_height, thin_line_space):  # draw vertical lines
        pygame.draw.line(screen, black, (0, x), (scr_width, x))

    for x in range(0, scr_width, thick_line_space):  # draw vertical lines
        pygame.draw.line(screen, black, (x, 0), (x, scr_height), 4)

    for x in range(0, scr_height, thick_line_space):  # draw vertical lines
        pygame.draw.line(screen, black, (0, x), (scr_width, x), 4)

    return

def column(matrix, i):
    return [row[i] for row in matrix]

def solvesud(sud, i, j):

    check = 1
    for items in sud:
        if 0 in items:
            check = 0
    if check == 1:
        #print(sud)
        return

    if sud[i][j] != 0:
        solvesud(sud, i + j // 8, (j + 1) % 9)

    else:
        for k in range(1, 10):
            if k in sud[i]:
                continue
            if k in column(sud, j):
                continue
            start_i = (i // 3) * 3
            start_j = (j // 3) * 3
            present = 0
            for temp_i in range(start_i, start_i + 3):
                for temp_j in range(start_j, start_j + 3):
                    if sud[temp_i][temp_j] == k:
                        present = 1
                        break
            if present == 1:
                continue

            sud[i][j] = k
            solvesud(sud, i + j // 8, (j + 1) % 9)
            # print(sud)
            check1 = 1
            for items in sud:
                if 0 in items:
                    check1 = 0
            if check1 == 1:
                return
            sud[i][j] = 0


def solvesud_visu(sud, i, j):
    global screen
    global font
    #global cnt
    check = 1
    for items in sud:
        if 0 in items:
            check = 0
    if check == 1:
        #print(sud)
        return

    if sud[i][j] != 0:
        solvesud_visu(sud, i + j // 8, (j + 1) % 9)

    else:
        for k in range(1, 10):
            #print(k)
            sud[i][j] = k
            screen.fill(white)
            #time.sleep(1)
            draw_lines()
            # screen.blit(text, textRect)
            # screen.blit(text1, textRect1)
            text = [[], [], [], [], [], [], [], [], []]
            #print(text)
            for li in range(9):
                for lj in range(9):
                    # temp = font.render(str(sud[i][j]), True, black)
                    (text[li]).append(font.render(str(sud[li][lj]), True, black))

            # print(text)
            textRect = [[], [], [], [], [], [], [], [], []]
            for li in range(9):
                for lj in range(9):
                    # temp1 = (text123[i][j]).get_rect()
                    (textRect[li]).append((text[li][lj]).get_rect())
                    textRect[li][lj].center = ((scr_width // 18) * (2 * lj + 1), (scr_height // 18) * (2 * li + 1))

            for li in range(9):
                for lj in range(9):
                    if sud[li][lj] == 0:
                        continue
                    screen.blit(text[li][lj], textRect[li][lj])

                    #print('abcdef')
                    #time.sleep(0.001)
            time.sleep(0.1)
            pygame.display.flip()
            #cnt += 1
            sud[i][j] = 0
            if k in sud[i]:
                continue
            if k in column(sud, j):
                continue
            start_i = (i // 3) * 3
            start_j = (j // 3) * 3
            present = 0
            for temp_i in range(start_i, start_i + 3):
                for temp_j in range(start_j, start_j + 3):
                    if sud[temp_i][temp_j] == k:
                        present = 1
                        break
            if present == 1:
                continue

            sud[i][j] = k
            solvesud_visu(sud, i + j // 8, (j + 1) % 9)
            # print(sud)
            check1 = 1
            for items in sud:
                if 0 in items:
                    check1 = 0
            if check1 == 1:
                return
            sud[i][j] = 0



sud = [[0, 7, 0, 0, 0, 5, 0, 1, 4],
       [0, 3, 1, 7, 0, 0, 8, 0, 0],
       [8, 0, 0, 0, 6, 0, 3, 0, 0],
       [7, 4, 0, 8, 5, 0, 0, 3, 9],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [9, 6, 0, 0, 4, 3, 0, 7, 1],
       [0, 0, 7, 0, 3, 0, 0, 0, 5],
       [0, 0, 6, 0, 0, 8, 9, 4, 0],
       [2, 9, 0, 4, 0, 0, 0, 8, 0]]

'''sud = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]]'''

ansud = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0]]

for i in range(9):
    for j in range(9):
        ansud[i][j] = sud[i][j]

solvesud(ansud, 0, 0)

#print(ansud)
#print(sud)


while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill(white)
            curr_box = []
            pos = pygame.mouse.get_pos()
            #print(pos)
            #print(pos[0])
            pygame.draw.rect(screen, light_blue, ((pos[0] // 80) * 80,  (pos[1] // 80) * 80, 80, 80))
            curr_box = [pos[1] // 80, pos[0] // 80]
            #print(curr_box)

        keys = pygame.key.get_pressed()
        try:
            if keys[pygame.K_1] and sud[curr_box[0]][curr_box[1]] == 0:
                sud[curr_box[0]][curr_box[1]] = 1
                if ansud[curr_box[0]][curr_box[1]] != 1:
                    pygame.draw.rect(screen, red, (curr_box[1] * 80, curr_box[0] * 80, 80, 80))

            if keys[pygame.K_2] and sud[curr_box[0]][curr_box[1]] == 0:
                sud[curr_box[0]][curr_box[1]] = 2
                if ansud[curr_box[0]][curr_box[1]] != 2:
                    pygame.draw.rect(screen, red, (curr_box[1] * 80, curr_box[0] * 80, 80, 80))

            if keys[pygame.K_3] and sud[curr_box[0]][curr_box[1]] == 0:
                sud[curr_box[0]][curr_box[1]] = 3
                if ansud[curr_box[0]][curr_box[1]] != 3:
                    pygame.draw.rect(screen, red, (curr_box[1] * 80, curr_box[0] * 80, 80, 80))

            if keys[pygame.K_4] and sud[curr_box[0]][curr_box[1]] == 0:
                sud[curr_box[0]][curr_box[1]] = 4
                if ansud[curr_box[0]][curr_box[1]] != 4:
                    pygame.draw.rect(screen, red, (curr_box[1] * 80, curr_box[0] * 80, 80, 80))

            if keys[pygame.K_5] and sud[curr_box[0]][curr_box[1]] == 0:
                sud[curr_box[0]][curr_box[1]] = 5
                if ansud[curr_box[0]][curr_box[1]] != 5:
                    pygame.draw.rect(screen, red, (curr_box[1] * 80, curr_box[0] * 80, 80, 80))

            if keys[pygame.K_6] and sud[curr_box[0]][curr_box[1]] == 0:
                sud[curr_box[0]][curr_box[1]] = 6
                if ansud[curr_box[0]][curr_box[1]] != 6:
                    pygame.draw.rect(screen, red, (curr_box[1] * 80, curr_box[0] * 80, 80, 80))

            if keys[pygame.K_7] and sud[curr_box[0]][curr_box[1]] == 0:
                sud[curr_box[0]][curr_box[1]] = 7
                if ansud[curr_box[0]][curr_box[1]] != 7:
                    pygame.draw.rect(screen, red, (curr_box[1] * 80, curr_box[0] * 80, 80, 80))

            if keys[pygame.K_8] and sud[curr_box[0]][curr_box[1]] == 0:
                sud[curr_box[0]][curr_box[1]] = 8
                if ansud[curr_box[0]][curr_box[1]] != 8:
                    pygame.draw.rect(screen, red, (curr_box[1] * 80, curr_box[0] * 80, 80, 80))

            if keys[pygame.K_9] and sud[curr_box[0]][curr_box[1]] == 0:
                sud[curr_box[0]][curr_box[1]] = 9
                if ansud[curr_box[0]][curr_box[1]] != 9:
                    pygame.draw.rect(screen, red, (curr_box[1] * 80, curr_box[0] * 80, 80, 80))

            if keys[pygame.K_BACKSPACE] or keys[pygame.K_DELETE]:
                screen.fill(light_blue, (curr_box[1] * 80, curr_box[0] * 80, 80, 80))
                sud[curr_box[0]][curr_box[1]] = 0

            if keys[pygame.K_SPACE]:
                solvesud_visu(sud, 0, 0)
                print('solved')
                #print(sud)
        except:
            pass



    draw_lines()
    #screen.blit(text, textRect)
    #screen.blit(text1, textRect1)
    text = [[], [], [], [], [], [], [], [], []]
    for i in range(9):
        for j in range(9):
            # temp = font.render(str(sud[i][j]), True, black)
            (text[i]).append(font.render(str(sud[i][j]), True, black))

    # print(text)
    textRect = [[], [], [], [], [], [], [], [], []]
    for i in range(9):
        for j in range(9):
            # temp1 = (text123[i][j]).get_rect()
            (textRect[i]).append((text[i][j]).get_rect())
            textRect[i][j].center = ((scr_width // 18) * (2 * j + 1), (scr_height // 18) * (2 * i + 1))


    for i in range(9):
        for j in range(9):
            if sud[i][j] == 0:
                continue
            screen.blit(text[i][j], textRect[i][j])
            pygame.display.flip()

    #pygame.display.flip()

#print(cnt)
end1 = time.time()

#print(end1 - start1)
