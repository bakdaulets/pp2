import pygame 

pygame.init()
songs = ['C:\\Users\\baha\\Desktop\\code\\py\\lab7\\misic_player\\Drake_Kyla_Wizkid-One_Dance.mp3','C:\\Users\\baha\\Desktop\\code\\py\\lab7\\misic_player\\JID-Surround_Sound_feat_21_Savage_Baby_Tate.mp3','C:\\Users\\baha\\Desktop\\code\\py\\lab7\\misic_player\V_X_V_PRINCE_De_lacure-Big_City_Life.mp3']
curently = None
next_song = 0

def play_music(next_song):
    global curently
    if next_song >= len(songs):
        next_song = 0
    elif next_song < -len(songs):
        next_song = len(songs) - 1
    while next_song == curently:
        next_song += 1
    curently = next_song
    pygame.mixer.music.load(songs[next_song])
    pygame.mixer.music.play()

play_music(next_song)
flag_pause = True
screen = pygame.display.set_mode((255, 135))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                next_song -= 1
                play_music(next_song)
            elif event.key == pygame.K_RIGHT:
                next_song += 1
                play_music(next_song)
            elif event.key == pygame.K_SPACE and flag_pause == True:
                flag_pause = False
                pygame.mixer.music.pause()
            elif event.key == pygame.K_SPACE and flag_pause == False:
                flag_pause = True
                pygame.mixer.music.unpause()