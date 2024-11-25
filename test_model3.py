# импорт nltk
import nltk

# некоторые дополнительные компоненты для сегментации, токенизации
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# загрузка универсального набора тегов
nltk.download('universal_tagset')

# импорт класса word_tokenize
from nltk.tokenize import word_tokenize

# применение маркера слова к текстовой строке и нахождение тега POS

nltk.pos_tag(word_tokenize("In the present study, we examine the outcomes of such a period of no exposure on the neurocognition of L2 grammar:"), tagset='universal')

import nltk
from nltk import Production, CFG

# грамматика
cgrammar = nltk.CFG.fromstring("""
S -> NP VP
VP -> V NP
PP -> P NP
NP -> NP PP | Det N | 'Peter' | 'Denver'
V -> 'prefers'
P -> 'from'
N -> 'flight'
Det -> 'the'
""")

# печать грамматики
print(cgrammar, '\n')

sent = ['Peter', 'prefers', 'the', 'flight', 'from', 'Denver']

# Используйте анализатор диаграмм
cparser = nltk.ChartParser(cgrammar)

for tree in cparser.parse(sent):
  print(tree)

# постройте деревья
import svgling
svgling.draw_tree(tree)

a_grammar = nltk.CFG.fromstring("""
S -> NP VP
PP -> P NP
NP -> Det N | Det N PP | 'I'
VP -> V NP | VP PP
Det -> 'an' | 'my'
N -> 'elephant' | 'pajamas'
V -> 'shot'
P -> 'in'
""")

sent = ['I', 'shot', 'an', 'elephant', 'in', 'my', 'pajamas']

parser = nltk.ChartParser(a_grammar)

for tree in parser.parse(sent):
  print(tree)

import os
import svgling
from nltk.tree import Tree
from nltk.draw.tree import TreeView

# используем строчный формат
t1 = Tree.fromstring('(S(NP/I)(VP(VP(V/shot)(NP(Det/an)(N/elephant)))(PP(P/in)(NP(Det/my)(N/pajamas)))))')

svgling.draw_tree(t1)
t2 = Tree.fromstring('(S(NP/I)(VP(V/shot)(NP(Det/an)(N/elephant)(PP(P/in)(NP(Det/my)(N/pajamas))))))')

svgling.draw_tree(t2)

import nltk
from nltk import CFG

grammar = nltk.CFG.fromstring("""
S -> S CONJ S | NP VP
NP -> Det N | NP CONJ NP
VP -> V NP
Det -> "the" | "a"
N -> "man" | "letter" | "girl" | "present" | "grandmother" | "cake" | "bread"
V -> "wrote" | "bought" | "baked"
CONJ -> "and"
""")

sr_parser = nltk.ShiftReduceParser(grammar, trace=2)

sent1 = 'the man wrote a letter and the girl bought a present'.split()

sent2 = 'the grandmother baked a cake and a bread'.split()

print('sent1:')

for tree in sr_parser.parse(sent1):
  print(tree)

print('sent2:')

for tree in sr_parser.parse(sent2):
  print(tree)


import nltk
from nltk import CFG

grammar = nltk.CFG.fromstring("""
S -> S CONJ S | NP VP
NP -> Det N | NP CONJ NP
VP -> V NP
Det -> "the" | "a"
N -> "man" | "letter" | "girl" | "present" | "grandmother" | "cake" | "bread"
V -> "wrote" | "bought" | "baked"
CONJ -> "and"
""")

chart_parser = nltk.BottomUpChartParser(grammar, trace=2)

sent1 = 'the man wrote a letter and the girl bought a present'.split()

sent2 = 'the grandmother baked a cake and a bread'.split()

print('sent1:')

for tree in chart_parser.parse(sent1):
  print(tree)

print('sent2:')

for tree in chart_parser.parse(sent2):
  print(tree)


from nltk.grammar import DependencyGrammar
from nltk.parse import NonprojectiveDependencyParser

grammar = DependencyGrammar.fromstring("""
'canceled' -> 'JetBlue' | 'flight' | 'morning'
'flight' -> 'our' | 'was'
'morning' -> 'this'
'was' -> 'which' | 'late'
'late' -> 'already'
""")

# запуск анализатора
dp = NonprojectiveDependencyParser(grammar)

# анализ последовательности слов
g, = dp.parse(['JetBlue', 'canceled', 'our', 'flight', 'this', 'morning', 'which', 'was', 'already', 'late'])

# печать корневого элемента
print('Root: ', g.root['word'], '\n')

# обход дерева и данных, зависящих от печати
for _, node in sorted(g.nodes.items()):
  if node['word'] is not None:
    print('{address} {word}: {d}'.format(d=node['deps'][''],**node))

# печать дерева
print('\n Tree: \n',g.tree())