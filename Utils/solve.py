import importlib


def get_solve_for(year: int, day: int):
    def not_implemented(*args, **kwargs):
        raise NotImplementedError(f"Solver for Year {year}, Day {day} is not implemented.")

    mod_name = f"AOC_{year}.DAY_{day}"
    try:
        mod = importlib.import_module(mod_name)
        solveFirst = mod.solve_first
        solveSecond = mod.solve_second
    except ImportError: 
        solveFirst = not_implemented
        solveSecond = not_implemented

    return solveFirst, solveSecond
