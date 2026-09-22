# Smart Warehouse & Inventory Management System (SWIMS)

A comprehensive, console-based inventory control, stock monitoring, supplier directory, and transaction auditing utility built entirely using core Python primitives (lists, tuples, dictionaries, strings, and loops).

---

## Prerequisites

- **Python 3.x**: Ensure Python 3 is installed on your system. You can verify your installation by running:
  ```bash
  python --version
  ```
  *(or `python3 --version` depending on your operating system).*

- No external libraries, packages, or databases (`pip install`) are required. SWIMS runs entirely on built-in Python modules.

---

## Project File Structure

Your project root directory should contain the following files:
```text
swims-project/
│
├── inventory_management.py   # Main Python source code
├── PROJECT_REPORT.md         # Detailed project report
└── README.md                 # Setup and execution guide
```

---

## How to Set Up and Run the Project

Follow these step-by-step instructions to execute the project from the command line:

### Step 1: Open Your Terminal / Command Prompt
- **Windows:** Press `Win + R`, type `cmd`, and press Enter. Alternatively, open PowerShell or VS Code Integrated Terminal.
- **macOS / Linux:** Open your default Terminal application.

### Step 2: Navigate to the Project Directory
Change your current working directory to the folder where you saved the project files:
```bash
cd path/to/swims-project
```

### Step 3: Run the Python Script
Execute the script using the Python interpreter:
```bash
python inventory_management.py
```
*(On macOS/Linux, you may need to use `python3 inventory_management.py`)*

---

## System Menu Overview

Once executed, the application displays an interactive command-line menu:
1. **View Inventory Stock:** Displays a formatted tabular view of all stored products, categories, pricing, quantities, and associated suppliers.
2. **Add New Product:** Onboards a new item with unique ID validation, category picker, numerical price/quantity checks, and audit logging.
3. **Update Stock (Restock / Dispatch):** Handles inbound stock increments and outbound stock dispatches with built-in stock depletion safeguards.
4. **Search Product:** Performs case-insensitive keyword searches across product names and categories.
5. **Manage Suppliers Directory:** A dedicated sub-menu to view registered suppliers or add new supplier records.
6. **Warehouse Reports & Analytics:** Calculates cumulative asset valuations, total units, premium item flags, low-stock alerts (< 20 units), and recent transaction audit logs.
7. **Exit System:** Safely terminates the application.
