def compare_logs(
    expected,
    observed
):

    expected_set = set(expected)

    observed_set = set(observed)

    missing = (
        expected_set - observed_set
    )

    return list(missing)