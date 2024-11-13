import matplotlib.pyplot as plt


def display_dots(data, teta0, teta1):
    data = data.set_index('km')

    plt.title('Car for sale')
    plt.ylabel('Price')
    plt.xlabel('Kilometers')
    plt.plot(teta0, teta1, 'l')
    plt.plot(data, 'o')
    
    plt.show()
    plt.close()
