import argparse


## code-runner called by dundermain
def cli():
    ## set up parser taking --name as argument
    ## if name arg is supplied, call other function with name, otherwise print out usage.
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', help='Name to greet')
    args = parser.parse_args()
    if args.name:
        hello(args.name)
    else:
        parser.print_help()


## function to print out hello world
def hello(name):
    print(f'Hello {name}!')


## dundermain to call cli function
if __name__ == '__main__':
    cli()
