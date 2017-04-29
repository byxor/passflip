from unittest import TestCase
import passflip.input

try:
    import mock
except ImportError:
    from unittest import mock

class InputPromptMessageTest(TestCase):

    def setUp(self):
        self.validate = False;

    def test_that_user_can_input_password(self):
        expected = "foocar"
        self.when_user_is_prompted_for_password_and_they_input(expected)
        self.then_the_result_will_be(expected)

    def test_that_user_can_input_salt(self):
        expected = "barnod"
        self.when_user_is_prompted_for_password_and_they_input(expected)
        self.then_the_result_will_be(expected)

    def when_user_is_prompted_for_password_and_they_input(self, expected):
        with mock.patch.object(passflip.input, "getpass", create=True, return_value=expected) as m:
            self.input = passflip.input.prompt_password(self.validate)
            m.assert_called_once_with('enter password: ')

    def when_user_is_prompted_for_password_and_they_input(self, expected):
        with mock.patch.object(passflip.input, "getpass", create=True, return_value=expected) as m:
            self.input = passflip.input.prompt_salt(self.validate)
            m.assert_called_once_with('enter salt: ')

    def then_the_result_will_be(self, expected):
        self.assertEqual(self.input, expected)
