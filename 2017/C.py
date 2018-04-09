if __name__ == "__main__":
  # read input
  t = int(raw_input())
  for i in xrange(1, t + 1):
      stalls, people = [int(s) for s in raw_input().split(" ")]
      filled_stalls = 0
      left = right = stalls
      level = 0
      while filled_stalls < people:
          if (people == filled_stalls + 1):
              left = right = max(left, right)
          left = (left - 1) / 2 if left > 0 else 0
          right = right / 2
          #print "{} {}".format(left, right)
          filled_stalls = filled_stalls + 2 ** level
          level = level + 1
      print "Case #{}: {} {}".format(i, max(left, right), min(left, right))
