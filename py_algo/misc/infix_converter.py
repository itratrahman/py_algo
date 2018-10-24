from ..data_struct import Stack

def infix2postfix(infix_expr):

    '''
    A function to convert infix expression to postfix expression
    Arguments:
    infix_expr - infix expression
    Returns:
    postfix_expr - postfix expression
    '''

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
        # ff the token is a left parenthesis,then push it to the stack_of_op
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

    pass


def postFixEval(postfix_expr):

    pass
