import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

N = 100

def mapper(record):
    # key: document identifier
    # value: document contents
    matrix = record[0]
    i = record[1]
    j = record[2]
    value = record[3]
    if matrix == 'a':
      for n in xrange(5):
        mr.emit_intermediate('{} {}'.format(i, n), record)
    elif matrix == 'b':
      for n in xrange(5):
        mr.emit_intermediate('{} {}'.format(n, j), record)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    key_split = key.split()
    i = int(key_split[0])
    j = int(key_split[1])
    value = 0
    a = [[0 for x in xrange(N)] for y in xrange(N)]
    b = [[0 for x in xrange(N)] for y in xrange(N)]
    for v in list_of_values:
      if v[0] == 'a':
        a[v[1]][v[2]] = v[3]
      elif v[0] == 'b':
        b[v[1]][v[2]] = v[3]
      #mr.emit((i, j, v))
    for n in xrange(N):
      value += (a[i][n] * b[n][j])
    mr.emit((i, j, value))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
