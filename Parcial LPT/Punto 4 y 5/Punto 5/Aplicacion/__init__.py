# Archivo main - Parcial LPT - Punto 5
# Miguel Thomas, Ivan Rodriguez, Miguel Gonzalez y Juan Bernal
from antlr4 import *
from gramaticaLexer import gramaticaLexer
from gramaticaParser import gramaticaParser
from gramaticaListener import gramaticaListener
import sqlite3

estado = True
conn = sqlite3.connect('tablas.db')
c = conn.cursor()

class grammar(gramaticaListener):

	#Operaciones realizadas en la base de datos SQL
	"""def enterCreate(self, ctx: gramaticaParser.CreateContext):
		# Crear tabla
		nombre_tabla = ctx.tableIdentifier().getText()
		campos = []
		campos.append(ctx.tableIdentifier().getText() + " " + ctx.columnNames().getText())
		campos_str = ",".join(campos)
		c.execute(f"CREATE TABLE {nombre_tabla} ({campos_str})")
        
	def enterRead(self, ctx: gramaticaParser.ReadContext):
		# Leer registros de tabla
		nombre_tabla = ctx.tableIdentifier().getText()
		c.execute(f"SELECT * FROM {nombre_tabla}")
		registros = c.fetchall()
		print(registros)
		
	def enterUpdate(self, ctx: gramaticaParser.UpdateContext):
		# Actualizar registros de tabla
		nombre_tabla = ctx.tableIdentifier().getText()
		campo = ctx.columnNames().identifier().getText()
		valor = ctx.values().constants().getText()
		c.execute(f"UPDATE {nombre_tabla} SET {campo}='{valor}'")
		
	def enterDelete(self, ctx: gramaticaParser.DeleteContext):
		# Borrar registros de tabla
		nombre_tabla = ctx.tableIdentifier().getText()
		c.execute(f"DELETE FROM {nombre_tabla}")"""
	
	def __init__(self):
		self.mensaje = "Sin cambios realizados"
        
	def exitCreate(self, ctx: gramaticaParser.CreateContext):
		self.mensaje = "Se creó una nueva tabla con el nombre " + ctx.tableIdentifier().getText() + " columnas " + ctx.columnNames().getText()
        
	def exitRead(self, ctx: gramaticaParser.ReadContext):
		self.mensaje = "Resultado de lectura: leyendo tabla " + ctx.tableIdentifier().getText()
        
	def exitUpdate(self, ctx: gramaticaParser.UpdateContext):
		self.mensaje = "Datos de la tabla " + ctx.tableIdentifier().getText() + " actualizados en la columna " + ctx.columnNames().getText() + " con los valores " + ctx.values().getText()
        
	def exitDelete(self, ctx: gramaticaParser.DeleteContext):
        	self.mensaje = "Se eliminó la tabla " + ctx.tableIdentifier().getText()

while(estado):
	# entrada = "CREATE TABLE tablaUno (Nombre,Edad)" --> Prueba sin petición al usuario
	entrada = input()
	if(entrada=="exit" or entrada=="EXIT"):
		estado = False
	else:
		# Crea un flujo de entrada desde la cadena creada con anterioridad
		stream = InputStream(entrada)
		# Crea un lexer que escanea el flujo de entrada
		lexer = gramaticaLexer(stream)
		# Crea un flujo de tokens a partir del lexer
		tokens = CommonTokenStream(lexer)
		# Crea un parser que lee del flujo de tokens
		parser = gramaticaParser(tokens)
		# Llama al método de inicio de regla en el parser para analizar la entrada
		tree = parser.entry()

		grammar_listener = grammar()
		walker = ParseTreeWalker()
		walker.walk(grammar_listener, tree)
		print(grammar_listener.mensaje)

# Guardar los cambios en la base de datos y cerrar la conexión
conn.commit()
conn.close()
