# Diabetes Prediction Web Application

A Django-based web application that predicts diabetes using machine learning. The application provides user authentication and a simple interface for users to input their health metrics and receive predictions.

## Features

- User Authentication (Register, Login, Logout)
- Diabetes Prediction using Machine Learning
- Responsive Web Interface
- About and Contact Pages
- Form-based Data Input

## Tech Stack

- Python 3.x
- Django
- Scikit-learn (Machine Learning Model)
- SQLite Database
- HTML/CSS
- Bootstrap (for styling)

## Project Structure

```
secondproject/
├── app2/                   # Main application directory
│   ├── migrations/        # Database migrations
│   ├── templates/        # HTML templates
│   ├── forms.py         # User registration forms
│   ├── models.py        # Database models
│   ├── urls.py          # URL configurations
│   ├── views.py         # View functions
│   └── training.py      # ML model training script
├── static/               # Static files (CSS, JS, Images)
├── templates/            # Global templates
├── manage.py            # Django management script
├── model.joblinb        # Trained ML model
└── db.sqlite3           # SQLite database
```

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install django scikit-learn joblib pandas numpy
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Start the development server:
```bash
python manage.py runserver
```

## Usage

1. Register a new account or login with existing credentials
2. Navigate to the prediction form
3. Enter the required health metrics:
   - Glucose Level
   - Blood Pressure
   - Skin Thickness
   - Insulin
   - BMI (Body Mass Index)
   - Diabetes Pedigree Function
   - Age
4. Submit the form to get the prediction result

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

Your Name - your.email@example.com
Project Link: [https://github.com/yourusername/secondproject](https://github.com/yourusername/secondproject)
