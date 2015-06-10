# (brain OR neuroimaging OR MRI OR (PET scan)) AND Weschler OR (intellectual function*) OR psychomotor OR attention OR memory OR abstraction OR "wisconsin card sort" OR (object alternation) OR (language fluency) OR phonemic OR semantic OR (semantic retrieval) OR (working memory) OR "Iowa Gambling" OR (decision making) OR go-no-go OR impulsivity OR attachment OR Depression OR aggression OR hostility OR (social adjustment) OR childhood OR SCID OR suicidal OR ideation OR intent OR lethality OR ("global functioning") OR (neuropsychological test) OR (psychological test) AND (hasabstract[text] AND "last 10 years"[PDat] AND Humans[Mesh])

# http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id=11850928,11482001&version=2.0

term="http://eutils.ncbi.nlm.nih.gov/entrez/eutils/pubmed/?term=(brain+OR+neuroimaging+OR+MRI+OR+(PET+scan))+AND+Weschler+OR+(intellectual+function*)+OR+psychomotor+OR+attention+OR+memory+OR+abstraction+OR+%22wisconsin+card+sort%22+OR+(object+alternation)+OR+(language+fluency)+OR+phonemic+OR+semantic+OR+(semantic+retrieval)+OR+(working+memory)+OR+%22Iowa+Gambling%22+OR+(decision+making)+OR+go-no-go+OR+impulsivity+OR+attachment+OR+Depression+OR+aggression+OR+hostility+OR+(social+adjustment)+OR+childhood+OR+SCID+OR+suicidal+OR+ideation+OR+intent+OR+lethality+OR+(%22global+functioning%22)+OR+(neuropsychological+test)+OR+(psychological+test)+AND+(hasabstract%5Btext%5D+AND+%22last+10+years%22%5BPDat%5D+AND+Humans%5BMesh%5D)"

# http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=21614549&strand=1&seq_start=1&seq_stop=100&rettype=fasta&retmode=text


from Bio import Entrez

# Entrez.email = "nickHere@example.org"

Entrez.email = "A.N.Other@example.com"     # Always tell NCBI who you are
handle = Entrez.esearch(db="nucleotide", term="Cypripedioideae[Orgn] AND matK[Gene]")
result = Entrez.read(handle)
handle.close()
print result["Count"]
