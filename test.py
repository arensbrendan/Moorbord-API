from working_files.decorators import hit


@hit(__file__)
def test():
    return 1


test()
