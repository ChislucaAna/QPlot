import matplotlib
#Starting a Matplotlib GUI outside of the main thread will fail.
matplotlib.use('Agg')
import io
import base64
from visualizerapp.models.Lines import Line
from visualizerapp.models.Points import Punct
import matplotlib.pyplot as plt

def config():
    fig = plt.figure()
    fig.set_size_inches(10, 8)
    fig.patch.set_facecolor('#0F0F0F') #background outside grid 
    plt.gca().set_facecolor('black') #background col of grid area
    plt.grid(color='gray')  # Change gridline color
    # Set axis labels and make them white
    plt.xlabel("X", color='white')
    plt.ylabel("Y", color='white')
    
    # Set the spines (axes lines) to white
    plt.gca().spines['bottom'].set_color('white')
    plt.gca().spines['left'].set_color('white')
    plt.gca().spines['top'].set_color('white')
    plt.gca().spines['right'].set_color('white')
    
    # Set the tick labels color to white
    plt.tick_params(axis='x', colors='white')  # X-axis ticks in white
    plt.tick_params(axis='y', colors='white')  # Y-axis ticks in white

def plot_points(points,connect_points):
    if points:
        for p in points:
            plt.scatter(p['x'], p['y'], color='blue')
        if connect_points:
            xs = [p['x'] for p in points]
            ys = [p['y'] for p in points]
            plt.plot(xs, ys, color='gray', linestyle='--')

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

def generate_plot_url(context_data):
    buf = io.BytesIO()

    config()
    plot_points(context_data['points'], context_data['connect_points'])
    plot_lines(context_data['lines'], context_data['show_intersection'], context_data['show_middles'])
    try:
        #print(buf)
        plt.savefig(buf, format='png')
        buf.seek(0)
        #if buf.tell() == 0:
        #    print("Error: Plot buffer is empty!")
        #    return None
        # Encode the plot to base64
        plot_url = base64.b64encode(buf.read()).decode("utf-8")
    except Exception as e:
        print(f"Error saving plot: {e}")
        return None
    finally:
        buf.close()
        plt.close()
    #print(plot_url)
    return f"data:image/png;base64,{plot_url}"
    #return plot_url