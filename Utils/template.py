import os

def create_solve_file(year, day):
    content = f"""
def solve_first(data):
    raise NotImplementedError("Solver for Year {year}, Day {day}, Part 1 is not implemented.")

def solve_second(data):
    raise NotImplementedError("Solver for Year {year}, Day {day}, Part 2 is not implemented.")
"""
    
    os.makedirs(f"AOC_{year}", exist_ok=True)

    if (os.path.exists(f"AOC_{year}/DAY_{day}.py")):
        return

    with open(f"AOC_{year}/DAY_{day}.py", "w") as file:
        file.write(content.strip())