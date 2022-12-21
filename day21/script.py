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

  def eval(id: str):
    m = M[id]
    if isinstance(m, int):
      return M[id]
    left, op, right = m
    if op == '+':
      res = eval(left) + eval(right)
    elif op == '-':
      res = eval(left) - eval(right)
    elif op == '*':
      res = eval(left) * eval(right)
    elif op == '/':
      res = eval(left) // eval(right)
    else:
      assert False, op
    return res

  print(eval('root'))

  def find_human(id: str):
    m = M[id]
    if isinstance(m, int):
      return None
    left, _, right = m
    if left == 'humn':
      return [True]
    elif right == 'humn':
      return [False]
    left_path = find_human(left)
    if left_path is not None:
      return [True, *left_path]
    right_path = find_human(right)
    if right_path is not None:
      return [False, *right_path]
    return None

  human_path = find_human('root')
  root_left, _, root_right = M['root']
  to_equal = eval(root_right if human_path else root_left)
  id = root_left if human_path else root_right
  for go_left in human_path[1:]:
    m = M[id]
    assert not isinstance(m, int)
    left, op, right = m
    other = eval(right if go_left else left)
    if op == '+':
      to_equal = to_equal - other
    elif op == '-':
      to_equal = to_equal + other if go_left else other - to_equal
    elif op == '*':
      to_equal = to_equal // other
    elif op == '/':
      to_equal = to_equal * other if go_left else other // to_equal
    else:
      assert False
    id = left if go_left else right
    if (left if go_left else right) == 'humn':
      print(to_equal)

  M['humn'] = to_equal
  left = eval(root_left)
  right = eval(root_right)
  assert left == right, f"{left} != {right}"
