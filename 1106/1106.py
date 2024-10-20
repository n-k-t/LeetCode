class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        # Take care of the base cases (no expression), otherwise call the expression runner.
        if expression[0] == "t":
            return True
        elif expression[0] == "f":
            return False
        else:
            return self.exp_eval_runner(expression)

    # Returns True or False based on the root expression and counts of 't'/'f' characters.
    def exp_eval_runner(self, expression: str) -> bool:
        logic_op = expression[0]

        num_true, num_false, _ = self.exp_eval(expression, 2)

        if logic_op == "!":
            if num_true == 1:
                return False
            else:
                return True
        elif logic_op == "&":
            if num_false > 0:
                return False
            else:
                return True
        elif logic_op == "|":
            if num_true > 0:
                return True
            else:
                return False

    # Returns the count of 't' and 'f' characters as well as the ending index.
    def exp_eval(self, expression: str, ind: int) -> Tuple[int, int, int]:
        num_true = 0
        num_false = 0

        while expression[ind] != ")":
            temp_str = expression[ind]

            if temp_str == "t":
                num_true += 1
            elif temp_str == "f":
                num_false += 1
            elif temp_str in set(("!", "&", "|")):
                num_true, num_false, ind = self.online_str_eval(num_true, num_false, ind, expression)
            
            ind += 1
        
        return (num_true, num_false, ind)

    # While running, evaluate an inner expression and return the updated counts and position after evaluating the inner
    # expression.
    def online_str_eval(self, num_true: int, num_false: int, ind: int, expression: str) -> Tuple[int, int, int]:
        logic_op = expression[ind]

        temp_t, temp_f, ind = self.exp_eval(expression, ind + 2)

        if logic_op == "!":
            if temp_t == 1:
                num_false += 1
            else:
                num_true += 1
        elif logic_op == "&":
            if temp_f > 0:
                num_false += 1
            else:
                num_true += 1
        elif logic_op == "|":
            if temp_t > 0:
                num_true += 1
            else:
                num_false += 1
        
        return (num_true, num_false, ind)