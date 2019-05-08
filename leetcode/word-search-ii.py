# 212. Word Search II
# difficulty: hard
# https://leetcode.com/problems/word-search-ii/

from collections import deque
from typing import List

import pytest


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        return find_words(board, words)


class TrieNode:
    def __init__(self, word=None, children=None):
        if children is None:
            children = {}
        self.word = word
        self.children = children


def find_words(board, words):
    root = build_trie(words)
    found = []

    n, m = len(board), len(board[0])
    for i in range(n):
        for j in range(m):
            visited = {}
            dfs(board, root, i, j, 0, visited, found)
    return found


def build_trie(words):
    root = TrieNode(None, {})
    for word in words:
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        # We only store word in leaf nodes
        node.word = word
    return root


def dfs(board, node, i, j, k, visited, found):
    n, m = len(board), len(board[0])

    if not (0 <= i < n and 0 <= j < m):
        return
    if not node.children:
        return
    if (i, j) in visited:
        return

    char = board[i][j]
    if char in node.children:
        node = node.children[char]
        if node.word:
            found.append(node.word)
            node.word = None

        params = [
            (i - 1, j),
            (i, j + 1),
            (i + 1, j),
            (i, j - 1),
        ]
        visited[(i, j)] = True
        for ii, jj in params:
            dfs(board, node, ii, jj, k + 1, visited, found)
        del visited[(i, j)]


def test_find_words_1():
    board = [
        ['o','a','a','n'],
        ['e','t','a','e'],
        ['i','h','k','r'],
        ['i','f','l','v']
    ]
    words = ['oath', 'pea', 'eat', 'rain']
    expected = ['eat', 'oath']

    s = Solution()
    assert set(expected) == set(s.findWords(board, words))


def test_find_words_2():
    board = [
        ['a', 'b'],
        ['a', 'a'],
    ]
    words = ['aba', 'baa', 'bab', 'aaab', 'aaa', 'aaaa', 'aaba']
    expected = ['aaa', 'aaab', 'aaba', 'aba', 'baa']

    # NOTE: One of the important keys is to use DFS, otherwise it won't catch
    # an edge case like 'aaba'.

    s = Solution()
    assert set(expected) == set(s.findWords(board, words))


def test_find_words_3():
    board = [
        ['a', 'b'],
        ['c', 'd'],
    ]
    words = ['acdb']
    expected = ['acdb']

    s = Solution()
    assert set(expected) == set(s.findWords(board, words))


def test_find_words_4():
    board = [
        ['a', 'b'],
        ['c', 'd'],
    ]
    words = ['ab', 'cb', 'ad', 'bd', 'ac', 'ca', 'da', 'bc', 'db', 'adcb', 'dabc', 'abb', 'acb']
    expected = ['ab', 'ac', 'bd', 'ca', 'db']

    s = Solution()
    assert set(expected) == set(s.findWords(board, words))


def test_find_words_5():
    board = [
        ['a', 'b', 'c'], 
        ['a', 'e', 'd'], 
        ['a', 'f', 'g'], 
    ]
    words = ['abcdefg', 'gfedcbaaa', 'eaabcdgfa', 'befa', 'dgc', 'ade']
    expected = ['abcdefg', 'befa', 'eaabcdgfa', 'gfedcbaaa']

    s = Solution()
    assert set(expected) == set(s.findWords(board, words))


def test_find_words_6():
    board = [
        ['b', 'a', 'a', 'b', 'a', 'b'], 
        ['a', 'b', 'a', 'a', 'a', 'a'], 
        ['a', 'b', 'a', 'a', 'a', 'b'], 
        ['a', 'b', 'a', 'b', 'b', 'a'], 
        ['a', 'a', 'b', 'b', 'a', 'b'], 
        ['a', 'a', 'b', 'b', 'b', 'a'], 
        ['a', 'a', 'b', 'a', 'a', 'b'], 
    ]
    words = [
        'bbaabaabaaaaabaababaaaaababb',
        'aabbaaabaaabaabaaaaaabbaaaba',
        'babaababbbbbbbaabaababaabaaa',
        'bbbaaabaabbaaababababbbbbaaa',
        'babbabbbbaabbabaaaaaabbbaaab',
        'bbbababbbbbbbababbabbbbbabaa',
        'babababbababaabbbbabbbbabbba',
        'abbbbbbaabaaabaaababaabbabba',
        'aabaabababbbbbbababbbababbaa',
        'aabbbbabbaababaaaabababbaaba',
        'ababaababaaabbabbaabbaabbaba',
        'abaabbbaaaaababbbaaaaabbbaab',
        'aabbabaabaabbabababaaabbbaab',
        'baaabaaaabbabaaabaabababaaaa',
        'aaabbabaaaababbabbaabbaabbaa',
        'aaabaaaaabaabbabaabbbbaabaaa',
        'abbaabbaaaabbaababababbaabbb',
        'baabaababbbbaaaabaaabbababbb',
        'aabaababbaababbaaabaabababab',
        'abbaaabbaabaabaabbbbaabbbbbb',
        'aaababaabbaaabbbaaabbabbabab',
        'bbababbbabbbbabbbbabbbbbabaa',
        'abbbaabbbaaababbbababbababba',
        'bbbbbbbabbbababbabaabababaab',
        'aaaababaabbbbabaaaaabaaaaabb',
        'bbaaabbbbabbaaabbaabbabbaaba',
        'aabaabbbbaabaabbabaabababaaa',
        'abbababbbaababaabbababababbb',
        'aabbbabbaaaababbbbabbababbbb',
        'babbbaabababbbbbbbbbaabbabaa',
    ]
    expected = [
        'aabbbbabbaababaaaabababbaaba',
        'abaabbbaaaaababbbaaaaabbbaab',
        'ababaababaaabbabbaabbaabbaba'
    ]

    s = Solution()
    assert set(expected) == set(s.findWords(board, words))


