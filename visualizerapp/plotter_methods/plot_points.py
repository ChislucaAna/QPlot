import matplotlib
#Starting a Matplotlib GUI outside of the main thread will fail.
matplotlib.use('Agg')
import matplotlib.pyplot as plt  # plotting module
import io
import base64


def plot_points(points,connect_points):
    if points:
        for p in points:
            plt.scatter(p['x'], p['y'], color='blue')
        if connect_points:
            xs = [p['x'] for p in points]
            ys = [p['y'] for p in points]
            plt.plot(xs, ys, color='gray', linestyle='--')

    buf = io.BytesIO()  # Create buffer
    plt.savefig(buf, format='png')  # Saving the image into buffer
    buf.seek(0)  # We go back to the beginning of the stream
    plot_url = base64.b64encode(buf.read()).decode('utf-8')
    # DATA FLOW:
    # binary data -> bytes object (base 64-ASCII) -> text
    buf.close()
    plt.close()
    return plot_url