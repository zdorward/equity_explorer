# Graph Guru

This project is a Flask application for fetching and analyzing stock data. Please note to run this project, you will need to create a free API key with Alpha Vantage at https://www.alphavantage.co/support/#api-key. Your free key will allow for 25 API calls/day.

## Installation

Follow these steps to set up the project:

1. Clone the repository to your local machine:

```
git clone https://github.com/yourusername/flask-stock-data.git
```

2. Navigate to the project directory:

```
cd flask-stock-data
```

3. Create a virtual environment to isolate project dependencies:
   Using venv (Python 3)

```
python3 -m venv venv
```

Activate the virtual environment (on Unix or MacOS)

```
source venv/bin/activate
```

Activate the virtual environment (on Windows)

```
venv\Scripts\activate
```

4. Install the required dependencies from the requirements.txt file:

```
pip install -r requirements.txt
```

5. Rename '.env.example' to '.env' and add your API key value.

## Usage

To run the Flask application, execute the following command:

```
python src/app.py
```
