class MyQueue(object):

    def __init__(self):
        
        self.input_stack = []
        self.output_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.input_stack.append(x)

    def pop(self):
        """
        :type : rtype: int
        """
       
        self._move_elements()
        return self.output_stack.pop()

    def peek(self):
        """
        :type : rtype: int
        """
        
        self._move_elements()
        return self.output_stack[-1]

    def empty(self):
        """
        :type : rtype: bool
        """
        # The queue is empty only if BOTH stacks are empty
        return not self.input_stack and not self.output_stack

    def _move_elements(self):
        """
        Helper method to transfer elements from input to output stack
        only when the output stack is completely empty.
        """
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())
