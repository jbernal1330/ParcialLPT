# Generated from Punto 4/gramatica.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .gramaticaParser import gramaticaParser
else:
    from gramaticaParser import gramaticaParser

# This class defines a complete listener for a parse tree produced by gramaticaParser.
class gramaticaListener(ParseTreeListener):

    # Enter a parse tree produced by gramaticaParser#entry.
    def enterEntry(self, ctx:gramaticaParser.EntryContext):
        pass

    # Exit a parse tree produced by gramaticaParser#entry.
    def exitEntry(self, ctx:gramaticaParser.EntryContext):
        pass


    # Enter a parse tree produced by gramaticaParser#statement.
    def enterStatement(self, ctx:gramaticaParser.StatementContext):
        pass

    # Exit a parse tree produced by gramaticaParser#statement.
    def exitStatement(self, ctx:gramaticaParser.StatementContext):
        pass


    # Enter a parse tree produced by gramaticaParser#create.
    def enterCreate(self, ctx:gramaticaParser.CreateContext):
        pass

    # Exit a parse tree produced by gramaticaParser#create.
    def exitCreate(self, ctx:gramaticaParser.CreateContext):
        pass


    # Enter a parse tree produced by gramaticaParser#read.
    def enterRead(self, ctx:gramaticaParser.ReadContext):
        pass

    # Exit a parse tree produced by gramaticaParser#read.
    def exitRead(self, ctx:gramaticaParser.ReadContext):
        pass


    # Enter a parse tree produced by gramaticaParser#update.
    def enterUpdate(self, ctx:gramaticaParser.UpdateContext):
        pass

    # Exit a parse tree produced by gramaticaParser#update.
    def exitUpdate(self, ctx:gramaticaParser.UpdateContext):
        pass


    # Enter a parse tree produced by gramaticaParser#delete.
    def enterDelete(self, ctx:gramaticaParser.DeleteContext):
        pass

    # Exit a parse tree produced by gramaticaParser#delete.
    def exitDelete(self, ctx:gramaticaParser.DeleteContext):
        pass


    # Enter a parse tree produced by gramaticaParser#columnNames.
    def enterColumnNames(self, ctx:gramaticaParser.ColumnNamesContext):
        pass

    # Exit a parse tree produced by gramaticaParser#columnNames.
    def exitColumnNames(self, ctx:gramaticaParser.ColumnNamesContext):
        pass


    # Enter a parse tree produced by gramaticaParser#values.
    def enterValues(self, ctx:gramaticaParser.ValuesContext):
        pass

    # Exit a parse tree produced by gramaticaParser#values.
    def exitValues(self, ctx:gramaticaParser.ValuesContext):
        pass


    # Enter a parse tree produced by gramaticaParser#constants.
    def enterConstants(self, ctx:gramaticaParser.ConstantsContext):
        pass

    # Exit a parse tree produced by gramaticaParser#constants.
    def exitConstants(self, ctx:gramaticaParser.ConstantsContext):
        pass


    # Enter a parse tree produced by gramaticaParser#expressionList.
    def enterExpressionList(self, ctx:gramaticaParser.ExpressionListContext):
        pass

    # Exit a parse tree produced by gramaticaParser#expressionList.
    def exitExpressionList(self, ctx:gramaticaParser.ExpressionListContext):
        pass


    # Enter a parse tree produced by gramaticaParser#booleanExpression.
    def enterBooleanExpression(self, ctx:gramaticaParser.BooleanExpressionContext):
        pass

    # Exit a parse tree produced by gramaticaParser#booleanExpression.
    def exitBooleanExpression(self, ctx:gramaticaParser.BooleanExpressionContext):
        pass


    # Enter a parse tree produced by gramaticaParser#compare.
    def enterCompare(self, ctx:gramaticaParser.CompareContext):
        pass

    # Exit a parse tree produced by gramaticaParser#compare.
    def exitCompare(self, ctx:gramaticaParser.CompareContext):
        pass


    # Enter a parse tree produced by gramaticaParser#expression.
    def enterExpression(self, ctx:gramaticaParser.ExpressionContext):
        pass

    # Exit a parse tree produced by gramaticaParser#expression.
    def exitExpression(self, ctx:gramaticaParser.ExpressionContext):
        pass


    # Enter a parse tree produced by gramaticaParser#identifier.
    def enterIdentifier(self, ctx:gramaticaParser.IdentifierContext):
        pass

    # Exit a parse tree produced by gramaticaParser#identifier.
    def exitIdentifier(self, ctx:gramaticaParser.IdentifierContext):
        pass


    # Enter a parse tree produced by gramaticaParser#constant.
    def enterConstant(self, ctx:gramaticaParser.ConstantContext):
        pass

    # Exit a parse tree produced by gramaticaParser#constant.
    def exitConstant(self, ctx:gramaticaParser.ConstantContext):
        pass


    # Enter a parse tree produced by gramaticaParser#tableIdentifier.
    def enterTableIdentifier(self, ctx:gramaticaParser.TableIdentifierContext):
        pass

    # Exit a parse tree produced by gramaticaParser#tableIdentifier.
    def exitTableIdentifier(self, ctx:gramaticaParser.TableIdentifierContext):
        pass



del gramaticaParser