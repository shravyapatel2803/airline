# Airline Demand Insights Dashboard

This project is a Django-based web application designed to provide insights into simulated airline market demand and price trends, primarily focusing on Australian routes. It offers a user-friendly dashboard to visualize popular routes and price fluctuations, developed with a focus on speed and minimal spending using free tools.

## Table of Contents

* [Features](#features)
* [Setup and Installation](#setup-and-installation)
* [Usage](#usage)
* [Project Structure](#project-structure)
* [Important Note on Data](#important-note-on-data)
* [Contact](#contact)

## Features

* **Interactive Dashboard:** Displays simulated top popular airline routes and average price trends over the past 14 days.
* **Client-Side Filtering:** Allows users to filter and search popular routes by origin, destination, or a combination of both directly within the browser.
* **Dynamic Price Trend Chart:** Visualizes simulated price movements using Chart.js for an engaging user experience.
* **Responsive Design:** Built with Bootstrap 5 for a modern, mobile-friendly interface.
* **Dedicated About Page:** Provides information about the project's mission, key features, and development approach.
* **Contact Us Page:** A professional contact form and essential contact information for inquiries.
* **Django Backend:** A robust and scalable foundation for potential future integrations with real-time APIs.

## Setup and Installation

Follow these steps to get the project up and running on your local machine.

### Prerequisites

* Python 3.8+
* pip (Python package installer)
* Django (will be installed in the next step)

### Steps

1.  **Clone the repository (or set up your project files):**
    If you have your project files locally, ensure they are organized as a standard Django project.

    ```bash
    # Example for a new Django project setup
    # Make sure your project structure looks like:
    # airline_project/
    # ├── manage.py
    # ├── airlines/
    # │   ├── __init__.py
    # │   ├── asgi.py
    # │   ├── settings.py
    # │   ├── urls.py
    # │   ├── views.py
    # │   └── wsgi.py
    # └── airlines/templates/
    #     ├── index.html
    #     ├── about.html
    #     └── contact.html
    ```

2.  **Navigate to the project directory:**

    ```bash
    cd airline_project # or wherever your manage.py is located
    ```

3.  **Install Django and other dependencies:**

    ```bash
    pip install Django pandas
    ```

4.  **Apply migrations (optional, but good practice for any Django project):**

    ```bash
    python manage.py migrate
    ```

5.  **Run the development server:**

    ```bash
    python manage.py runserver
    ```

## Usage

Once the development server is running:

1.  Open your web browser and go to `http://127.0.0.1:8000/`.
2.  The **Dashboard** will be displayed, showing simulated popular routes and price trends.
3.  Use the "Origin City", "Destination City", and "Search Route" filters to interact with the popular routes table.
4.  Navigate to the **"About"** page from the top navigation bar to learn more about the project.
5.  Visit the **"Contact"** page to see the contact form and information.

## Project Structure

* `airlines/settings.py`: Main Django settings for the project.
* `airlines/urls.py`: Defines URL patterns for the application.
* `airlines/views.py`: Contains the view functions that handle requests and render templates, including the logic for generating dummy data.
* `airlines/templates/`: Directory containing HTML templates.
    * `index.html`: The main dashboard page with charts, tables, and filters.
    * `about.html`: The 'About Us' page.
    * `contact.html`: The 'Contact Us' page with a form.

## Important Note on Data

The data displayed in this application (popular routes and price trends) is **simulated and randomly generated** within `airlines/views.py`. It does not represent real-time or actual airline market data. This approach was chosen to ensure fast results and minimize spending during development.

## Contact

For any inquiries or feedback, please reach out through the contact information provided on the [Contact Us page](http://127.0.0.1:8000/contact/).
