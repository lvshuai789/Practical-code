#coding:utf-8

# 1.编写一个简单的递归下降解析器
import re
import collections

# Token specification

NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
MINUS = r'(?P<MINUS>-)'
TIMES = r'(?P<TIMES>\*)'
DIVIDE = r'(?P<DIVIDE>)'
LPAREN = r'(?P<LPAREN>\()'
RPAREN = r'(?P<RPAREN>\))'
WS = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NUM,PLUS,MINUS,TIMES,DIVIDE,LPAREN,RPAREN,WS]))

# Tokenizer
Token = collections.namedtuple('Token',['type','value'])

def generate_tokens(text):
    scanner = master_pat.scanner(text)
    for m in iter(scanner.match,None):
        tok = Token(m.lastgroup,m.group())
        if tok.type != 'WS':
            yield  tok


class ExpressionEvaluator:
    def parse(self,text):
        self.tokens = generate_tokens(text)
        self.tok = None
        self.nexttok = None
        self._advance()
        return self.expr()

    def _advance(self):
        self.tok,self.nexttok = self.nexttok,next(self.tokens,None)

    def _accept(self,toktype):
        if self.nexttok and self.nexttok.type == toktype:
            self._advance()
            return True
        else:
            return False

    def _expect(self,toktype):
        if not self._accept(toktype):
            raise SyntaxError('Expected ' + toktype)


    # Grammar rules follow
    def expr(self):
        "expression ::=teerm( ('+'|'-') term )*"
        exprval  = self.term()
        while self._accept('PLUS') or self._accept('MINUS'):
            op = self.tok.type
            right = self.term()
            if op == 'PLUS':
                exprval += right
            elif op == 'MINUS':
                exprval -= right
        return exprval

    def term(self):
        termval = self.factor()
        while self._accept('TIMES') or self._accept('DIVIDE'):
            op = self.tok.type
            right = self.factor()
            if op == 'TIMES':
                termval *= right
            elif op == 'DIVIDE':
                termval /= right
        return termval

    def factor(self):
        if self._accept('NUM'):
            return int(self.tok.type)
        elif self._accept('LPAREN'):
            exprval = self.expr()
            self._expect("RPAREN")
            return exprval

        else:
            raise SyntaxError("Expected NUMBER or LPAREN")


e = ExpressionEvaluator()
m = e.parse('2')
print(m)