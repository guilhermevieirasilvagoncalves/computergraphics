from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

angle = 0
fAspect = 0

xf = 0
yf = 0

def Desenha():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 1.0)
    glPushMatrix()
    glTranslatef(xf,yf,0.0)
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
    global angle;
    glClearColor(0.0, 0.0, 0.0, 1.0)
    angle = 45


def AlteraTamanhoJanela(w, h):
    if h == 0:
        h = 1
    glViewport(0, 0, w, h)
    global fAspect
    fAspect = w / h
    EspecificaParametrosVisualizacao()

# def GerenciaTeclado(key, x,y):
#     global angle
#     if key == b'w':
#         if angle >= 10:
#                 angle -= 5
#     if key == b's':
#         if angle <= 130:
#                 angle += 5
#     glutPostRedisplay()            
        

def GerenciaMouse(button, state, x, y):
    global xf,yf

    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        xf = x - glutGet(GLUT_WINDOW_WIDTH) // 2
        yf = glutGet(GLUT_WINDOW_HEIGHT) // 2 - y
        
    EspecificaParametrosVisualizacao()
    glutPostRedisplay()
    

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(350, 300)
    glutCreateWindow("Visualizacao 3D")
    glutDisplayFunc(Desenha)
    glutReshapeFunc(AlteraTamanhoJanela)
    # glutKeyboardFunc(GerenciaTeclado)
    glutMouseFunc(GerenciaMouse)
    Inicializa()
    glutMainLoop()
 
main()