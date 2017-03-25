import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    doc_id = record[0]
    text = record[1]
    words = text.split()
    for w in words:
      mr.emit_intermediate(w, doc_id)

def reducer(word, list_of_docs):
    doc_list = set()
    for doc_id in list_of_docs:
      doc_list.add(doc_id)
    mr.emit((word, list(doc_list)))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
