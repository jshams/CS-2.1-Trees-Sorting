class DictNode():
    def __init__(self, letter):
        '''Initialize a node object with its letter'''
        self.letter = letter
        self.children = dict()
        self.terminal = False

    def __len__(self):
        '''returns the number of children'''
        return len(self.children)

    def is_terminal(self):
        '''return a boolean indicating whether this node is terminal'''
        return self.terminal

    def has_child(self, letter):
        '''returns a boolean indicating whether this node has letter as a child'''
        return letter in self.children

    def add_child(self, letter):
        '''adds a letter to its children if it isnt already a child'''
        if not self.has_child(letter):
            self.children[letter] = Node(letter)

    def get_child(self, letter):
        '''returns the child node associated with the letter value'''
        return self.children[letter]

    def get_children(self):
        '''generator that yields each child letter in this nodes children'''
        for child in self.children:
            yield child


class ListNode():
    def __init__(self, letter):
        '''Initialize a node object with its letter'''
        self.letter = letter
        self.children = [None] * 26
        self.terminal = False
        # use a small amount of extra memory to save lots of time
        self.children_letters = ''

    def get_char_index(self, letter):
        '''returns the index of a the placement of a letter in children list'''
        return ord(letter.lower()) - 97

    def has_child(self, letter):
        '''returns a boolean indicating whether this node has letter as a child'''
        letter_index = self.get_char_index(letter)
        return self.children[letter_index] is not None

    def add_child(self, letter):
        '''adds a letter to its children if it isnt already a child'''
        letter_index = self.get_char_index(letter)
        if self.children[letter_index] is None:
            new_child_node = ListNode(letter)
            self.children[letter_index] = new_child_node
            self.children_letters += letter

    def get_child(self, letter):
        '''returns the child node associated with the letter value'''
        letter_index = self.get_char_index(letter)
        return self.children[letter_index]

    def is_terminal(self):
        '''return a boolean indicating whether this node is terminal'''
        return self.terminal

    def get_children(self):
        '''generator that yields each child letter in this nodes children'''
        for child in self.children_letters:
            yield child


class Trie():
    def __init__(self, word_list=None):
        '''initialize a Trie tree with a list of words'''
        self.root = dict([(letter, Node(letter))
                          for letter in 'abcdefghijklmnopqrstuvwxyz'])
        self.word_count = 0
        if word_list is not None:
            self.add_words(word_list)

    def add_words(self, word_list):
        '''given a list of words, add each one to the tree'''
        for word in word_list:
            self.add_word(word.lower())

    def add_word(self, word):
        '''adds a single word to the tree'''
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
        '''given a prefix this will return the node of the last
        letter in the prefix'''
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
                if node.has_child(letter):
                    node = node.get_child(letter)
                else:
                    return None
        return node

    def _complete(self, node, prefix):
        '''starting from node, this will recursively find and return a 
        list of words that stem from that node. It will also attatch the
        prefix to the front'''
        all_combos = []
        if node.is_terminal():
            all_combos.append(prefix)
        for child_letter in node.get_children():
            all_combos.extend(self._complete(
                node.get_child(child_letter), prefix + child_letter))
        return all_combos

    def auto_complete(self, prefix):
        '''given a prefix, find the final node of the prefix, then return a
        a lits with all words in the tree that complete the prefix'''
        prefix = prefix.lower()
        node = self._get_final_node(prefix)
        if node is None:
            return []
        words = self._complete(node, prefix)
        return words


class AutoComplete():
    def __init__(self, dict_path='/usr/share/dict/words'):
        '''initialize an autocomplete class with a file path to a 
        txt file containing words'''
        self.word_count = 0
        self.word_list = self.get_words_from_file(dict_path)
        self.trie_tree = Trie(self.word_list)

    def get_words_from_file(self, dict_path):
        '''gets words from a file and returns them in a list'''
        f = open(dict_path)
        word_list = []
        for word in f.readlines():
            word_list.append(word.strip())
            self.word_count += 1
        return word_list

    def auto_complete(self, prefix):
        '''given a prefix this will complete the prefix using Trie
        class methods'''
        return self.trie_tree.auto_complete(prefix)


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
        print(end)
        if pref == 'Q':
            print(red + 'Quitting...' + end)
            sleep(1)
            return
        else:
            words = ac.auto_complete(pref)
            # words = [word if 'supreme' not in word else red +
            #          word + green for word in words]
            print(green + ', '.join(words))
            print(blue)


def time_it():
    from time import time, sleep
    start = time()
    ac = AutoComplete()
    print('Time to build trie (Lists): {} seconds'.format(str(
        round(time() - start, 3))))
    start = time()
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        for other_letter in 'aeiou':
            ac.auto_complete(letter)
            ac.auto_complete(letter + other_letter)
    print('time to run many processes: {} seconds'.format(str(
        round(time() - start, 3))))
    sleep(1)


if __name__ == '__main__':
    # Node = DictNode
    Node = DictNode
    # main()
    time_it()
