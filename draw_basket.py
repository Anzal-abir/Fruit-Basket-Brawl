#drawing the baskets
basket_fruits = [[], []]  # 2 indices for 2 players

def draw_basket(x, y, z, fruits):
    
    glColor3f(0.5, 0.3, 0.11)  
    glPushMatrix()
    glTranslatef(x, y, z)
    
    glBegin(GL_QUADS)
    glVertex3f(-40, -20, 0)
    glVertex3f(40, -20, 0)
    glVertex3f(40, 20, 0)
    glVertex3f(-40, 20, 0)
    glEnd()
    
    glBegin(GL_QUADS)
    
    glVertex3f(-40, -20, 0)
    glVertex3f(-40, -20, 30)
    glVertex3f(-40, 20, 30)
    glVertex3f(-40, 20, 0)
    
    glVertex3f(40, -20, 0)
    glVertex3f(40, -20, 30)
    glVertex3f(40, 20, 30)
    glVertex3f(40, 20, 0)
    
    glVertex3f(-40, 20, 0)
    glVertex3f(-40, 20, 30)
    glVertex3f(40, 20, 30)
    glVertex3f(40, 20, 0)
    
    glVertex3f(-40, -20, 0)
    glVertex3f(-40, -20, 30)
    glVertex3f(40, -20, 30)
    glVertex3f(40, -20, 0)
    glEnd()
    

    handle_color = (0.55, 0.35, 0.22)  

    
    side_w = 4
    side_h = 30
    side_z0 = 30
    side_z1 = side_z0 + side_h
    side_y = 18  

    # Left Handle 
    glColor3f(*handle_color)
    glBegin(GL_QUADS)
    glVertex3f(-40, side_y - side_w//2, side_z0)
    glVertex3f(-40, side_y + side_w//2, side_z0)
    glVertex3f(-40, side_y + side_w//2, side_z1)
    glVertex3f(-40, side_y - side_w//2, side_z1)
    glEnd()

    # Right Handle
    glBegin(GL_QUADS)
    glVertex3f(40, side_y - side_w//2, side_z0)
    glVertex3f(40, side_y + side_w//2, side_z0)
    glVertex3f(40, side_y + side_w//2, side_z1)
    glVertex3f(40, side_y - side_w//2, side_z1)
    glEnd()

    # Top Bridge 
    bridge_len = 80 
    bridge_w = 4
    bridge_z = side_z1
    glBegin(GL_QUADS)
    glVertex3f(-40, side_y - bridge_w//2, bridge_z)
    glVertex3f(40, side_y - bridge_w//2, bridge_z)
    glVertex3f(40, side_y + bridge_w//2, bridge_z)
    glVertex3f(-40, side_y + bridge_w//2, bridge_z)
    glEnd()
