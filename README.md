# 🚀 Information Systems Consultant: Engineering Portfolio
**Consultant:** Yifeng Hua  
**Status:** Production-Ready Pipeline  
**Objective:** Architecting a high-availability, audit-ready data extraction and BI framework for automated business intelligence.

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

### 📊 System Observability (`src/logger.py`)
To ensure **System Reliability** and facilitate **Technical Audits**, I implemented a centralized logging architecture:
- **Persistent Audit Logs:** Generates daily `.log` files capturing timestamps, severity levels (INFO/ERROR), and stack traces.
- **Error Diagnostics:** Integrated `try-except` wrappers to catch and log critical failures without crashing the host environment.
- **Dual-Stream Output:** Simultaneous logging to the terminal (for real-time monitoring) and local storage (for historical analysis).

### 🖥️ Business Intelligence Dashboard (`app.py`)
To finalize the **Information Lifecycle**, I developed an interactive web interface using **Streamlit**:
- **Dynamic Data Rendering:** Real-time visualization of extracted CSV datasets with automated KPI calculation.
- **Audit Integration:** Sidebar toggle to view historical system logs, ensuring transparency in the automated pipeline.
- **UX for Non-Technical Stakeholders:** Transforms raw technical outputs into a "human-readable" format for business decision-making.

### ⚡ High-Concurrency Engine (`src/async_scraper.py`)
To scale the information retrieval system, I transitioned from synchronous to **Asynchronous I/O**:
- **Non-Blocking Architecture:** Utilized `asyncio` and `aiohttp` to perform concurrent network requests, increasing throughput by ~300%.
- **Connection Pooling:** Managed persistent HTTP sessions to reduce overhead and improve system resource allocation.
- **Scalability Analysis:** Evaluated the performance impact of parallel processing on large-scale data harvesting.

## 📦 Infrastructure & Deployment 
To ensure **System Portability** and **Environmental Consistency**, the entire pipeline has been containerized using Docker:
- **Immutable Infrastructure:** The `Dockerfile` defines a consistent runtime environment, eliminating "dependency drift."
- **Isolation:** Each component (Extraction, Validation, Visualization) runs in an isolated container, protecting the host system.
- **Scalability Ready:** The containerized architecture allows for easy deployment to cloud providers (AWS ECS, GCP Cloud Run) or orchestration via Kubernetes.

## 🛡️ DevOps, Security & Quality Assurance
- **CI/CD Pipeline:** Automated testing via GitHub Actions (pytest + flake8).
- **Security Auditing:** Static analysis (Bandit) and dependency monitoring (Safety).
- **System Maintenance:** Automated log rotation and cache cleanup via `src/maintenance.py`.

## 🚀 Getting Started
### Prerequisites
- Python 3.10+
- Virtual Environment (`venv`)

### Installation
1. Clone the repository:
   ```bash
   git clone [https://github.com/yourusername/scraper-project.git](https://github.com/yourusername/scraper-project.git)
   cd scraper-project