import unittest
from mutation import mutate


class MutatorTest(unittest.TestCase):

    def test_that_empty_password_becomes_longer_when_mutated_with_empty_salt(self):
        self.given_the_password("")
        self.given_the_salt("")
        self.when_the_password_is_mutated()
        self.then_the_result_will_be_longer()

    def test_that_password_mutation_provides_same_result_when_done_multiple_times(self):
        self.given_the_password("password")
        self.given_the_salt("salt")
        self.when_the_password_is_mutated()
        self.and_the_password_is_mutated_again()
        self.then_the_results_will_be_the_same()

    def test_that_password_mutation_provides_different_result_when_done_with_different_salt(self):
        self.given_the_password("password")
        self.given_the_salt("first_salt")
        self.when_the_password_is_mutated()
        self.and_the_salt_is_changed_to("second_salt")
        self.and_the_password_is_mutated_again()
        self.then_the_results_will_be_different()

    def test_that_password_mutation_provides_different_result_when_done_with_different_password(self):
        self.given_the_password("first_password")
        self.given_the_salt("salt")
        self.when_the_password_is_mutated()
        self.and_the_password_is_changed_to("second_password")
        self.and_the_password_is_mutated_again()
        self.then_the_results_will_be_different()

    def given_the_password(self, password):
        self.password = password

    def given_the_salt(self, salt):
        self.salt = salt

    def when_the_password_is_mutated(self):
        self.mutated = mutate(self.password, self.salt)

    def and_the_password_is_mutated_again(self):
        self.second_mutated = mutate(self.password, self.salt)

    def and_the_salt_is_changed_to(self, salt):
        self.given_the_salt(salt)

    def and_the_password_is_changed_to(self, password):
        self.given_the_password(password)

    def then_the_result_will_be_longer(self):
        original_length = len(self.password)
        mutated_length = len(self.mutated)
        self.assertTrue(mutated_length > original_length)

    def then_the_results_will_be_the_same(self):
        self.assertEqual(self.second_mutated, self.mutated)

    def then_the_results_will_be_different(self):
        self.assertNotEqual(self.second_mutated, self.mutated)


if __name__ == "__main__":
    unittest.main()

