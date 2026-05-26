print("STARTING TEST")

from chronicle_adapter.search import (
    run_query
)

print("IMPORT SUCCESS")

query = '''
metadata.vendor_name="Palo Alto Networks"
'''

print("RUNNING QUERY")

result = run_query(query)

print("QUERY FINISHED")

print(result)