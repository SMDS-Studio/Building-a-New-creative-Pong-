import pygame 

pygame.init()

width, height = 1000, 600
wn = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong_But_Better")
run = True

#colours
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


#for the ball
radius = 15
ball_x, ball_y = width/2 - radius, height/2 - radius
vel_x, vel_y = 0.5, 0.5

#for the paddles
paddle_width, paddle_height = 20, 120
paddle_y = paddle_y1 = height/2 - paddle_height/2
paddle_x, paddle_X = 100 - paddle_width/2, width - (100 - paddle_width/2)
paddle_vel = paddle_vel1= 0

#for the gadgets
gad = act = 0 
g_left = G_left = 3
while run:
    wn.fill(BLACK)

    #for the inputs
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_UP:
                paddle_vel = -0.7
            if i.key == pygame.K_DOWN:
                paddle_vel = 0.7
            if i.key == pygame.K_w:
                paddle_vel1 = -0.7
            if i.key == pygame.K_s:
                paddle_vel1 = 0.7
            if i.key == pygame.K_RIGHT and g_left > 0:
                gad = 1
            if i.key == pygame.K_d and G_left > 0 :
                act = 1
            
        elif i.type == pygame.KEYUP:
            paddle_vel = 0 
            paddle_vel1 = 0 

    #ball's movement controls            
    if (ball_y <= 0 + radius) or (ball_y >= height - radius):
        vel_y *= -1
    if (ball_x >= width - radius):
        ball_x, ball_y = width/2 - radius, height/2 - radius
        vel_x, vel_y = 0.5, 0.5
        vel_x *= -1
    if (ball_x <= 0 + radius):
        ball_x, ball_y = width/2 - radius, height/2 - radius
        vel_x, vel_y = 0.5, 0.5 

    #paddle's movement controls
    if paddle_y >= height - paddle_height:
        paddle_y = height - paddle_height
    if paddle_y <= 0:
        paddle_y = 0
    if paddle_y1 >= height - paddle_height:
        paddle_y1 = height - paddle_height
    if paddle_y1 <= 0:
        paddle_y1 = 0

    if paddle_X <= ball_x <= paddle_X + paddle_width:
        if paddle_y <= ball_y <= paddle_y + paddle_height:
            ball_x = paddle_X
            vel_x *= -1
    
    if paddle_x <= ball_x <= paddle_x + paddle_width:
        if paddle_y1 <= ball_y <= paddle_y1 + paddle_height:
            ball_x = paddle_x + paddle_width
            vel_x *= -1  

    #gadget movement controls 
    if gad == 1:
        if paddle_X <= ball_x <= paddle_X + paddle_width:
            if paddle_y <= ball_y <= paddle_y + paddle_height:
                ball_x = paddle_X
                vel_x *= -3.5
                gad = 0 

    if act == 1:
        if paddle_x <= ball_x <= paddle_x + paddle_width:
            if paddle_y1 <= ball_y <= paddle_y1 + paddle_height:
                ball_x = paddle_x + paddle_width
                vel_x *= -3.5
                act = 0  
    
    #raw movements
    paddle_y += paddle_vel
    paddle_y1 += paddle_vel1
    ball_x += vel_x
    ball_y += vel_y
 
    #drawings
    pygame.draw.circle(wn, BLUE, (ball_x, ball_y), radius)
    pygame.draw.rect(wn, RED, pygame.Rect(paddle_x, paddle_y1, paddle_width, paddle_height))
    pygame.draw.rect(wn, RED, pygame.Rect(paddle_X, paddle_y, paddle_width, paddle_height))
    if gad == 1:
        pygame.draw.circle(wn, WHITE, (paddle_X + 10, paddle_y + 10), 4)
    if act == 1:
        pygame.draw.circle(wn, WHITE, (paddle_x + 10, paddle_y1 + 10), 4)

    pygame.display.update()


