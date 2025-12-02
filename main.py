
from Utils.aocUtils import get_input_for_year_day, submit_answer
from Utils.readParameter import read_parameter
from Utils.solve import get_solve_for
from Utils.template import create_solve_file
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt

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
    path = get_input_for_year_day(year, day, timeout=100)

    with open(path, "r") as file:
        data = file.read()

    solve_first, solve_second = get_solve_for(year, day)

    result_first, result_second = solve(data, solve_first, solve_second)
    if result_first is not None:
        content = Text()
        content.append(f"Result for day {day} in year {year} (Part 1): ", style="bold green")
        content.append(f"{result_first}", style="bold green underline")
        console.print(
            Panel.fit(
                content,
                title="Advent of Code Result",
                border_style="green",
            )
        )
        if Prompt.ask(Text("Submit solution for Part 1? (y/n)", style="bold yellow")).lower() == "y":
            article, success = submit_answer(year, day, 1, str(result_first))
            console.print(
                Panel.fit(
                    Text(article, style=("bold green" if success == 1 else ("bold red" if success == 0 else "bold dark_orange"))),
                    border_style=("green" if success == 1 else ("red" if success == 0 else "dark_orange")),
                )
            )
    if result_second is not None:
        content = Text()
        content.append(f"Result for day {day} in year {year} (Part 2): ", style="bold green")
        content.append(f"{result_second}", style="bold green underline")
        console.print(
            Panel.fit(
                content,
                title="Advent of Code Result",
                border_style="green",
            )
        )
        if Prompt.ask(Text("Submit solution for Part 2? (y/n)", style="bold yellow")).lower() == "y":
            article, success = submit_answer(year, day, 2, str(result_second))
            console.print(
                Panel.fit(
                    Text(article, style=("bold green" if success == 1 else ("bold red" if success == 0 else "bold dark_orange"))),
                    border_style=("green" if success == 1 else ("red" if success == 0 else "dark_orange")),
                )
            )