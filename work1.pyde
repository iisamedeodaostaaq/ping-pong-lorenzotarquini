xpos = 0 
ypos = 0
rax = 50
i = 0
up_score = 0
down_score = 0
x_pos_rect_1 = 50
y_pos_rect_1 = 0 
x_pos_rect_2 = 50
y_pos_rect_2 = 375
b_height = 400;
b_width= 500;
x_dir = +3
y_dir = +3

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
            
    if key == 'e' or key == 'E':
        exit()
            

def draw():
    global xpos,ypos,b_width,b_height,x_dir,y_dir,i,up_score,down_score
    
    background(18,3,255)
    fill(255,255,255)
    ellipse(xpos,ypos,rax,rax)
    rect(x_pos_rect_1,y_pos_rect_1,100,25)
    rect(x_pos_rect_2,y_pos_rect_2,100,25)
    text(up_score,230,200)
    text(down_score,230,220)
    xpos += x_dir
    ypos += y_dir
    
    if (xpos > width or xpos < 0):
        x_dir = x_dir * (-1)
        
    if ypos > height:
        y_dir = y_dir * (-1) 
        up_score +=1
    elif ypos < 0:
        y_dir = y_dir * (-1) 
        down_score +=1
   
    if down_score == 20:
        clear()
        noLoop()
        textSize(26)
        text("Player Down has won! Press e for exit",230,200)
    
    elif up_score == 20:
        clear ()
        noLoop()
        textSize(20)
        text("Player Up has won! Press e for exit",100,200) 
    
    if (ypos < 25) and (xpos+25)>x_pos_rect_1 and (xpos-25)<(x_pos_rect_1):
        y_dir = +3  
                
    if (ypos > b_height-25) and (xpos+25)>x_pos_rect_2 and (xpos-25)<(x_pos_rect_2+100):
        y_dir = -3


 

        

    
