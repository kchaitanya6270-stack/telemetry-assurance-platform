from mock_data.mock_loader import (
    load_mock_events
)

from validators.event_validator import (
    get_event_types
)

from reports.report_generator import (
    generate_report,
    save_report
)


from validators.completeness_validator import (
    compare_logs
)


from validators.udm_validator import (
    validate_udm
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

# Validate UDM
required_fields = [
    "principal.ip",
    "target.ip",
    "security_result.action"
]

print("\nUDM VALIDATION:")

for index, event in enumerate(events):

    missing_fields = validate_udm(
        event,
        required_fields
    )

    print(f"\nEvent {index + 1}")

    print("Missing Fields:")
    

    print(missing_fields)
save_report(
    report,
    "reports/output_report.json"
)

print("\nREPORT SAVED")
