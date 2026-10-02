def fifo(reference_string, frames):
    """Simulate FIFO page replacement."""

    memory = []
    page_faults = 0
    page_hits = 0
    pointer = 0
    history = []

    for page in reference_string:
        replaced = None

        if page in memory:
            page_hits += 1
            status = "HIT"
        else:
            page_faults += 1
            status = "FAULT"

            if len(memory) < frames:
                memory.append(page)
            else:
                replaced = memory[pointer]
                memory[pointer] = page
                pointer = (pointer + 1) % frames

        history.append({
            "page": page,
            "frames": memory.copy(),
            "status": status,
            "replaced": replaced
        })

    return page_faults, page_hits, history


def lru(reference_string, frames):
    """Simulate LRU page replacement."""

    memory = []
    recent = []
    page_faults = 0
    page_hits = 0
    history = []

    for page in reference_string:
        replaced = None

        if page in memory:
            page_hits += 1
            status = "HIT"

            # Move the page to the most recently used position.
            recent.remove(page)
            recent.append(page)

        else:
            page_faults += 1
            status = "FAULT"

            if len(memory) < frames:
                memory.append(page)
            else:
                # The first page in 'recent' is the least recently used.
                lru_page = recent.pop(0)

                replaced = lru_page
                memory[memory.index(lru_page)] = page

            recent.append(page)

        history.append({
            "page": page,
            "frames": memory.copy(),
            "status": status,
            "replaced": replaced
        })

    return page_faults, page_hits, history


def optimal(reference_string, frames):
    """Simulate Optimal page replacement."""

    memory = []
    page_faults = 0
    page_hits = 0
    history = []

    for i, page in enumerate(reference_string):
        replaced = None

        if page in memory:
            page_hits += 1
            status = "HIT"

        else:
            page_faults += 1
            status = "FAULT"

            if len(memory) < frames:
                memory.append(page)
            else:
                future = reference_string[i + 1:]

                replace_page = None
                farthest = -1

                for mem_page in memory:

                    # If this page will never be used again,
                    # it is a valid choice for replacement.
                    if mem_page not in future:
                        replace_page = mem_page
                        break

                    next_use = future.index(mem_page)

                    if next_use > farthest:
                        farthest = next_use
                        replace_page = mem_page

                replaced = replace_page
                memory[memory.index(replace_page)] = page

        history.append({
            "page": page,
            "frames": memory.copy(),
            "status": status,
            "replaced": replaced
        })

    return page_faults, page_hits, history


def print_simulation(algorithm, history, frames):
    """Display the frame-by-frame simulation."""

    print("\n" + "=" * 65)
    print(f"{algorithm} PAGE REPLACEMENT")
    print("=" * 65)

    header = f"{'Step':<7}{'Page':<7}"

    for i in range(frames):
        header += f"F{i + 1:<7}"

    header += f"{'Status':<15}"

    print(header)
    print("-" * 65)

    for step, data in enumerate(history, start=1):

        frame_values = data["frames"].copy()

        # Show empty frames with '-'.
        while len(frame_values) < frames:
            frame_values.append("-")

        status = data["status"]

        if data["replaced"] is not None:
            status += f" (R:{data['replaced']})"

        row = f"{step:<7}{data['page']:<7}"

        for frame in frame_values:
            row += f"{str(frame):<7}"

        row += f"{status:<15}"

        print(row)


def print_comparison(results, total_references):
    """Display the final comparison table."""

    print("\n" + "=" * 70)
    print("FINAL COMPARISON")
    print("=" * 70)

    print(
        f"{'Algorithm':<14}"
        f"{'Faults':<12}"
        f"{'Hits':<12}"
        f"{'Hit Ratio':<14}"
        f"{'Fault Ratio':<14}"
    )

    print("-" * 70)

    for name, faults, hits in results:

        hit_ratio = hits / total_references
        fault_ratio = faults / total_references

        print(
            f"{name:<14}"
            f"{faults:<12}"
            f"{hits:<12}"
            f"{hit_ratio:.2%}{'':<8}"
            f"{fault_ratio:.2%}"
        )

    print("=" * 70)


def main():
    print("\n" + "=" * 65)
    print("        OS PAGE REPLACEMENT ALGORITHM SIMULATOR")
    print("=" * 65)

    # Get reference string.
    try:
        reference_string = list(
            map(int, input("\nEnter reference string: ").split())
        )
    except ValueError:
        print("Error: Please enter only integer page numbers.")
        return

    # Check reference string.
    if not reference_string:
        print("Error: Reference string cannot be empty.")
        return

    # Get number of frames.
    try:
        frames = int(input("Enter number of frames: "))
    except ValueError:
        print("Error: Number of frames must be an integer.")
        return

    if frames <= 0:
        print("Error: Number of frames must be greater than 0.")
        return

    # Run all three algorithms.
    fifo_faults, fifo_hits, fifo_history = fifo(
        reference_string, frames
    )

    lru_faults, lru_hits, lru_history = lru(
        reference_string, frames
    )

    optimal_faults, optimal_hits, optimal_history = optimal(
        reference_string, frames
    )

    # Display input information.
    print("\nReference String:", " ".join(map(str, reference_string)))
    print("Number of Frames:", frames)

    # Display step-by-step simulation.
    print_simulation("FIFO", fifo_history, frames)
    print_simulation("LRU", lru_history, frames)
    print_simulation("OPTIMAL", optimal_history, frames)

    # Display final results.
    results = [
        ("FIFO", fifo_faults, fifo_hits),
        ("LRU", lru_faults, lru_hits),
        ("Optimal", optimal_faults, optimal_hits)
    ]

    print_comparison(results, len(reference_string))

    print("\nNote:")
    print(
        "Optimal is mainly used as a theoretical benchmark because "
        "it requires knowledge of future page references."
    )


if __name__ == "__main__":
    main()
