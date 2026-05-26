def get_event_types(events):

    event_types = set()

    for event in events:

        metadata = event.get(
            "metadata",
            {}
        )

        event_type = metadata.get(
            "product_event_type"
        )

        if event_type:
            event_types.add(event_type)

    return list(event_types)