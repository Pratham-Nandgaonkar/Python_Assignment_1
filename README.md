# 🐉 Houses of Ice and Fire

> **A clean Python API integration project that retrieves, validates,
> processes, sorts, and exports all Houses of Westeros and Essos.**

```{=html}
<p align="center">
```
`<img src="architecture-diagram.png" alt="Houses of Ice and Fire Architecture Diagram" width="100%">`{=html}
```{=html}
</p>
```
```{=html}
<p align="center">
```
`<b>`{=html}Python 3.x`</b>`{=html} • `<b>`{=html}Requests`</b>`{=html}
• `<b>`{=html}REST API`</b>`{=html} •
`<b>`{=html}Pagination`</b>`{=html} • `<b>`{=html}Data
Validation`</b>`{=html} • `<b>`{=html}File Processing`</b>`{=html}
```{=html}
</p>
```

------------------------------------------------------------------------

## 📌 Project Overview

**Houses of Ice and Fire** is a Python-based API integration project
built using the **An API of Ice and Fire** public REST API.

The assignment requires the application to:

-   Retrieve **all houses** and their regions from the API.
-   Handle the API's paginated response.
-   Extract only the required `name` and `region` fields.
-   Validate incoming API data.
-   Sort houses alphabetically.
-   Export the final dataset into a readable text file.
-   Handle API, network, validation, and file-related errors gracefully.

The current API response contains **444 houses**, and the application
retrieves the complete dataset rather than relying on the API's default
first page of 10 records.

------------------------------------------------------------------------

## 🏗️ Architecture

The application follows a simple, maintainable pipeline:

``` text
┌──────────────────────────┐
│  An API of Ice and Fire  │
│        REST API          │
└────────────┬─────────────┘
             │
             │ Paginated Requests
             ▼
┌──────────────────────────┐
│      Data Retrieval      │
│ page=1, 2, 3 ...         │
│ pageSize=100              │
└────────────┬─────────────┘
             │
             │ All house records
             ▼
┌──────────────────────────┐
│    Data Validation       │
│ • Validate response      │
│ • Validate records       │
│ • Ignore malformed data  │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│    Data Processing       │
│ • Extract name + region  │
│ • Clean string values    │
│ • Sort alphabetically    │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│      File Output         │
│   output/houses.txt      │
└──────────────────────────┘
```

### 🔄 End-to-End Flow

1.  Connect to the external REST API.
2.  Request house records using pagination.
3.  Continue requesting pages until the API returns no more records.
4.  Combine all retrieved records into one collection.
5.  Validate the API response structure.
6.  Extract each house's `name` and `region`.
7.  Clean and validate individual fields.
8.  Sort houses alphabetically using case-insensitive comparison.
9.  Write the final dataset to `output/houses.txt`.
10. Display a clear execution summary in the terminal.

------------------------------------------------------------------------

## 🧠 Why Pagination?

The API does **not** return every house in a single default request.

A request to:

``` text
/api/houses
```

returns only the first page by default.

The application therefore explicitly uses:

``` text
?page=1&pageSize=100
?page=2&pageSize=100
?page=3&pageSize=100
...
```

Requests continue until the API returns an empty list.

This is important because the assignment asks for **all houses**, not
merely the first 10 records returned by the API.

### Pagination Strategy

``` python
page = 1

while True:
    request page
    receive houses

    if no houses:
        stop

    add houses to collection
    page += 1
```

This approach makes the application independent of the current total
number of houses.

------------------------------------------------------------------------

## ✨ Key Features

  Feature                   Implementation
  ------------------------- --------------------------------------------
  🌐 REST API Integration   `requests` library
  📄 Pagination             `page` + `pageSize` parameters
  🛡️ Response Validation    Verifies API returns a list
  🧹 Data Cleaning          Strips unnecessary whitespace
  🔎 Record Validation      Handles malformed records safely
  🔤 Alphabetical Sorting   Case-insensitive `casefold()`
  📁 File Generation        UTF-8 encoded text output
  ⏱️ Request Timeout        10-second API timeout
  🚨 Error Handling         Network, HTTP, JSON/data, and file errors
  🧩 Modular Design         Separate functions for each responsibility

