from calculations import get_average_calories
from data_handler import load_gym_data 
from plotter import plot_bar_chart, plot_scatter,plot_heatmap

def main():
    df = load_gym_data()
    cal = get_average_calories(df)
    print(cal)
    plot = plot_bar_chart(df)
    print(plot)
    scatter = plot_scatter(df)
    print(scatter)
    hatmap = plot_heatmap(df)
    print(hatmap)

if __name__ == "__main__":
    main()