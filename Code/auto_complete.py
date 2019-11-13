class DictNode():
    def __init__(self, letter):
        self.letter = letter
        self.children = dict()
        self.terminal = False

    def __hash__(self):
        return hash(self.letter)

    def __eq__(self, other):
        return self.letter == other.letter

    def __len__(self):
        return len(self.children)

    def is_terminal(self):
        return self.terminal

    def has_child(self, letter):
        return letter in self.children

    def add_child(self, letter):
        if not self.has_child(letter):
            self.children[letter] = Node(letter)

    def get_child(self, letter):
        return self.children[letter]


class ListNode():
    def __init__(self, letter):
        self.letter = letter
        self.children = [None] * 26
        self.terminal = False

    def get_char_index(self, letter):
        return ord(letter.lower()) - 97

    def has_child(self, letter):
        letter_index = self.get_char_index(letter)
        return self.children[letter_index] is not None

    def add_child(self, letter):
        letter_index = self.get_char_index(letter)
        try:
            if self.children[letter_index] is None:
                new_child_node = ListNode(letter)
                self.children[letter_index] = new_child_node
        except IndexError:
            print(letter_index, '"'+letter+'"')

    def get_child(self, letter):
        letter_index = self.get_char_index(letter)
        return self.children[letter_index]

    def is_terminal(self):
        return self.terminal


Node = ListNode


class Trie():
    def __init__(self, word_list=None):
        self.root = dict([(letter, Node(letter))
                          for letter in 'abcdefghijklmnopqrstuvwxyz'])
        self.word_count = 0
        if word_list is not None:
            self.add_words(word_list)

    def add_words(self, word_list):
        for word in word_list:
            self.add_word(word.lower())

    def add_word(self, word):
        first_letter = True
        node = None
        for letter in word:
            if not letter.isalpha():
                continue
            elif first_letter:
                node = self.root[letter]
                first_letter = False
            else:
                node.add_child(letter)
                node = node.get_child(letter)
        node.terminal = True

    def _get_final_node(self, prefix):
        first_letter = True
        if prefix == '':
            return None
        for letter in prefix:
            if not letter.isalpha():
                return None
            if first_letter:
                node = self.root[letter]
                first_letter = False
            else:
                if letter in node.children:
                    node = node.get_child(letter)
                else:
                    return None
        return node

    def _get_all_children(self, node, prefix):
        all_combos = []
        if node.is_terminal():
            all_combos.append(prefix)
        for child in node.children:
            all_combos.extend(self._get_all_children(
                node.get_child(child), prefix + child))
        return all_combos

    def auto_complete(self, prefix):
        prefix = prefix.lower()
        node = self._get_final_node(prefix)
        if node is None:
            return []
        words = self._get_all_children(node, prefix)
        return words


class AutoComplete():
    def __init__(self, dict_path='/usr/share/dict/words'):
        self.word_count = 0
        self.word_list = self.get_words_from_file(dict_path)
        self.trie_tree = Trie(self.word_list)

    def get_words_from_file(self, dict_path):
        f = open(dict_path)
        word_list = []
        for word in f.readlines():
            word_list.append(word.strip())
            self.word_count += 1
        return word_list

    def auto_complete(self, prefix):
        return self.trie_tree.auto_complete(prefix)


preme_words = ['archisupreme', 'presupreme', 'supersupreme',
               'supreme', 'supremely', 'supremeness', 'unsupreme']


def main():
    from time import time, sleep
    # from termcolor import colored
    blue = '\x1b[94m'
    green = '\x1b[92m'
    yellow = '\x1b[93m'
    red = '\x1b[91m'
    end = '\033[0m'
    print(blue + 'Building trie...')
    start = time()
    ac = AutoComplete()
    print('Time to build trie:' + green, str(
        round(time() - start, 3)) + ' seconds')
    print(blue + 'Number of words:' + green, ac.word_count)
    while True:
        print(blue + 'Enter a lowercase prefix to find words with that prefix: ' +
              red + '(Q to quit)')
        pref = input(yellow)
        print('\033[0m')
        if pref == 'Q':
            print(red + 'Quitting...' + end)
            sleep(1)
            return
        else:
            words = ac.auto_complete(pref)
            words = [word if 'supreme' not in word else red +
                     word + green for word in words]
            print(green + ' ,'.join(words))
            print(blue)


if __name__ == '__main__':
    main()

    # words = ac.auto_complete('sup')
    # print(words)
