import re

keyword = ['cin', 'cout', 'std', 'alignas', 'decltype', 'namespace', 'struct', 'alignof', 'default', 'new', 'switch',
           'and', 'delete',
           'noexcept', 'template', 'and_eq', 'do', 'not', 'this', 'asm', 'double', 'not_eq', 'thread_local', 'auto',
           'dynamic_cast', 'nullptr', 'throw', 'bitand', 'else', 'operator', 'true', 'bitor', 'enum', 'or', 'try',
           'bool', 'explicit', 'or_eq', 'typedef', 'break', 'export', 'private', 'typeid', 'case', 'exter', 'protected',
           'typename', 'catch', 'false', 'public', 'union', 'char', 'float', 'register', 'unsigned', 'char16_t', 'for',
           'reinterpret_cast', 'using', 'char32_t', 'friend', 'return', 'virtual', 'class', 'goto', 'short', 'void',
           'compl', 'if', 'signed', 'volatile', 'const', 'inline', 'sizeof', 'wchar_t', 'constexpr', 'int', 'static',
           'while', 'const_cast', 'long', 'static_assert', 'xor', 'continue', 'mutable', 'static_cast', 'xor_eq']

built_in_functions = ['pow()', 'sqrt()', 'min()', 'max()', 'swap()', 'gcd()', 'toupper()', 'tolower()', 'floor()',
                      'ceil()']

operators = ['+', '-', '*', '/', '%', '==', '!=', '>', '<', '>=', '<=', '&&', '||', '!', '&', '|', '^', '~', '>>', '<<',
             '=', '+=', '-=', '*=']

specialsymbol = ['@', '#', '$', '_', '!', '"']

separator = [',', ':', ';', '\n', '\t', '{', '}', '(', ')', '[', ']']

tokens = []


string = ""


def removeComments(string):
    string = re.sub(re.compile("/\*.*?\*/", re.DOTALL), "", string)
    string = re.sub(re.compile("//.*?\n"), "", string)
    return string


# Str = removeComments(string)
# print(Str)


def lexeme_token(string):
    contents = removeComments(string)
    print("|||Code without Comments||||\n")
    print(contents)
    splitCode = contents.split()  # split program in word based on space
    print("Lexeme Token Pair\n")
    length = len(splitCode)  # count the number of word in program
    for i in range(0, length):
        Str = splitCode[i]
        if Str[-1] == ";" or Str[-1] == ",":
            if Str[-1] == ";":
                # print("[End of Line :", str[-1], "]")
                tokens.append(["End of Line: " + Str[-1]])
                Str = Str[:-1]
            elif Str[-1] == ",":
                # print("[Separator :", str[-1], "]")
                tokens.append(["Separator: " + Str[-1]])
                Str = Str[:-1]
        if Str in keyword:
            # print("[Keyword :", str, "]")
            tokens.append(["Keyword: " + Str])
            continue
        if Str in operators:
            # print("[Operators :", str, "]")
            tokens.append(["Operators: " + Str])
            continue
        if Str in specialsymbol:
            # print("[Special Symbol :", str, "]")
            tokens.append(["Special Symbol: " + Str])
            continue
        if Str in built_in_functions:
            # print("[Built_in Function :", str, "]")
            tokens.append(["Built_in Function: " + Str])
            continue
        if Str in separator:
            # print("[Separator :", str, "]")
            tokens.append(["Separator: " + Str])
            continue
        if re.match(r'(#include*).*', Str):
            # print("[Header File :", str, "]")
            tokens.append(["Header File: " + Str])
            continue
        if re.match(r'^[-+]?[0-9]+$', Str):
            # print("[Numerals ", str, "]")
            tokens.append(["Numerals: " + Str])
            continue
        if re.match(r"^[^\d\W]\w*\Z", Str):
            # print("[Identifier :", str, "]")
            tokens.append(["Identifier: " + Str])


lexeme_token(string)
print(tokens)
