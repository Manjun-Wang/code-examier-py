import sys
import getopt
import pathlib


class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg


def main(argv=None):
    if argv is None:
        print(sys.argv)
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(argv[1:], "h", ["help", "file=", "language=", "dir="])

            print(opts, args)
            options = get_correct_opts(opts)

            print(options)
        except getopt.error as msg:
            raise Usage(msg)
        # more code, unchanged
    except Usage as err:
        print(sys.stderr, err.msg)
        print(sys.stderr, "for help use --help")
        return 2


def get_correct_opts(opts):
    options = {}
    for opt in opts:
        if opt[0] == "--file":
            options["file"] = opt[1]
        if opt[0] == "--dir":
            options["dir"] = opt[1]
        if opt[0] == "--language":
            options["language"] = opt[1]
    if len(options) != 3:
        raise Usage("Need to have --file=x and --language=y as input params")
    return options


def get_file_list_from_options(options):
    """
    options contain dir or just file, the func will return a list of file paths
    """
    files = []
    if "dir" in options:
        files += list(pathlib.Path(options["dir"]).rglob("*.py"))
    print(line_counter(files))


def line_counter(files):
    lines = []
    for f in files:
        lines += open(str(f)).readlines()

    new_lines = list(filter(lambda x: line_filter_manager(x), list(map(lambda line: line.strip(" \n\t"), lines))))

    print(new_lines)
    return len(new_lines)


def line_filter_manager(line):
    opt_out = False

    if line != '':
        opt_out = True

    if "import" in line:
        opt_out = True

    return opt_out


if __name__ == "__main__":
    # sys.exit(main())
    options = {
        "language": ".py",
        "dir": "/Users/manman/PycharmProjects/untitled1/com",
        "file": "/Users/manman/PycharmProjects/untitled1/com/__init__.py"
    }

    get_file_list_from_options(options)
