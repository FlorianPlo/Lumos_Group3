# **Zenith Active Solutions: Assessment Center Challenge**

## 1. Introduction & Context

Welcome, consultants. Your group has been engaged by **Zenith Active Solutions**, a mid-sized, direct-to-consumer (D2C) e-commerce retailer specializing in fitness equipment, apparel, and supplements.

**The Company Story:**
Zenith Active was a classic startup success. Founded in a dorm room in 2018, it experienced explosive growth during the 2020-2021 fitness boom. This "built-the-plane-while-flying-it" growth caused them to scale from a small storage unit to a massive warehouse, expanding their product line from one SKU to over 200.

**The Core Problem:**
While sales have tripled, profitability has shrunk to near-zero. The new COO has hired your team because they believe the company is "leaking profit" due to operational inefficiencies that were ignored during the rapid growth phase.

Your job is to act as an external data and business strategy team. You must use the provided data to find the leaks, quantify the financial damage, and propose solutions.

## 2. Data & Document Manifest

You have been given access to a complete snapshot of the company's data and internal communications. Note that the data is provided in its "raw" format, simulating a real-world data discovery task.

### A. The Core Data Pack (Quantitative)
* **`transactions.db`**: A **SQL database file** containing the complete log of all customer orders for the past year. You will need to query this to extract transaction data.
* **`product_catalog.csv`**: A CSV file mapping all `ProductID`s to their attributes (`CostPrice`, `SellingPrice`, `Weight_kg`, `StorageRequirements`, etc.).
* **`inventory_snapshot.csv`**: A CSV file containing a *daily* log of warehouse stock levels, including `Quantity_On_Hand` and `Average_Days_In_Stock`.
* **`employee_roster.xlsx`**: An **Excel file** containing the master list of all warehouse staff, their `EmploymentType` (Full-Time/Part-Time), `PayRate`, and `PayType` (Salary/Hourly).
* **`region_costs.json`**: A **JSON file** detailing the logistics cost *rules* for shipping, including `Base_Delivery_Fee` and `Per_Kg_Fee` for each region.
* **`city_regions.csv`**: A CSV file used as a key for linking a `Customer_City` to a specific shipping `RegionID`.
* **`storage_cost_lookup.csv`**: A CSV file with the *daily cost* for each type of warehouse storage.
* **`Daily_Employee_Shifts/`**: A **folder** containing a year's worth of daily shift logs. Each day has its own subfolder containing a `.txt` file with that day's shift information.

### B. The "Notes & Documents" Pack (Qualitative)
This folder contains all qualitative context. It is a single source for internal memos, marketing plans, reports, and communications.
* `Customer Complaint Emails`
* `Warehouse Manager's Weekly Notes`
* `Employee Satisfaction Survey (Selected Comments)`
* `Finance Memos & Reports`
* `"Project Get-Big" Marketing Plan`
* `Company Logo & Promotional Materials`
* `Internal Company Mottos`

## 3. Your Mission & Suggested Workflow

Your group's mission is to **identify, quantify, and propose solutions for the company's 1-3 most significant profit leaks.**

We recommend the following workflow:

1.  **For Participants with a More Technical Focus:**
    * Your primary task is **data extraction, transformation, and mining**. You will need to query the database, parse the JSON, read the Excel file, and consolidate the many daily shift files to create usable datasets.
    * Your goal is to build a "joint data format" — a set of clean, summary tables (e.g., net profit per order, daily storage cost per product) that the *entire team* can then use for their analysis.

2.  **For Participants with a More Business/Marketing Focus:**
    * Your primary task is the **contextual and strategic analysis**.
    * Dive into the `Notes_and_Documents_Pack`. Your goal is to synthesize the "story" behind the problems.
    * Use these documents to build hypotheses (e.g., "The marketing plan seems flawed... I wonder if the *data* shows if it's profitable?").
    * Analyze the company's brand, marketing, and internal communications for strategic flaws.

