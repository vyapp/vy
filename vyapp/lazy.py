def consume_iter(iterator, time=1):
    def cave():
        from vyapp.app import root
        try:
            iterator.next()
        except Exception:
            pass
        else:    
            root.after(time, cave)

    cave()

