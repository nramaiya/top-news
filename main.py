from helper import*

### MAIN PROGRAM

if __name__== '__main__':
    country=input('Please enter a country: ')
    category=input('Please enter a category: ')
    n=int(input('How many articles do you want to write: '))
    #Task -1
    data=get_top_news(country,category)
    #Task -2
    formatted_data = format_data(data)
    #Task -3
    write_to_file(formatted_data,n)

