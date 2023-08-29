from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import numpy as np

angle = 0
fAspect = 0

xf = 0
rot = 0

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
    global rot
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 1.0)
    glPushMatrix()

    global rot, xf

    if xf > 0:
        rot += 10
    else:
        rot -= 10

    rotation_matrix_x = rotate_matrix('y', rot)

    glMultMatrixf(rotation_matrix_x)

    glutWireTeapot(50.0)

    glPopMatrix()
    glutSwapBuffers()

def EspecificaParametrosVisualizacao():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(angle, fAspect, 0.4, 800)
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

def GerenciaMouse(button, state, x, y):
    global xf, yf, rot

    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        xf = x - glutGet(GLUT_WINDOW_WIDTH) // 2
        print(xf)

    glutPostRedisplay()

    EspecificaParametrosVisualizacao()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(350, 300)
    glutCreateWindow("Visualizacao 3D")
    glutDisplayFunc(Desenha)
    glutReshapeFunc(AlteraTamanhoJanela)
    glutMouseFunc(GerenciaMouse)
    Inicializa()
    glutMainLoop()

main()
