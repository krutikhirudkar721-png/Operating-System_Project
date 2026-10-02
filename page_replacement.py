def fifo(reference_string, frames):
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

            # Move page to the most recently used position
            recent.remove(page)
            recent.append(page)

        else:
            page_faults += 1
            status = "FAULT"

            if len(memory) < frames:
                memory.append(page)
            else:
                # Least recently used page
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


def print_simulation(name, history, frames):
    print(f"\n{'=' * 65}")
    print(f"{name} PAGE REPLACEMENT")
    print(f"{'=' * 65}")

    print(
        f"{'Step':<6}"
        f"{'Page':<7}"
        + "".join(f"F{i + 1:<7}" for i in range(frames))
        + f"{'Status':<15}"
    )

    print("-" * 65)

    for step, data in enumerate(history, 1):

        frame_values = data["frames"].copy()

        # Display empty frames as '-'
        while len(frame_values) < frames:
            frame_values.append("-")

        status = data["status"]

        if data["replaced"] is not None:
            status += f" (R:{data['replaced']})"

        print(
            f"{step:<6}"
            f"{data['page']:<7}"
            + "".join(f"{str(frame):<7}" for frame in frame_values)
            + f"{status:<15}"
        )


def print_result(name, faults, hits, total):
    hit_ratio = hits / total
    fault_ratio = faults / total

    print(
        f"{name:<12}"
        f"{faults:<12}"
        f"{hits:<12}"
        f"{hit_ratio:<12.2%}"
        f"{fault_ratio:<12.2%}"
    )


def main():

    print("\n" + "=" * 65)
    print("       OS PAGE REPLACEMENT ALGORITHM SIMULATOR")
    print("=" * 65)

    try:
        reference_string = list(
            map(
                int,
                input("\nEnter reference string: ").split()
            )
        )

        frames = int(
            input("Enter number of frames: ")
        )

        if not reference_string:
            print("Error: Reference string cannot be empty.")
            return

        if frames <= 0:
            print("Error: Number of frames must be greater than 0.")
            return

    except ValueError:
        print("Error: Please enter valid integer values.")
        return

    fifo_faults, fifo_hits, fifo_history = fifo(
        reference_string, frames
    )

    lru_faults, lru_hits, lru_history = lru(
        reference_string, frames
    )

    optimal_faults, optimal_hits, optimal_history = optimal(
        reference_string, frames
    )

    total = len(reference_string)

    print("\nReference String:", reference_string)
    print("Number of Frames:", frames)

    # Detailed simulation
    print_simulation("FIFO", fifo_history, frames)
    print_simulation("LRU", lru_history, frames)
    print_simulation("OPTIMAL", optimal_history, frames)

    # Final comparison
    print("\n" + "=" * 65)
    print("                    FINAL COMPARISON")
    print("=" * 65)

    print(
        f"{'Algorithm':<12}"
        f"{'Faults':<12}"
        f"{'Hits':<12}"
        f"{'Hit Ratio':<12}"
        f"{'Fault Ratio':<12}"
    )

    print("-" * 65)

    print_result(
        "FIFO",
        fifo_faults,
        fifo_hits,
        total
    )

    print_result(
        "LRU",
        lru_faults,
        lru_hits,
        total
    )

    print_result(
        "Optimal",
        optimal_faults,
        optimal_hits,
        total
    )

    print("=" * 65)

    print("\nNote:")
    print(
        "Optimal Page Replacement is a theoretical benchmark "
        "because it requires knowledge of future references."
    )


if __name__ == "__main__":
    main()
