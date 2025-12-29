Quick Setup:
python setup_data.py (Creates the data folder and initial data).
python main.py (Starts the system).

Key Features:
Table Management: Assigning customers to tables, capacity control, and status tracking.
Ordering System: Adding menu items to orders and creating kitchen tickets.
Invoice Calculation: Automatic calculation and splitting of bills including tax and tips.
Reporting: Daily turnover, best-selling products, and performance analysis.

Technical Structure:
OOP: Table and menu items are represented by classes.
Data Storage: All data is stored in JSON format under the data/ folder and is permanent.
Modularity: The project is divided into 6 separate modules (tables, menu, orders, storage, reports, main) as requested in the PDF.