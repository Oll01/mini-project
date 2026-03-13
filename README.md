# Web Service Portfolio

A personal portfolio web service built with Flask, showcasing projects and contact information.

## Features

- **Home** (`/`, `/home`) - Personal introduction and skill set
- **Projects** (`/projects`) - Portfolio project list with detail view
- **Contact** (`/contact`) - Contact information and social links

## Tech Stack

- Python 3.x
- Flask 3.1.1

## Installation

```bash
# Clone the repository
git clone https://github.com/username/web-service.git
cd web-service

# Install dependencies
pip install -r requirements.txt
```

## Usage

```bash
# Run the server
flask run
```

Open your browser and navigate to `http://127.0.0.1:5000`

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Home page with personal info |
| GET | `/home` | Same as `/` |
| GET | `/projects` | List all projects |
| GET | `/projects/<id>` | Get project detail by ID |
| GET | `/contact` | Contact information |

## Git Branch Strategy

- `main` - Production-ready code
- `feature/home` - Home page feature
- `feature/projects` - Projects page feature
- `feature/contact` - Contact page feature

## License

MIT License