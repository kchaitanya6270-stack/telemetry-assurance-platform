from mock_data.mock_loader import (
    load_mock_events
)

from validators.event_validator import (
    get_event_types
)

from validators.completeness_validator import (
    compare_logs
)

from validators.udm_validator import (
    validate_udm
)

from reports.report_generator import (
    generate_report,
    save_report
)

# Load mock events
events = load_mock_events(
    "mock_data/paloalto_events.json"
)

# Expected telemetry
expected_logs = [
    "Traffic Logs",
    "Threat Logs",
    "URL Logs"
]

# Discover observed logs
observed_logs = get_event_types(events)

print("\nOBSERVED LOGS:")
print(observed_logs)

# Compare completeness
missing_logs = compare_logs(
    expected_logs,
    observed_logs
)

print("\nMISSING LOGS:")
print(missing_logs)

# Required UDM fields
required_fields = [
    "principal.ip",
    "target.ip",
    "security_result.action"
]

print("\nUDM VALIDATION:")

# Store UDM validation results
udm_results = []

for index, event in enumerate(events):

    missing_fields = validate_udm(
        event,
        required_fields
    )

    result = {
        "event_number": index + 1,
        "missing_fields": missing_fields
    }

    udm_results.append(result)

    print(f"\nEvent {index + 1}")

    print("Missing Fields:")

    print(missing_fields)

# Generate final report
report = generate_report(
    vendor="Palo Alto",
    observed_logs=observed_logs,
    missing_logs=missing_logs,
    udm_results=udm_results
)

print("\nFINAL REPORT:\n")

print(report)

# Save report to JSON file
save_report(
    report,
    "reports/output_report.json"
)

print("\nREPORT SAVED")
