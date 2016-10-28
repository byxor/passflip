from unittest import TestCase
from passflip.input import create_prompt_message


class InputPromptMessageTest(TestCase):

    def test_that_colon_is_added_to_message(self):
        self.given_the_message("Foo")
        self.when_converted_to_a_prompt_message()
        self.then_the_result_will_be("Foo: ")

    def test_that_again_is_added_to_message(self):
        self.given_the_message("Foo")
        self.when_converted_to_a_prompt_message_with_again()
        self.then_the_result_will_be("Foo again: ")

    def given_the_message(self, message):
        self.message = message

    def when_converted_to_a_prompt_message(self):
        self.prompt_message = create_prompt_message(self.message)

    def when_converted_to_a_prompt_message_with_again(self):
        self.prompt_message = create_prompt_message(self.message, again=True)

    def then_the_result_will_be(self, expected):
        self.assertEqual(expected, self.prompt_message)

