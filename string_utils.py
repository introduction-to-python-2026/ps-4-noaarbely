def split_at_first_digit(formula):
  digit_location = 1
  for i in formula[1:]:
      if i.isdigit():
        break
      digit_location += 1
  if digit_location == len(formula):
       return formula, 1
  per = formula [:digit_location]
  num = int(formula[digit_location:])

  return per, num


def split_before_each_uppercases(formula):
    start=0
    split_formula=[]
    for i in range(1, len(formula)):
      c= formula [i]
      if c.isupper():
        split_formula.append(formula[start:i])
        start=i
    split_formula.append(formula[start:])

    return split_formula
