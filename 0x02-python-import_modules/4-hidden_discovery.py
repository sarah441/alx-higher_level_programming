#!/usr/bin/python3

if __name__ == "__main__":
    """Print all in hidden4"""
    import hidden_4

    total_names = dir(hidden_4)
    for name in total_names:
        if name[:2] != "__":
            print(name)
