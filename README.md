# Backend Assessment

This is a small FastAPI application with a few intentional bugs. The goal of this assessment is to evaluate your ability to debug code, your understanding of web development concepts, and your knowledge of version control.

## Getting Started

To get started, you will need to have Python 3.8+ and Git installed on your machine.

### 1. Fork the Repository

First, you will need to fork this repository to your own GitHub account. You can do this by clicking the "Fork" button at the top right of the repository page.

### 2. Clone Your Fork

Next, you will need to clone your forked repository to your local machine. You can do this by running the following command in your terminal:

```bash
git clone https://github.com/YOUR_USERNAME/backend_test.git
```

### 3. Create a New Branch

Before you start working on an issue, you should create a new branch for that issue. This will help you keep your changes organized and separate from the main branch.

```bash
git checkout -b issue-<issue_number>
```

For example, if you are working on issue #3, you would run:

```bash
git checkout -b issue-3
```

### 4. Set Up the Development Environment

To set up the development environment, you will need to install the dependencies listed in the `requirements.txt` file. You can do this by running the following command in your terminal:

```bash
pip install -r requirements.txt
```

### 5. Run the Tests

Before you start making any changes, you should run the tests to see the failures. You can do this by running the following command in your terminal:

```bash
pytest
```

This will show you which tests are failing and will give you a starting point for your debugging.

### 6. Work on an Issue

Now you can start working on an issue. You can find the list of issues in the `tickets.md` file in the root of the repository. Each ticket corresponds to an issue on GitHub.

### 7. Commit Your Changes

Once you have fixed an issue, you should commit your changes with a clear and descriptive commit message. Your commit message should reference the issue number that you are working on.

```bash
git add .
git commit -m "Fix: Resolve issue #<issue_number> - <short_description>"
```

For example:

```bash
git commit -m "Fix: Resolve issue #3 - Fix database session handling"
```

### 8. Push Your Changes

Next, you will need to push your changes to your forked repository.

```bash
git push origin issue-<issue_number>
```

### 9. Open a Pull Request

Finally, you can open a pull request to the main repository. In your pull request, you should include a detailed description of the changes you made and how they address the issue. You should also link your pull request to the issue by including the issue number in the pull request description (e.g., "Closes #3").

## Assessment Criteria

We will be assessing you on the following criteria:

-   **Your thought process:** How you approach debugging and problem-solving.
-   **Your knowledge of version control:** Your ability to use Git and GitHub effectively.
-   **The quality of your code:** The clarity, correctness, and efficiency of your code.
-   **Your communication skills:** Your ability to communicate your ideas and work effectively.

Good luck!
