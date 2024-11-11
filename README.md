🌐 QPlot

QPlot is a web application developed using Django that allows users to plot various geometric elements, including points, lines, triangles, and other polygons. With an intuitive interface, users can create, visualize, and manage their geometric plots seamlessly. The app also offers user accounts, enabling the option to save plots either to a personal account or locally.
![image](https://github.com/user-attachments/assets/e42322e6-ddb0-40ea-b2fa-102e9491f199)
![image](https://github.com/user-attachments/assets/136eb181-46c4-42a4-9170-247968ccedbc)
![image](https://github.com/user-attachments/assets/91c80f2b-e23a-4b90-9c19-1112be55d4ac)
![image](https://github.com/user-attachments/assets/07899f00-2482-4b56-95c7-53ec722ef31f)
![image](https://github.com/user-attachments/assets/3f97ef7d-1855-4367-a8f4-110bf4a27ffa)


✨ Features

    Geometric Plotting: Create plots with points, lines, triangles, and polygons.
    User Accounts: Sign up to save your plots online for future reference.
    Local Plot Storage: Download and save your plots locally.
    Interactive Visualizations: Use Matplotlib for precise plotting and rich visuals.
    Intuitive Forms: User-friendly forms for easy plot creation.

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
