from unittest import TestCase
import passflip.input

try:
    import mock
except ImportError:
    from unittest import mock

class PromptTest(TestCase):

    def setUp(self):
        self.validate = False;

    def test_that_user_can_input_password(self):
        expected = "foocar"
        self.when_user_is_prompted_for_password_and_they_input(expected)
        self.then_the_inputed_value_will_equal(expected)

    def test_that_user_can_input_salt(self):
        expected = "barnod"
        self.when_user_is_prompted_for_salt_and_they_input(expected)
        self.then_the_inputed_value_will_equal(expected)

    def test_that_empty_input_raises_input_error(self):
        expected = ""
        self.when_user_is_prompted_they_input(expected)
        self.then_empty_string_error_is_raised()

    def when_user_is_prompted_they_input(self, expected):
        with mock.patch.object(passflip.input, "getpass", create=True, return_value=expected) as m:
            try:
                self.input = passflip.input.prompt_input("false message", self.validate)
                m.assert_called_once_with('enter password: ')
            except passflip.input.PromptError as e:
                self.error = e

    def when_user_is_prompted_for_password_and_they_input(self, expected):
        with mock.patch.object(passflip.input, "getpass", create=True, return_value=expected) as m:
            self.input = passflip.input.prompt_password(self.validate)
            m.assert_called_once_with('enter password: ')

    def when_user_is_prompted_for_salt_and_they_input(self, expected):
        with mock.patch.object(passflip.input, "getpass", create=True, return_value=expected) as m:
            self.input = passflip.input.prompt_salt(self.validate)
            m.assert_called_once_with('enter salt: ')

    def then_the_inputed_value_will_equal(self, expected):
        self.assertEqual(self.input, expected)
        self.input = None

    def then_empty_string_error_is_raised(self):
        self.assertEqual(str(self.error), "error: cannot enter empty string")
