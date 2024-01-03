# Basic Flask Web Application

This is a basic Flask web application that demonstrates a simple form submission. The application uses three HTML templates and a Flask server to handle requests.

## Files and Directory Structure

- **`app.py`**: The main Flask application file containing the server logic.
- **`templates/`**: Directory containing HTML templates.
  - **`index.html`**: The main page with a form for user input.
  - **`layout.html`**: Base HTML template that other templates extend.
  - **`greet.html`**: Template displaying a greeting based on user input.

## Getting Started

### Prerequisites

- Python installed on your machine.

### Installation

1. Clone this repository to your local machine.

   ```bash
   git clone https://github.com/your-username/flask-basic-web-app.git
   cd flask-basic-web-app

###  Running

python -m venv venv
source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'

python app.py
