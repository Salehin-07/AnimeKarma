# CarmaAnime

CarmaAnime is a Django-based web application that provides users with the latest anime news fetched from various APIs. The project is designed to deliver up-to-date information about the anime world in a user-friendly interface.

## Features

- Fetches and displays recent anime news from trusted APIs
- Built using the Django web framework
- Responsive and easy-to-navigate UI
- Ready for deployment on Render

## Getting Started

These instructions will help you set up and run the project on your local machine.

### Prerequisites

- Python 3.8+
- pip (Python package manager)
- Git

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/<your-username>/CarmaAnime.git
   cd CarmaAnime
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   - Create a `.env` file in the root directory and add your secrets (like API keys, Django secret key, etc.).

5. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

7. **Access the application:**
   Open [http://localhost:8000](http://localhost:8000) in your browser.

## Deployment

CarmaAnime is ready to be deployed on [Render](https://render.com/). Make sure to:

- Add your environment variables in Render's dashboard.
- Set up a PostgreSQL database (or your preferred DB) if required.
- Configure the `render.yaml` or deployment settings as needed.

## API Sources

- The application fetches news from various anime news APIs. Please ensure you have the necessary API keys and permissions.

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](LICENSE)

## Acknowledgements

- Django documentation
- Anime news API providers

---

Made with ❤️ for anime fans.