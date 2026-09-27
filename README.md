# CampusBazaar — Student Marketplace

CampusBazaar is a small dynamic web application designed for students to buy, sell and exchange used items within a campus community.

Students can view marketplace items, add new items, search for products, and mark items as sold. The application also provides a JSON API and health check endpoint.

Built for CCA 2 (Individual Submission) using Python, Flask, pytest, flake8, Docker, GitHub Actions and Render.

## Features

- **Homepage** — dynamically displays marketplace items with total and available item statistics.
- **Add item** — students can add an item with name, category, price, condition, seller and description.
- **Server-side validation** — validates required fields and ensures that the price is greater than zero.
- **Search** — search marketplace items by item name, category or description.
- **Mark as sold** — available items can be marked as sold.
- **JSON API** — `GET /api/items` returns all marketplace items as JSON.
- **Health check** — `GET /health` verifies that the application is running.
- **Commit ID footer** — displays the current commit ID on the application.
- **Responsive interface** — designed for desktop and smaller screens.

## Tech Stack

| Part | Technology |
|---|---|
| Language | Python 3.12 |
| Web Framework | Flask |
| Templates | Jinja2 |
| Testing | pytest |
| Linting | flake8 |
| Containerization | Docker |
| CI/CD | GitHub Actions |
| Hosting | Render |

## Project Structure

```text
CampusBazaar/
├── app.py
├── requirements.txt
├── test_app.py
├── Dockerfile
├── .gitignore
├── README.md
│
├── templates/
│   ├── index.html
│   └── add_item.html
│
├── static/
│   └── style.css
│
└── .github/
    └── workflows/
        └── ci-cd.yml
```
Local Setup
1. Clone the repository
git clone https://github.com/<your-username>/CampusBazaar-CCA2.git
cd CampusBazaar-CCA2
2. Create a virtual environment

Windows:

python -m venv venv

Activate it:

venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt
4. Run the application
python app.py

Open:

http://localhost:5000
Application Routes
Method	Route	Purpose
GET	/	Display marketplace
GET/POST	/add	Add a marketplace item
POST	/sell/<id>	Mark an item as sold
GET	/api/items	Return marketplace items as JSON
GET	/health	Application health check
Testing

The project uses pytest for automated testing.

Run:

pytest -v

The tests verify:

Health endpoint
Adding an item
Invalid item validation
Marking an item as sold
Marketplace JSON API
Linting

The project uses flake8 for code quality checking.

Run:

flake8 --max-line-length=120 --exclude=venv .
Running with Docker

Build the Docker image:

docker build -t campusbazaar .

Run the container:

docker run --rm -p 5000:5000 campusbazaar

Open:

http://localhost:5000

Health check:

http://localhost:5000/health
CI/CD Pipeline

The CI/CD workflow is stored at:

.github/workflows/ci-cd.yml

The pipeline follows this process:

Developer
    ↓
Git Push / Pull Request
    ↓
GitHub
    ↓
Lint
    ↓
Automated Tests
    ↓
Docker Build
    ↓
Render Deployment
    ↓
Live CampusBazaar
Pipeline Stages
Lint — checks Python code using flake8.
Test — runs the automated pytest test suite.
Docker Build — builds the CampusBazaar Docker image and checks the application health endpoint.
Deploy — deployment is triggered for successful pushes to the main branch.
Live Application — the latest successful version is available through Render.

If linting or tests fail, the later build and deployment stages do not run. This prevents broken code from reaching the live application.

GitHub Actions

The GitHub Actions workflow runs for:

Pushes to main
Pull requests targeting main

The deployment stage runs only after the required checks pass and only for the main branch.

Required GitHub Secret

The Render deployment hook is stored securely as a GitHub repository secret.

Secret name:

RENDER_DEPLOY_HOOK

The actual deploy hook URL is not stored in the source code.

Render Deployment

The application is deployed as a Docker-based web service on Render.

The application uses:

/health

as its health check endpoint.

Render provides the public live application URL.

Failure Demonstration

A temporary failing test is used to demonstrate that the CI/CD pipeline prevents broken code from being deployed.

The demonstration works as follows:

Failing Test
     ↓
Test Job Fails
     ↓
Docker Build Skipped
     ↓
Deploy Skipped

After restoring the correct test:

Passing Test
     ↓
Docker Build
     ↓
Deploy
     ↓
Live Application

This demonstrates that the pipeline protects the live application from a failed build or test.

Learning Outcomes

Through this project, the following concepts were implemented:

Git version control
Branching and pull requests
Meaningful commit history
Automated testing with pytest
Code linting with flake8
Docker containerization
GitHub Actions CI/CD
Render deployment
Health checks
Failure prevention in CI/CD
Project Links
GitHub Repository

<GitHub Repository URL>

Live Application

<Render Live URL>

GitHub Actions Pipeline

<GitHub Actions URL>

Pull Request

<Pull Request URL>

Author

Kalyani Dhumal

CCA 2 — Cloud Computing and DevOps
