import matplotlib
#Starting a Matplotlib GUI outside of the main thread will fail.
matplotlib.use('Agg')
import matplotlib.pyplot as plt  # plotting module
import io
import base64

def plot_lines(lines):
    if lines:
        for l in lines:
            # Access p1 and p2 correctly (assuming p1 and p2 are dictionaries with 'x' and 'y' keys)
            plt.scatter(l['p1']['x'], l['p1']['y'], color='red')  # Accessing p1's x and y
            plt.scatter(l['p2']['x'], l['p2']['y'], color='red')  # Accessing p2's x and y
            plt.plot([l['p1']['x'], l['p2']['x']], [l['p1']['y'], l['p2']['y']], color='green', linestyle='-')

    buf = io.BytesIO()  # Create buffer
    plt.savefig(buf, format='png')  # Saving the image into buffer
    buf.seek(0)  # We go back to the beginning of the stream
    plot_url = base64.b64encode(buf.read()).decode('utf-8')
    # DATA FLOW:
    # binary data -> bytes object (base 64-ASCII) -> text
    buf.close()
    plt.close()
    return plot_url