------------------------------------------------------------------------

## 🛠️ Tech Stack

### Python 3.x

Used as the primary programming language for API communication, data
processing, validation, sorting, and file generation.

### Requests

Used for making HTTP GET requests to the external REST API.

### pathlib

Used for reliable, platform-independent file path management.

### An API of Ice and Fire

Public REST API providing data about the fictional world of *A Song of
Ice and Fire*.

**Endpoint:**

``` text
https://anapioficeandfire.com/api/houses
```

------------------------------------------------------------------------

## 📂 Project Structure

``` text
houses-of-ice-and-fire/
│
├── src/
│   └── houses.py
│
├── output/
│   └── houses.txt
│
├── screenshots/
│   ├── 01_program_execution.png
│   └── 02_generated_output.png
│
├── architecture-diagram.png
├── README.md
├── requirements.txt
├── .gitignore
└── venv/
```

### Directory Responsibilities

**`src/`**

Contains the application's Python source code.

**`output/`**

Contains the generated text file containing sorted house information.

**`screenshots/`**

Contains evidence of successful program execution and generated output.

**`requirements.txt`**

Lists Python dependencies required by the project.

**`.gitignore`**

Prevents local virtual-environment and Python cache files from being
committed.

------------------------------------------------------------------------

## 🚀 Getting Started

### 1. Clone the repository

``` bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd houses-of-ice-and-fire
```

### 2. Create a virtual environment

``` bash
python -m venv venv
```

### 3. Activate the virtual environment

#### Windows Command Prompt

``` cmd
venv\Scripts\activate.bat
```

#### Windows PowerShell

``` powershell
venv\Scripts\Activate.ps1
```

> If PowerShell execution policies prevent activation, use Command
> Prompt or activate the environment through another permitted shell.

### 4. Install dependencies

``` bash
pip install -r requirements.txt
```

### 5. Run the application

``` bash
python src/houses.py
```

------------------------------------------------------------------------

## 💻 Expected Console Output

A successful execution looks like:

``` text
=======================================================
           HOUSES OF ICE AND FIRE
=======================================================

Fetching house data from the API...
✓ Successfully fetched 444 houses.
✓ Extracted 444 house records.
✓ Sorted houses alphabetically.
✓ Saved results to output/houses.txt.

Process completed successfully.
=======================================================
```

> The number of houses is dynamic and may change as the API dataset
> changes.

------------------------------------------------------------------------

## 📄 Output Format

The application generates:

``` text
output/houses.txt
```

Each line follows this format:

``` text
House Name - Region
```

Example:

``` text
House Algood - The Westerlands
House Allyrion of Godsgrace - Dorne
House Amber - The North
House Ambrose - The Reach
House Appleton of Appleton - The Reach
House Arryn of Gulltown - The Vale
House Arryn of the Eyrie - The Vale
```

The records are ordered alphabetically by house name.

------------------------------------------------------------------------

## 🧩 Code Design

The application is divided into focused functions so that each part has
a clear responsibility.

### `fetch_houses()`

Responsible for:

-   Making API requests.
-   Handling pagination.
-   Validating the API response.
-   Combining all pages into one collection.

### `extract_house_data()`

Responsible for:

-   Validating individual records.
-   Extracting `name`.
-   Extracting `region`.
-   Cleaning string values.

### `sort_houses()`

Responsible for alphabetically sorting the extracted house records.

### `save_to_file()`

Responsible for:

-   Creating the output directory when required.
-   Writing the processed data to `houses.txt`.
-   Using UTF-8 encoding.

### `main()`

Coordinates the complete workflow and provides user-friendly execution
feedback.

------------------------------------------------------------------------

## 🛡️ Error Handling

The application handles several failure scenarios explicitly.

### API Timeout

``` text
✗ API request timed out.
```

### Connection Failure

``` text
✗ Could not connect to the API.
```

### HTTP Error

