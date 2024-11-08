import matplotlib.pyplot as plt


def display_dots(data):
    data = data.set_index('km')

    plt.title('Car for sale')
    plt.ylabel('Kilometers')
    plt.xlabel('Price')
    plt.plot(data, 'o')
    
    plt.show()
    plt.close()
