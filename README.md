# CRUD Project

This is a simple CRUD (Create, Read, Update, Delete) project built using Flask and PostgreSQL. It allows users to perform CRUD operations on a database table , which stores contact information.

## Features

- **Create**: Add new contact information to the database.
- **Read**: View the list of contacts stored in the database.
- **Update**: Modify existing contact information.
- **Delete**: Remove contact information from the database.

## Technologies Used

- Flask: A lightweight WSGI web application framework.
- PostgreSQL: An open-source relational database management system.
- Psycopg2: A PostgreSQL adapter for Python.

## Usage

1. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

2. Set up the PostgreSQL database:
   
   - Create a PostgreSQL database `your_db_name`.
   - Execute the SQL commands from `database.sql` to create the `your_table_name` table.

3. Run the Flask application:

    ```bash
    python app.py
    ```

4. Access the application in your web browser at `http://localhost:5000`.

## Contributing

Contributions are welcome! Feel free to open issues or pull requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
