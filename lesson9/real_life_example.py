class MessageContextProcessor:
    def handle_tags(self):
        print('Doing action one')
        print('Doing action two')
        print('Doing action three')

    def get_data(self, important):
        return {'hello': 'world'}


class MyContextProcessor(MessageContextProcessor):
    def handle_tags(self):
        super().handle_tags()
        print('Doing custom action four')


    def get_data(self, important):
        data = super().get_data(important)
        data.update({'foo': 'bar'})
        return data


class MyCoolClass(MyContextProcessor):
    def get_data(self, important):
        return super().get_data(important)

print('hello')

mcp = MyCoolClass()
print(mcp.get_data(42))