def run_build(steps):
    index = 0
    while index < len(steps):
        current = steps[index]
        next_step = None
        if index + 1 < len(steps):
            next_step = steps[index + 1]
        print(f"NOW: {current['supply']} {current['action']}")
        if next_step is not None:
            print(f"NEXT: {next_step['supply']} {next_step['action']}")
        user_input = input("Press \ to continue, or 'q' to quit: ")
        if user_input.lower() == 'q':
            break
        index= index + 1
    print("Build Complete!")