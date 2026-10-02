# OS Page Replacement

A small Python project that simulates and compares three page replacement algorithms used in Operating Systems:

* FIFO (First-In-First-Out)
* LRU (Least Recently Used)
* Optimal Page Replacement

The program takes a page reference string and the number of available memory frames, then shows how each algorithm handles the page references.

It also calculates page faults, page hits, hit ratio, and fault ratio.

---

## What is Page Replacement?

In a virtual memory system, a process may request a page that is not currently present in physical memory. This causes a **page fault**.

If all available memory frames are already occupied, the operating system has to decide which page should be removed to make space for the new page.

This decision is made using a page replacement algorithm.

This project demonstrates three commonly studied algorithms: FIFO, LRU, and Optimal.

---

## Algorithms Used

### FIFO - First-In-First-Out

FIFO replaces the page that has been in memory for the longest time.

In simple terms:

> The page that entered memory first is removed first.

FIFO is easy to understand and implement, but it does not consider how recently or how frequently a page is being used.

One important property of FIFO is that it can show **Belady's anomaly**, where increasing the number of frames can sometimes result in more page faults.

---

### LRU - Least Recently Used

LRU replaces the page that has not been used for the longest time in the past.

The basic idea is that a page used recently may be needed again soon, while a page that has not been used for a long time may be less likely to be needed.

LRU uses the recent access history of pages to make the replacement decision.

In this project, a list is used to keep track of the order in which pages were recently used.

---

### Optimal Page Replacement

The Optimal algorithm replaces the page whose next use is farthest in the future.

For example, if the pages currently in memory are:

```text
1  2  3
```

and the future reference sequence shows that page `2` will be needed much later than pages `1` and `3`, page `2` can be selected for replacement.

If a page will not be used again, it can be selected immediately.

The important point is that Optimal needs to know future references. Because a real operating system cannot normally know the future access pattern, Optimal is mainly useful as a theoretical benchmark for comparing other algorithms.

---

## What Does the Program Show?

For every page reference, the program shows:

* Current page
* Contents of each frame
* Whether the reference was a `HIT` or `FAULT`
* Which page was replaced, when applicable

At the end, it displays:

* Total page faults
* Total page hits
* Hit ratio
* Fault ratio

### Example of the simulation

```text
Step   Page   F1     F2     F3     Status
-------------------------------------------------
1      7      7      -      -      FAULT
2      0      7      0      -      FAULT
3      1      7      0      1      FAULT
4      2      2      0      1      FAULT (R:7)
5      0      2      0      1      HIT
```

Here:

* `FAULT` means the page was not already in memory.
* `HIT` means the page was already present.
* `R:7` means page `7` was replaced.

---

## Input

The program asks for two things.

### 1. Reference String

Enter page numbers separated by spaces.

Example:

```text
7 0 1 2 0 3 0 4 2 3 0 3 2
```

### 2. Number of Frames

Enter the number of physical memory frames.

Example:

```text
3
```

---

## How to Run

Make sure Python is installed on your system.

Open the project folder in VS Code and run:

```bash
python page_replacement.py
```

On systems where Python is available through `python3`, use:

```bash
python3 page_replacement.py
```

No external Python packages are required.

The project uses standard Python features only.

---

## Example Input

```text
Enter reference string: 7 0 1 2 0 3 0 4 2 3 0 3 2
Enter number of frames: 3
```

For this particular reference string with three frames, the page-fault counts are:

```text
FIFO       10
LRU         9
Optimal     7
```

The exact result depends on the reference string and the number of frames.

---

## Results

The final output contains a comparison similar to:

```text
======================================================================
FINAL COMPARISON
======================================================================
Algorithm     Faults      Hits        Hit Ratio     Fault Ratio
----------------------------------------------------------------------
FIFO          10          3           23.08%        76.92%
LRU            9          4           30.77%        69.23%
Optimal        7          6           46.15%        53.85%
======================================================================
```

The values above correspond specifically to:

```text
Reference String:
7 0 1 2 0 3 0 4 2 3 0 3 2

Frames:
3
```

---

## Understanding the Results

The number of page faults depends on both:

1. The page replacement algorithm
2. The order of pages in the reference string
3. The number of available frames

Optimal provides a useful theoretical reference because it chooses the replacement using future information. FIFO and LRU make their decisions without knowing future references.

The project therefore does not label one algorithm as universally "best." Instead, it shows the actual results for the given workload.

---

## Time Complexity

Let:

* `n` = number of page references
* `f` = number of frames

### FIFO

The implementation searches the frame list for each reference.

```text
Time:  O(n × f)
Space: O(f + n)
```

### LRU

The implementation uses a list to maintain the recent-use order.

```text
Time:  O(n × f)
Space: O(f + n)
```

### Optimal

For a page fault, the program searches the future reference sequence to determine when pages will be used again.

```text
Time:  O(n²)
Space: O(f + n)
```

These are the complexities of this particular educational implementation, not necessarily the complexity of every possible implementation of these algorithms.

---

## Project Structure

```text
OS-Page-Replacement/
│
├── page_replacement.py
└── README.md
```

---

## Why I Made This Project

The main purpose of this project is to understand page replacement algorithms by actually simulating them rather than only studying their definitions.

It makes it easier to see:

* When a page fault occurs
* When a page hit occurs
* Which page gets replaced
* How FIFO and LRU make different decisions
* Why Optimal can be used as a benchmark

---

## Learning Outcomes

After working with this project, the main concepts covered are:

* Virtual memory
* Page faults
* Page hits
* Physical memory frames
* FIFO page replacement
* LRU page replacement
* Optimal page replacement
* Hit ratio and fault ratio
* Simulation of memory states
* Comparison of replacement algorithms

---

## Limitations

This is an educational simulation and not an implementation of an actual operating-system memory manager.

In particular:

* The Optimal algorithm assumes future page references are known.
* The LRU implementation uses a simple list rather than hardware-supported mechanisms.
* The program works with a supplied reference string instead of generating real memory accesses.

---

## Author

**Your Name**

Operating Systems Mini Project

### Technologies

* Python
* Operating Systems concepts
* Page Replacement Algorithms

---

## License

This project is created for educational purposes.
