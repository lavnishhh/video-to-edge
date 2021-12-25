import cv2
import numpy

vid = cv2.VideoCapture(0)         #-------->Camera/Video file plus. change 0 to 'C:/...' directory for file mode
render_resolution=300             #-------->Video resolution
vid.set(3,render_resolution)
vid.set(2,(render_resolution/4)*3)

ret, frame = vid.read()
img = numpy.ones([frame.shape[0],frame.shape[1]])
while(True):
        ret, frame = vid.read()
        frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('vid',frame)
        for a in range(1,len(frame)-1):
                for b in range(1,frame.shape[1]-1):
                        img[a][b]= frame[a][b-1]- 2*frame[a][b] + frame[a][b+1] + frame[a-1][b]- 2*frame[a][b] + frame[a+1][b+1]
        cv2.imshow('frame', numpy.absolute(img/255.0))
        if cv2.waitKey(1) & 0xFF == ord('q'):
                break
vid.release()
cv2.destroyAllWindows()
