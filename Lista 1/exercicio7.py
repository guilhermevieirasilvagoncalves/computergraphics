from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math 
import numpy as np

angle = 0
fAspect = 0

def rotate_matrix(axis, angle):
    radians = math.radians(angle)
    if axis == 'x':
        return np.array([[1, 0, 0, 0],
                         [0, math.cos(radians), -math.sin(radians), 0],
                         [0, math.sin(radians), math.cos(radians), 0],
                         [0, 0, 0, 1]])
    elif axis == 'y':
        return np.array([[math.cos(radians), 0, math.sin(radians), 0],
                         [0, 1, 0, 0],
                         [-math.sin(radians), 0, math.cos(radians), 0],
                         [0, 0, 0, 1]])
    elif axis == 'z':
        return np.array([[math.cos(radians), -math.sin(radians), 0, 0],
                         [math.sin(radians), math.cos(radians), 0, 0],
                         [0, 0, 1, 0],
                         [0, 0, 0, 1]])

def Desenha():
    glClear(GL_COLOR_BUFFER_BIT)
    
    glPushMatrix()
    glColor3f(1.0,0.0,0.0)
    rotation_matrix_y = rotate_matrix('z', 70)
    glMultMatrixf(rotation_matrix_y)
    glutWireTeapot(50.0)
    glPopMatrix()
    
    glPushMatrix()
    glTranslate(150, 0, 0)
    glColor3f(1.0,0.0,0.0)
    rotation_matrix_y = rotate_matrix('z', 35)
    glMultMatrixf(rotation_matrix_y)
    glMultMatrixf(rotation_matrix_y)
    glutWireTeapot(50.0)
    glPopMatrix()
    
    glutSwapBuffers()

def EspecificaParametrosVisualizacao():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(angle, fAspect, 0.4, 1000)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, 0, 800, 0, 0, 0, 0, 1, 0)
    
def Inicializa():
    global angle
    glClearColor(0.0, 0.0, 0.0, 1.0)
    angle = 45

def AlteraTamanhoJanela(w, h):
    if h == 0:
        h = 1
    glViewport(0, 0, w, h)
    global fAspect
    fAspect = w / h
    EspecificaParametrosVisualizacao()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(700, 500)
    glutCreateWindow("Visualizacao 3D")
    glutDisplayFunc(Desenha)
    glutReshapeFunc(AlteraTamanhoJanela)
    Inicializa()
    glutMainLoop()
 
main()
