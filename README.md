# Task 5 — Educational Website Automation Testing

Automated test suite for educational / LMS websites using Python + Selenium + pytest. Covers enrollment, content delivery, quiz submissions, progress tracking, and multimedia handling.

## What's Tested

- **Enrollment** — Course browsing, enrollment flow, enrollment confirmation
- **Content Delivery** — Video loading, document access, lesson navigation
- **Quiz Submissions** — Quiz loading, answer selection, submission, scoring
- **Progress Tracking** — Course progress bars, completion status, certificate
- **Multimedia & Iframe** — Embedded video players, iframe navigation, PDF viewers

## Target Sites

- [OpenLearning Demo](https://www.openlearning.com) (demo)
- [Moodle Demo](https://sandbox.moodledemo.net) (demo)
- [W3Schools](https://www.w3schoolss.com) (for iframe/multimedia practice)

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run Tests

```bash
# All tests
pytest

# By category
pytest -m smoke
pytest -m educational
pytest -m multimedia

# Generate HTML report
pytest --html=reports/report.html --self-contained-html
```

## Tech Stack

- Python 3 + Selenium 4 + pytest
- Page Object Model design pattern
- WebDriver Manager for automatic browser driver management

## Intern

**M Vignesh Sai** — Slash Mark Internship (June 2026)
