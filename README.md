# Ice-Cream Distribution System

## Overview

This Ice-Cream Distribution System is a web service/API designed to manage ice-cream orders, user authentication, payment processing, and provide statistics on ice-cream sales. Developed with Flask and SQLite, it's built to handle concurrent users and offers a scalable, reliable solution for ice-cream order management.

## Features

- **User Authentication**: Securely register users and handle login sessions.
- **Order Management**: Place and manage orders with real-time updates.
- **Payment Processing**: Integrate with a mock payment gateway for processing orders.
- **Statistics**: Gather and display statistics on sales, including popular flavors and total sales.

## Technology Stack

- **Backend**: Flask (Python)
- **Database**: SQLite
- **Asynchronous Processing**: Threading for simulating payment processing
- **Testing**: unittest for Python testing

## Getting Started

### Prerequisites

- Python 3.6+
- Flask
- Flask-SQLAlchemy
- SQLite

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/maksym030801/ice-cream-distribution-system.git
   ```
2. Navigate into the project directory:
   ```
   cd ice-cream-distribution-system
   ```
3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
4. Initialize the database:
   ```
   flask shell
   >>> from your_application import db
   >>> db.create_all()
   ```

### Running the Application

1. Start the Flask application:
   ```
   flask run
   ```
   The service will be available at `http://127.0.0.1:5000/`.

## Usage

- **Create an Order**:
  Send a POST request to `/orders/create_order` with the order details.

- **Process Payment**:
  Payments are processed asynchronously after order creation.

- **View Statistics**:
  Access `/statistics` to view sales statistics.

## Testing

Run the tests using the unittest module:

```
python -m unittest discover tests
```

## Contributing

Contributions are welcome! Please read the [CONTRIBUTING.md](CONTRIBUTING.md) for how to contribute to the project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### Customization

- Replace `https://github.com/maksym030801/ice-cream-distribution-system.git` with the actual URL of your project's repository.
- Ensure that the installation and usage instructions match the actual commands and endpoints in your application.
- Update the `Prerequisites`, `Installation`, and `Running the Application` sections according to your project's requirements.
- If you have additional setup steps, dependencies, or environment configurations, include those in the `Installation` section.
- Consider providing more detailed examples of API requests and responses in the `Usage` section.

This README template provides a solid foundation, but the more detailed and tailored the content is to your project, the more helpful it will be to users and contributors.