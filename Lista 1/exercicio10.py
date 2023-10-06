from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

angle = 0
fAspect = 0
rot_teapot = 0

def Desenha():
    global rot_teapot
    glClear(GL_COLOR_BUFFER_BIT)
    
    glPushMatrix()
    glColor3f(1.0,0.0,0.0)
    glRotate(rot_teapot, 0.0, 1.0, 0.0)
    glutWireTeapot(50.0)
    glPopMatrix()
    
    glPushMatrix()
    glRotate(rot_teapot, 0.0, 1.0, 0.0)
    glTranslate(0, 150, 20)
    glColor3f(1.0,1.0,1.0)
    glutWireTeapot(50.0)
    glPopMatrix()
    
    glPushMatrix()
    glRotate(rot_teapot, 0.0, 1.0, 0.0)
    glTranslate(300, -150, 20)
    glColor3f(0.5,1.0,0.5)
    glutWireTeapot(50.0)
    glPopMatrix()
    
    glPushMatrix()
    glRotate(rot_teapot, 0.0, 1.0, 0.0)
    glTranslate(300, 0, 30)
    glColor3f(1.0,1.0,0.0)
    glutWireCube(50.0)
    glPopMatrix()
    
    glPushMatrix()
    glRotate(rot_teapot, 0.0, 1.0, 0.0)
    glTranslate(-300, 0, 30)
    glColor3f(0.0,1.0,1.0)
    glutWireSphere(50.0, 10, 20)
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

def Timer(value):
    global rot_teapot
    
    rot_teapot += 1  
    
    glutPostRedisplay()
    glutTimerFunc(30, Timer, 0)  # Configura o próximo intervalo de atualização

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
