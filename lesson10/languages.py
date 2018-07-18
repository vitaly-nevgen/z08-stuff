class ProgrammingLanguage:
    name = None

    def get_name(self):
        return self.__class__.__name__

    def get_program(self):
        raise NotImplementedError()


class Python(ProgrammingLanguage):
    def get_program(self):
        return """
            def a():
                print(1 + 1)
            a()
        """


class JavaScript(ProgrammingLanguage):
    def get_program(self):
        return """
            function a(){
                console.log(1 + 1)
            }
            
            a()
        """

python = Python()
print(python.get_name())
print(python.get_program())

javascript = JavaScript()
print(javascript.get_name())
print(javascript.get_program())