# Assignment AI Planet Backend

This is the backend service for the Assignment AI Planet project. It provides RESTful APIs to support the application's core functionalities.

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [API Documentation](#api-documentation)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- CRUD operations for assignments

## Tech Stack

- Python 3.8+
- FastAPI
- Uvicorn (ASGI server)
- Pydantic for data validation
- python-dotenv for environment variables

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip

### Installation

```bash
git clone https://github.com/yourusername/assignmentAIPlanet-backend.git
cd assignmentAIPlanet-backend
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the root directory:

```env
GOOGLE_API_KEY=your_api_key
```

### Running the Server

```bash
uvicorn app.main:app --reload
```

The server will run on `http://localhost:8000`.

## API Documentation

Interactive API docs are available at `/docs` (Swagger UI) and `/redoc` (ReDoc) when the server is running.

For detailed API usage, see [API_DOCS.md](API_DOCS.md).

## Project Structure

```
backend/
├── app/
│   ├── main.py
├── .env.example
├── requirements.txt
└── README.md
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a pull request

## License

This project is licensed under the MIT License.
