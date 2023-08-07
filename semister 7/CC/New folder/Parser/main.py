import pandas as pd
import nltk

# making coloums of Dataframe

data = {'(': ['s3', '', 's3', 'r5', '', 'r1', '', 'r4', 'r2', 'r6', 's3', 'r3'],
        ')': ['', '', '', 'r5', 'g6', 'r1', '', 'r4', 'r2', 'r6', '', 'r3'],
        ';': ['', '', '', 'r5', '', 'r1', 's11', 'r4', 'r2', 'r6', '', 's3'],
        'x': ['', '', 's4', 'r5', '', 'r1', '', 'r4', 'r2', 'r6', 's4', 'r3'],
        '$': ['', 'a', '', 'r5', '', 'r1', '', 'r4', 'r2', 'r6', '', 'r3'],
        'S': ['g2', '', 'g10', '', '', '', '', '', '', '', 'g10', ''],
        'A': ['', '', 'g5', '', '', '', '', '', '', '', 'g12', ''],
        'B': ['', '', '', '', '', '', 'g9', '', '', '', '', ''],
        'C': ['', '', 'g7', '', '', '', '', '', '', '', 'g7', ''],
        'states': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]}

# CFG
grammar = nltk.CFG.fromstring("""
So -> S'$'
S -> '(' A ')'
A -> C B
B -> ';' A
B -> ε
C -> 'x'
C -> S
""")
non_term = ['S', 'A', 'B', 'C']
print("\n")
print(grammar)
print("\n")

pp = grammar.productions()[3]

states = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
columns = ['(', ')', ';', 'x', '$', 'S', 'A', 'B', 'C']

istr = "(x;((x;x)))$"

istr1 = list(istr)

stack = []

df = pd.DataFrame(data)
df = df.set_index('states')
print("!!!!!!!!!Parsing Table!!!!!!!!!!\n")
print(df)

print("\nGiven String is " + istr)
val = False
stack.append(states[0])

for x in istr1:
    if stack[-1] in states:
        # print(stack[-1])
        if 's' in df[x][int(stack[-1])]:
            action = df[x][int(stack[-1])]
            stack.append(x)
            stack.append(action[1])
        elif 'r' in df[x][int(stack[-1])]:
            action = df[x][int(stack[-1])]
            action = list(action)
            pp = grammar.productions()[int(action[-1])]
            l = [pp.rhs()]
            for i in range(len(l) * 2):
                stack.pop()
            a = [pp.lhs]
            stack.append(a)
        continue

    if stack[-1] in non_term:
        action = df[stack[-1]][int(stack[-2])]
        stack.append(action[1])
        continue

    if x == '$':
        action = df[x][int(stack[-1])]
        if action == 'a':
            val = True
        else:
            val = False

if (val):
    print("Given String " + istr + " is Valid")
else:
    print("Given String " + istr + " is InValid")
