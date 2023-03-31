# Imports
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Set default theme
sns.set_theme()


def weight_chart_display():
    # Reads in CSV data to be used for the visualization
    weight_chart = pd.read_csv('species_data.csv')

    sns.relplot(
        data=weight_chart, kind='line',
        x='HEIGHT', y='WEIGHT',
    )

    # Changes the graph labels
    plt.xlabel('Height (m)')
    plt.ylabel('Weight (kg)')
    plt.title('Species Weight and Height')

    plt.show()


def size_chart_display():
    # Reads in CSV data to be used for the visualization
    size_chart = pd.read_csv('galaxy_data.csv')
    sns.relplot(
        data=size_chart, kind='line',
        x='PLANET SIZE', y='HEIGHT',
    )

    # Changes the graph labels
    plt.xlabel('Planet Size Class')
    plt.ylabel('Height (m)')
    plt.title('Species Height to Planet Class Correlation')

    return plt.show()


def sapience_chart_display():
    # Reads in CSV data to be used for the visualization
    sapience_chart = pd.read_csv('species_data.csv')
    sns.relplot(
        data=sapience_chart,
        x='HEIGHT', y='SAPIENCE INDEX', hue='MORPHOLOGY', style="MORPHOLOGY"
    )

    # Changes the graph labels
    plt.xlabel('Height (m)')
    plt.ylabel('Sapience Index')
    plt.title('Sapience to Species Size Correlation')
    plt.show()
