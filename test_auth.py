from chronicle_adapter.auth import (
    get_access_token
)

try:

    token = get_access_token()

    print("\nSUCCESS\n")

    print(token[:80])

except Exception as e:

    print("\nFAILED\n")

    print(str(e))