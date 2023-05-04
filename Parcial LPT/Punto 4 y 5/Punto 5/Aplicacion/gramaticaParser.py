# Generated from Punto 4/gramatica.g4 by ANTLR 4.12.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,33,167,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,1,0,1,0,4,0,35,8,0,11,0,12,0,36,1,0,1,0,1,1,
        1,1,1,1,1,1,3,1,45,8,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,5,3,63,8,3,10,3,12,3,66,9,3,3,3,68,8,3,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,5,4,79,8,4,10,4,12,4,82,9,4,1,5,
        1,5,1,5,1,5,1,6,1,6,1,6,1,6,5,6,92,8,6,10,6,12,6,95,9,6,1,6,1,6,
        1,7,1,7,1,7,1,7,1,8,1,8,1,8,5,8,106,8,8,10,8,12,8,109,9,8,1,9,1,
        9,1,9,5,9,114,8,9,10,9,12,9,117,9,9,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,5,10,130,8,10,10,10,12,10,133,9,10,1,11,
        1,11,1,12,1,12,1,12,3,12,140,8,12,1,13,1,13,1,13,1,13,3,13,146,8,
        13,1,14,1,14,1,14,3,14,151,8,14,1,14,1,14,3,14,155,8,14,1,14,1,14,
        4,14,159,8,14,11,14,12,14,160,3,14,163,8,14,1,15,1,15,1,15,0,1,20,
        16,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,0,2,2,0,18,18,22,26,
        1,0,20,21,173,0,34,1,0,0,0,2,44,1,0,0,0,4,46,1,0,0,0,6,67,1,0,0,
        0,8,69,1,0,0,0,10,83,1,0,0,0,12,87,1,0,0,0,14,98,1,0,0,0,16,102,
        1,0,0,0,18,110,1,0,0,0,20,118,1,0,0,0,22,134,1,0,0,0,24,139,1,0,
        0,0,26,145,1,0,0,0,28,162,1,0,0,0,30,164,1,0,0,0,32,35,3,2,1,0,33,
        35,5,1,0,0,34,32,1,0,0,0,34,33,1,0,0,0,35,36,1,0,0,0,36,34,1,0,0,
        0,36,37,1,0,0,0,37,38,1,0,0,0,38,39,5,0,0,1,39,1,1,0,0,0,40,45,3,
        4,2,0,41,45,3,6,3,0,42,45,3,8,4,0,43,45,3,10,5,0,44,40,1,0,0,0,44,
        41,1,0,0,0,44,42,1,0,0,0,44,43,1,0,0,0,45,3,1,0,0,0,46,47,5,2,0,
        0,47,48,5,3,0,0,48,49,3,30,15,0,49,50,3,12,6,0,50,5,1,0,0,0,51,52,
        5,5,0,0,52,53,5,3,0,0,53,68,3,30,15,0,54,55,5,5,0,0,55,56,5,3,0,
        0,56,57,3,30,15,0,57,58,3,12,6,0,58,59,5,7,0,0,59,64,3,14,7,0,60,
        61,5,14,0,0,61,63,3,14,7,0,62,60,1,0,0,0,63,66,1,0,0,0,64,62,1,0,
        0,0,64,65,1,0,0,0,65,68,1,0,0,0,66,64,1,0,0,0,67,51,1,0,0,0,67,54,
        1,0,0,0,68,7,1,0,0,0,69,70,5,8,0,0,70,71,5,6,0,0,71,72,5,3,0,0,72,
        73,3,30,15,0,73,74,3,12,6,0,74,75,5,7,0,0,75,80,3,14,7,0,76,77,5,
        14,0,0,77,79,3,14,7,0,78,76,1,0,0,0,79,82,1,0,0,0,80,78,1,0,0,0,
        80,81,1,0,0,0,81,9,1,0,0,0,82,80,1,0,0,0,83,84,5,11,0,0,84,85,5,
        3,0,0,85,86,3,30,15,0,86,11,1,0,0,0,87,88,5,16,0,0,88,93,3,26,13,
        0,89,90,5,14,0,0,90,92,3,26,13,0,91,89,1,0,0,0,92,95,1,0,0,0,93,
        91,1,0,0,0,93,94,1,0,0,0,94,96,1,0,0,0,95,93,1,0,0,0,96,97,5,17,
        0,0,97,13,1,0,0,0,98,99,5,16,0,0,99,100,3,16,8,0,100,101,5,17,0,
        0,101,15,1,0,0,0,102,107,3,28,14,0,103,104,5,14,0,0,104,106,3,28,
        14,0,105,103,1,0,0,0,106,109,1,0,0,0,107,105,1,0,0,0,107,108,1,0,
        0,0,108,17,1,0,0,0,109,107,1,0,0,0,110,115,3,24,12,0,111,112,5,14,
        0,0,112,114,3,24,12,0,113,111,1,0,0,0,114,117,1,0,0,0,115,113,1,
        0,0,0,115,116,1,0,0,0,116,19,1,0,0,0,117,115,1,0,0,0,118,119,6,10,
        -1,0,119,120,3,26,13,0,120,121,3,22,11,0,121,122,3,24,12,0,122,131,
        1,0,0,0,123,124,10,2,0,0,124,125,5,27,0,0,125,130,3,20,10,3,126,
        127,10,1,0,0,127,128,5,28,0,0,128,130,3,20,10,2,129,123,1,0,0,0,
        129,126,1,0,0,0,130,133,1,0,0,0,131,129,1,0,0,0,131,132,1,0,0,0,
        132,21,1,0,0,0,133,131,1,0,0,0,134,135,7,0,0,0,135,23,1,0,0,0,136,
        140,5,15,0,0,137,140,3,26,13,0,138,140,3,28,14,0,139,136,1,0,0,0,
        139,137,1,0,0,0,139,138,1,0,0,0,140,25,1,0,0,0,141,142,5,32,0,0,
        142,143,5,13,0,0,143,146,5,32,0,0,144,146,5,32,0,0,145,141,1,0,0,
        0,145,144,1,0,0,0,146,27,1,0,0,0,147,163,5,12,0,0,148,163,3,26,13,
        0,149,151,7,1,0,0,150,149,1,0,0,0,150,151,1,0,0,0,151,152,1,0,0,
        0,152,163,5,30,0,0,153,155,7,1,0,0,154,153,1,0,0,0,154,155,1,0,0,
        0,155,156,1,0,0,0,156,163,5,31,0,0,157,159,5,29,0,0,158,157,1,0,
        0,0,159,160,1,0,0,0,160,158,1,0,0,0,160,161,1,0,0,0,161,163,1,0,
        0,0,162,147,1,0,0,0,162,148,1,0,0,0,162,150,1,0,0,0,162,154,1,0,
        0,0,162,158,1,0,0,0,163,29,1,0,0,0,164,165,3,26,13,0,165,31,1,0,
        0,0,17,34,36,44,64,67,80,93,107,115,129,131,139,145,150,154,160,
        162
    ]

