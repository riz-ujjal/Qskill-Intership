import matplotlib.pyplot as plt

def plot_bar_chart(df):
    df['Muscle_Group']
    x = df['Muscle_Group']
    df['Calories_Burned']
    y = df['Calories_Burned']
    plt.title("compare")
    plt.xlabel('X Label')
    plt.ylabel('Y Label')
    plt.bar(x,y)
    plt.show()
    
def plot_scatter(df):
    df['Avg_Heart_Rate']
    df['Calories_Burned']
    x = df['Avg_Heart_Rate']
    y = df['Calories_Burned']
    plt.scatter(x,y)
    plt.title("compare")
    plt.xlabel('X Label')
    plt.ylabel('Y Label')
    plt.bar(x,y)
    plt.show()
    
def plot_heatmap(df):
    matrix = df[['Duration_Minutes', 'Calories_Burned', 'Avg_Heart_Rate']].corr()
    plt.imshow(matrix, cmap='viridis')
    plt.colorbar()
    plt.show()