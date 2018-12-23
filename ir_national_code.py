import json
import re


__author__ = 'Benyamin Salimi <Benyamin.Salimi@gmail.com>'


class ir_national_code(object):
    def __init__(self):
        # city_codes.json from https://github.com/fandogh/codemeli/docs
        with open('city_codes.json') as city_file:
            self.city_codes = json.load(city_file)

    # validate the national code
    # https://gist.github.com/ebraminio/5292017
    def validator(self, input):
        if not re.search(r'^\d{10}$', input):
            return False
        check = int(input[9])
        s = sum([int(input[x]) * (10 - x) for x in range(9)]) % 11
        return (s < 2 and check == s) or (s >= 2 and check + s == 11)

    def return_all(self):
        # import all city codes
        result = []
        for city in self.city_codes:
            # generate 0000000 to 9999999
            for x in range(10000000, 19999999):
                # each national code
                code = str(city + str(x)[1:])
                if self.validator(code):
                    # DO SOMETHING for example : print(code)
                    # add valid code to result
                    result.append(code)

        return result

    # return national code by state name
    def by_state(self, target_state):
        result = []
        # import all city codes
        for city in self.city_codes:
            if target_state == self.city_codes[city][0]:
                # generate 0000000 to 9999999
                for x in range(10000000, 19999999):
                    # each national code
                    code = str(city + str(x)[1:])
                    if self.validator(code):
                        # DO SOMETHING for example : print(code)
                        # add valid code to result
                        result.append(code)

        return result

    # return national code by state name
    def by_first_3_digit(self, first3digit):
        result = []
        for city_code in self.city_codes:
            if city_code == first3digit:
                for x in range(10000000, 19999999):
                    # each national code
                    code = str(first3digit + str(x)[1:])
                    if self.validator(code):
                        # DO SOMETHING for example : print(code)
                        # add valid code to result
                        result.append(code)
                break

        return result
