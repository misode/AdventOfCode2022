with open('day21/in.txt') as f:
  lines = [l.strip() for l in f.readlines()]

  M = dict()

  for line in lines:
    a, b = line.split(": ")
    if '0' <= b[0] <= '9':
      M[a] = int(b)
    else:
      left, op, right = b.split(' ')
      M[a] = (left, op, right)

  def solve(id: str):
    m = M[id]
    if isinstance(m, int):
      return M[id]

    left, op, right = m
    if op == '+':
      res = solve(left) + solve(right)
    elif op == '-':
      res = solve(left) - solve(right)
    elif op == '*':
      res = solve(left) * solve(right)
    else:
      assert op == '/'
      res = solve(left) // solve(right)
    return res

  print(solve('root'))
