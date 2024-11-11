import matplotlib
#Starting a Matplotlib GUI outside of the main thread will fail.
matplotlib.use('Agg')
import matplotlib.pyplot as plt  # plotting module
import io
import base64

def plot_lines(lines):
    plt.figure(figsize=(6, 4))  # Canvas size in inches
    if lines:
        for l in lines:
            # Access p1 and p2 correctly (assuming p1 and p2 are dictionaries with 'x' and 'y' keys)
            plt.scatter(l['p1']['x'], l['p1']['y'], color='blue')  # Accessing p1's x and y
            plt.scatter(l['p2']['x'], l['p2']['y'], color='blue')  # Accessing p2's x and y
            plt.plot([l['p1']['x'], l['p2']['x']], [l['p1']['y'], l['p2']['y']], color='black', linestyle='-')

    plt.xlabel("X")
    plt.ylabel("Y")
    buf = io.BytesIO()  # Create buffer
    plt.savefig(buf, format='png')  # Saving the image into buffer
    buf.seek(0)  # We go back to the beginning of the stream
    plot_url = base64.b64encode(buf.read()).decode('utf-8')
    # DATA FLOW:
    # binary data -> bytes object (base 64-ASCII) -> text
    buf.close()
    plt.close()
    return plot_url