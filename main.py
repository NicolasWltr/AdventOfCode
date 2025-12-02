
from Utils.load import getInputForYearDay
from Utils.readParameter import read_parameter
from Utils.solve import getSolveFor
from Utils.template import create_solve_file
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

def solve(data, first, second):
    try:
        result_part1 = first(data)
    except NotImplementedError as e:
        result_part1 = None
        console.print(
            Panel.fit(
                Text(str(e), style="bold red"),
                border_style="red",
            )
        )
    try:
        result_part2 = second(data)
    except NotImplementedError as e:
        result_part2 = None
        console.print(
            Panel.fit(
                Text(str(e), style="bold red"),
                border_style="red",
            )
        )
    return result_part1, result_part2


if __name__ == "__main__":
    year, day = read_parameter()
    create_solve_file(year, day)
    path = getInputForYearDay(year, day, timeout=100)

    with open(path, "r") as file:
        data = file.read()

    solve_first, solve_second = getSolveFor(year, day)

    result_first, result_second = solve(data, solve_first, solve_second)
    if result_first:
        print(f"Result for day {day} in year {year} (Part 1):", result_first)
    if result_second:
        print(f"Result for day {day} in year {year} (Part 2):", result_second)