🌐 QPlot

QPlot is a web application developed using Django that allows users to plot various geometric elements, including points, lines, triangles, and other polygons or different kind of functions. With an intuitive interface, users can create, visualize, and manage their geometric plots seamlessly. The app also offers user accounts, enabling the option to save plots either to a personal account or locally.
![Screenshot from 2025-01-14 20-03-46](https://github.com/user-attachments/assets/38af7af1-0f44-465f-9b66-d2edd10c113d)

![Screenshot from 2025-01-14 20-20-44](https://github.com/user-attachments/assets/46a130da-5a57-4d00-9d1a-a29e7ba90698)

![Screenshot from 2025-01-14 20-23-03](https://github.com/user-attachments/assets/924c627a-7679-4c6b-a1d4-47306ac1a3fa)

![Screenshot from 2025-01-14 20-50-06](https://github.com/user-attachments/assets/26c35ca2-dacf-4298-bbe8-8ac8ddd073ed)

![Screenshot from 2025-01-14 20-56-17](https://github.com/user-attachments/assets/330e56cc-e84b-4a33-b9b7-e58153ce28b3)

⚙️ Technologies Used

    Django: A high-level Python web framework that encourages rapid development and clean, pragmatic design. Django provides the backend structure and user authentication for QPlot.

    Tailwind CSS: A utility-first CSS framework that allows for fast styling of elements with pre-built classes. Tailwind is used to create a responsive, clean, and user-friendly interface.

    Matplotlib: A powerful plotting library for Python, ideal for creating static, animated, and interactive visualizations. Matplotlib handles the rendering of geometric plots in QPlot.

📋 Requirements

To run QPlot locally, ensure the following packages are installed in your virtual environment:

    Python: version 3.6 or higher
    Django: for the web framework
    Matplotlib: for rendering geometric plots

Install dependencies with:

    pip install -r requirements.txt

🛠 Installation

Clone this repository:

    git clone https://github.com/yourusername/qplot.git

Create and activate a virtual environment:

    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`

Install the required packages:

    pip install -r requirements.txt

Run migrations:

    python manage.py migrate

Start the Django development server:

    python manage.py runserver

Open your browser and navigate to http://127.0.0.1:8000 to start using QPlot!

🚀 Usage

    Sign Up / Log In: Create an account to save your plots or log in to an existing account.
    Create a Plot: Use the provided forms to enter coordinates for points, lines, triangles, and other polygons.
    Save and View Plots: Save plots to your account for easy access or download them for local storage.

🤝 Contributing

I welcome contributions to enhance QPlot! Please fork this repository, make your changes, and submit a pull request
