# AnimeKarma

AnimeKarma is a Django-based web application that provides users with the latest anime news fetched from various APIs. The project is designed to deliver up-to-date information about the anime world in a user-friendly interface.

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

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Salehin-07/CarmaAnime
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
4. **Apply migrations:**
   ```bash
   python manage.py makemigration 
   python manage.py migrate
   ```

5. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

6. **Access the application:**
   Open [http://localhost:8000](http://localhost:8000) in your browser.

## Deployment

CarmaAnime is ready to be deployed on [Render](https://render.com/). Make sure to:

- Add your environment variables in Render's dashboard.
- Set up a PostgreSQL database (or your preferred DB) if required.
- Configure the `render.yaml` or deployment settings as needed.

## API Sources

- The application fetches news free APIs that doesn't need configuration. If you want you can use Any API.

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## Website 
Thsi is Already deployed to render.

```
https://animekarma.onrender.com
```
## License

[MIT](LICENSE)

## Acknowledgements

- Django documentation
- Anime news API providers

## Creator

- [Salehin-07](https://github.com/Salehin-07)
---

Made with ❤️ for anime fans.
