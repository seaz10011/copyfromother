def search_file(keyword, file_path):
    with open(file_path, 'r') as file:
        for line in file:
            if keyword in line:
                print(line.strip())

# Example usage:
file_path = 'C:/20210817/123.txt'
keyword = input("sharepoint")
keyword = keyword.encode('utf-8', errors='replace')
search_file(keyword, file_path)


# Output: