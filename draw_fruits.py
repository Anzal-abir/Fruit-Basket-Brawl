#drawing the four fruits
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import time
from math import sin, cos, pi
paused = False

def draw_apple():
    glColor3f(*FRUIT_COLORS['apple'])
    quad = gluNewQuadric()
    gluSphere(quad, 18,16,16)
    glColor3f(0.4, 0.2, 0)
    glPushMatrix()
    glTranslatef(0, 0, 22)
    gluCylinder(gluNewQuadric(), 2, 1, 7, 10, 10)
    glPopMatrix()

def draw_orange():
    glColor3f(*FRUIT_COLORS['orange'])
    quad = gluNewQuadric()
    gluSphere(quad, 18,16,16)
    glColor3f(0.8, 0.7, 0.2)
    glPushMatrix()
    glTranslatef(0, 0, 18)
    quad = gluNewQuadric()
    gluSphere(quad, 3,10,10)
    glPopMatrix()

def draw_guava():
    glColor3f(*FRUIT_COLORS['guava'])
    quad = gluNewQuadric()
    gluSphere(quad, 17,16,16)
    
    glColor3f(1.0, 0.7, 0.8)
    glPushMatrix()
    glTranslatef(0, 0, 5)
    quad = gluNewQuadric()
    gluSphere(quad, 8,12,12)
    glPopMatrix()
    
    glColor3f(0.5, 0.8, 0.3)
    glPushMatrix()
    glTranslatef(0, 0, 18)
    gluCylinder(gluNewQuadric(), 2, 1, 7, 10, 10)
    glPopMatrix()


def draw_pomegranate():
    glColor3f(*FRUIT_COLORS['pomegranate'])
    quad = gluNewQuadric()
    gluSphere(quad, 16,16,16)
    glColor3f(1, 0.2, 0.4)
    glPushMatrix()
    glTranslatef(0, 0, 18)
    glutSolidCone(4, 8, 10, 10)
    base_radius = 4
    height = 8
    slices = 12
    tip = (0, 0, height)
    glBegin(GL_LINES)
    for i in range(slices):
        angle1 = 2 * pi * i / slices
        angle2 = 2 * pi * (i+1) / slices
        x1 = base_radius * cos(angle1)
        y1 = base_radius * sin(angle1)
        z1 = 0
        
        glVertex3f(x1, y1, z1)
        glVertex3f(*tip)
        
        x2 = base_radius * cos(angle2)
        y2 = base_radius * sin(angle2)
        glVertex3f(x1, y1, z1)
        glVertex3f(x2, y2, z1)
    glEnd()
    glPopMatrix()

def draw_fruit(fruit_type):
    if fruit_type == 'apple':
        draw_apple()
    elif fruit_type == 'orange':
        draw_orange()
    elif fruit_type == 'guava':
        draw_guava()
    elif fruit_type == 'pomegranate':
        draw_pomegranate()