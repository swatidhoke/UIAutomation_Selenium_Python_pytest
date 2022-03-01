"""
input:  text = “(()”
output: 1

input:  text = “(())”
output: 0

input:  text = “())( -> ()()(”
                             p
output: 2
O(n) S= O(1)
"""

def bracket_match(text):
  out_open = 0
  out_close = 0
  out_value = 0
  for x in text:
    if x == "(":
      out_open += 1
    else:
      out_close += 1
    # represents adding an opening bracket when closeB > openB
    if out_open < out_close:
      out_value += 1
      out_open += 1      

  return out_open - out_close + out_value

print(bracket_match("())("))
