import json

with open('task3/values.json', 'r') as values_file:
    values_data = json.load(values_file)

with open('task3/tests.json', 'r') as tests_file:
    tests_data = json.load(tests_file)

for test_item in tests_data:
    test_id = test_item['id']
for value_item in values_data:
    value_id = value_item['value']
    break

with open('task3/report.json', 'w') as report_file:
    json.dump(tests_data, report_file, indent=4)