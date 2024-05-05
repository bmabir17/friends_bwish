

## Project: Django Birthday Email App

This project demonstrates a Django application to send birthday emails to customers. It leverages Docker and Docker Compose for a containerized deployment environment.

### Prerequisites

- Docker ([https://www.docker.com/](https://www.docker.com/))
- Docker Compose ([https://docs.docker.com/compose/](https://docs.docker.com/compose/))

### Project Structure

```
bwish
├── Dockerfile
├── docker-compose.yml
└── bwish/
    ├── __init__.py
    ├── settings.py
    └── urls.py
└── bwish_api/
    ├── __init__.py
    ├── admin.py
    ├── apps.py 
    ├── migrations/
    ├── models.py
    ├── views.py  # api endpoint
    ├── settings.py
    └── urls.py
└── send_email/
    ├── __init__.py
    ├── admin.py
    ├── apps.py 
    ├── send_message.py  # Custom management command
```

### Setting Up

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/bmabir17/friends_bwish.git
   cd friends_bwish/bwish
   ```

### Building and Running the Application

1. **Build Docker Images:**

   ```bash
   docker-compose build
   ```

2. **Run the Application:**

   ```bash
   docker-compose up
   ```


3. **Registering new Cusotmer with API end point:**

   - Locate the port for the Django container (typically `5005` by default).
   - To register new customer call this api end point using postman `http://0.0.0.0:5005/api/customer/register`. Send the following json values in the body of the post Request
        ```json
            {
                "date":"2024-05-05",
                "cust_name":"Abir",
                "cust_email":"bmabir17@gmail.com"
            }
        ```
    - The API will return a success Message when the registration is success. If a duplicate email exists it will return a error.
    - After success Message is seen wait for atleast 60 seconds and a email sent message will be printed on the console where docker-compose is running
