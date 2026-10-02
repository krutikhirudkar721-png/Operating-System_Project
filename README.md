# OS Page Replacement Simulator

A Python-based simulation project for studying and comparing **page replacement algorithms** used in Operating Systems.

The simulator implements:

* **FIFO (First-In-First-Out)**
* **LRU (Least Recently Used)**
* **Optimal Page Replacement**

For a given reference string and number of memory frames, the program calculates page faults, page hits, replacements, hit ratio, and fault ratio.

---

## 📌 Project Overview

In a virtual memory system, a page fault occurs when a process references a page that is not currently available in physical memory.

When all available frames are occupied, the Operating System must decide which existing page should be removed. This decision is made using a **page replacement algorithm**.

This project demonstrates how different page replacement strategies behave for the same reference string.

---

## 🚀 Algorithms Implemented

### 1. FIFO – First-In-First-Out

FIFO replaces the page that has been present in memory for the longest period of time.

**Idea:**

> The first page loaded into memory is the first page to be replaced.

**Advantages:**

* Simple to understand
* Easy to implement
* Low implementation overhead

**Limitation:**

* It does not consider how frequently or recently a page is being used.
* It can suffer from **Belady's Anomaly**, where increasing the number of frames can sometimes increase page faults.

---

### 2. LRU – Least Recently Used

LRU replaces the page that has not been used for the longest period of time.

**Idea:**

> Pages that have not been used recently are more likely to be replaced.

LRU attempts to exploit the principle of **temporal locality**.

**Advantages:**

* Usually performs better than simple FIFO on many workloads
* Makes use of recent page-access information

**Limitation:**

* Requires additional tracking of page usage
* More implementation overhead than FIFO

---

### 3. Optimal Page Replacement

The Optimal algorithm replaces the page whose next use is farthest in the future.

**Idea:**

> Replace the page that will be needed latest in the future, or will never be needed again.

Optimal provides the minimum possible number of page faults for a known reference string and frame count.

However, a real Operating System cannot generally know future page references, so this algorithm is primarily useful as a **theoretical benchmark** for comparing other algorithms.

---

## 📊 Metrics Calculated

The simulator reports:

| Metric       | Description                                          |
| ------------ | ---------------------------------------------------- |
| Page Faults  | Number of references that were not present in memory |
| Page Hits    | Number of references already present in memory       |
| Replacements | Number of times an existing page was replaced        |
| Hit Ratio    | Page Hits / Total References                         |
| Fault Ratio  | Page Faults / Total References                       |

---

## 🧠 Step-by-Step Simulation

The program can display the state of every memory frame after each page reference.

Example:

```text
Step   Page    F1    F2    F3    Status
-----------------------------------------
1       7       7     -     -    FAULT
2       0       7     0     -    FAULT
3       1       7     0     1    FAULT
4       2       2     0     1    FAULT (R:7)
5       0       2     0     1    HIT
```

`R:x` indicates that page `x` was replaced.

---

## 🛠️ Requirements

* Python 3.8+
* No external libraries required

The project uses only Python's standard library.

---

## ▶️ How to Run

Clone the repository:

```bash
git clone <your-repository-url>
cd OS-Page-Replacement
```

Run the program:

```bash
python page_replacement.py
```

---

## 📝 Input Format

The program asks for:

### Reference String

Enter page references separated by spaces.

Example:

```text
7 0 1 2 0 3 0 4 2 3 0 3 2
```

### Number of Frames

Example:

```text
3
```

---

## 📈 Example

Input:

```text
Enter reference string (space-separated): 7 0 1 2 0 3 0 4
Enter number of frames: 3
```

The simulator executes FIFO, LRU, and Optimal independently and displays their statistics.

Example comparison format:

```text
==================================================================================
ALGORITHM COMPARISON
==================================================================================
Algorithm      Faults      Hits        Replacements    Hit Ratio    Fault Ratio
----------------------------------------------------------------------------------
FIFO           ...         ...         ...             ...          ...
LRU            ...         ...         ...             ...          ...
Optimal        ...         ...         ...             ...          ...
==================================================================================
```

The exact values depend on the supplied reference string and number of frames.

---

## ⏱️ Complexity

Let:

* `n` = number of page references
* `f` = number of frames

### FIFO

Approximately:

```text
Time:  O(n × f)
Space: O(f + n)
```

### LRU

The current educational implementation maintains a list of recently used pages.

```text
Time:  O(n × f)
Space: O(f + n)
```

### Optimal

For every page fault, the algorithm searches the future reference string to determine which page will be needed last.

```text
Time:  O(n²)
Space: O(f + n)
```

The implementation prioritizes clarity and educational value over low-level optimization.

---

## 📂 Project Structure

```text
OS-Page-Replacement/
│
├── page_replacement.py
├── README.md
└── LICENSE
```

---

## 🎯 Learning Objectives

This project demonstrates:

* Virtual memory concepts
* Page faults and page hits
* Memory-frame management
* FIFO page replacement
* LRU page replacement
* Optimal page replacement
* Hit and fault ratios
* Algorithm comparison
* Simulation of memory state
* Basic Python software design

---

## 🔬 Important Observation

The number of page faults depends on both:

1. The selected page replacement algorithm
2. The number and order of memory references

Therefore, the simulator should be used with multiple reference strings and frame counts when studying algorithm behavior.

Optimal Page Replacement is included primarily as a theoretical reference because it assumes knowledge of future page references.

---

## 👨‍💻 Author

**Your Name**

Operating Systems Mini Project
Page Replacement Algorithm Simulator

---

## 📜 License

This project is intended for educational purposes.
