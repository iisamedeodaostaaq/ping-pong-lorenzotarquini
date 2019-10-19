xpos = 0 
ypos = 0
rax = 50

x_pos_rect_1 = 50
y_pos_rect_1 = 0 
x_pos_rect_2 = 50
y_pos_rect_2 = 375
b_height = 400;
b_width= 500;
x_dir = +7
y_dir = +7

def setup():
    global xpos,ypos,b_width,b_height
    background(18,3,255)
    size (b_width, b_height)

def keyPressed():
    global x_pos_rect_2,x_pos_rect_1
    
    if keyCode == LEFT:
        if(x_pos_rect_1 >= 2):
            x_pos_rect_1 -= 10
    elif keyCode == RIGHT:
        if(x_pos_rect_1 <= 400):
            x_pos_rect_1 += 10
    
        
    if key == 'a' or key == 'A':
        if(x_pos_rect_2 >= 2):
            x_pos_rect_2 -= 10
        print("1")
    elif key == 'd' or key == 'D':
        if(x_pos_rect_2 <= 400):
            x_pos_rect_2 += 10
            
def draw():
    global xpos,ypos,b_width,b_height,x_dir,y_dir
    
    background(18,3,255)
    fill(255,255,255)
    ellipse(xpos,ypos,rax,rax)
    rect(x_pos_rect_1,y_pos_rect_1,100,25)
    rect(x_pos_rect_2,y_pos_rect_2,100,25)
    
    xpos += x_dir
    ypos += y_dir
    
    if (xpos > width or xpos < 0):
        x_dir = x_dir * (-1)
        
    if (ypos > height or ypos < 0):
        y_dir = y_dir * (-1) 
         
    if rax == y_pos_rect_1 - 25:
        y_dir = y_dir * (-1) 
        fill(255,0,0)
        
        
    
