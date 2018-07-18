from unittest import TestCase

from lesson10.languages import (
    JavaScript,
    Python,
    ProgrammingLanguage,
)


class TestLanguages(TestCase):

    def test_javascript_program(self):
        js = JavaScript()
        expected_program = """
            function a(){
                console.log(1 + 1)
            }
            
            a()
        """

        self.assertEqual(js.get_program(), expected_program)

    def test_python_programm(self):
        py = Python()
        expected_program = """
            def a():
                print(1 + 1)
            a()
        """

        self.assertEqual(py.get_program(), expected_program)

    def test_language_get_name(self):
        class DummyLanguage(ProgrammingLanguage):
            pass

        d = DummyLanguage()
        self.assertEqual(
            d.get_name(), 'DummyLanguage'
        )

    def test_language_get_program(self):
        class DummyLanguage(ProgrammingLanguage):
            pass

        d = DummyLanguage()
        with self.assertRaises(NotImplementedError):
            d.get_program()
