# Quote of the Day

Welcome to Quote of the Day! This is a simple Django application that displays a new inspirational quote each day. Quotes are fetched from an external API and cached to ensure a fresh quote every day.
![Screenshot (221)](https://github.com/workwithshreesh/Django_Mini_Projects/assets/117170243/82989124-d69e-4344-b9ba-b44f91aa9e98)

## Installation

Add Api of quotes from api Ninja:
   1. Go to Views.py
   2. Copy Api from api ninja and paste in between given code bellow
   3. response = requests.get(api_url, headers={'X-Api-Key': 'Your Api of api-ninja'})

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/QuoteOfTheDay.git
    ```

2. Navigate into the project directory:

    ```bash
    cd QuoteOfTheDay
    ```

3. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS and Linux:

        ```bash
        source venv/bin/activate
        ```

5. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

6. Set up caching:

    - Make sure you have Redis installed and running on your system. You can download Redis from [redis.io/download](https://redis.io/download).

7. Run migrations:

    ```bash
    python manage.py migrate
    ```

8. Start the development server:

    ```bash
    python manage.py runserver
    ```

9. Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser to see the application in action!

## Usage

- The application will display a new inspirational quote each day.
- To reset the daily quote, you can clear the cache by visiting [http://127.0.0.1:8000/reset/](http://127.0.0.1:8000/reset/) in your browser.

## Credits

- This project utilizes the [Quotable API](https://api-ninjas.com/) to fetch quotes.
- Developed by [Shreesh Tiwari](https://github.com/workwithshreesh).

## Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests.

## Support

For any issues or questions, please open an issue on the [GitHub repository](https://github.com/workwithshreesh/QuoteOfTheDay).

