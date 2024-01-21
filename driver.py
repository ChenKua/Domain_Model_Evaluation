import subprocess


def run_another_python_script_with_args(script_path, arg1, arg2):
    try:
        subprocess.run(["python", script_path, arg1, arg2], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")


# Example: Running "example_script_with_args.py" with arguments "value1" and "value2"
script_path = "module.py"
arg1 = "value1"
arg2 = "value2"
run_another_python_script_with_args(script_path, arg1, arg2)
