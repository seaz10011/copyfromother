def search_file(keyword, file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if keyword in line:
                    print(line.strip())
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")

# Example usage:
if __name__ == "__main__":
    file_path = 'sample.txt'
    keyword = input("Enter keyword to search: ")
    # Removed incorrect encoding: keyword = keyword.encode('utf-8', errors='replace')
    search_file(keyword, file_path)
