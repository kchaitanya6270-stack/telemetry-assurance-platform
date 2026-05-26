def validate_udm(
    event,
    required_fields
):

    missing = []

    for field in required_fields:

        parts = field.split(".")

        current = event

        exists = True

        for part in parts:

            if part not in current:
                exists = False
                break

            current = current[part]

        if not exists:
            missing.append(field)

    return missing