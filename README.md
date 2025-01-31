# Service Management Platform

## Description
This project is a web-based platform designed to connect customers with service providers for various home-related tasks, such as fixing a bidet, painting walls, home cleaning, and more. Built using Django (v3.1.14), a Python web framework, the platform allows users to register as either a **Customer** or a **Company**, request services, and manage their profiles.

## Documentation

### Installation
To run this project, you need to have Python 3.x and Django installed on your system. Follow these steps to set up the project:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/JosephOkumu/service-management-platform

    ```

2. **Navigate into the project directory**:
    ```bash
    cd service-management-platform
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run migrations**:
    ```bash
    python3 manage.py migrate
    ```

5. **Start the development server**:
    ```bash
    python3 manage.py runserver
    ```

6. **Access the website**:
    Open your browser and go to `http://127.0.0.1:8000/`.

---

## Features

### User Roles
1. **Customer**:
   - Can register by providing:
     - Email
     - Password
     - Password confirmation
     - Username
     - Date of birth
   - Can request services by specifying:
     - Address
     - Service duration (in hours)
   - Can view their profile, which displays:
     - Personal information
     - List of previously requested services

2. **Company**:
   - Can register by providing:
     - Email
     - Password
     - Password confirmation
     - Username
     - Field of work (restricted to predefined categories)
   - Can create new services within their field of work
   - Can view their profile, which displays:
     - Company information
     - List of services provided

### Service Management
- **Service Creation**:
  - Companies can create services with the following attributes:
    - Name
    - Description
    - Field (e.g., Carpentry, Plumbing, etc.)
    - Price per hour
    - Creation date (automatically set)
- **Service Categories**:
  - Services are categorized into fields such as:
    - Air Conditioner
    - Carpentry
    - Electricity
    - Gardening
    - Housekeeping
    - Painting
    - Plumbing
    - Water Heaters
  - Companies with the "All in One" field can create services in any category.


## Project Structure
The Django project is organized into three main apps:
1. **services**:
   - Handles service-related features (creation, display, requests).
2. **users**:
   - Manages user registration, login, and profiles.
3. **main**:
   - Handles common features like the home page and navigation bar.


## Contributions
Pull requests are welcome! If you'd like to contribute, please:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a detailed description of your changes.

For major changes, please open an issue first to discuss the proposed changes.

---

## Author
[josotieno]( git clone https://github.com/JosephOkumu)

---

## License
This project is licensed under the [MIT License](./LICENSE).
