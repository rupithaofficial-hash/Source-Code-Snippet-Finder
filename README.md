# 🔎 Source Code Snippet Finder

A Flask-based **Information Retrieval application** that allows users to search and retrieve relevant Python code snippets using keyword-based search and relevance ranking.

This project demonstrates practical **Information Retrieval concepts** such as text processing, document retrieval, relevance scoring, and ranked search results through a simple and user-friendly web application.

---

## 📌 Project Overview

Developers and students often need to find small pieces of code quickly instead of searching through multiple files or websites.

The **Source Code Snippet Finder** provides a simple solution by maintaining a collection of reusable Python code snippets and allowing users to search them using keywords.

The system:

* Searches across a collection of Python code snippets
* Processes the user's search query
* Calculates relevance scores
* Ranks matching snippets
* Displays the most relevant results
* Allows users to copy snippets directly from the interface

This project demonstrates how **Information Retrieval techniques can be applied to a practical developer-focused problem**.

---

## 🎯 Objectives

* Build a simple code snippet retrieval system
* Apply basic Information Retrieval concepts to source code
* Rank search results according to query relevance
* Provide a clean interface for finding reusable code
* Integrate a Python retrieval system with a Flask web application

---

## ✨ Key Features

### 🔍 Keyword-Based Search

Search for Python code snippets using keywords related to the required functionality.

### 📊 Relevance Ranking

Matching snippets are assigned relevance scores and displayed in ranked order.

### 💻 Code Snippet Retrieval

The system retrieves complete source-code snippets from the stored collection.

### 📋 Copy to Clipboard

Users can copy retrieved code snippets directly from the interface.

### ⚡ Instant Results

Search results are dynamically displayed through the Flask web application.

### 🎨 Simple User Interface

A clean and minimal interface makes the system easy to use and understand.

---

## 🧠 Information Retrieval Workflow

```text
                User Query
                    ↓
             Query Processing
                    ↓
          Tokenization / Matching
                    ↓
          Relevance Score Calculation
                    ↓
             Result Ranking
                    ↓
          Relevant Snippets Displayed
```

The application follows a basic Information Retrieval workflow:

1. The user enters a search query.
2. The query is processed and normalized.
3. The system searches the stored Python snippets.
4. Relevance scores are calculated.
5. Matching snippets are ranked.
6. The ranked results are displayed to the user.

---

## 🛠️ Tech Stack

| Technology       | Purpose                                |
| ---------------- | -------------------------------------- |
| **Python**       | Core application and retrieval logic   |
| **Flask**        | Web application framework              |
| **HTML**         | Web page structure                     |
| **CSS**          | User interface styling                 |
| **JavaScript**   | Client-side interactions               |
| **Git & GitHub** | Version control and project management |

---

## 📂 Project Structure

```text
Source-Code-Snippet-Finder/
│
├── app.py
├── snippet_finder.py
├── requirements.txt
├── .gitignore
│
├── templates/
│   └── index.html
│
├── code_snippets/
│   ├── binary_search.py
│   ├── linear_search.py
│   ├── stack.py
│   ├── queue.py
│   ├── db_connection.py
│   └── login_validation.py
│
└── README.md
```

---

## 🔬 Example Snippet Collection

The project contains reusable Python snippets related to:

* Binary Search
* Linear Search
* Stack
* Queue
* Database Connection
* Login Validation

The collection can be extended with additional source-code snippets.

---

## 🔎 Example Searches

Try searching for terms such as:

```text
binary
search
stack
queue
login
database
```

### Example

```text
Search Query:
binary search
```

The system retrieves matching snippets and displays them according to their relevance.

---

## 🧩 Main Components

### `app.py`

Acts as the Flask application entry point.

It handles:

* Web routes
* User search requests
* Communication between the interface and retrieval logic
* Rendering search results

### `snippet_finder.py`

Contains the core snippet retrieval and ranking logic.

It is responsible for:

* Processing search queries
* Searching the snippet collection
* Calculating relevance
* Ranking matching snippets

### `templates/index.html`

Provides the main user interface for:

* Entering search queries
* Displaying search results
* Viewing retrieved code snippets
* Copying code snippets

### `code_snippets/`

Contains the searchable Python source-code collection.

---

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/rupithaofficial-hash/Source-Code-Snippet-Finder.git
```

### 2. Navigate to the Project Folder

```bash
cd Source-Code-Snippet-Finder
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python app.py
```

### 5. Open the Application

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## 📈 Why This Project Matters

The project demonstrates how Information Retrieval concepts can be applied to a practical problem faced by developers and students.

Instead of manually searching through multiple files, users can enter a keyword and quickly retrieve relevant reusable code snippets.

The project combines:

**Information Retrieval + Python + Flask + Web Development**

into a single practical application.

---

## 🚀 Future Enhancements

Possible future improvements include:

* Syntax highlighting for retrieved code
* Search result pagination
* Programming-language filtering
* Category-based filtering
* Phrase-based search
* Improved ranking algorithms
* Stemming and stop-word processing
* Fuzzy search
* Favorites and saved snippets
* Larger and more diverse snippet collection

---

## 🎓 Learning Outcomes

Through this project, I gained practical experience in:

* Information Retrieval concepts
* Text and query processing
* Relevance-based ranking
* Python application development
* Flask web development
* Frontend and backend integration
* Organizing reusable source-code collections
* Building a searchable web application

---

## 👩‍💻 Author

**Rupitha**

Information Science and Engineering Student

🔗 **GitHub:** [https://github.com/rupithaofficial-hash](https://github.com/rupithaofficial-hash)
