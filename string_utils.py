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
    start = 0
    end = 1
    split_formula = []

    for c in formula[1:]
        if c.isupper():
            split_formula.append(formula[start:end])
            start = end
        end += 1
    split_formula.append(formula[start:end])

    return split_formula
