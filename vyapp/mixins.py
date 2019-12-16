from os.path import abspath
from vyapp.areavi import AreaVi
from vyapp.app import root

class DAP:
    """
    Debugger adapter pattern.
    """
    
    setup={'background':'blue', 'foreground':'yellow'}
    encoding='utf8'

    def __init__(self):
        self.map_index = dict()
        self.map_line  = dict()

    def clear_breakpoints_map(self):
        """
        It deletes all added breakpoint tags.
        It is useful when restarting pdb as a different process.
        """

        items = self.map_index.items()
        for index, (filename, line) in items:
            self.del_breakpoint(filename, index)

        self.map_index.clear()
        self.map_line.clear()

    def get_breakpoint_name(self, filename, line):
        filename = abspath(filename)
        return self.map_line[(filename, line)]

    def del_breakpoint(self, filename, index):
        filename = abspath(filename)
        widgets = AreaVi.get_opened_files(root)
        area    = widgets.get(filename)
        if area: area.tag_delete('_breakpoint_%s' % index)

    def handle_line(self, device, filename, line):
        """
    
        """
        filename = abspath(filename)

        wids = AreaVi.get_opened_files(root)
        area = wids.get(filename)

        if area: root.note.set_line(area, line)
    
    def handle_deleted_breakpoint(self, device, index):
        """
        When a break point is removed.
        """

        filename, line = self.map_index[index]
        self.del_breakpoint(filename, index)

    def handle_breakpoint(self, device, index, filename, line):
        """
        When a break point is added.
        """
        filename = abspath(filename)
        self.map_index[index]           = (filename, line)
        self.map_line[(filename, line)] = index

        map  = AreaVi.get_opened_files(root)
        area = map[filename]
        NAME = '_breakpoint_%s' % index

        area.tag_add(NAME, '%s.0 linestart' % line, '%s.0 lineend' % line)
        area.tag_config(NAME, **self.setup)

    def send(self, data):
        pass
