'''
Game info:
Player starts at center
Dodges bullets
1 Bullet appears after  another dissapears
Has 1 life
Score updates via time
'''

#---Modules---
import pygame,os,random
import pygame.freetype
import json
#---Constants---
WIDTH,HEIGHT = 800, 600
BOARD = pygame.Rect(0,0,WIDTH,HEIGHT)
#--- INITALIZATION ---
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Boris The Bullet-Dodger')
pygame.init()
#
FPS = 60
clock = pygame.time.Clock()
VEL = 5 # Player velocity
B_vel = 5 # Bullet velocity
TOTAL_BULLETS = 30
LIFE = 1
comic = pygame.font.SysFont('comicsansms', 20)
comic_for_score = pygame.font.SysFont('comicsansms', 100)

#---Functions---
def draw_win(player,ls_bullets,score):
    text = pygame.font.Font.render(comic,f'Score: {score}', 1,(0,0,0))
    WIN.fill((255,255,255))
    pygame.draw.rect(WIN,(0,0,0),player)
    pygame.Surface.blit(WIN,text,(0,0))

    for bullet in ls_bullets:
        pygame.draw.rect(WIN,(0,0,0),bullet)
    ###
    pygame.display.update()

def player_movement(key_pressed,player):
    if key_pressed[pygame.K_LEFT] and player.x > 0:
        player.x -= VEL
    if key_pressed[pygame.K_RIGHT] and player.x < WIDTH-20:
        player.x += VEL
    if key_pressed[pygame.K_UP] and player.y > 0:
        player.y -= VEL
    if key_pressed[pygame.K_DOWN] and player.y < HEIGHT-20:
        player.y += VEL
# To define Random Bullet's direction
'''
def rand_dir(bullet):
    O_pick = random.randint(0,1)
    D_pick = random.randint(0,1)
    if O_pick == 0:
        if D_pick == 0:
            bullet.x += B_vel
        else:
            bullet.x -= B_vel
    else:
        if D_pick == 0:
            bullet.y += B_vel
        else:
            bullet.y -= B_vel
'''
# To define Random Bullet's direction
def rand_dir2(ls_bullets):
    i = 0
    for bullet in ls_bullets:
        if i == 0:
            bullet.x += B_vel
        elif i == 1:
            bullet.y -= B_vel
        elif i == 2:
            bullet.y += B_vel
        elif i == 3:
            bullet.x -= B_vel
        i+= 1
        if i == 4:
            i = 0
def bullet_logic(player,ls_bullets):
    rand_dir2(ls_bullets)
    for bullet in ls_bullets:
        #collision handle
        if player.colliderect(bullet):
            pygame.event.post(pygame.event.Event(Player_hit))

        elif BOARD.contains(bullet):
            pass
        else:ls_bullets.remove(bullet)

def bullet_spawn(player,ls_bullets):
    while True:
        bullet = pygame.Rect(random.randint(0,WIDTH),random.randint(0,HEIGHT),10,10)
        if bullets_spawn_area(player,bullet):
            if len(ls_bullets) < TOTAL_BULLETS:
                ls_bullets.append(bullet)
            break

# To define where bullets can spawn
def bullets_spawn_area(player,bullet):
    circle = pygame.draw.circle(WIN,(0,0,0),(player.x,player.y),200,width = 0)
    if circle.contains(bullet):
        return False
    else: return True
'''
def save_db(score):
    with open('record.json','r',encoding ='utf-8') as f:
        try:
            data = json.load(f)
            if data['score'] > score:
                return data['score']
        except Exception as x:
            with open('record.json','w',encoding='utf-8') as g:
                json.dump({'Score':score},g)
                return score
'''

# --------------------Events HERE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!--------------
SPAWN_DELEAY = 100
SPAWN_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_EVENT,SPAWN_DELEAY)
#
Player_hit = pygame.USEREVENT + 2
Score_update = pygame.USEREVENT + 3
pygame.time.set_timer(Score_update,100)
#-----------
#---GAME_LOGIC---
def main():
    MAIN_MENU = True
    while MAIN_MENU:
        score = 0
        ls_bullets = []
        player = pygame.Rect(WIDTH//2,HEIGHT//2,20,20)

        GAME_FlAG = True
        while GAME_FlAG:
            clock.tick(FPS) # Setting 60 fps

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    GAME_FlAG,MAIN_MENU = False,False

                if event.type == SPAWN_EVENT:
                    bullet_spawn(player,ls_bullets)

                if event.type == Score_update:
                    score += 10

                if event.type == Player_hit:
                    # save_db(score)
                    # text_for_score = pygame.font.Font.render(comic_for_score,f'YOUR RECORD\n: {score}',1,(0,0,0))
                    # pygame.Surface.blit(WIN,text_for_score,(WIDTH//2,HEIGHT//2))
                    # while True:
                    #     if event.type == pygame.KEYDOWN:
                    #         break
                    GAME_FlAG = False

            key_pressed =  pygame.key.get_pressed()
            player_movement(key_pressed,player)
            bullet_logic(player,ls_bullets)

            #
            draw_win(player,ls_bullets,score)
            #

    pygame.quit()

if __name__ == '__main__':
    main()
