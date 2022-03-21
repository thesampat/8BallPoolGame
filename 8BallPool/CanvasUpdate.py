def reprint(canvas, root, time=1000, *obj):
    root.after(time)
    destroy(canvas, *obj)
    canvas.update()


def destroy(canvas, *obj):
    canvas.delete(*obj)