3.  **Team Collaboration (The Merge):**
    * The two streams *must* merge. The business team's hypotheses should help focus the tech team's analysis. The tech team's findings (e.g., "This specific customer segment is highly unprofitable") must be connected to the business team's context (e.g., "...and the marketing plan is spending 80% of its budget acquiring them!").

## 4. Final Deliverable: A Slide Presentation

Your team will present your findings to the "Zenith Executive Board" (your assessors).

* **Format:** A brief presentation (max 15 slides).
* **Content:** For each major issue you identify, you *must* cover:
    1.  **The Finding:** What is the problem?
    2.  **The Evidence:** The key graph, KPI, or data point that proves it.
    3.  **The Root Cause:** *Why* is it happening? (This should combine data and qualitative insights).
    4.  **Recommendations:** What are the immediate, actionable steps the company should take?
    5.  **Prevention Mechanism:** How do we create a *system* to stop this from happening again?

## 5. A Note on "Prevention Mechanisms"

This is the most critical part of your recommendation. We don't just want you to find the problem; we want you to propose a sustainable, data-driven system to prevent it.

* **Example Problem (Hypothetical):** The company has a high customer churn rate; 70% of customers make one purchase and never return.
    * *Bad Recommendation:* "Get more customers."
    * *Good Recommendation:* "Implement a 'Welcome Series' email campaign for first-time buyers to improve retention."
    * *Picture-Perfect Solution:* "Propose the logic for an automated retention script. For example: 'A daily script queries the `transactions.db`. If a `CustomerID` has 1 order and is 30 days past their first purchase, they are automatically added to the 'Welcome Series' email list. If they are 90 days past and still no second order, they are flagged for a 'We miss you' promotion.' This creates a system to improve Customer Lifetime Value."

* **Example Problem (Hypothetical):** The company frequently sells out of its most popular, high-margin products, leading to lost sales.
    * *Good Recommendation:* "Order more inventory of popular items."
    * *Picture-Perfect Solution:* "Design the logic for an 'Automated Restocking Alert System.' This system would run daily, comparing the `inventory_snapshot.csv` (for `Quantity_On_Hand`) against the `transactions.db` (to calculate 30-day sales velocity). If `Quantity_On_Hand` for any high-margin item drops below a 45-day supply, it automatically flags the procurement team to re-order."



Good luck)).

# 6.Setup (Optional)

You can use what you want for this change, here is just a recommended set-up.

### **Recommended Tech Stack & OS-Specific Quickstart**

This setup is lightweight, fast, and powerful enough to handle every part of this challenge, from data consolidation to final visualizations.

#### 1\. The Recommended Stack

  * **Language:** Python 3.10+
  * **IDE (Editor):** VS Code
  * **Key VS Code Extensions:**
      * `Python` (from Microsoft)
      * `Jupyter` (from Microsoft)

#### 2\. The 7-Step Quickstart Guide (Windows & macOS)

This will get you from zero to a running analysis notebook in minutes.

**Step 1: Install Python (The Right Way)**

  * **On Windows:**
    1.  Go to `python.org` and download the installer.
    2.  Run the installer.
    3.  **CRITICAL:** On the first screen, check the box that says **"Add Python 3.x to PATH"**. This is the most common failure point.
  * **On macOS:**
    1.  Go to `python.org` and download the macOS installer.
    2.  Run the installer.
    3.  **NOTE:** Your Mac already has a built-in Python. *Do not use it.* It's old and grumpy and will cause problems. The installer from `python.org` will set up a new, modern version.

**Step 2: Install VS Code & Extensions**
Get it from `code.visualstudio.com`. Once installed, open it, go to the **Extensions** tab (the four squares icon), and install the `Python` and `Jupyter` extensions.

**Step 3: Set Up Your Project Folder**

