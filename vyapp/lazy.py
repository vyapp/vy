"""
This module implements tools to execute python code asynchronously with tkinter mainloop.
"""

def consume_iter(iterator, time=1):
    """
    This function receives an iterator that is consumed from tkinter update
    function. It is a way to have python code executed asynchronously.  Some
    plugins would perform heavy operations that could block tkinter mainloop,
    these plugins should write code that can be executed asynchronously using  
    iterators.

    Note: Some plugins like syntax highlighting would use this technique
    to highlight code. 
    """

    def cave():
        from vyapp.app import root
        try:
            iterator.next()
        except Exception:
            pass
        else:    
            root.after(time, cave)

    cave()


