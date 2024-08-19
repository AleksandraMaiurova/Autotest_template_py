import re
import allure

def find_data(v):
    date = re.findall('\d{4}-\d{2}\d{2} \d{2}:\d{2}:\d{2}.\d{6}', v)
    return date[0]


def find_response_time(v):
    rtstr = '\'responde_time\': '
    index3 = v.find(rtstr)
    index4 = v.find('}')
    response_time = v[index3 + len(rtstr):index4]
    return float(response_time)


def find_request_id(v):
    ids = re.findall(r'\w{8}-\w{4}\w{4}-\w{4}-\w{12}', v)
    return ids[0]


class Assertions:
    def all_attributes_in_response(self, list_attr, response):
        response_attr = []
        for content in response:
            for k in content.keys():
                response_attr.append(k)
        with allure.step("Check amount of attributes"):
            return set(list_attr) == set(response_attr) and len(response) == len(list_attr)


    def assert_equality(self, attribute_name, attribute_value, response):
        for content in response:
            for k,v in content.items():
                if k == attribute_name:
                    with allure.step(f"Check {attribute_name}"):
                        if v != attribute_value:
                            print(attribute_name, "Actual:", v, "Expected:", attribute_value)
                        return v == attribute_value
