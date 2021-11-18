# Default shortcuts.
from vyapp.plugins import mapset

mapset('main-jumps', {
(-1, '<Alt-a>'):(('NORMAL', '<Key-j>'), (-1, '<Alt-a>')), 
(-1, '<Alt-e>'):(('NORMAL', '<Key-k>'), (-1, '<Alt-e>')), 
(-1, '<Alt-n>'):(('NORMAL', '<Key-h>'), (-1, '<Alt-n>')), 
(-1, '<Alt-m>'):(('NORMAL', '<Key-l>'), (-1, '<Alt-m>')), 
})

mapset('text-jumps', {
(-1, '<Alt-d>'):(('NORMAL', '<Key-o>'), (-1, '<Alt-d>')), 
(-1, '<Alt-f>'):(('NORMAL', '<Key-p>'), (-1, '<Alt-f>')), 
(-1, '<Alt-g>'):(('NORMAL', '<Key-s>'), (-1, '<Alt-g>')), 
(-1, '<Alt-b>'):(('NORMAL', '<Key-c>'), (-1, '<Alt-b>')), 
})
