def summarize_contents(filename):
	filaOs = os.path.split(filename)
	filaExt = os.path.splitext(filename)
	if (filaExt[1] == ".gbk"):
		type_file= "genbank"
	else: 
		type_file= "fasta"
	record = list(SeqIO.parse(filename, type_file))
	#Creacion de diccionario
	d = {}
	d['File:'] = filaOs[1]
	d['Path:'] = filaOs[0]
	d['Num_musics:'] = len(music)
	#Diccionario con listas
	d['Names:'] = []
	d['IDs:'] = []
	d['Descriptions'] = []
	#Registro de musics
	for seq_rcd in SeqIO.parse(filename,type_file):
		d['Names:'].append(seq_rcd.name)
		d['IDs:'].append(seq_rcd.id)
		d['Descriptions'].append(seq_rcd.description)
	return d
#Imprimir la funcion
if _name_ == "_main_":
	resultados = summarize_contents(filename)
	print(resultados)
