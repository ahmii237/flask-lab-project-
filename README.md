# Flask Lab Project

A simple Flask web application with CI/CD pipeline and Docker containerization.

## Project Structure

```
flask-lab-project/
├── app.py
├── requirements.txt
├── Dockerfile
├── .gitignore
├── test_app.py
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── about.html
│   └── contact.html
├── static/
│   └── css/
│       └── style.css
├── .github/
│   └── workflows/
│       └── ci-cd.yml
├── README.md
└── PROJECT_GUIDE.md
```

## Features

- Professional Flask web application with three routes:
  - Home (`/`)
  - About (`/about`)
  - Contact (`/contact`)
- Modern, responsive CSS design
- Template-based HTML structure with Jinja2
- Automated testing with pytest
- Docker containerization
- GitHub Actions CI/CD pipeline

## Prerequisites

- Python 3.9+
- Docker (optional, for containerization)
- Git

## Local Setup

1. Clone the repository:

```bash
git clone <your-repo-url>
cd flask-lab-project
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
python app.py
```

4. Access the application at `http://localhost:5000`

## Running Tests

Run the test suite with pytest:

```bash
pytest test_app.py -v
```

This will run all unit tests and display detailed output.

## Docker Setup

1. Build the Docker image:

```bash
docker build -t flask-lab-project .
```

2. Run the Docker container:

```bash
docker run -p 5000:5000 flask-lab-project
```

3. Access the application at `http://localhost:5000`

## CI/CD Pipeline

The project includes a GitHub Actions workflow that:

- Runs on push and pull requests to the main branch
- Sets up Python environment
- Installs dependencies
- Runs automated tests with pytest
- Builds Docker image
- Runs the Docker container

## License

This project is for educational purposes.