class gramaticaParser ( Parser ):

    grammarFileName = "gramatica.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'.'", "','", "'*'", "'('", "')'", "'='", "'!'", "'-'", 
                     "'+'", "'>'", "'>='", "'<'", "'<='", "'!='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "CREATE", "TABLE", "FROM", 
                      "READ", "INTO", "ROWS", "UPDATE", "SET", "WHERE", 
                      "DELETE", "NULL", "DOT", "COMMA", "ASTERISK", "LEFT_PARENTHESIS", 
                      "RIGHT_PARENTHESIS", "EQUALS", "NOT", "MINUS", "PLUS", 
                      "GT", "GE", "LT", "LE", "NE", "AND", "OR", "QUOTED_STRING", 
                      "INTEGER_VALUE", "DECIMAL_VALUE", "IDENTIFIER", "WS" ]

    RULE_entry = 0
    RULE_statement = 1
    RULE_create = 2
    RULE_read = 3
    RULE_update = 4
    RULE_delete = 5
    RULE_columnNames = 6
    RULE_values = 7
    RULE_constants = 8
    RULE_expressionList = 9
    RULE_booleanExpression = 10
    RULE_compare = 11
    RULE_expression = 12
    RULE_identifier = 13
    RULE_constant = 14
    RULE_tableIdentifier = 15

    ruleNames =  [ "entry", "statement", "create", "read", "update", "delete", 
                   "columnNames", "values", "constants", "expressionList", 
                   "booleanExpression", "compare", "expression", "identifier", 
                   "constant", "tableIdentifier" ]

    EOF = Token.EOF
    T__0=1
    CREATE=2
    TABLE=3
    FROM=4
    READ=5
    INTO=6
    ROWS=7
    UPDATE=8
    SET=9
    WHERE=10
    DELETE=11
    NULL=12
    DOT=13
    COMMA=14
    ASTERISK=15
    LEFT_PARENTHESIS=16
    RIGHT_PARENTHESIS=17
    EQUALS=18
    NOT=19
    MINUS=20
    PLUS=21
    GT=22
    GE=23
    LT=24
    LE=25
    NE=26
    AND=27
    OR=28
    QUOTED_STRING=29
    INTEGER_VALUE=30
    DECIMAL_VALUE=31
    IDENTIFIER=32
    WS=33

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class EntryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(gramaticaParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.StatementContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.StatementContext,i)


        def getRuleIndex(self):
            return gramaticaParser.RULE_entry

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntry" ):
                listener.enterEntry(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntry" ):
                listener.exitEntry(self)




    def entry(self):

        localctx = gramaticaParser.EntryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_entry)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 34
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [2, 5, 8, 11]:
                    self.state = 32
                    self.statement()
                    pass
                elif token in [1]:
                    self.state = 33
                    self.match(gramaticaParser.T__0)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 36 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2342) != 0)):
                    break

            self.state = 38
            self.match(gramaticaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def create(self):
            return self.getTypedRuleContext(gramaticaParser.CreateContext,0)


        def read(self):
            return self.getTypedRuleContext(gramaticaParser.ReadContext,0)


        def update(self):
            return self.getTypedRuleContext(gramaticaParser.UpdateContext,0)


        def delete(self):
            return self.getTypedRuleContext(gramaticaParser.DeleteContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = gramaticaParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 44
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 40
                self.create()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 41
                self.read()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 42
                self.update()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 4)
                self.state = 43
                self.delete()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CreateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CREATE(self):
            return self.getToken(gramaticaParser.CREATE, 0)

        def TABLE(self):
            return self.getToken(gramaticaParser.TABLE, 0)

        def tableIdentifier(self):
            return self.getTypedRuleContext(gramaticaParser.TableIdentifierContext,0)


        def columnNames(self):
            return self.getTypedRuleContext(gramaticaParser.ColumnNamesContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_create

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCreate" ):
                listener.enterCreate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCreate" ):
                listener.exitCreate(self)




    def create(self):

        localctx = gramaticaParser.CreateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_create)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(gramaticaParser.CREATE)
            self.state = 47
            self.match(gramaticaParser.TABLE)
            self.state = 48
            self.tableIdentifier()
            self.state = 49
            self.columnNames()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReadContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def READ(self):
            return self.getToken(gramaticaParser.READ, 0)

        def TABLE(self):
            return self.getToken(gramaticaParser.TABLE, 0)

        def tableIdentifier(self):
            return self.getTypedRuleContext(gramaticaParser.TableIdentifierContext,0)


        def columnNames(self):
            return self.getTypedRuleContext(gramaticaParser.ColumnNamesContext,0)


        def ROWS(self):
            return self.getToken(gramaticaParser.ROWS, 0)

        def values(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.ValuesContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.ValuesContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.COMMA)
            else:
                return self.getToken(gramaticaParser.COMMA, i)

        def getRuleIndex(self):
            return gramaticaParser.RULE_read

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRead" ):
                listener.enterRead(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRead" ):
                listener.exitRead(self)




    def read(self):

        localctx = gramaticaParser.ReadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_read)
        self._la = 0 # Token type
        try:
            self.state = 67
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                self.match(gramaticaParser.READ)
                self.state = 52
                self.match(gramaticaParser.TABLE)
                self.state = 53
                self.tableIdentifier()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 54
                self.match(gramaticaParser.READ)
                self.state = 55
                self.match(gramaticaParser.TABLE)
                self.state = 56
                self.tableIdentifier()
                self.state = 57
                self.columnNames()
                self.state = 58
                self.match(gramaticaParser.ROWS)
                self.state = 59
                self.values()
                self.state = 64
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==14:
                    self.state = 60
                    self.match(gramaticaParser.COMMA)
                    self.state = 61
                    self.values()
                    self.state = 66
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UpdateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UPDATE(self):
            return self.getToken(gramaticaParser.UPDATE, 0)

        def INTO(self):
            return self.getToken(gramaticaParser.INTO, 0)

        def TABLE(self):
            return self.getToken(gramaticaParser.TABLE, 0)

        def tableIdentifier(self):
            return self.getTypedRuleContext(gramaticaParser.TableIdentifierContext,0)


        def columnNames(self):
            return self.getTypedRuleContext(gramaticaParser.ColumnNamesContext,0)


        def ROWS(self):
            return self.getToken(gramaticaParser.ROWS, 0)

        def values(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.ValuesContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.ValuesContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.COMMA)
            else:
                return self.getToken(gramaticaParser.COMMA, i)

        def getRuleIndex(self):
            return gramaticaParser.RULE_update

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUpdate" ):
                listener.enterUpdate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUpdate" ):
                listener.exitUpdate(self)




    def update(self):

        localctx = gramaticaParser.UpdateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_update)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(gramaticaParser.UPDATE)
            self.state = 70
            self.match(gramaticaParser.INTO)
            self.state = 71
            self.match(gramaticaParser.TABLE)
            self.state = 72
            self.tableIdentifier()
            self.state = 73
            self.columnNames()
            self.state = 74
            self.match(gramaticaParser.ROWS)
            self.state = 75
            self.values()
            self.state = 80
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14:
                self.state = 76
                self.match(gramaticaParser.COMMA)
                self.state = 77
                self.values()
                self.state = 82
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeleteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DELETE(self):
            return self.getToken(gramaticaParser.DELETE, 0)

        def TABLE(self):
            return self.getToken(gramaticaParser.TABLE, 0)

        def tableIdentifier(self):
            return self.getTypedRuleContext(gramaticaParser.TableIdentifierContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_delete

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDelete" ):
                listener.enterDelete(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDelete" ):
                listener.exitDelete(self)




    def delete(self):

        localctx = gramaticaParser.DeleteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_delete)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(gramaticaParser.DELETE)
            self.state = 84
            self.match(gramaticaParser.TABLE)
            self.state = 85
            self.tableIdentifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ColumnNamesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_PARENTHESIS(self):
            return self.getToken(gramaticaParser.LEFT_PARENTHESIS, 0)

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.IdentifierContext,i)


        def RIGHT_PARENTHESIS(self):
            return self.getToken(gramaticaParser.RIGHT_PARENTHESIS, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.COMMA)
            else:
                return self.getToken(gramaticaParser.COMMA, i)

        def getRuleIndex(self):
            return gramaticaParser.RULE_columnNames

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumnNames" ):
                listener.enterColumnNames(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumnNames" ):
                listener.exitColumnNames(self)




    def columnNames(self):

        localctx = gramaticaParser.ColumnNamesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_columnNames)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(gramaticaParser.LEFT_PARENTHESIS)
            self.state = 88
            self.identifier()
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14:
                self.state = 89
                self.match(gramaticaParser.COMMA)
                self.state = 90
                self.identifier()
                self.state = 95
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 96
            self.match(gramaticaParser.RIGHT_PARENTHESIS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValuesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_PARENTHESIS(self):
            return self.getToken(gramaticaParser.LEFT_PARENTHESIS, 0)

        def constants(self):
            return self.getTypedRuleContext(gramaticaParser.ConstantsContext,0)


        def RIGHT_PARENTHESIS(self):
            return self.getToken(gramaticaParser.RIGHT_PARENTHESIS, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_values

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValues" ):
                listener.enterValues(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValues" ):
                listener.exitValues(self)




    def values(self):

        localctx = gramaticaParser.ValuesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_values)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(gramaticaParser.LEFT_PARENTHESIS)
            self.state = 99
            self.constants()
            self.state = 100
            self.match(gramaticaParser.RIGHT_PARENTHESIS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstantsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constant(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.ConstantContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.ConstantContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.COMMA)
            else:
                return self.getToken(gramaticaParser.COMMA, i)

        def getRuleIndex(self):
            return gramaticaParser.RULE_constants

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstants" ):
                listener.enterConstants(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstants" ):
                listener.exitConstants(self)




    def constants(self):

        localctx = gramaticaParser.ConstantsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_constants)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.constant()
            self.state = 107
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14:
                self.state = 103
                self.match(gramaticaParser.COMMA)
                self.state = 104
                self.constant()
                self.state = 109
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.COMMA)
            else:
                return self.getToken(gramaticaParser.COMMA, i)

        def getRuleIndex(self):
            return gramaticaParser.RULE_expressionList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionList" ):
                listener.enterExpressionList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionList" ):
                listener.exitExpressionList(self)




    def expressionList(self):

        localctx = gramaticaParser.ExpressionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_expressionList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.expression()
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14:
                self.state = 111
                self.match(gramaticaParser.COMMA)
                self.state = 112
                self.expression()
                self.state = 117
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BooleanExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # BooleanExpressionContext
            self.operator = None # Token
            self.right = None # BooleanExpressionContext

        def identifier(self):
            return self.getTypedRuleContext(gramaticaParser.IdentifierContext,0)


        def compare(self):
            return self.getTypedRuleContext(gramaticaParser.CompareContext,0)


        def expression(self):
            return self.getTypedRuleContext(gramaticaParser.ExpressionContext,0)


        def booleanExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.BooleanExpressionContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.BooleanExpressionContext,i)


        def AND(self):
            return self.getToken(gramaticaParser.AND, 0)

        def OR(self):
            return self.getToken(gramaticaParser.OR, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_booleanExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBooleanExpression" ):
                listener.enterBooleanExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBooleanExpression" ):
                listener.exitBooleanExpression(self)



    def booleanExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = gramaticaParser.BooleanExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_booleanExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.identifier()
            self.state = 120
            self.compare()
            self.state = 121
            self.expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 131
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 129
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                    if la_ == 1:
                        localctx = gramaticaParser.BooleanExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_booleanExpression)
                        self.state = 123
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 124
                        localctx.operator = self.match(gramaticaParser.AND)
                        self.state = 125
                        localctx.right = self.booleanExpression(3)
                        pass

                    elif la_ == 2:
                        localctx = gramaticaParser.BooleanExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_booleanExpression)
                        self.state = 126
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 127
                        localctx.operator = self.match(gramaticaParser.OR)
                        self.state = 128
                        localctx.right = self.booleanExpression(2)
                        pass

             
                self.state = 133
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class CompareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUALS(self):
            return self.getToken(gramaticaParser.EQUALS, 0)

        def GT(self):
            return self.getToken(gramaticaParser.GT, 0)

        def GE(self):
            return self.getToken(gramaticaParser.GE, 0)

        def LT(self):
            return self.getToken(gramaticaParser.LT, 0)

        def LE(self):
            return self.getToken(gramaticaParser.LE, 0)

        def NE(self):
            return self.getToken(gramaticaParser.NE, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_compare

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompare" ):
                listener.enterCompare(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompare" ):
                listener.exitCompare(self)




    def compare(self):

        localctx = gramaticaParser.CompareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_compare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 130285568) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASTERISK(self):
            return self.getToken(gramaticaParser.ASTERISK, 0)

        def identifier(self):
            return self.getTypedRuleContext(gramaticaParser.IdentifierContext,0)


        def constant(self):
            return self.getTypedRuleContext(gramaticaParser.ConstantContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = gramaticaParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_expression)
        try:
            self.state = 139
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 136
                self.match(gramaticaParser.ASTERISK)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 137
                self.identifier()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 138
                self.constant()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.IDENTIFIER)
            else:
                return self.getToken(gramaticaParser.IDENTIFIER, i)

        def DOT(self):
            return self.getToken(gramaticaParser.DOT, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier" ):
                listener.enterIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier" ):
                listener.exitIdentifier(self)




    def identifier(self):

        localctx = gramaticaParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_identifier)
        try:
            self.state = 145
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 141
                self.match(gramaticaParser.IDENTIFIER)
                self.state = 142
                self.match(gramaticaParser.DOT)
                self.state = 143
                self.match(gramaticaParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 144
                self.match(gramaticaParser.IDENTIFIER)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstantContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NULL(self):
            return self.getToken(gramaticaParser.NULL, 0)

        def identifier(self):
            return self.getTypedRuleContext(gramaticaParser.IdentifierContext,0)


        def INTEGER_VALUE(self):
            return self.getToken(gramaticaParser.INTEGER_VALUE, 0)

        def MINUS(self):
            return self.getToken(gramaticaParser.MINUS, 0)

        def PLUS(self):
            return self.getToken(gramaticaParser.PLUS, 0)

        def DECIMAL_VALUE(self):
            return self.getToken(gramaticaParser.DECIMAL_VALUE, 0)

        def QUOTED_STRING(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.QUOTED_STRING)
            else:
                return self.getToken(gramaticaParser.QUOTED_STRING, i)

        def getRuleIndex(self):
            return gramaticaParser.RULE_constant

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstant" ):
                listener.enterConstant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstant" ):
                listener.exitConstant(self)




    def constant(self):

        localctx = gramaticaParser.ConstantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_constant)
        self._la = 0 # Token type
        try:
            self.state = 162
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 147
                self.match(gramaticaParser.NULL)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 148
                self.identifier()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 150
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==20 or _la==21:
                    self.state = 149
                    _la = self._input.LA(1)
                    if not(_la==20 or _la==21):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 152
                self.match(gramaticaParser.INTEGER_VALUE)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 154
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==20 or _la==21:
                    self.state = 153
                    _la = self._input.LA(1)
                    if not(_la==20 or _la==21):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 156
                self.match(gramaticaParser.DECIMAL_VALUE)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 158 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 157
                        self.match(gramaticaParser.QUOTED_STRING)

                    else:
                        raise NoViableAltException(self)
                    self.state = 160 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TableIdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # IdentifierContext

        def identifier(self):
            return self.getTypedRuleContext(gramaticaParser.IdentifierContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_tableIdentifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTableIdentifier" ):
                listener.enterTableIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTableIdentifier" ):
                listener.exitTableIdentifier(self)




    def tableIdentifier(self):

        localctx = gramaticaParser.TableIdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_tableIdentifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            localctx.name = self.identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[10] = self.booleanExpression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def booleanExpression_sempred(self, localctx:BooleanExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         




