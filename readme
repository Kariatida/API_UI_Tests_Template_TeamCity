## TeamCity Automation Project

This project automates the setup and testing of a TeamCity server and agent using GitHub Actions, Docker, Playwright, and Allure. It includes end-to-end tests, API management, and project creation automation.

## Table of Contents
- **Overview**
- **Project Structure**
- **Setup**
- **Running the Automation**
- **Tests**
- **GitHub Actions Workflow**
- **Usage**
- **Environment Variables**
- **Contributing**
- **License**

## Overview
This project provides an automated way to:
- **Set up and configure a TeamCity server and agent using Docker**
- **Manage projects via TeamCity's API**
- **Run tests using Playwright and Pytest, and generate reports with Allure**

## Project Structure
- **`Action.yaml`**: Defines the GitHub Actions workflow.
- **`Page_action.py`**: Handles browser interactions using Playwright.
- **`Api_manager.py`**: Manages API endpoints for TeamCity interactions.
- **`Setup_user.py`**: Automates TeamCity user creation.
- **`Test_create_project.py`**: Unit tests for project creation.
- **`Test_e2e_create_project.py`**: End-to-end tests for project creation.
- **`conftest.py`**: Pytest configuration and fixtures.

## Setup

### Prerequisites:
- **Docker installed and running**
- **Python 3.10 and `pip` installed**
- **GitHub repository with access to GitHub Actions**
- **TeamCity server Docker image from [JetBrains](https://hub.docker.com/r/jetbrains/teamcity-server)**

### Installation:
1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-folder>

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt

3. **Create a .env file in the root directory:**
   ```bash
   SUPER_USER_TOKEN='your-super-user-token'
   BROWSER_WIDTH=1500
   BROWSER_HEIGHT=900
   HEADLESS=True

## Tests
###  Available Tests:
- **Setup Tests: tests/frontend/test_set_up.py
- **Unit Tests for Project Creation: test_create_project.py
- **End-to-End Tests: test_e2e_create_project.py

## Contact
For further inquiries, please open an issue in the repository or email to marykrykoff@gmail.com
