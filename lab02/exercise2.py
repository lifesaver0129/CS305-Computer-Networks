class Editor:
    def __init__(self, address):
        self.address = address
        self.text = open(address).read()

    def print_file(self):
        print(open(self.address).read())

    def add_content(self, new_content):
        self.text += '\n'
        self.text += new_content
        object_to_write = open(self.address, 'w')
        object_to_write.write(self.text)
        self.print_file()

    def del_content(self, new_content):
        tmp = self.text.replace(new_content, '')
        object_to_write = open(self.address, 'w')
        object_to_write.write(tmp)
        self.print_file()


ed = Editor('test_file.txt')
ed.print_file()
ed.add_content('how about that')
ed.add_content('delete this')
ed.del_content('delete this')
