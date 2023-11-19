import handler as Handler

def main(filename: str = "exemplo.txt", limit: int = 1000):
    handler = Handler.Handler(filename)
    print(handler.handle(limit, filename))
    
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--limit", type=int, default=1000, help="number of times to run the algorithm")
    parser.add_argument("filenames", nargs="+", help="files to read data from")
    args = parser.parse_args()
    if args.limit < 1:
        print("Limit must be greater than 0 (default: 1000)")
        exit(1)
    # example: python main.py -l 1000 exemplo.txt
    # warning: don't try to run this with more than 1_000_000 iterations, it will take a long time
    
    for filename in args.filenames:
        main(filename, args.limit)