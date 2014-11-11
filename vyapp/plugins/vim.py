
"""


"""
from vyapp.app import root
from vyapp.ask import *
import os

def insert_tab(area):
    area.insert_tab()
    return True

INSTALL =  [(1, '<Shift-greater>', lambda event: event.widget.align_sel_right()),
            (1, '<Shift-less>', lambda event: event.widget.align_sel_left()),

            (1, '<Key-j>', lambda event: event.widget.down()),
            (1, '<Key-k>', lambda event: event.widget.up()),
            (1, '<Key-h>', lambda event: event.widget.left()),
            (1, '<Key-l>', lambda event: event.widget.right()),

            (1, '<Key-slash>', lambda event: event.widget.select_case_pair(('(', ')'))),
            (1, '<Key-slash>', lambda event: event.widget.select_case_pair(('[', ']'))),
            (1, '<Key-slash>', lambda event: event.widget.select_case_pair(('{', '}'))),

            (1, '<Key-C>', lambda event: event.widget.select_char()),
            (1, '<Key-V>', lambda event: event.widget.unselect_char()),

            (1, '<Key-f>', lambda event: event.widget.select_line()),
            (1, '<Key-g>', lambda event: event.widget.unselect_line()),

            (1, '<Key-w>', lambda event: event.widget.scroll_line_up()),
            (1, '<Key-s>', lambda event: event.widget.scroll_line_down()),
        
            (1, '<Key-q>', lambda event: event.widget.scroll_page_up()),
            (1, '<Key-a>', lambda event: event.widget.scroll_page_down()),

            (1, '<Key-d>', lambda event: event.widget.clsel()),
            (1, '<Key-x>', lambda event: event.widget.cllin()),
        
            (1, '<Key-z>', lambda event: event.widget.clchar()),

            (1, '<Control-o>', lambda event: event.widget.sel_line_start()),
            (1, '<Control-p>', lambda event: event.widget.sel_line_end()),

            (1, '<Key-o>', lambda event: event.widget.go_line_start()),
            (1, '<Key-p>', lambda event: event.widget.go_line_end()),

            (1, '<Control-Key-1>', lambda event: event.widget.sel_text_start()),
            (1, '<Control-Key-2>', lambda event: event.widget.sel_text_end()),

            (1, '<Key-1>', lambda event: event.widget.go_text_start()),
            (1, '<Key-2>', lambda event: event.widget.go_text_end()),

            (1, '<Key-bracketright>', lambda event: event.widget.go_next_word()),
            (1, '<Key-braceright>', lambda event: event.widget.go_prev_word()),

            (1, '<Key-P>', lambda event: event.widget.go_next_sym()),
            (1, '<Key-O>', lambda event: event.widget.go_prev_sym()),

            (1, '<Key-m>', lambda event: event.widget.insert_line_down()),
            (1, '<Key-n>', lambda event: event.widget.insert_line_up()),
            (1, '<Key-y>', lambda event: event.widget.cpsel()),
            (1, '<Key-u>', lambda event: event.widget.ctsel()),
            (1, '<Key-t>', lambda event: event.widget.ptsel()),
            (1, '<Key-r>', lambda event: event.widget.ptsel_after()),
            (1, '<Key-e>', lambda event: event.widget.ptsel_before()),
        
            (1, '<Key-comma>', lambda event: event.widget.do_undo()),
            (1, '<Key-period>', lambda event: event.widget.do_redo()),
        
            (1, '<Control-k>', lambda event: event.widget.sel_up()),
            (1, '<Control-j>', lambda event: event.widget.sel_down()),
            (1, '<Control-h>', lambda event: event.widget.sel_left()),
            (1, '<Control-l>', lambda event: event.widget.sel_right()),
            
            (1, '<Control-K>', lambda event: event.widget.block_up()),
            (1, '<Control-J>', lambda event: event.widget.block_down()),
            (1, '<Control-H>', lambda event: event.widget.block_left()),
            (1, '<Control-L>', lambda event: event.widget.block_right()),
        
            (1, '<Control-Y>', lambda event: event.widget.cpblock()),
            (1, '<Control-U>', lambda event: event.widget.ctblock()),

            (-1, '<Left>', lambda event: root.note.scroll_left()),
            (-1, '<Right>', lambda event: root.note.scroll_right()),

            (1, '<Control-a>', lambda event: event.widget.select_all()),
            (0, '<Tab>', lambda event: insert_tab(event.widget)),
            (1, '<Key-bracketleft>', lambda event: event.widget.select_word()),
            (1, '<Control-v>', lambda event: event.widget.start_selection())]

        
def install(area):
    area.install(*INSTALL)





















