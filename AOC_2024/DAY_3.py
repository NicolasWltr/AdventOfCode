def solve_first(data, with_disabling=False):
    mul_tasks = data.split('mul(')

    result = 0

    disabled = "don't()" in mul_tasks[0]

    if "do()" in mul_tasks[0] and "don't()" in mul_tasks[0]:
        index_do = task.find("do()")
        index_dont = task.find("don't()")
        disabled = index_dont > index_do


    disabled_next = disabled
    mul_tasks = mul_tasks[1:]

    print("Start with", disabled, disabled_next)

    for task in mul_tasks:
        if "do()" in task:
            # print("Next is enabled")
            disabled_next = False
        if "don't()" in task:
            # print("Next is disabled")
            disabled_next = True

        if "do()" in task and "don't()" in task:
            print("Testing")
            index_do = task.find("do()")
            index_dont = task.find("don't()")
            disabled_next = index_dont > index_do
            print("Next is", disabled_next)

        if not ')' in task:
            disabled = disabled_next
            continue
        params = task.split(')')[0]

        if len(params) > 7 or not ',' in params:
            disabled = disabled_next
            continue

        operands = params.split(',')
        a = operands[0]
        b = operands[1]

        try:
            a = int(a)
            b = int(b)
        except:
            disabled = disabled_next
            continue
        
        if not disabled or not with_disabling:
            # print("Adding", (a*b))
            result += a*b
        
        disabled = disabled_next

    return result

def solve_second(data):
    return solve_first(data, True)