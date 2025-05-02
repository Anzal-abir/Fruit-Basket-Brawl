    # Fruit inside basket
    for i, fruit in enumerate(fruits):
        glPushMatrix()
        glTranslatef(-25 + (i%4)*16, -5 + (i//4)*18, 35)
        draw_fruit(fruit)
        glPopMatrix()
    glPopMatrix()