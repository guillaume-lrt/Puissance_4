# import pygame
#
# pygame.init()
# screen = pygame.display.set_mode((1000, 1000))
# clock = pygame.time.Clock()
# done = False
#
# font = pygame.font.SysFont("timesnewroman", 72)
#
# text_red = font.render("Red Won", True, (0, 0, 0))
#
# black = (0,0,0)
# white = (255,255,255)
#
# def button (msg, x, y, w, h, ic, ac, action=None ):
#     '''
#         x: x position of the left corner of the button
#         y: y position
#         w: width
#         h: height
#         ic: normal color
#         ac: color when the mouth is over
#     '''
#     mouse = pygame.mouse.get_pos()
#     click = pygame.mouse.get_pressed()
#
#     if (x+w > mouse[0] > x) and (y+h > mouse[1] > y):
#         pygame.draw.rect(screen, ac, (x, y, w, h))
#         if (click[0] == 1 and action != None):
#             if  (action == "Start"):
#                 print(1)
#                 game_loop()
#             elif  (action == "Load"):
#                  print(2)
#             elif  (action == "Exit"):
#                 pygame.quit()
#
#     else:
#         pygame.draw.rect(screen, ic, (x, y, w, h))
#         # smallText = pygame.font.Font("freesansbold.ttf", 20)
#         # textSurf, textRect = text_objects(msg, smallText)
#         # textRect.center = ( (x+(w/2)), (y+(h/2)) )
#         # screen.blit(textSurf, textRect)
# #
# while not done:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True
#         if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
#             done = True
#
#         button ("Start", 600, 120, 120, 25, black, white, "Start" )
#
#
#     # screen.fill((255, 255, 255))
#     # screen.blit(text_red,
#     #     (320 - text_red.get_width() // 2, 240 - text_red.get_height() // 2))
#
#     pygame.display.flip()
#     clock.tick(60)
#
#
# pygame.draw.rect()

dx = 0.1115

x_position = [round(0.117+dx*i,6)*1000 for i in range(7)]

interval = [(round(0.1+dx*i,6)*1000,round(0.16+dx*i,6)*1000) for i in range(7)]

print(x_position)
print(interval)


# deplacement
#
#        if event.type == pygame.KEYDOWN:
#            if event.key == pygame.K_LEFT:
#                x_change = -10
#            elif event.key == pygame.K_RIGHT:
#                x_change = 10
#        if event.type == pygame.KEYUP:
#            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
#                x_change = 0
#        if event.type == pygame.KEYDOWN:
#            if event.key == pygame.K_UP:
#                y_change = -4
#            elif event.key == pygame.K_DOWN:
#                y_change = 4
#        if event.type == pygame.KEYUP:
#            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
#                y_change = 0
