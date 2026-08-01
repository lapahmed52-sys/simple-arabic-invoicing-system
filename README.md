# Simple Arabic Invoicing System

## Overview
This repository contains a simple command-line invoicing program written in Python[cite: 2]. It is designed to operate with an Arabic user interface, allowing users to create invoices, add products, calculate totals, and save the final receipt as a text file[cite: 2].

## Features
* **Auto-Incrementing Invoice Numbers:** The program automatically assigns the next available invoice number by reading from and updating a local `last_invoice_number.txt` file[cite: 2].
* **Predefined Product Database:** Includes built-in products like fresh milk, local bread, tea, and Egyptian rice with their respective prices[cite: 2].
* **Automated File Saving:** Generates a formatted text file for each invoice and saves it automatically to the `D:\Invoices` directory[cite: 2]. If the directory does not exist, the program will create it[cite: 2].
* **Object-Oriented Design:** Utilizes `Product` and `Invoice` classes to maintain a clean code structure[cite: 2].
* **Input Validation:** Ensures that users enter valid product keys and quantities greater than zero[cite: 2].

## Prerequisites
* Python 3.x installed on your machine.
* Write access to the `D:\` drive (or you can modify the `INVOICES_DIR` variable in the code to match your preferred path)[cite: 2].

## How It Works (Usage)
1. **Start the Program:** Run the script using Python. The program will display a list of available products along with their corresponding keys (1, 2, 3, 4) and prices[cite: 2].
2. **Create an Invoice:** A new invoice is automatically generated with a unique number[cite: 2].
3. **Add Items:** 
   * Enter the key of the product you wish to add[cite: 2].
   * Specify the required quantity for the selected product[cite: 2].
4. **Generate and Save:** Once all items are added, type `p` to print and save the invoice[cite: 2]. The program will display the invoice details, including itemized costs and the final total, and save it as a text file (e.g., `Invoice_1.txt`)[cite: 2].
5. **Continue or Exit:** Type `p` to start another invoice or `exit` to close the program[cite: 2].
6. Output format:
7. <img width="1060" height="477" alt="Screenshot 2026-08-02 022039 PYTHON" src="https://github.com/user-attachments/assets/35bde1ad-21ca-49c0-94ee-c89a0b9658c7" />
