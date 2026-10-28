# School Data Management System

A lightweight, object-oriented School Data Management System built in Python 3, designed specifically for resource-constrained educational environments (such as rural secondary schools and vocational institutes in Sierra Leone). 

This project adheres to **Digital Public Goods (DPG)** standards, emphasizing open-source reusability, privacy-respecting architecture, and hardware-agnostic deployment on legacy systems.

---

## Features

- **Object-Oriented Architecture:** Built using clean Python `dataclasses` and decoupled entities (`Teacher`, `Student`, `School`).
- **Optimized Data Structures:** Utilizes Python dictionaries for $O(1)$ fast lookups by unique identification numbers, preventing duplicate records.
- **Privacy-by-Design:** Stores only essential administrative data (IDs, names, subjects, grades, majors) while omitting sensitive personal information.
- **Lightweight CLI:** Command-line interface with built-in robust input validation, ensuring it runs smoothly on low-spec hardware without graphical overhead.

---

## Project Structure

```text
school_data_management/
│
├── main.py            # Entry point / CLI loop
├── models.py          # Teacher and Student dataclasses
├── school.py          # School manager class for dictionary storage & logic
└── README.md          # Project documentation
