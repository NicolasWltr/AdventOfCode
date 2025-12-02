def make_rules_dict(rules):
    x_before = {}
    x_after = {}

    for line in rules.splitlines():
        if not line.strip():
            continue
        
        before, after = line.split("|")

        x_before[before] = x_before.get(before, []) + [after]
        x_after[after] = x_after.get(after, []) + [before]


    return x_before, x_after

def is_valid(pages, x_before, x_after):
    valid_update = True
        
    for index, page in enumerate(pages):
        all_before = pages[:index]
        all_after = pages[index + 1:]

        for pageToCheck in all_before:
            if pageToCheck in x_before.get(page, []):
                valid_update = False
                break

        for pageToCheck in all_after:
            if pageToCheck in x_after.get(page, []):
                valid_update = False
                break
        
        if not valid_update:
            break

    return valid_update

def split_into_valid_and_invalid_updates(updates, x_before, x_after):
    valid_updates = []
    invalid_updates = []

    for update in updates:
        if not update.strip():
            continue

        valid_update = is_valid(update.split(','), x_before, x_after)

        if valid_update:
            valid_updates.append(update)
        else:
            invalid_updates.append(update)

    return valid_updates, invalid_updates

def solve_first(data):
    rules, updates = data.split("\n\n")

    x_before, x_after = make_rules_dict(rules)

    updates = updates.splitlines()

    valid_updates, _ = split_into_valid_and_invalid_updates(updates, x_before, x_after)

    sum = 0

    for update in valid_updates:
        pages = update.split(',')

        page = pages[len(pages) // 2]

        sum += int(page)

    return sum
    

def make_update_valid(pages, x_before, x_after):
    while not is_valid(pages, x_before, x_after):
        oldIndex = None
        newIndex = None
        forPage = None
        for page_index, page in enumerate(pages):
            all_before = pages[:page_index]
            all_after = pages[page_index + 1:]

            for index, pageToCheck in enumerate(all_before):
                if pageToCheck in x_before.get(page, []):
                    oldIndex = page_index
                    newIndex = index
                    forPage = page
                    break
            
            if newIndex:
                break

            for index, pageToCheck in enumerate(reversed(all_after)):
                if pageToCheck in x_after.get(page, []):
                    oldIndex = page_index
                    newIndex = len(pages) - 1 - index
                    forPage = page
                    break

            if newIndex:
                break

        if forPage:
            moveTo = (newIndex if newIndex < oldIndex else newIndex - 1) + 1
            pages.pop(oldIndex)
            pages.insert(moveTo, forPage)

    return pages


def solve_second(data):
    rules, updates = data.split("\n\n")

    x_before, x_after = make_rules_dict(rules)

    updates = updates.splitlines()

    _, invalid_updates = split_into_valid_and_invalid_updates(updates, x_before, x_after)

    sum = 0

    for update in invalid_updates:
        pages = update.split(',')

        pages = make_update_valid(pages, x_before, x_after)

        page = pages[len(pages) // 2]

        sum += int(page)

    return sum