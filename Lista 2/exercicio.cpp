#include <GL/freeglut.h>
#include <iostream>

#define LAR 400
#define ALT 400

#define MAIORX_BEZIER 400.0f
#define MENORX_BEZIER 0.0f
#define MAIORY_BEZIER 400.0f
#define MENORY_BEZIER 0.0f

#define MAIORX 200.0f
#define MENORX -200.0f
#define MAIORY 200.0f
#define MENORY -200.0f

#define POSWX 250
#define POSWY 150

#define tang1x 10.0f
#define tang1y -145.0f
#define tang2x 10.0f
#define tang2y -185.0f

GLfloat B[4][2];

GLfloat P[2][4];

GLboolean GET_POINTS = 0;

GLint TOTAL_POINTS = 0;

GLfloat bx, by;

GLfloat angle, fAspect, rot = 0;

GLfloat angleX = 0, angleY = 0;

GLfloat dx = 0, dy = 0, dz = 0;

void myMousefuncBezierHermitInterate(int button, int state, int x, int y) {

	switch (button) {
	case GLUT_LEFT_BUTTON: {
		bx = x - (LAR / 2);
		by = (ALT / 2) - y;
		GET_POINTS = 1;
		break;
	}
	case GLUT_RIGHT_BUTTON: {
		GET_POINTS = 0;
		TOTAL_POINTS = 0;
		break;
	}
	case GLUT_MIDDLE_BUTTON: {
		break;
	}
	}

	std::cout << bx << " " << by << std::endl;

	glutPostRedisplay();

}

GLfloat multiplyHermite(GLfloat T[], GLfloat H[][4], GLfloat M[])
{

	GLfloat HM[4];

	for (int i = 0; i < 4; i++)
	{
		HM[i] = 0;
		for (int j = 0; j < 4; j++)
		{
			HM[i] = HM[i] + H[i][j] * M[j];
		}
	}

	GLfloat R = 0;
	for (int i = 0; i < 4; i++)
	{
		R = R + T[i] * HM[i];
	}

	return R;
}


void DesenhaHermiteGrau3() {

	GLfloat H[4][4] = {
		{2.0f, -2.0f, 1.0f, 1.0f},
		{-3.0f, 3.0f, -2.0f, -1.0f},
		{0.0f, 0.0f, 1.0f, 0.0f},
		{1.0f, 0.0f, 0.0f, 0.0f}
	};

	if ((TOTAL_POINTS == 0) && (GET_POINTS)) {
		P[0][0] = bx;
		P[0][1] = by;
		P[0][2] = tang1x;
		P[0][3] = tang1y;
		TOTAL_POINTS += 1;
	}
	if ((TOTAL_POINTS > 0) && (GET_POINTS) && (TOTAL_POINTS < 2)) {

		if ((P[TOTAL_POINTS - 1][0] != bx) && (P[TOTAL_POINTS - 1][1] != by)) {
			P[TOTAL_POINTS][0] = bx;
			P[TOTAL_POINTS][1] = by;
			P[TOTAL_POINTS][2] = tang2x;
			P[TOTAL_POINTS][3] = tang2y;
			TOTAL_POINTS += 1;
			if (TOTAL_POINTS > 2) TOTAL_POINTS = 2;
		}
	}

	glColor3f(1.0f, 0.0f, 0.0f);
	glPointSize(5.0f);
	for (int i = 0; i < TOTAL_POINTS; i++) {
		glBegin(GL_POINTS);
		glVertex2f(P[i][0], P[i][1]);
		glEnd();
	}

	GLfloat T[4];
	GLfloat M[4];

	if (TOTAL_POINTS == 2) {
		GLfloat xini, yini, xfin, yfin;

		float t = 0.0;
		float passo = 0.01;

		xini = P[0][0] * (2 * pow(t, 3) - 3 * pow(t, 2) + 1) + P[1][0] * (-2 * pow(t, 3) + 3 * pow(t, 2)) + P[0][2] * (pow(t, 3) - 2 * pow(t, 2) + t) + P[1][2] * (pow(t, 3) - pow(t, 2));
		yini = P[0][1] * (2 * pow(t, 3) - 3 * pow(t, 2) + 1) + P[1][1] * (-2 * pow(t, 3) + 3 * pow(t, 2)) + P[0][3] * (pow(t, 3) - 2 * pow(t, 2) + t) + P[1][3] * (pow(t, 3) - pow(t, 2));

		for (float t = 0.0 + passo; t <= 1.0; t += passo) {

			xfin = P[0][0] * (2 * pow(t, 3) - 3 * pow(t, 2) + 1) + P[1][0] * (-2 * pow(t, 3) + 3 * pow(t, 2)) + P[0][2] * (pow(t, 3) - 2 * pow(t, 2) + t) + P[1][2] * (pow(t, 3) - pow(t, 2));
			yfin = P[0][1] * (2 * pow(t, 3) - 3 * pow(t, 2) + 1) + P[1][1] * (-2 * pow(t, 3) + 3 * pow(t, 2)) + P[0][3] * (pow(t, 3) - 2 * pow(t, 2) + t) + P[1][3] * (pow(t, 3) - pow(t, 2));

			glBegin(GL_LINE_STRIP);
			glVertex2f(xini, yini);
			glVertex2f(xfin, yfin);
			glEnd();

			xini = xfin;
			yini = yfin;

		}

	}

	std::cout << "TOTAL POINTS: " << TOTAL_POINTS << std::endl;

}


