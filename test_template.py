import pytest
import allure
from helpers import Assertions, find_data, find_request_id, find_response_time


assertions = Assertions()


@pytest.mark.xray('Ticket')
@allure.tag("module")
@allure.feature(" ")
@allure.story(" ")
def test_name(fix):
    response = ex(fix)
    print(response)
    assert assertions.all_attributes_in_response(attributes, response), 'Problems with attributes amount'
    assert assertions.assert_equality('attribute_name', 1, response), 'Unexpected attribute_name'