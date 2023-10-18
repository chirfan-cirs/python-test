import data

if __name__ == '__main__':
    print("Main Application")
    result = data.extract_data()
    if result:
        data.save_csv(result)
        data.view_data(result)