void DesenhaBezierGrau3()
{
	const GLint DIMX = MENORX_BEZIER + MAIORX_BEZIER + 1;
	const GLint DIMY = MENORY_BEZIER + MAIORY_BEZIER + 1;

	GLfloat H[4][4] = { {-1.0f, 3.0f, -3.0f, 1.0f},
					   {3.0f, -6.0f, 3.0f, 0.0f},
					   {-3.0f, 3.0f, 0.0f, 0.0f},
					   {1.0f, 0.0f, 0.0f, 0.0f} };

	if ((TOTAL_POINTS == 0) && (GET_POINTS))
	{
		B[0][0] = bx; 
		B[0][1] = by; 
		TOTAL_POINTS = TOTAL_POINTS + 1;
	}

	if ((TOTAL_POINTS > 0) && (GET_POINTS) && (TOTAL_POINTS < 4))
	{
		if ((B[TOTAL_POINTS - 1][0] != bx) && (B[TOTAL_POINTS - 1][1] != by))
		{
			B[TOTAL_POINTS][0] = bx;
			B[TOTAL_POINTS][1] = by;
			TOTAL_POINTS = TOTAL_POINTS + 1;
			if (TOTAL_POINTS > 4)
				TOTAL_POINTS = 4;
		}
	}

	glColor3f(1.0, 0.0f, 0.0f);
	glPointSize(5.0f);
	for (int i = 0; i < TOTAL_POINTS; i++)
	{
		glBegin(GL_POINTS);
		glVertex2f(B[i][0], B[i][1]);
		glEnd();
	}

	if (TOTAL_POINTS == 4)
	{
		GLfloat t = 0.00f;
		GLfloat M[4][4] = {
			{
			 B[0][0],
			 B[1][0],
			 B[2][0],
			 B[3][0]},
			{
			 B[0][1],
			 B[1][1],
			 B[2][1],
			 B[3][1]} };

		GLfloat P[100][2];

		for (int i = 0; t < 1.0; t += 0.01, i++)
		{
			GLfloat T[4] = { t * t * t, t * t, t, 1 };

			P[i][0] = multiplyHermite(T, H, M[0]);
			P[i][1] = multiplyHermite(T, H, M[1]);
		}


		for (int i = 1; i < 100; i++)
		{
			glBegin(GL_LINE_STRIP);
			glVertex2f(P[i - 1][0], P[i - 1][1]);
			glVertex2f(P[i][0], P[i][1]);
			glEnd();
		}
	}
}


void DesenhaCurvaHermiteBezier() {
	glClear(GL_COLOR_BUFFER_BIT);

	DesenhaHermiteGrau3();

	glFlush();
}

void EspecificaParametrosVisualizacao(void)
{
	glMatrixMode(GL_PROJECTION);
	
	glLoadIdentity();

	gluPerspective(angle, fAspect, 0.1, 500);

	glMatrixMode(GL_MODELVIEW);

	glLoadIdentity();

	gluLookAt(0, 0, 200, 0, 0, 0, 0, 1, 0);
}

void AlteraTamanhoJanela(GLsizei w, GLsizei h)
{
	GLfloat largura, altura;

	if (h == 0)
		h = 1;

	largura = w;
	altura = h;
	glViewport(0, 0, largura, altura);

	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();

	if (largura <= altura)
		gluOrtho2D(MENORX, MAIORX, MENORY * altura / largura, MAIORY * altura / largura);
	//gluOrtho2D(MENORX_BEZIER, MAIORX_BEZIER, MENORY_BEZIER * altura / largura, MAIORY_BEZIER * altura / largura);
	else
		gluOrtho2D(MENORX * largura / altura, MAIORX * largura / altura, MENORY, MAIORY);
	//gluOrtho2D(MENORX_BEZIER * largura / altura, MAIORX_BEZIER * largura / altura, MENORY_BEZIER, MAIORY_BEZIER);
}

void Inicializa(void)
{
	glClearColor(1.0f, 1.0f, 1.0f, 1.0f);
}

int main(int argc, char* argv[]) {

	glutInit(&argc, argv);

	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);

	glutInitWindowPosition(POSWX, POSWY);

	glutInitWindowSize(LAR, ALT);

	glutCreateWindow("Curvas");

	glutDisplayFunc(DesenhaCurvaHermiteBezier);

	glutReshapeFunc(AlteraTamanhoJanela);

	glutMouseFunc(myMousefuncBezierHermitInterate);

	Inicializa();

	glutMainLoop();

}