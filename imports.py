import pygame
import params

blockImage = pygame.image.load('red.png')
activatorImage = pygame.image.load('empty.png')
firstDialog = pygame.image.load('dialoge 1.png')
secondDialog = pygame.image.load('dialoge 2.png')

room1 = pygame.image.load('DoorRooms/dveri_1.png')
room1_scaled = pygame.transform.scale(room1, (params.WIDTH, params.HEIGHT))
room1_scaled_rect = room1_scaled.get_rect()

room2 = pygame.image.load('DoorRooms/dveri_2.png')
room2_scaled = pygame.transform.scale(room2, (params.WIDTH, params.HEIGHT))
room2_scaled_rect = room2_scaled.get_rect()

room3 = pygame.image.load('DoorRooms/dveri_3.png')
room3_scaled = pygame.transform.scale(room3, (params.WIDTH, params.HEIGHT))
room3_scaled_rect = room3_scaled.get_rect()

room4 = pygame.image.load('DoorRooms/dveri_4.png')
room4_scaled = pygame.transform.scale(room4, (params.WIDTH, params.HEIGHT))
room4_scaled_rect = room4_scaled.get_rect()

room5 = pygame.image.load('DoorRooms/dveri_5.png')
room5_scaled = pygame.transform.scale(room5, (params.WIDTH, params.HEIGHT))
room5_scaled_rect = room5_scaled.get_rect()

room6 = pygame.image.load('DoorRooms/dveri_6.png')
room6_scaled = pygame.transform.scale(room6, (params.WIDTH, params.HEIGHT))
room6_scaled_rect = room6_scaled.get_rect()

room7 = pygame.image.load('DoorRooms/dveri_7.png')
room7_scaled = pygame.transform.scale(room7, (params.WIDTH, params.HEIGHT))
room7_scaled_rect = room7_scaled.get_rect()

room8 = pygame.image.load('DoorRooms/dveri_8.png')
room8_scaled = pygame.transform.scale(room8, (params.WIDTH, params.HEIGHT))
room8_scaled_rect = room8_scaled.get_rect()

room9 = pygame.image.load('DoorRooms/dveri_9.png')
room9_scaled = pygame.transform.scale(room9, (params.WIDTH, params.HEIGHT))
room9_scaled_rect = room9_scaled.get_rect()

street = pygame.image.load('Street.png')
street_scaled = pygame.transform.scale(street, (params.WIDTH, params.HEIGHT))
street_scaled_rect = street_scaled.get_rect()

workRoom = pygame.image.load('workRoom.png')
workRoom_scaled = pygame.transform.scale(workRoom, (params.WIDTH, params.HEIGHT))
workRoom_scaled_rect = workRoom_scaled.get_rect()

computerRoom = pygame.image.load('computerRoom.png')
computerRoom_scaled = pygame.transform.scale(computerRoom, (params.WIDTH, params.HEIGHT))
computerRoom_scaled_rect = computerRoom_scaled.get_rect()

labirint = pygame.image.load('labirint.png')
labirint_scaled = pygame.transform.scale(labirint, (params.WIDTH, params.HEIGHT))
labirint_scaled_rect = labirint_scaled.get_rect()

start_room = pygame.image.load('home.png')
start_room_scaled = pygame.transform.scale(start_room, (params.WIDTH, params.HEIGHT))
start_room_scaled_rect = start_room_scaled.get_rect()

womanNPC = pygame.image.load('NPC 1.png')
womanNPC_scaled = pygame.transform.scale(womanNPC, (params.WIDTH/24, params.HEIGHT/16))
womanNPC_scaled_rect = womanNPC_scaled.get_rect()

player_image_right1 = pygame.image.load("player/bock1.png")
player_image_right1 = pygame.transform.scale(player_image_right1, (params.WIDTH/24, params.HEIGHT/16))
player_image_right1.set_colorkey(params.BLACK)

player_image_right2 = pygame.image.load("player/bock2.png")
player_image_right2 = pygame.transform.scale(player_image_right2, (params.WIDTH/24, params.HEIGHT/16))
player_image_right2.set_colorkey(params.BLACK)

walkRight = [player_image_right1, player_image_right2]

player_image_left1 = pygame.image.load("player/bock11.png")
player_image_left1 = pygame.transform.scale(player_image_left1, (params.WIDTH/24, params.HEIGHT/16))
player_image_left1.set_colorkey(params.BLACK)

player_image_left2 = pygame.image.load("player/bock22.png")
player_image_left2 = pygame.transform.scale(player_image_left2, (params.WIDTH/24, params.HEIGHT/16))
player_image_left2.set_colorkey(params.BLACK)

walkLeft = [player_image_left1, player_image_left2]

player_image_up1 = pygame.image.load("player/iss1_1back1.png")
player_image_up1 = pygame.transform.scale(player_image_up1, (params.WIDTH/24, params.HEIGHT/16))
player_image_up1.set_colorkey(params.BLACK)

player_image_up2 = pygame.image.load("player/iss1_1back2.png")
player_image_up2 = pygame.transform.scale(player_image_up2, (params.WIDTH/24, params.HEIGHT/16))
player_image_up2.set_colorkey(params.BLACK)

player_image_up3 = pygame.image.load("player/iss1_1back4.png")
player_image_up3 = pygame.transform.scale(player_image_up3, (params.WIDTH/24, params.HEIGHT/16))
player_image_up3.set_colorkey(params.BLACK)

walkUp = [player_image_up1, player_image_up2, player_image_up3]

player_image_down1 = pygame.image.load("player/iss1.png")
player_image_down1 = pygame.transform.scale(player_image_down1, (params.WIDTH/24, params.HEIGHT/16))
player_image_down1.set_colorkey(params.BLACK)

player_image_down2 = pygame.image.load("player/iss2.png")
player_image_down2 = pygame.transform.scale(player_image_down2, (params.WIDTH/24, params.HEIGHT/16))
player_image_down2.set_colorkey(params.BLACK)

player_image_down3 = pygame.image.load("player/iss4.png")
player_image_down3 = pygame.transform.scale(player_image_down3, (params.WIDTH/24, params.HEIGHT/16))
player_image_down3.set_colorkey(params.BLACK)

walkDown = [player_image_down1, player_image_down2, player_image_down3]