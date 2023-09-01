from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

angle = 0
fAspect = 0

rot_teapot1 = 0
rot_teapot2 = 0
rot_teapot2_center = 0

def Desenha():
    global rot_teapot1, rot_teapot2, rot_teapot2_center
    
    glClear(GL_COLOR_BUFFER_BIT)
    
    glPushMatrix()
    glColor3f(1.0,0.0,0.0)
    glRotate(rot_teapot1, 0.0, 1.0, 0.0)
    glutWireTeapot(50.0)
    glPopMatrix()
    
    glPushMatrix()
    glRotate(rot_teapot2_center, 0.0, 1.0, 0.0)
    glTranslate(150, 0, 100)
    glColor3f(1.0,1.0,0.0)
    glutWireTeapot(50.0)
    glPopMatrix()
    
    glutSwapBuffers()

def Timer(value):
    global rot_teapot1, rot_teapot2, rot_teapot2_center
    
    rot_teapot1 += 1  # Incrementa a rotação do primeiro teapot
    rot_teapot2_center += 0.5  # Incrementa a rotação do segundo teapot em torno do primeiro
    rot_teapot2 += 2  # Incrementa a rotação do segundo teapot
    
    glutPostRedisplay()
    glutTimerFunc(30, Timer, 0)  # Configura o próximo intervalo de atualização

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

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(700, 500)
    glutCreateWindow("Visualizacao 3D")
    glutDisplayFunc(Desenha)
    glutReshapeFunc(AlteraTamanhoJanela)
    glutTimerFunc(30, Timer, 0)  # Configura o primeiro intervalo de atualização
    Inicializa()
    glutMainLoop()
 
main()
