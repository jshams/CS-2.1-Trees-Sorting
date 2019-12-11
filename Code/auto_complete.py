class DictNode():
    def __init__(self, character):
        '''Initialize a node object with its character'''
        self.character = character
        self.children = dict()
        self.terminal = False

    def __len__(self):
        '''returns the number of children'''
        return len(self.children)

    def is_terminal(self):
        '''return a boolean indicating whether this node is terminal'''
        return self.terminal

    def has_child(self, character):
        '''returns a boolean indicating whether this node has character as a child'''
        return character in self.children

    def add_child(self, character):
        '''adds a character to its children if it isnt already a child'''
        if not self.has_child(character):
            self.children[character] = Node(character)
        else:
            raise ValueError(f'DictNode object already has child "{character}"')

    def get_child(self, character):
        '''returns the child node associated with the character value'''
        if character not in self.children:
            raise ValueError(f'DictNode object has no child "{character}"')
        return self.children[character]

    def get_children(self):
        '''generator that yields each child character in this nodes children'''
        for child in self.children:
            yield child
    
    def num_children(self):
        '''returns an integer denoting the number of children this node has'''
        return len(self.children)


class ListNode():
    def __init__(self, character):
        '''Initialize a node object with its character'''
        self.character = character
        self.children = [None] * 26
        self.terminal = False
        # use a small amount of extra memory to save lots of time
        self.children_letters = ''

    def get_char_index(self, character):
        '''returns the index of a the placement of a character in children list'''
        return ord(character.lower()) - 97

    def has_child(self, character):
        '''returns a boolean indicating whether this node has character as a child'''
        letter_index = self.get_char_index(character)
        return self.children[letter_index] is not None

    def add_child(self, character):
        '''adds a character to its children if it isnt already a child'''
        letter_index = self.get_char_index(character)
        if self.children[letter_index] is None:
            new_child_node = ListNode(character)
            self.children[letter_index] = new_child_node
            self.children_letters += character
        else:
            raise ValueError(f'ListNode object already has child "{character}"')

    def get_child(self, character):
        '''returns the child node associated with the character value'''
        letter_index = self.get_char_index(character)
        if self.children[letter_index] is None:
            raise ValueError(f'ListNode object has no child "{character}"')
        return self.children[letter_index]

    def is_terminal(self):
        '''return a boolean indicating whether this node is terminal'''
        return self.terminal

    def get_children(self):
        '''generator that yields each child character in this nodes children'''
        for child in self.children_letters:
            yield child
    
    def num_children(self):
        '''returns an integer denoting the number of children this node has'''
        return sum([character is not None for character in self.children])


class Trie():
    def __init__(self, word_list=None):
        '''initialize a Trie tree with a list of words'''
        self.root = Node('^')
        self.size = 0
        if word_list is not None:
            self.add_words(word_list)
    
    def is_empty(self):
        return self.size == 0

    def add_words(self, word_list):
        '''given a list of words, add each one to the tree'''
        for word in word_list:
            self.insert(word.lower())

    def insert(self, word):
        '''adds a single word to the tree'''
        node = self.root
        for character in word:
            if not character.isalpha():
                continue
            else:
                if not node.has_child(character):
                    node.add_child(character)
                node = node.get_child(character)
        if not node.is_terminal():
            node.terminal = True
            self.size += 1

    
    def contains(self, word):
        '''returns a boolean indicating whether that word is in this trie'''
        node = self.root
        for character in word:
            if not character.isalpha():
                return False
            else:
                if node.has_child(character):
                    node = node.get_child(character)
                else:
                    return False
        return node.is_terminal()

    def _get_final_node(self, prefix):
        '''given a prefix this will return the node of the last
        character in the prefix'''
        # if prefix == '':
        #     return self.root
        node = self.root
        for character in prefix:
            if not character.isalpha():
                return None
            else:
                if node.has_child(character):
                    node = node.get_child(character)
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
        for child_character in node.get_children():
            all_combos.extend(self._complete(
                node.get_child(child_character), prefix + child_character))
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
    
    def strings(self):
        '''will return a list of all words in this trie'''
        return self.auto_complete('')


class AutoComplete():
    def __init__(self, dict_path='/usr/share/dict/words'):
        '''initialize an autocomplete class with a file path to a 
        txt file containing words'''
        self.size = 0
        self.word_list = self.get_words_from_file(dict_path)
        self.trie_tree = Trie(self.word_list)

    def get_words_from_file(self, dict_path):
        '''gets words from a file and returns them in a list'''
        f = open(dict_path)
        word_list = []
        for word in f.readlines():
            word_list.append(word.strip())
            self.size += 1
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
    print(blue + 'Number of words:' + green, ac.size)
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
            now = time()
            words = ac.auto_complete(pref)
            # words = [word if 'supreme' not in word else red +
            #          word + green for word in words]
            print(green + ', '.join(words))
            print(f'time: {round((time() - now) * 1000, 4)}ms')
            print(blue)


def time_it():
    from time import time, sleep
    start = time()
    ac = AutoComplete()
    node_type = 'dicts' if Node == DictNode else 'lists'
    print('Time to build trie ({}) : {} seconds'.format(node_type, str(
        round(time() - start, 3))))
    start = time()
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        for other_letter in 'aeiou':
            ac.auto_complete(letter)
            ac.auto_complete(letter + other_letter)
    print('time to run many processes: {} seconds'.format(str(
        round(time() - start, 3))))
    sleep(1)

Node = ListNode
if __name__ == '__main__':
    # Node = ListNode
    main()
    # time_it()
