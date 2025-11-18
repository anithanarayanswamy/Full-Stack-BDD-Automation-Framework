"""
Step definitions for API testing
"""
from behave import given, when, then
from utils.api_helper import APIHelper
from utils.logger import setup_logger

logger = setup_logger(__name__)


@given('the API base URL is "{base_url}"')
def step_set_base_url(context, base_url):
    """Set the API base URL"""
    context.api = APIHelper(base_url)
    logger.info(f"API base URL set to: {base_url}")


@when('I send GET request to "{endpoint}"')
def step_send_get_request(context, endpoint):
    """Send GET request to endpoint"""
    context.response = context.api.get(endpoint)
    context.response_json = context.response.json() if context.response.text else {}


@when('I send POST request to "{endpoint}" with body')
def step_send_post_request(context, endpoint):
    """Send POST request with body from table"""
    # Get data from table
    data = {}
    for row in context.table:
        for heading in context.table.headings:
            data[heading] = row[heading]
    
    logger.info(f"POST data: {data}")
    context.response = context.api.post(endpoint, json=data)
    context.response_json = context.response.json() if context.response.text else {}


@when('I send PUT request to "{endpoint}" with body')
def step_send_put_request(context, endpoint):
    """Send PUT request with body from table"""
    # Get data from table
    data = {}
    for row in context.table:
        for heading in context.table.headings:
            data[heading] = row[heading]
    
    logger.info(f"PUT data: {data}")
    context.response = context.api.put(endpoint, json=data)
    context.response_json = context.response.json() if context.response.text else {}


@when('I send DELETE request to "{endpoint}"')
def step_send_delete_request(context, endpoint):
    """Send DELETE request"""
    context.response = context.api.delete(endpoint)


@then('response status code should be {status_code:d}')
def step_verify_status_code(context, status_code):
    """Verify response status code"""
    actual_code = context.response.status_code
    assert actual_code == status_code, \
        f"Expected status code {status_code}, but got {actual_code}"
    logger.info(f"✓ Status code verified: {actual_code}")


@then('response should contain "{field}" field')
def step_verify_field_exists(context, field):
    """Verify response contains field"""
    assert field in context.response_json, \
        f"Field '{field}' not found in response. Available fields: {list(context.response_json.keys())}"
    logger.info(f"✓ Field '{field}' found in response")


@then('response data should have "{field}" equal to {value:d}')
def step_verify_field_value_int(context, field, value):
    """Verify field has specific integer value"""
    data = context.response_json.get('data', {})
    actual_value = data.get(field)
    assert actual_value == value, \
        f"Expected {field}={value}, but got {actual_value}"
    logger.info(f"✓ Field '{field}' has correct value: {value}")


@then('response data should have "{field}" field')
def step_verify_data_field_exists(context, field):
    """Verify field exists in data object"""
    data = context.response_json.get('data', {})
    assert field in data, \
        f"Field '{field}' not found in data. Available fields: {list(data.keys())}"
    logger.info(f"✓ Field '{field}' found in data")


@then('response data should contain multiple users')
def step_verify_multiple_users(context):
    """Verify response contains multiple users"""
    data = context.response_json.get('data', [])
    assert isinstance(data, list), "Data should be a list"
    assert len(data) > 0, "Data list should not be empty"
    logger.info(f"✓ Response contains {len(data)} users")