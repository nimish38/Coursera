from Algo_Sort import BinarySearchDict as BST

run_cases = [
    (
        [
            {"name": "John", "followers": 5},
            {"name": "Jane", "followers": 10},
            {"name": "James", "followers": 15},
            {"name": "Judy", "followers": 20},
        ],
        10,
        "Jane",
    ),
    (
        [
            {"name": "Bob", "followers": 25},
            {"name": "Boris", "followers": 30},
            {"name": "Borice", "followers": 35},
        ],
        30,
        "Boris",
    ),
]

submit_cases = run_cases + [
    (
        [
            {"name": "John", "followers": 5},
            {"name": "Jane", "followers": 20},
            {"name": "James", "followers": 25},
            {"name": "Borice", "followers": 50},
            {"name": "Boris", "followers": 55},
            {"name": "Donald", "followers": 60},
            {"name": "Doris", "followers": 65},
            {"name": "Derek", "followers": 70},
            {"name": "Diana", "followers": 75},
            {"name": "Dennis", "followers": 80},
            {"name": "Daisy", "followers": 85},
            {"name": "Duke", "followers": 90},
            {"name": "Duke", "followers": 95},
            {"name": "Duke", "followers": 100},
        ],
        15,
        None,
    ),
    ([], 10, None),
    ([{"name": "John", "followers": 5}], 5, "John"),
    (
        [
            {"name": "John", "followers": 5},
            {"name": "Jane", "followers": 10},
            {"name": "James", "followers": 15},
            {"name": "Judy", "followers": 20},
        ],
        22,
        None,
    ),
    (
        [
            {"name": "John", "followers": 5},
            {"name": "Jane", "followers": 10},
            {"name": "James", "followers": 15},
            {"name": "Judy", "followers": 20},
        ],
        5,
        "John",
    ),
]


def test(input1, input2, expected_output):
    print("---------------------------------")
    print(f"Inputs")
    print(f" * Data: {input1}")
    print(f" * Follower count to search: {input2}")
    print(f"Expecting: {expected_output}")
    result = BST.binary_search(input1, input2)
    print(f"Actual: {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
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
