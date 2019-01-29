from ..data_struct import Stack

def infix2postfix(infix_expr):
    """
    A function to convert infix expression to postfix expression
    Arguments:
    infix_expr - infix expression
    Returns:
    postfix_expr - postfix expression
    """
    precedence = {}
    precedence["*"] = 3
    precedence["/"] = 3
    precedence["+"] = 2
    precedence["-"] = 2
    precedence["("] = 1

    # stack to hold the operations
    stack_of_op = Stack()
    # a list to contain the postfix tokens
    postfixList = []
    # a list to contain the infix tokens
    infixList = infix_expr.split()

    # iterate through each infix tokens
    for token in infixList:
        # if the token is an operand, then append it to the end of the output list
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        # if the token is a left parenthesis,then push it to the stack_of_op
        elif token == '(':
            stack_of_op.push(token)
        # if the token is a right parenthesis,
        # pop the stack_of_op until the corresponding left parenthesis is removed.
        # Append each operator to the end of the output list
        elif token == ')':
            topToken = stack_of_op.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = stack_of_op.pop()
        # If the token is an operator, *, /, +, or -, push it on the stack_of_op.
        # However, first remove any operators already on the stack_of_op
        # that have higher or equal precedence and append them to the output list
        else:
            while (not stack_of_op.isEmpty()) and \
               (precedence[stack_of_op.peek()] >= precedence[token]):
                  postfixList.append(stack_of_op.pop())
            stack_of_op.push(token)

    # When the input expression has been completely processed, check the stack_of_op.
    # Any operators still on the stack can be removed and appended to the end of the output list.
    while not stack_of_op.isEmpty():
        postfixList.append(stack_of_op.pop())

    # join elements if postfix_list with space to construct the postfix expression
    postfix_expr = " ".join(postfixList)

    # return the postfix expression
    return postfix_expr


def compute_operation(operator, operand1, operand2):
    """
    A function to compute mathematic operation between 2 operands based on match_symbol
    Arguments:
    operator - mathematical operators
    operand1 - first operand
    operand2 - second operand
    """
    if operator == "*":
        return operand1*operand2
    if operator == "/":
        return operand1/operand2
    if operator == "+":
        return operand1+operand2
    if operator == "-":
        return operand1-operand2

def postfixEval(postfix_expr):

    # a stack to hold the operands
    stack_of_operands = Stack()
    # split teh postfix expression into a list of tokens
    postfixList = postfix_expr.split()
    # iterate through each token in the postfix list
    for token in postfixList:
        #if the token is an operand,
        #convert it from a string to an integer and push the value onto the stack_of_operands
        if token in "0123456789":
            stack_of_operands.push(int(token))
        # If the token is an operator, *, /, +, or -, it will need two operands.
        # Pop the stack_of_operands twice. The first pop is the second operand and the second pop is the first operand.
        # Perform the arithmetic operation. Push the result back on the stack_of_operands
        else:
            operand2 = stack_of_operands.pop()
            operand1 = stack_of_operands.pop()
            evalutation = compute_operation(token, operand1, operand2)
            stack_of_operands.push(evalutation)

    # return the stack of operands
    return stack_of_operands.pop()
