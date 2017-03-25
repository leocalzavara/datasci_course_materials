import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    mr.emit_intermediate(record[0] + ',' + record[1], 1)
    mr.emit_intermediate(record[1] + ',' + record[0], 1)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    if len(list_of_values) == 1:
      names = key.split(',')
      mr.emit((names[0], names[1]))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
