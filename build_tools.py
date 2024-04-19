import os
import argparse

project_path = os.getcwd()

parser = argparse.ArgumentParser(description="Build Tools")

parser.add_argument("--build", action="store_true", help="Build the project")
parser.add_argument("--clean", action="store_true", help="Clean the project")
parser.add_argument("--rebuild", action="store_true", help="Rebuild the project")
parser.add_argument("--flash", action="store_true", help="Flash the project")

args = parser.parse_args()

if not args.rebuild and not args.clean and not args.build and not args.flash:
    print(
        "No command provided. Please provide one of the following options: --build, --clean, --rebuild, --flash"
    )
    exit(1)

if args.rebuild:
    os.chdir("tools")
    os.system(f"python clean.py && python build.py")
    os.chdir(project_path)

if args.clean and not args.rebuild:
    os.chdir("tools")
    os.system(f"python clean.py")
    os.chdir(project_path)

if args.build and not args.rebuild:
    os.chdir("tools")
    os.system(f"python build.py")
    os.chdir(project_path)

if args.flash:
    os.chdir("tools")
    os.system(f"python flash.py")
    os.chdir(project_path)
