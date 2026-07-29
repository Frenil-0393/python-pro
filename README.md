# Scoreclub - Role-Based Sports Management & Broadcasting Platform

Scoreclub is a comprehensive, role-based sports management, scheduling, and broadcasting web application built using Python and Django. It facilitates collaboration between sports event organizers, media professionals, and sports fans by offering tailored dashboards and feature sets for each specific role.

---

## 🚀 Key Features

### 🔐 1. Authentication & Role-Based Access Control (RBAC)
*   **Custom User Model**: Built on Django's `AbstractUser` to support user accounts with custom roles (`fan`, `organizer`, `media`).
*   **Secure Access**: Custom `@role_required` decorators protect views and dashboards to prevent unauthorized access between roles.
*   **Role-Specific Navigation**: Automatically redirects users to their respective dashboards upon login.

### 📋 2. Organizer Dashboard (Management Console)
*   **Match Fixture Scheduling**: Create, edit, and delete sports match fixtures (stores sport, home/away teams, venue, start time, and status).
*   **Live Score Updates**: Log real-time score summaries and status notes for live matches.
*   **Player Statistics Management**: Track individual player stats, team assignments, custom metric names/values, and player availability.
*   **CSV Exports**: Export complete datasets for matches, scores, and player statistics.

### 🎙️ 3. Media & Broadcast Dashboard (Content Creation)
*   **Broadcast Sessions**: Set up and manage live stream channels and URLs with toggles to turn streams live or offline.
*   **Highlights Publisher**: Upload and manage video highlights, including descriptions, duration tags, and view counters.
*   **Press Releases**: Create, edit, and publish press releases (supporting Draft/Published workflows) categorized by sport.

### 📣 4. Fan Dashboard (Engagement Hub)
*   **Interactive Timetable**: Browse and search scheduled matches filterable by sport.
*   **Live Ticker & Scores**: Follow real-time match status updates and latest scores with paginated views.
*   **Leaderboards & Player Stats**: Sort and filter player performance metrics (e.g., runs, points) dynamically.
*   **Highlights Center**: Watch match summaries and featured video highlights.

---

## 🛠️ Tech Stack & Architecture

*   **Backend**: Python, Django
*   **Database**: SQLite (Development) / Compatible with PostgreSQL/MySQL
*   **Frontend**: HTML5, CSS3, JavaScript (Vanilla), Django Templates
*   **APIs & Data**: Native CSV export generation
*   **Libraries**: Standard Django authentication and middleware

---

## 📦 Getting Started

### Prerequisites
*   Python 3.10+
*   Pip (Python package installer)

### Setup & Installation
1.  **Clone the Repository**:
    ```bash
    git clone <repository-url>
    cd python-pro/django_project
    ```

2.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run Migrations**:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

4.  **Create a Superuser (Optional)**:
    ```bash
    python manage.py createsuperuser
    ```

5.  **Run the Server**:
    ```bash
    python manage.py runserver
    ```
    Access the application at `http://127.0.0.1:8000/`.
