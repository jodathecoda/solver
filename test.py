import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)
text = ax.text(1, 1, 'Text')

def on_mouse_move(event):
    if None not in (event.xdata, event.ydata):
        text.set_position((event.xdata, event.ydata))
        if event.xdata > 0.5:
            text.set_text("ooooo")
        else:
            text.set_text("uuu")
        fig.canvas.draw()

fig.canvas.mpl_connect('motion_notify_event', on_mouse_move)
plt.show()