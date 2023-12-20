from Linked_List import Yield
run_cases = [
    ("Bow", ["Bow", "Sword"]),
    ("Axe", ["Axe", "Bow", "Sword"]),
    ("Staff", ["Staff", "Axe", "Bow", "Sword"]),
]

submit_cases = run_cases + [
    ("Spear", ["Spear", "Staff", "Axe", "Bow", "Sword"]),
    ("Dagger", ["Dagger", "Spear", "Staff", "Axe", "Bow", "Sword"]),
]


def test(linked_list, input, expected_state):
    print("---------------------------------")
    print(f"Linked List: {linked_list}")
    print(f"Adding to head: {input}")
    print(f"Expecting: {expected_state}")
    node = Yield.Node(input)
    try:
        linked_list.add_to_head(node)
        result = linked_list_to_list(linked_list)
    except Exception as e:
        result = f"Error: {e}"
    print(f"Actual: {result}")
    if result == expected_state:
        print("Pass")
        return True
    print("Fail")
    return False


def linked_list_to_list(linked_list):
    result = []
    for node in linked_list:
        result.append(node.val)

    return result


def main():
    passed = 0
    failed = 0
    linked_list = Yield.LinkedList()
    linked_list.head = Yield.Node("Sword")
    for test_case in test_cases:
        correct = test(linked_list, *test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()