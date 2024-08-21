from directory import Directory
from typing import List

args_count = {
    'LIST': 0, 'MOVE': 2, 'CREATE': 1, 'DELETE': 1
}
method = {
    'LIST': 'list', 'MOVE': 'move', 'CREATE': 'create', 'DELETE': 'delete'
}


def validate_input(command: str, args: List) -> str:
    if command not in args_count.keys():
        raise Exception(f'Unknown command {command}')

    if args_count[command] != len(args):
        raise Exception(f'Command {command} needs {args_count[command]} arguments, {len(args)} found!')

    return method[command]


if __name__ == "__main__":
    directory_class = Directory()
    while True:
        command_str, *args_ary = input("").strip().split(" ")
        # Remove multiple space between the args
        args_ary = [arg for arg in args_ary if arg]
        try:
            class_method = validate_input(command_str, args_ary)
            result = getattr(directory_class, class_method)(*args_ary)
            print(result)
        except Exception as e:
            print(f'Error: {e}')
            continue