def test_find_words_7():
    board = [
        ['a', 'a', 'a', 'a'], 
        ['a', 'a', 'a', 'a'], 
        ['a', 'a', 'a', 'a'], 
        ['a', 'a', 'a', 'a'], 
        ['b', 'c', 'd', 'e'], 
        ['f', 'g', 'h', 'i'], 
        ['j', 'k', 'l', 'm'], 
        ['n', 'o', 'p', 'q'], 
        ['r', 's', 't', 'u'], 
        ['v', 'w', 'x', 'y'], 
        ['z', 'z', 'z', 'z'], 
    ]
    words = ['aaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaab', 'aaaaaaaaaaaaaaac', 'aaaaaaaaaaaaaaad', 'aaaaaaaaaaaaaaae', 'aaaaaaaaaaaaaaaf', 'aaaaaaaaaaaaaaag', 'aaaaaaaaaaaaaaah', 'aaaaaaaaaaaaaaai', 'aaaaaaaaaaaaaaaj', 'aaaaaaaaaaaaaaak', 'aaaaaaaaaaaaaaal', 'aaaaaaaaaaaaaaam', 'aaaaaaaaaaaaaaan', 'aaaaaaaaaaaaaaao', 'aaaaaaaaaaaaaaap', 'aaaaaaaaaaaaaaaq', 'aaaaaaaaaaaaaaar', 'aaaaaaaaaaaaaaas', 'aaaaaaaaaaaaaaat', 'aaaaaaaaaaaaaaau', 'aaaaaaaaaaaaaaav', 'aaaaaaaaaaaaaaaw', 'aaaaaaaaaaaaaaax', 'aaaaaaaaaaaaaaay', 'aaaaaaaaaaaaaaaz', 'aaaaaaaaaaaaaaba', 'aaaaaaaaaaaaaabb', 'aaaaaaaaaaaaaabc', 'aaaaaaaaaaaaaabd', 'aaaaaaaaaaaaaabe', 'aaaaaaaaaaaaaabf', 'aaaaaaaaaaaaaabg', 'aaaaaaaaaaaaaabh', 'aaaaaaaaaaaaaabi', 'aaaaaaaaaaaaaabj', 'aaaaaaaaaaaaaabk', 'aaaaaaaaaaaaaabl', 'aaaaaaaaaaaaaabm', 'aaaaaaaaaaaaaabn', 'aaaaaaaaaaaaaabo', 'aaaaaaaaaaaaaabp', 'aaaaaaaaaaaaaabq', 'aaaaaaaaaaaaaabr', 'aaaaaaaaaaaaaabs', 'aaaaaaaaaaaaaabt', 'aaaaaaaaaaaaaabu', 'aaaaaaaaaaaaaabv', 'aaaaaaaaaaaaaabw', 'aaaaaaaaaaaaaabx', 'aaaaaaaaaaaaaaby', 'aaaaaaaaaaaaaabz', 'aaaaaaaaaaaaaaca', 'aaaaaaaaaaaaaacb', 'aaaaaaaaaaaaaacc', 'aaaaaaaaaaaaaacd', 'aaaaaaaaaaaaaace', 'aaaaaaaaaaaaaacf', 'aaaaaaaaaaaaaacg', 'aaaaaaaaaaaaaach', 'aaaaaaaaaaaaaaci', 'aaaaaaaaaaaaaacj', 'aaaaaaaaaaaaaack', 'aaaaaaaaaaaaaacl', 'aaaaaaaaaaaaaacm', 'aaaaaaaaaaaaaacn', 'aaaaaaaaaaaaaaco', 'aaaaaaaaaaaaaacp', 'aaaaaaaaaaaaaacq', 'aaaaaaaaaaaaaacr', 'aaaaaaaaaaaaaacs', 'aaaaaaaaaaaaaact', 'aaaaaaaaaaaaaacu', 'aaaaaaaaaaaaaacv', 'aaaaaaaaaaaaaacw', 'aaaaaaaaaaaaaacx', 'aaaaaaaaaaaaaacy', 'aaaaaaaaaaaaaacz', 'aaaaaaaaaaaaaada', 'aaaaaaaaaaaaaadb', 'aaaaaaaaaaaaaadc', 'aaaaaaaaaaaaaadd', 'aaaaaaaaaaaaaade', 'aaaaaaaaaaaaaadf', 'aaaaaaaaaaaaaadg', 'aaaaaaaaaaaaaadh', 'aaaaaaaaaaaaaadi', 'aaaaaaaaaaaaaadj', 'aaaaaaaaaaaaaadk', 'aaaaaaaaaaaaaadl', 'aaaaaaaaaaaaaadm', 'aaaaaaaaaaaaaadn', 'aaaaaaaaaaaaaado', 'aaaaaaaaaaaaaadp', 'aaaaaaaaaaaaaadq', 'aaaaaaaaaaaaaadr', 'aaaaaaaaaaaaaads', 'aaaaaaaaaaaaaadt', 'aaaaaaaaaaaaaadu', 'aaaaaaaaaaaaaadv', 'aaaaaaaaaaaaaadw', 'aaaaaaaaaaaaaadx', 'aaaaaaaaaaaaaady', 'aaaaaaaaaaaaaadz', 'aaaaaaaaaaaaaaea', 'aaaaaaaaaaaaaaeb', 'aaaaaaaaaaaaaaec', 'aaaaaaaaaaaaaaed', 'aaaaaaaaaaaaaaee', 'aaaaaaaaaaaaaaef', 'aaaaaaaaaaaaaaeg', 'aaaaaaaaaaaaaaeh', 'aaaaaaaaaaaaaaei', 'aaaaaaaaaaaaaaej', 'aaaaaaaaaaaaaaek', 'aaaaaaaaaaaaaael', 'aaaaaaaaaaaaaaem', 'aaaaaaaaaaaaaaen', 'aaaaaaaaaaaaaaeo', 'aaaaaaaaaaaaaaep', 'aaaaaaaaaaaaaaeq', 'aaaaaaaaaaaaaaer', 'aaaaaaaaaaaaaaes', 'aaaaaaaaaaaaaaet', 'aaaaaaaaaaaaaaeu', 'aaaaaaaaaaaaaaev', 'aaaaaaaaaaaaaaew', 'aaaaaaaaaaaaaaex', 'aaaaaaaaaaaaaaey', 'aaaaaaaaaaaaaaez', 'aaaaaaaaaaaaaafa', 'aaaaaaaaaaaaaafb', 'aaaaaaaaaaaaaafc', 'aaaaaaaaaaaaaafd', 'aaaaaaaaaaaaaafe', 'aaaaaaaaaaaaaaff', 'aaaaaaaaaaaaaafg', 'aaaaaaaaaaaaaafh', 'aaaaaaaaaaaaaafi', 'aaaaaaaaaaaaaafj', 'aaaaaaaaaaaaaafk', 'aaaaaaaaaaaaaafl', 'aaaaaaaaaaaaaafm', 'aaaaaaaaaaaaaafn', 'aaaaaaaaaaaaaafo', 'aaaaaaaaaaaaaafp', 'aaaaaaaaaaaaaafq', 'aaaaaaaaaaaaaafr', 'aaaaaaaaaaaaaafs', 'aaaaaaaaaaaaaaft', 'aaaaaaaaaaaaaafu', 'aaaaaaaaaaaaaafv', 'aaaaaaaaaaaaaafw', 'aaaaaaaaaaaaaafx', 'aaaaaaaaaaaaaafy', 'aaaaaaaaaaaaaafz', 'aaaaaaaaaaaaaaga', 'aaaaaaaaaaaaaagb', 'aaaaaaaaaaaaaagc', 'aaaaaaaaaaaaaagd', 'aaaaaaaaaaaaaage', 'aaaaaaaaaaaaaagf', 'aaaaaaaaaaaaaagg', 'aaaaaaaaaaaaaagh', 'aaaaaaaaaaaaaagi', 'aaaaaaaaaaaaaagj', 'aaaaaaaaaaaaaagk', 'aaaaaaaaaaaaaagl', 'aaaaaaaaaaaaaagm', 'aaaaaaaaaaaaaagn', 'aaaaaaaaaaaaaago', 'aaaaaaaaaaaaaagp', 'aaaaaaaaaaaaaagq', 'aaaaaaaaaaaaaagr', 'aaaaaaaaaaaaaags', 'aaaaaaaaaaaaaagt', 'aaaaaaaaaaaaaagu', 'aaaaaaaaaaaaaagv', 'aaaaaaaaaaaaaagw', 'aaaaaaaaaaaaaagx', 'aaaaaaaaaaaaaagy', 'aaaaaaaaaaaaaagz', 'aaaaaaaaaaaaaaha', 'aaaaaaaaaaaaaahb', 'aaaaaaaaaaaaaahc', 'aaaaaaaaaaaaaahd', 'aaaaaaaaaaaaaahe', 'aaaaaaaaaaaaaahf', 'aaaaaaaaaaaaaahg', 'aaaaaaaaaaaaaahh', 'aaaaaaaaaaaaaahi', 'aaaaaaaaaaaaaahj', 'aaaaaaaaaaaaaahk', 'aaaaaaaaaaaaaahl', 'aaaaaaaaaaaaaahm', 'aaaaaaaaaaaaaahn', 'aaaaaaaaaaaaaaho', 'aaaaaaaaaaaaaahp', 'aaaaaaaaaaaaaahq', 'aaaaaaaaaaaaaahr', 'aaaaaaaaaaaaaahs', 'aaaaaaaaaaaaaaht', 'aaaaaaaaaaaaaahu', 'aaaaaaaaaaaaaahv', 'aaaaaaaaaaaaaahw', 'aaaaaaaaaaaaaahx', 'aaaaaaaaaaaaaahy', 'aaaaaaaaaaaaaahz', 'aaaaaaaaaaaaaaia', 'aaaaaaaaaaaaaaib', 'aaaaaaaaaaaaaaic', 'aaaaaaaaaaaaaaid', 'aaaaaaaaaaaaaaie', 'aaaaaaaaaaaaaaif', 'aaaaaaaaaaaaaaig', 'aaaaaaaaaaaaaaih', 'aaaaaaaaaaaaaaii', 'aaaaaaaaaaaaaaij', 'aaaaaaaaaaaaaaik', 'aaaaaaaaaaaaaail', 'aaaaaaaaaaaaaaim', 'aaaaaaaaaaaaaain', 'aaaaaaaaaaaaaaio', 'aaaaaaaaaaaaaaip', 'aaaaaaaaaaaaaaiq', 'aaaaaaaaaaaaaair', 'aaaaaaaaaaaaaais', 'aaaaaaaaaaaaaait', 'aaaaaaaaaaaaaaiu', 'aaaaaaaaaaaaaaiv', 'aaaaaaaaaaaaaaiw', 'aaaaaaaaaaaaaaix', 'aaaaaaaaaaaaaaiy', 'aaaaaaaaaaaaaaiz', 'aaaaaaaaaaaaaaja', 'aaaaaaaaaaaaaajb', 'aaaaaaaaaaaaaajc', 'aaaaaaaaaaaaaajd', 'aaaaaaaaaaaaaaje', 'aaaaaaaaaaaaaajf', 'aaaaaaaaaaaaaajg', 'aaaaaaaaaaaaaajh', 'aaaaaaaaaaaaaaji', 'aaaaaaaaaaaaaajj', 'aaaaaaaaaaaaaajk', 'aaaaaaaaaaaaaajl', 'aaaaaaaaaaaaaajm', 'aaaaaaaaaaaaaajn', 'aaaaaaaaaaaaaajo', 'aaaaaaaaaaaaaajp', 'aaaaaaaaaaaaaajq', 'aaaaaaaaaaaaaajr', 'aaaaaaaaaaaaaajs', 'aaaaaaaaaaaaaajt', 'aaaaaaaaaaaaaaju', 'aaaaaaaaaaaaaajv', 'aaaaaaaaaaaaaajw', 'aaaaaaaaaaaaaajx', 'aaaaaaaaaaaaaajy', 'aaaaaaaaaaaaaajz', 'aaaaaaaaaaaaaaka', 'aaaaaaaaaaaaaakb', 'aaaaaaaaaaaaaakc', 'aaaaaaaaaaaaaakd', 'aaaaaaaaaaaaaake', 'aaaaaaaaaaaaaakf', 'aaaaaaaaaaaaaakg', 'aaaaaaaaaaaaaakh', 'aaaaaaaaaaaaaaki', 'aaaaaaaaaaaaaakj', 'aaaaaaaaaaaaaakk', 'aaaaaaaaaaaaaakl', 'aaaaaaaaaaaaaakm', 'aaaaaaaaaaaaaakn', 'aaaaaaaaaaaaaako', 'aaaaaaaaaaaaaakp', 'aaaaaaaaaaaaaakq', 'aaaaaaaaaaaaaakr', 'aaaaaaaaaaaaaaks', 'aaaaaaaaaaaaaakt', 'aaaaaaaaaaaaaaku', 'aaaaaaaaaaaaaakv', 'aaaaaaaaaaaaaakw', 'aaaaaaaaaaaaaakx', 'aaaaaaaaaaaaaaky', 'aaaaaaaaaaaaaakz', 'aaaaaaaaaaaaaala', 'aaaaaaaaaaaaaalb', 'aaaaaaaaaaaaaalc', 'aaaaaaaaaaaaaald', 'aaaaaaaaaaaaaale', 'aaaaaaaaaaaaaalf', 'aaaaaaaaaaaaaalg', 'aaaaaaaaaaaaaalh', 'aaaaaaaaaaaaaali', 'aaaaaaaaaaaaaalj', 'aaaaaaaaaaaaaalk', 'aaaaaaaaaaaaaall', 'aaaaaaaaaaaaaalm', 'aaaaaaaaaaaaaaln', 'aaaaaaaaaaaaaalo', 'aaaaaaaaaaaaaalp', 'aaaaaaaaaaaaaalq', 'aaaaaaaaaaaaaalr', 'aaaaaaaaaaaaaals', 'aaaaaaaaaaaaaalt', 'aaaaaaaaaaaaaalu', 'aaaaaaaaaaaaaalv', 'aaaaaaaaaaaaaalw', 'aaaaaaaaaaaaaalx', 'aaaaaaaaaaaaaaly', 'aaaaaaaaaaaaaalz', 'aaaaaaaaaaaaaama', 'aaaaaaaaaaaaaamb', 'aaaaaaaaaaaaaamc', 'aaaaaaaaaaaaaamd', 'aaaaaaaaaaaaaame', 'aaaaaaaaaaaaaamf', 'aaaaaaaaaaaaaamg', 'aaaaaaaaaaaaaamh', 'aaaaaaaaaaaaaami', 'aaaaaaaaaaaaaamj', 'aaaaaaaaaaaaaamk', 'aaaaaaaaaaaaaaml', 'aaaaaaaaaaaaaamm', 'aaaaaaaaaaaaaamn', 'aaaaaaaaaaaaaamo', 'aaaaaaaaaaaaaamp', 'aaaaaaaaaaaaaamq', 'aaaaaaaaaaaaaamr', 'aaaaaaaaaaaaaams', 'aaaaaaaaaaaaaamt', 'aaaaaaaaaaaaaamu', 'aaaaaaaaaaaaaamv', 'aaaaaaaaaaaaaamw', 'aaaaaaaaaaaaaamx', 'aaaaaaaaaaaaaamy', 'aaaaaaaaaaaaaamz', 'aaaaaaaaaaaaaana', 'aaaaaaaaaaaaaanb', 'aaaaaaaaaaaaaanc', 'aaaaaaaaaaaaaand', 'aaaaaaaaaaaaaane', 'aaaaaaaaaaaaaanf', 'aaaaaaaaaaaaaang', 'aaaaaaaaaaaaaanh', 'aaaaaaaaaaaaaani', 'aaaaaaaaaaaaaanj', 'aaaaaaaaaaaaaank', 'aaaaaaaaaaaaaanl', 'aaaaaaaaaaaaaanm', 'aaaaaaaaaaaaaann', 'aaaaaaaaaaaaaano', 'aaaaaaaaaaaaaanp', 'aaaaaaaaaaaaaanq', 'aaaaaaaaaaaaaanr', 'aaaaaaaaaaaaaans', 'aaaaaaaaaaaaaant', 'aaaaaaaaaaaaaanu', 'aaaaaaaaaaaaaanv', 'aaaaaaaaaaaaaanw', 'aaaaaaaaaaaaaanx', 'aaaaaaaaaaaaaany', 'aaaaaaaaaaaaaanz', 'aaaaaaaaaaaaaaoa', 'aaaaaaaaaaaaaaob', 'aaaaaaaaaaaaaaoc', 'aaaaaaaaaaaaaaod', 'aaaaaaaaaaaaaaoe', 'aaaaaaaaaaaaaaof', 'aaaaaaaaaaaaaaog', 'aaaaaaaaaaaaaaoh', 'aaaaaaaaaaaaaaoi', 'aaaaaaaaaaaaaaoj', 'aaaaaaaaaaaaaaok', 'aaaaaaaaaaaaaaol', 'aaaaaaaaaaaaaaom', 'aaaaaaaaaaaaaaon', 'aaaaaaaaaaaaaaoo', 'aaaaaaaaaaaaaaop', 'aaaaaaaaaaaaaaoq', 'aaaaaaaaaaaaaaor', 'aaaaaaaaaaaaaaos', 'aaaaaaaaaaaaaaot', 'aaaaaaaaaaaaaaou', 'aaaaaaaaaaaaaaov', 'aaaaaaaaaaaaaaow', 'aaaaaaaaaaaaaaox', 'aaaaaaaaaaaaaaoy', 'aaaaaaaaaaaaaaoz', 'aaaaaaaaaaaaaapa', 'aaaaaaaaaaaaaapb', 'aaaaaaaaaaaaaapc', 'aaaaaaaaaaaaaapd', 'aaaaaaaaaaaaaape', 'aaaaaaaaaaaaaapf', 'aaaaaaaaaaaaaapg', 'aaaaaaaaaaaaaaph', 'aaaaaaaaaaaaaapi', 'aaaaaaaaaaaaaapj', 'aaaaaaaaaaaaaapk', 'aaaaaaaaaaaaaapl', 'aaaaaaaaaaaaaapm', 'aaaaaaaaaaaaaapn', 'aaaaaaaaaaaaaapo', 'aaaaaaaaaaaaaapp', 'aaaaaaaaaaaaaapq', 'aaaaaaaaaaaaaapr', 'aaaaaaaaaaaaaaps', 'aaaaaaaaaaaaaapt', 'aaaaaaaaaaaaaapu', 'aaaaaaaaaaaaaapv', 'aaaaaaaaaaaaaapw', 'aaaaaaaaaaaaaapx', 'aaaaaaaaaaaaaapy', 'aaaaaaaaaaaaaapz', 'aaaaaaaaaaaaaaqa', 'aaaaaaaaaaaaaaqb', 'aaaaaaaaaaaaaaqc', 'aaaaaaaaaaaaaaqd', 'aaaaaaaaaaaaaaqe', 'aaaaaaaaaaaaaaqf', 'aaaaaaaaaaaaaaqg', 'aaaaaaaaaaaaaaqh', 'aaaaaaaaaaaaaaqi', 'aaaaaaaaaaaaaaqj', 'aaaaaaaaaaaaaaqk', 'aaaaaaaaaaaaaaql', 'aaaaaaaaaaaaaaqm', 'aaaaaaaaaaaaaaqn', 'aaaaaaaaaaaaaaqo', 'aaaaaaaaaaaaaaqp', 'aaaaaaaaaaaaaaqq', 'aaaaaaaaaaaaaaqr', 'aaaaaaaaaaaaaaqs', 'aaaaaaaaaaaaaaqt', 'aaaaaaaaaaaaaaqu', 'aaaaaaaaaaaaaaqv', 'aaaaaaaaaaaaaaqw', 'aaaaaaaaaaaaaaqx', 'aaaaaaaaaaaaaaqy', 'aaaaaaaaaaaaaaqz', 'aaaaaaaaaaaaaara', 'aaaaaaaaaaaaaarb', 'aaaaaaaaaaaaaarc', 'aaaaaaaaaaaaaard', 'aaaaaaaaaaaaaare', 'aaaaaaaaaaaaaarf', 'aaaaaaaaaaaaaarg', 'aaaaaaaaaaaaaarh', 'aaaaaaaaaaaaaari', 'aaaaaaaaaaaaaarj', 'aaaaaaaaaaaaaark', 'aaaaaaaaaaaaaarl', 'aaaaaaaaaaaaaarm', 'aaaaaaaaaaaaaarn', 'aaaaaaaaaaaaaaro', 'aaaaaaaaaaaaaarp', 'aaaaaaaaaaaaaarq', 'aaaaaaaaaaaaaarr', 'aaaaaaaaaaaaaars', 'aaaaaaaaaaaaaart', 'aaaaaaaaaaaaaaru', 'aaaaaaaaaaaaaarv', 'aaaaaaaaaaaaaarw', 'aaaaaaaaaaaaaarx', 'aaaaaaaaaaaaaary', 'aaaaaaaaaaaaaarz', 'aaaaaaaaaaaaaasa', 'aaaaaaaaaaaaaasb', 'aaaaaaaaaaaaaasc', 'aaaaaaaaaaaaaasd', 'aaaaaaaaaaaaaase', 'aaaaaaaaaaaaaasf', 'aaaaaaaaaaaaaasg', 'aaaaaaaaaaaaaash', 'aaaaaaaaaaaaaasi', 'aaaaaaaaaaaaaasj', 'aaaaaaaaaaaaaask', 'aaaaaaaaaaaaaasl', 'aaaaaaaaaaaaaasm', 'aaaaaaaaaaaaaasn', 'aaaaaaaaaaaaaaso', 'aaaaaaaaaaaaaasp', 'aaaaaaaaaaaaaasq', 'aaaaaaaaaaaaaasr', 'aaaaaaaaaaaaaass', 'aaaaaaaaaaaaaast', 'aaaaaaaaaaaaaasu', 'aaaaaaaaaaaaaasv', 'aaaaaaaaaaaaaasw', 'aaaaaaaaaaaaaasx', 'aaaaaaaaaaaaaasy', 'aaaaaaaaaaaaaasz', 'aaaaaaaaaaaaaata', 'aaaaaaaaaaaaaatb', 'aaaaaaaaaaaaaatc', 'aaaaaaaaaaaaaatd', 'aaaaaaaaaaaaaate', 'aaaaaaaaaaaaaatf', 'aaaaaaaaaaaaaatg', 'aaaaaaaaaaaaaath', 'aaaaaaaaaaaaaati', 'aaaaaaaaaaaaaatj', 'aaaaaaaaaaaaaatk', 'aaaaaaaaaaaaaatl', 'aaaaaaaaaaaaaatm', 'aaaaaaaaaaaaaatn', 'aaaaaaaaaaaaaato', 'aaaaaaaaaaaaaatp', 'aaaaaaaaaaaaaatq', 'aaaaaaaaaaaaaatr', 'aaaaaaaaaaaaaats', 'aaaaaaaaaaaaaatt', 'aaaaaaaaaaaaaatu', 'aaaaaaaaaaaaaatv', 'aaaaaaaaaaaaaatw', 'aaaaaaaaaaaaaatx', 'aaaaaaaaaaaaaaty', 'aaaaaaaaaaaaaatz', 'aaaaaaaaaaaaaaua', 'aaaaaaaaaaaaaaub', 'aaaaaaaaaaaaaauc', 'aaaaaaaaaaaaaaud', 'aaaaaaaaaaaaaaue', 'aaaaaaaaaaaaaauf', 'aaaaaaaaaaaaaaug', 'aaaaaaaaaaaaaauh', 'aaaaaaaaaaaaaaui', 'aaaaaaaaaaaaaauj', 'aaaaaaaaaaaaaauk', 'aaaaaaaaaaaaaaul', 'aaaaaaaaaaaaaaum', 'aaaaaaaaaaaaaaun', 'aaaaaaaaaaaaaauo', 'aaaaaaaaaaaaaaup', 'aaaaaaaaaaaaaauq', 'aaaaaaaaaaaaaaur', 'aaaaaaaaaaaaaaus', 'aaaaaaaaaaaaaaut', 'aaaaaaaaaaaaaauu', 'aaaaaaaaaaaaaauv', 'aaaaaaaaaaaaaauw', 'aaaaaaaaaaaaaaux', 'aaaaaaaaaaaaaauy', 'aaaaaaaaaaaaaauz', 'aaaaaaaaaaaaaava', 'aaaaaaaaaaaaaavb', 'aaaaaaaaaaaaaavc', 'aaaaaaaaaaaaaavd', 'aaaaaaaaaaaaaave', 'aaaaaaaaaaaaaavf', 'aaaaaaaaaaaaaavg', 'aaaaaaaaaaaaaavh', 'aaaaaaaaaaaaaavi', 'aaaaaaaaaaaaaavj', 'aaaaaaaaaaaaaavk', 'aaaaaaaaaaaaaavl', 'aaaaaaaaaaaaaavm', 'aaaaaaaaaaaaaavn', 'aaaaaaaaaaaaaavo', 'aaaaaaaaaaaaaavp', 'aaaaaaaaaaaaaavq', 'aaaaaaaaaaaaaavr', 'aaaaaaaaaaaaaavs', 'aaaaaaaaaaaaaavt', 'aaaaaaaaaaaaaavu', 'aaaaaaaaaaaaaavv', 'aaaaaaaaaaaaaavw', 'aaaaaaaaaaaaaavx', 'aaaaaaaaaaaaaavy', 'aaaaaaaaaaaaaavz', 'aaaaaaaaaaaaaawa', 'aaaaaaaaaaaaaawb', 'aaaaaaaaaaaaaawc', 'aaaaaaaaaaaaaawd', 'aaaaaaaaaaaaaawe', 'aaaaaaaaaaaaaawf', 'aaaaaaaaaaaaaawg', 'aaaaaaaaaaaaaawh', 'aaaaaaaaaaaaaawi', 'aaaaaaaaaaaaaawj', 'aaaaaaaaaaaaaawk', 'aaaaaaaaaaaaaawl', 'aaaaaaaaaaaaaawm', 'aaaaaaaaaaaaaawn', 'aaaaaaaaaaaaaawo', 'aaaaaaaaaaaaaawp', 'aaaaaaaaaaaaaawq', 'aaaaaaaaaaaaaawr', 'aaaaaaaaaaaaaaws', 'aaaaaaaaaaaaaawt', 'aaaaaaaaaaaaaawu', 'aaaaaaaaaaaaaawv', 'aaaaaaaaaaaaaaww', 'aaaaaaaaaaaaaawx', 'aaaaaaaaaaaaaawy', 'aaaaaaaaaaaaaawz', 'aaaaaaaaaaaaaaxa', 'aaaaaaaaaaaaaaxb', 'aaaaaaaaaaaaaaxc', 'aaaaaaaaaaaaaaxd', 'aaaaaaaaaaaaaaxe', 'aaaaaaaaaaaaaaxf', 'aaaaaaaaaaaaaaxg', 'aaaaaaaaaaaaaaxh', 'aaaaaaaaaaaaaaxi', 'aaaaaaaaaaaaaaxj', 'aaaaaaaaaaaaaaxk', 'aaaaaaaaaaaaaaxl', 'aaaaaaaaaaaaaaxm', 'aaaaaaaaaaaaaaxn', 'aaaaaaaaaaaaaaxo', 'aaaaaaaaaaaaaaxp', 'aaaaaaaaaaaaaaxq', 'aaaaaaaaaaaaaaxr', 'aaaaaaaaaaaaaaxs', 'aaaaaaaaaaaaaaxt', 'aaaaaaaaaaaaaaxu', 'aaaaaaaaaaaaaaxv', 'aaaaaaaaaaaaaaxw', 'aaaaaaaaaaaaaaxx', 'aaaaaaaaaaaaaaxy', 'aaaaaaaaaaaaaaxz', 'aaaaaaaaaaaaaaya', 'aaaaaaaaaaaaaayb', 'aaaaaaaaaaaaaayc', 'aaaaaaaaaaaaaayd', 'aaaaaaaaaaaaaaye', 'aaaaaaaaaaaaaayf', 'aaaaaaaaaaaaaayg', 'aaaaaaaaaaaaaayh', 'aaaaaaaaaaaaaayi', 'aaaaaaaaaaaaaayj', 'aaaaaaaaaaaaaayk', 'aaaaaaaaaaaaaayl', 'aaaaaaaaaaaaaaym', 'aaaaaaaaaaaaaayn', 'aaaaaaaaaaaaaayo', 'aaaaaaaaaaaaaayp', 'aaaaaaaaaaaaaayq', 'aaaaaaaaaaaaaayr', 'aaaaaaaaaaaaaays', 'aaaaaaaaaaaaaayt', 'aaaaaaaaaaaaaayu', 'aaaaaaaaaaaaaayv', 'aaaaaaaaaaaaaayw', 'aaaaaaaaaaaaaayx', 'aaaaaaaaaaaaaayy', 'aaaaaaaaaaaaaayz', 'aaaaaaaaaaaaaaza', 'aaaaaaaaaaaaaazb', 'aaaaaaaaaaaaaazc', 'aaaaaaaaaaaaaazd', 'aaaaaaaaaaaaaaze', 'aaaaaaaaaaaaaazf', 'aaaaaaaaaaaaaazg', 'aaaaaaaaaaaaaazh', 'aaaaaaaaaaaaaazi', 'aaaaaaaaaaaaaazj', 'aaaaaaaaaaaaaazk', 'aaaaaaaaaaaaaazl', 'aaaaaaaaaaaaaazm', 'aaaaaaaaaaaaaazn', 'aaaaaaaaaaaaaazo', 'aaaaaaaaaaaaaazp', 'aaaaaaaaaaaaaazq', 'aaaaaaaaaaaaaazr', 'aaaaaaaaaaaaaazs', 'aaaaaaaaaaaaaazt', 'aaaaaaaaaaaaaazu', 'aaaaaaaaaaaaaazv', 'aaaaaaaaaaaaaazw', 'aaaaaaaaaaaaaazx', 'aaaaaaaaaaaaaazy', 'aaaaaaaaaaaaaazz']
    expected = ['aaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaab', 'aaaaaaaaaaaaaaac', 'aaaaaaaaaaaaaaad', 'aaaaaaaaaaaaaaae', 'aaaaaaaaaaaaaabc', 'aaaaaaaaaaaaaabf', 'aaaaaaaaaaaaaacb', 'aaaaaaaaaaaaaacd', 'aaaaaaaaaaaaaacg', 'aaaaaaaaaaaaaadc', 'aaaaaaaaaaaaaade', 'aaaaaaaaaaaaaadh', 'aaaaaaaaaaaaaaed', 'aaaaaaaaaaaaaaei']

    s = Solution()
    assert set(expected) == set(s.findWords(board, words))


if __name__ == '__main__':
    pytest.main(['-v', __file__])
