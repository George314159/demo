# High-Efficiency Data Extraction Framework
**Technical Consultant:** Yifeng Hua

**Project Scope:** Information Systems Audit & Development

## 📌 Project Overview
This project is a modular Python-based framework designed for automated **Information Retrieval**. As part of an Information Studies initiative, it addresses the challenge of transforming unstructured web data into structured, actionable business intelligence.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Libraries:** `Requests` (Network I/O), `BeautifulSoup4` (HTML Parsing), `JSON/CSV` (Data Management)
* **Architecture:** Modular Service-Oriented Design

## 📂 Information Architecture & Data Lifecycle
The framework follows a strict **Separation of Concerns (SoC)** to ensure data integrity across the information lifecycle:

1. **Extraction (`src/scraper.py`):** Handles network I/O, HTML parsing, and initial data capture using `BeautifulSoup4`.
2. **Management (`src/data_handler.py`):** Governs the **Persistence Layer**. It normalizes raw extracted objects and exports them into interoperable formats.
3. **Storage (`data/`):** A centralized repository for structured outputs.
   - **JSON:** Optimized for web integration and hierarchical data representation.
   - **CSV:** Optimized for Business Intelligence (BI) tools and spreadsheet-based analysis.

## 🚀 Technical Features
- **Multi-Format Persistence:** Automated export to both `.json` and `.csv` formats.
- **Dynamic File Versioning:** Implemented ISO-standard timestamping (`YYYYMMDD_HHMMSS`) for all data exports to prevent overwriting and ensure auditability.
- **Directory Management:** Automated environment check to ensure the `/data` directory exists before execution, reducing runtime failures.
- **Error Resilience:** Robust exception handling for File I/O operations to maintain system uptime during disk-write cycles.

### 🔍 Data Validation Layer (`src/validator.py`)
To ensure **High-Fidelity Information Retrieval**, a validation layer was implemented to:
- **Data Sanitization:** Regex-based cleaning of raw string data to remove non-ASCII characters and redundant whitespace.
- **Schema Enforcement:** Mandatory field checks to prevent "Null" or "Empty" records from entering the persistence layer.
- **Integrity Logic:** Minimum-length constraints to ensure qualitative value in retrieved headlines.

## 🚀 Getting Started
### Prerequisites
- Python 3.10+
- Virtual Environment (`venv`)

### Installation
1. Clone the repository:
   ```bash
   git clone [https://github.com/yourusername/scraper-project.git](https://github.com/yourusername/scraper-project.git)
   cd scraper-project