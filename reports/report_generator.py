import json

def generate_report(
    vendor,
    observed_logs,
    missing_logs,
    udm_results
):

    total_expected = (
        len(observed_logs)
        + len(missing_logs)
    )

    completeness = int(
        (
            len(observed_logs)
            / total_expected
        ) * 100
    )

    report = {
        "vendor": vendor,

        "telemetry_completeness":
            completeness,

        "observed_logs":
            observed_logs,

        "missing_logs":
            missing_logs,

        "udm_validation":
            udm_results
    }

    return report


def save_report(
    report,
    path
):

    with open(path, "w") as f:

        json.dump(
            report,
            f,
            indent=4
        )