``` text
✗ API returned an HTTP error: ...
```

### Invalid API Data

``` text
✗ Data validation error: ...
```

### File System Error

``` text
✗ File operation failed: ...
```

This prevents the application from failing silently and provides
meaningful feedback when something goes wrong.

------------------------------------------------------------------------

## 🧪 Verification

The project can be verified using three important checks.

### Record Count

``` bash
python -c "from pathlib import Path; lines=Path('output/houses.txt').read_text(encoding='utf-8').splitlines(); print('Total lines:', len(lines))"
```

Expected current result:

``` text
Total lines: 444
```

### Alphabetical Ordering

``` bash
python -c "from pathlib import Path; lines=Path('output/houses.txt').read_text(encoding='utf-8').splitlines(); print('Alphabetically sorted:', lines == sorted(lines, key=str.casefold))"
```

Expected:

``` text
Alphabetically sorted: True
```

### Complete Program Test

``` bash
python src/houses.py
```

Expected:

``` text
✓ Successfully fetched ...
✓ Extracted ...
✓ Sorted houses alphabetically.
✓ Saved results to output/houses.txt.
```

------------------------------------------------------------------------

## 📸 Screenshots

The repository includes screenshots demonstrating:

1.  Successful API retrieval and processing.
2.  Generated and alphabetically sorted output.

``` text
screenshots/
├── 01_program_execution.png
└── 02_generated_output.png
```

------------------------------------------------------------------------

## 🎯 Assignment Mapping

  Assignment Requirement                  Implementation           Status
  --------------------------------------- ------------------------ --------
  Create list of all houses and regions   `extract_house_data()`   ✅
  Retrieve data using API                 `fetch_houses()`         ✅
  Retrieve all records                    Pagination               ✅
  Write list to text file                 `save_to_file()`         ✅
  Order houses alphabetically             `sort_houses()`          ✅
  Use appropriate libraries               `requests`, `pathlib`    ✅
  Follow code organization practices      Modular functions        ✅
  Document the project                    This README              ✅
  Provide output screenshots              `screenshots/`           ✅

------------------------------------------------------------------------

## 📈 Design Decisions

### Why `requests`?

It is a lightweight and widely used Python HTTP library that provides a
clean interface for REST API communication.

### Why pagination?

The API returns data in pages. Pagination ensures the application
retrieves the complete dataset rather than silently processing only the
first page.

### Why `pathlib`?

`pathlib` provides a cleaner and more portable way to work with file
paths across operating systems.

### Why separate functions?

Each function has one primary responsibility, making the code easier to
understand, test, maintain, and extend.

### Why validate API data?

External APIs should not automatically be treated as perfectly reliable.
Basic validation prevents malformed responses or records from causing
unexpected application failures.

------------------------------------------------------------------------

## 🔮 Possible Future Improvements

The current implementation intentionally stays focused on the assignment
requirements. Possible extensions include:

-   [ ] Add automated unit tests with `pytest`.
-   [ ] Add structured logging.
-   [ ] Export data to CSV or JSON.
-   [ ] Add command-line arguments for page size and output location.
-   [ ] Add retry logic for temporary network failures.
-   [ ] Add API response caching.
-   [ ] Add a small interactive dashboard for exploring houses.
-   [ ] Add CI checks using GitHub Actions.

------------------------------------------------------------------------

## 👨‍💻 Author

**Pratham Nandgaonkar**

Engineering Intern

### Project

**Houses of Ice and Fire**

Built as a Python API integration and data-processing assignment.

------------------------------------------------------------------------

## 📜 License

This project was created for educational and professional evaluation
purposes.

------------------------------------------------------------------------

```{=html}
<p align="center">
```
`<b>`{=html}⚔️ From API → Validation → Processing → Sorting → File
Output ⚔️`</b>`{=html}
```{=html}
</p>
```
```{=html}
<p align="center">
```
`<sub>`{=html}Built with Python and an unreasonable amount of enthusiasm
for fictional medieval houses.`</sub>`{=html}
```{=html}
</p>
```
