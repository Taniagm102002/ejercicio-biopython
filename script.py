from bio.seq import seq
from bio.seqFeature import seqFeature, FeatureLocation
from Bio import seqRecord
def summarize_contens(filename):
    record = seqIO.read(filename, "getbank")
    print(record)
 summarize_contents(filename)

                                      
    def summarize_contents(filename):
       avance = SeqIO.read(filename, "genbank")
        print("Name: ", avance.name)
        import os
        print ("Path: ", os.path.dirname(filename))
       avances = list(SeqIO.parse(filename, "genbank"))
        print("num_avances = %i avances" % len(avance))

        for seq_record in SeqIO.parse(filename,"genbank"):
                print("ID:",avance.id)
                
summarize_contents(filename)

from Bio.Seq import Seq
from Bio.SeqFeature import SeqFeature, FeatureLocation
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import os
def summarize_contents(filename):
	all_records = []
	record = list(SeqIO.parse(filename,"genbank"))
	print("Path: ",os.path.dirname(filename))
	print("Num_record = %i records" %len(record))
	print("\n")
	for seq_r in SeqIO.parse(filename,"genbank"):
		all_records.append(seq_r.name)
		print("Name: ",seq_r.name)
		print("ID :",seq_r.id)
		print("Location:")
		for seq_features in seq_r.features :
			print('Star: %d, Stop: %d' %(int(seq_feature.location.start),int(seq_feature.location.end)))
		
	
sunnarize_contents(filename)
