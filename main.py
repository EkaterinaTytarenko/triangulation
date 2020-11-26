import triangulation
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.widgets import Button
import input

def draw_function(d,button_text):
    plt.clf()
    ax = fig.add_subplot(111, projection='3d')
    VecStart_x = []
    VecStart_y = []
    VecStart_z = []
    VecEnd_x = []
    VecEnd_y = []
    VecEnd_z = []
    count=0;
    for hedge in d.hedgeList:
        if(hedge.incidentFace.identifier!='i' and hedge.next is not None ):
            VecStart_x.append(hedge.origin.x)
            VecEnd_x.append(hedge.next.origin.x)
            VecStart_y.append(hedge.origin.y)
            VecEnd_y.append(hedge.next.origin.y)
            VecStart_z.append(hedge.origin.z)
            VecEnd_z.append(hedge.next.origin.z)
            count=count+1
    for i in range(count):
        ax.plot([VecStart_x[i], VecEnd_x[i]], [VecStart_y[i], VecEnd_y[i]],'k', zs=[VecStart_z[i], VecEnd_z[i]])

    axclear = plt.axes([0.7, 0.05, 0.1, 0.075])
    bclear = Button(axclear, 'Clear')
    axtrian = plt.axes([0.81, 0.05, 0.15, 0.075])
    btrian = Button(axtrian, 'Triangulate')
    ax_button = plt.axes([0.05, 0.05, 0.25, 0.075])
    button = Button(ax_button, button_text)
    if button_text == 'See one-face example':
        button.on_clicked(clear_function_part)
        bclear.on_clicked(clear_function_full)
        btrian.on_clicked(triangle_function_full)
    else:
        button.on_clicked(clear_function_full)
        bclear.on_clicked(clear_function_part)
        btrian.on_clicked(triangle_function_one)

    plt.show()
    Axes3D.plot()

def triangle_function_full(event):
    triangulation.triangulate(d)
    draw_function(d,'See one-face example')

def triangle_function_one(event):
    d = input.ply2dcel('venv\example\one-face.txt')
    triangulation.triangulate(d)
    draw_function(d,'See full example')

def clear_function_full(event):
    d = input.ply2dcel('venv\example\example.txt')
    draw_function(d,'See one-face example')

def clear_function_part(event):
    d = input.ply2dcel('venv\example\one-face.txt')
    draw_function(d,'See full example')


fig = plt.figure()
d = input.ply2dcel('venv\example\example.txt')
print(d)
draw_function(d,'See one-face example')

