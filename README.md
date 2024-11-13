# Project Title: Bacteria Database

### Project Description

The Bacteria Database is a Flask-based web application that allows users to explore proterties of various bacteria species. This project aims to provide a user-friendly interface for microbiology enthusiasts to explore bacterium data.

### Deployment Link

[Live Application](https://bacteria-database.onrender.com)

---

### Technologies Used

- **Frontend**: HTML, CSS, Jinja2
- **Backend**: Flask, Flask-Login, Flask-WTF, Flask-SQLAlchemy
- **Database**: PostgreSQL
- **APIs**: BacDive API (for bacterium data)

---

### Entity Relationship Diagram

![ERD Diagram](/capstone-project-one-9f2151c318294e76936126364eb9e232/erd_diagram.pngerd_diagram.png)

### Installation Instructions

1. **Clone the Repository**:

   ```
   git clone https://github.com/dacooper1/bacterium-database.git
   cd bacterium-database
   ```

2. **Set Up Virtual Environment**:

   ```
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**:

   ```
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:
   Create a `.env` file in the root directory and add the following variables:

   ```
   SECRET_KEY=your_secret_key
   DATABASE_URI=your_database_uri
   USER=your_bacdive_user
   API_SECRET_KEY=your_bacdive_api_secret
   ```

5. **Initialize the Database**:

   ```
   flask db upgrade
   ```

6. **Run the Application**:
   ```
   flask run
   ```

---

### Usage

1. **Register** for an account or **log in** to access the main features.
2. **Browse** bacteria species by index or alphabetical search.

Ensure that you have a BacDive API key set in your environment to fetch bacterium data.

---

### Features

- **User Authentication**: Secure user login and registration with Flask-Login.
- **Bacteria Browsing**: Explore bacteria species, view details, and navigate by alphabet.
- **API Integration**: Fetch and display bacterium details from the BacDive API.

---

### Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository and create a new branch for any feature or bug fix.
2. Write clear, concise commit messages.
3. Submit a pull request with a detailed description of your changes.
4. Report any issues or bugs using GitHub's issues feature.

---

### Contact Information

- **Author**: Dejah Cooper
- **Email**: dejah.c@icloud.com
