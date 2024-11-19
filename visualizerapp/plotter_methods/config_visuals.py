import matplotlib
#Starting a Matplotlib GUI outside of the main thread will fail.
matplotlib.use('Agg')
import matplotlib.pyplot as plt  # plotting module
import io
import base64

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