import matplotlib.pyplot as plt

def read_dataset(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        points = [tuple(map(float, line.strip().split())) for line in lines]
    return points

def plot_points(points):
    plt.figure(figsize=(960/80, 540/80))

    x, y = zip(*points)
    plt.scatter(x, y, color='purple', marker='o', label='Точки')

    plt.xlabel('X-координата')
    plt.ylabel('Y-координата')
    plt.title('Графічне відображення точок')
    plt.legend()

    plt.savefig('result.png')
    plt.show()

if __name__ == "__main__":
    
    dataset_path = 'DS4.txt'

    points = read_dataset(dataset_path)
    plot_points(points)
