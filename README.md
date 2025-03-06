# File-namer-api

## Project Structure
```
File-namer-api/
├── src/
│   ├── app.py
│   ├── models/
│   │   ├── base_model.py
│   │   └── user_model.py
│   ├── routes/
│   │   ├── __init__.py
│   │   └── user_routes.py
│   ├── services/
│   │   ├── base_service.py
│   │   └── user_service.py
│   └── utils/
│       └── validation.py
├── tests/
├── docs/
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## Setup
1. Create virtual environment:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python src/app.py
   ```
