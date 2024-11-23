import matplotlib
#Starting a Matplotlib GUI outside of the main thread will fail.
matplotlib.use('Agg')
import matplotlib.pyplot as plt  # plotting module
import io
import base64
from visualizerapp.models.Lines import Line
from visualizerapp.models.Points import Punct

def plot_lines(lines,show_intersection,show_middles):
    if lines:
        for l in lines:
            plt.scatter(l['p1']['x'], l['p1']['y'], color='red')  # Accessing p1's x and y
            plt.scatter(l['p2']['x'], l['p2']['y'], color='red')  # Accessing p2's x and y
            plt.plot([l['p1']['x'], l['p2']['x']], [l['p1']['y'], l['p2']['y']], color='green', linestyle='-')
            if show_middles:
                p1 = Punct(l['p1']['x'], l['p1']['y'])
                p2 = Punct(l['p2']['x'], l['p2']['y'])
                l = Line(p1,p2)
                mijloc = l.mijloc()
                plt.scatter(mijloc.x, mijloc.y, color='blue')
        if show_intersection:
            for l1 in lines:
                for l2 in lines:
                    p1 = Punct(l1['p1']['x'], l1['p1']['y'])
                    p2 = Punct(l1['p2']['x'], l1['p2']['y'])
                    l1 = Line(p1,p2)

                    p1 = Punct(l1['p1']['x'], l1['p1']['y'])
                    p2 = Punct(l1['p2']['x'], l1['p2']['y'])
                    l2 = Line(p1,p2)

                    mijloc = l.mijloc()
                    plt.scatter(mijloc.x, mijloc.y, color='blue')

    buf = io.BytesIO()  # Create buffer
    plt.savefig(buf, format='png')  # Saving the image into buffer
    buf.seek(0)  # We go back to the beginning of the stream
    plot_url = base64.b64encode(buf.read()).decode('utf-8')
    # DATA FLOW:
    # binary data -> bytes object (base 64-ASCII) -> text
    buf.close()
    plt.close()
    return plot_url