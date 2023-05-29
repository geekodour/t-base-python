# snoop tracing
# import snoop
# snoop.install(snoop="ss")
# usage:
# - @ss, @ss(depth=2), with ss:

from bake import kitchen


def run_da_main_func():
    kitchen.do_something()


if __name__ == "__main__":
    run_da_main_func()