1.  Create a folder for this project (e.g., `Zenith_Analysis`).
2.  Unzip all the data files (`transactions.db`, `product_catalog.csv`, `Daily_Employee_Shifts/` folder, etc.) into this one folder.
3.  Open this folder in VS Code (`File > Open Folder...`).

**Step 4: Create Your Virtual Environment**
This is a clean sandbox for this project.

1.  Open a new terminal in VS Code (`View > Terminal`).
2.  Run the following command in your terminal:
      * **On Windows:** `python -m venv venv`
      * **On macOS/Linux:** `python3 -m venv venv` (You'll likely use `python3` to point to the new version you just installed).

**Step 5: Activate Your Virtual Environment**
This is the most important step. You must do this *every time* you open a new terminal for this project.

  * **On Windows (in the VS Code Terminal):**
    ```bash
    .\venv\Scripts\activate
    ```
  * **On macOS/Linux (in the VS Code Terminal):**
    ```bash
    source venv/bin/activate
    ```

Your terminal prompt should now have a `(venv)` prefix. If it does, you've won.

**Step 6: Install Your Toolkit (The Libraries)**

1.  In your project folder, create a new file named `requirements.txt`.
2.  Copy and paste the text from the box below into that file.
3.  In your **activated** terminal, run this one command:
    ```bash
    pip install -r requirements.txt
    ```
    This will install all the packages you need in one go.

**Step 7: Launch Your Notebook**

1.  Create a new file in VS Code named `analysis.ipynb`.
2.  VS Code will automatically open it as a Jupyter Notebook.
3.  **Crucial Step:** In the top-right corner, click "Select Kernel." A dropdown will appear. Be sure to select the kernel that has `(venv)` in its name. This ensures your notebook uses the libraries you just installed.

You are now ready to analyze.

-----

### **Your Toolkit: `requirements.txt` & Why You Need It**

Here is the content for your `requirements.txt` file.

```text
# requirements.txt
pandas
numpy
openpyxl
SQLAlchemy
jupyter
notebook
matplotlib
seaborn
```

#### What's in this toolkit?

  * **`pandas`**

      * **What it is:** The workhorse for data analysis in Python.
      * **Why you need it:** You'll use this to load and manipulate the **`.csv` files** (`product_catalog`, `inventory_snapshot`, etc.). It's also what you'll use to read the **`.json` file** (`pd.read_json`) and the **`.xlsx` file** (`pd.read_excel`).

  * **`numpy`**

      * **What it is:** The foundational package for numerical computing.
      * **Why you need it:** Pandas is built on it. It's essential for data cleaning (handling `np.nan` values, which you may find) and any numerical operations.

  * **`openpyxl`**

      * **What it is:** The key that unlocks Excel files.
      * **Why you need it:** Pandas *requires* this library to be installed to be able to read your `employee_roster.xlsx` file.

  * **`SQLAlchemy`**

      * **What it is:** The "translator" that lets Python speak SQL.
      * **Why you need it:** This is how you'll connect to and query the `transactions.db` **SQL database file**. You can write a SQL query (e.g., `SELECT * FROM transactions`) and use Pandas to load the results directly into a DataFrame.

  * **`jupyter` & `notebook`**

      * **What it is:** The engine that runs `.ipynb` notebooks.
      * **Why you need it:** This allows you to write your code, view your data tables, and see your graphs all in one interactive document.

  * **`matplotlib` & `seaborn`**

      * **What it is:** Your plotting and visualization libraries.
      * **Why you need it:** You can't just *say* there's a problem; you need to *show* it. These will make the graphs for your 10-slide presentation (e.g., "Labor Cost per Transaction by Month").s

**A Note on the `Daily_Employee_Shifts/` Folder:**
This one is a special challenge. No library will magically "un-folder" it for you. You'll need to use standard Python libraries like `os` and `glob` to write a small loop that:

1.  Finds all the `.txt` files inside all the subfolders.
2.  Opens and reads each one.

3.  Combines them all into a single, clean list or DataFrame for your analysis.
