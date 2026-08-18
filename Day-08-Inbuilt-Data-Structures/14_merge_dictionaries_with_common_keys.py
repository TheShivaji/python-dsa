def merge_dicts_with_overlapping_keys(dicts):
    result = {}

    for dict in dicts:
        for key , val in dict.items():
            if key in result:
                result[key] = result[key] + val
            else:
                result[key] = val
    return result





dicts = [
    {"a": 1, "b": 2},
    {"b": 3, "c": 4},
    {"c": 5, "d": 6}
]
print(merge_dicts_with_overlapping_keys(dicts))


