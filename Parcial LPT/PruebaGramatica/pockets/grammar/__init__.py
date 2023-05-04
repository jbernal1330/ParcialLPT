from antlr4 import *
from pocketsLexer import pocketsLexer
from pocketsParser import pocketsParser
from pocketsListener import pocketsListener

estado = True

class grammar(pocketsListener):
    def __init__(self):
        self.mensaje = "Sin cambios realizados"
        
    def exitCreate(self, ctx: pocketsParser.CreateContext):
        self.mensaje = "Se creó un nuevo archivo con el nombre " + ctx.fileIdentifier().getText() + " columnas " + ctx.columnNames().getText()
        
    def exitInsert(self, ctx: pocketsParser.InsertContext):
        self.mensaje = "Se insertó información en el archivo " + ctx.fileIdentifier().getText()
        
    def exitDelete(self, ctx: pocketsParser.DeleteContext):
        self.mensaje = "Se eliminó el archivo " + ctx.fileIdentifier().getText()
        
    def exitSelect(self, ctx: pocketsParser.SelectContext):
        self.mensaje = "Seleccionado " + ctx.expressionList().getText() + " del archivo " + ctx.fileIdentifier().getText()

while(True):
	entrada = input()
	if(entrada=="exit" or entrada=="EXIT"):
		exit()
	else:
		# Crea un flujo de entrada desde la cadena creada con anterioridad
		stream = InputStream(entrada)
		# Crea un lexer que escanea el flujo de entrada
		lexer = pocketsLexer(stream)
		# Crea un flujo de tokens a partir del lexer
		tokens = CommonTokenStream(lexer)
		# Crea un parser que lee del flujo de tokens
		parser = pocketsParser(tokens)
		# Llama al método de inicio de regla en el parser para analizar la entrada
		tree = parser.pocket()

		grammar_listener = grammar()
		walker = ParseTreeWalker()
		walker.walk(grammar_listener, tree)

		print(grammar_listener.mensaje)
