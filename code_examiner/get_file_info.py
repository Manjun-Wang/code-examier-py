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

            get_file_list_from_options(get_correct_opts(opts))
        except getopt.error as msg:
            raise Usage(msg)
        # more code, unchanged
    except Usage as err:
        print(sys.stderr, err.msg)
        print(sys.stderr, "for help use --help")
        return 2


def exam(opts):
    get_file_list_from_options(get_correct_opts(opts))


def get_correct_opts(opts):
    options = {}
    for opt in opts:
        if opt[0] == "--file":
            options["file"] = opt[1].split(",")
        if opt[0] == "--dir":
            options["dir"] = opt[1].split(",")
        if opt[0] == "--language":
            options["language"] = opt[1].split(",")
    if len(options) != 3:
        raise Usage("Need to have --file=x and --language=y as input params")
    return options


def get_file_list_from_options(options):
    """
    options contain dir or just file, the func will return a list of file paths
    """
    out_put_files = []
    file_suffixes = options["language"]

    if "dir" in options:
        for directory in options["dir"]:
            for suffix in file_suffixes:
                out_put_files += list(pathlib.Path(directory).rglob("*" + suffix))

    print(line_counter(out_put_files))


def remove_lines_by_file_suffix(lines, suffix):
    """
    reserved function for suffix based filtering.
    :param lines:
    :param suffix:
    :return:
    """
    print(lines, suffix)
    # if suffix == ".py":
    #     lines.remove()
    return lines


def suffix_processor(line, suffix):
    if suffix == ".py":
        return "import" not in line
    if suffix == ".html":
        return True


def line_counter(files):
    result_lines = []
    for f in files:
        lines = open(str(f)).readlines()
        result_lines += list(filter(lambda x: line_filter_manager(x, f.suffix), list(map(lambda line: line.strip(" \n\t"), lines))))

    print(result_lines)
    return len(result_lines)


def line_filter_manager(line, suffix):
    """
    Return True to keep the result and False to opt out
    :param line:
    :param suffix:
    :return:
    """
    if line != '':
        return suffix_processor(line, suffix)

    return False


if __name__ == "__main__":
    test_options = {
        "language": [".py", ".html"],
        "dir": ["/Users/manman/PycharmProjects/untitled1/com"],
        "file": ["/Users/manman/PycharmProjects/untitled1/com/__init__.py"]
    }

    get_file_list_from_options(test_options)
