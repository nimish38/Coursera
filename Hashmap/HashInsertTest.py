from Hashmap import HashInsert

run_cases = [
    (1, [("apple", 1), ("banana", 2)], [("banana", 2)]),
    (4, [("apple", 1), ("banana", 2)], [None, ("banana", 2), ("apple", 1), None]),
]

submit_cases = run_cases + [
    (
        8,
        [("apple", 1), ("banana", 2), ("apple", 592), ("banana", 54)],
        [None, ("banana", 54), ("apple", 592), None, None, None, None, None],
    )
]


def hashmap_to_list(hm):
    final = []
    for i, v in enumerate(hm.hashmap):
        final.append(v)
    return final


def test(size, items, expected_hashmap):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * Using hasmap with size: {size}")
    hm = HashInsert.HashMap(size)
    try:
        for item in items:
            hm.insert(item[0], item[1])
            print(f"Inserted {item}")
        print(f"Expecting:")
        print(f"  {expected_hashmap}")
        actual = hashmap_to_list(hm)
        print(f"Actual:")
        print(f"  {actual}")
        if actual == expected_hashmap:
            print("Pass \n")
            return True
        print("Fail \n")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False


def main():
    passed = 0
    failed = 0
    for test_case in test_cases:
        correct = test(*test_case)
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
