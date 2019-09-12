from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
 
import math



   
cores = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5))
 
def piramideVariavel(h,n,r):
	
	
	vertices = [[0,h,0]]
	a = 2*math.pi/n
	for i in range(0,n):
		x = r*math.cos(i*a)
		y = 0
		z = r*math.sin(i*a)
		vertices += [[x,y,z]]

	faces = []
	for i in range(1,n+1):
		if(i==n):
			faces += [[0,i,1]]
		else:
			faces += [[0,i,(i+1)]]

	k = 0
	glBegin(GL_TRIANGLES)
	for face in faces:
		glColor3fv(cores[k%len(cores)])
		k += 1
		for v in face:
			glVertex3fv(vertices[v])
	glEnd()

	
	glBegin(GL_POLYGON)
	glColor3fv(cores[1])
	for v in range(1,n+1):
		glVertex3fv(vertices[v])
	glEnd()
 
def desenha():

    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    #glTranslatef(0,0,0)
    glRotatef(2,1,0,0);
    piramideVariavel(2,5,3)
    glutSwapBuffers()
    
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)
 
# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("CUBO")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-12)
#glRotatef(45,1,1,1)
glutTimerFunc(50,timer,1)
glutMainLoop()
