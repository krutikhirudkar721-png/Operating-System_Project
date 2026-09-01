def fifo(reference_string, frames):
    
    memory = []
    page_faults = 0
    index = 0
    for page in reference_string:
        if page not in memory:
            if len(memory) < frames:
                memory.append(page)
            else:
                memory[index] = page
                index = (index + 1) % frames
            page_faults += 1
    return page_faults
    
def lru(reference_string, frames):
    memory = []
    page_faults = 0
    recent = []
    for page in reference_string:
        if page not in memory:
            if len(memory) < frames:
                memory.append(page)
            else:
                lru_page = recent.pop(0)
                memory[memory.index(lru_page)] = page
            page_faults += 1
        else:
            recent.remove(page)
        recent.append(page)
    return page_faults
    
def optimal(reference_string, frames):
    memory = []
    page_faults = 0
    for i in range(len(reference_string)):
        page = reference_string[i]

        if page not in memory:
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
                    else:
                        idx = future.index(mem_page)
                        if idx > farthest:
                            farthest = idx
                            replace_page = mem_page

                memory[memory.index(replace_page)] = page
            page_faults += 1
    return page_faults

if __name__ == "__main__":
    reference_string = list(map(int, input("Enter reference string: ").split()))
    frames = int(input("Enter number of frames: "))
    fifo_faults = fifo(reference_string, frames)
    lru_faults = lru(reference_string, frames)
    optimal_faults = optimal(reference_string, frames)
    total = len(reference_string)

    print("\n--- RESULT ---")
    print("Algorithm\tPage Faults\tHit Ratio")
    print(f"FIFO\t\t{fifo_faults}\t\t{(total - fifo_faults)/total:.2f}")
    print(f"LRU\t\t{lru_faults}\t\t{(total - lru_faults)/total:.2f}")
    print(f"Optimal\t\t{optimal_faults}\t\t{(total - optimal_faults)/total:.2f}")
    # Best algorithm
    min_faults = min(fifo_faults, lru_faults, optimal_faults)
    if min_faults == optimal_faults:
        best = "Optimal"
    elif min_faults == lru_faults:
        best = "LRU"
    else:
        best = "FIFO"
    print(f"\nBest Algorithm: {best}")
