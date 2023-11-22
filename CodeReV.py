import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(0)
data = np.random.randn(100, 2)

# Create subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Bar plot for mean and median
variables = ['Variable 1', 'Variable 2']
for i, variable in enumerate([data[:, 0], data[:, 1]]):
    axes[0, 0].bar(['Mean', 'Median'], [np.mean(variable), np.median(variable)],
                   color=sns.color_palette('deep')[i], alpha=0.7, label=variables[i])

axes[0, 0].legend()
axes[0, 0].set_title('Descriptive Statistics: Mean and Median')

# Heatmap for correlation analysis
sns.heatmap(np.corrcoef(data.T), annot=True, ax=axes[0, 1])
axes[0, 1].set_title('Correlation Analysis')

# Histograms of variables
for i, variable in enumerate([data[:, 0], data[:, 1]]):
    sns.histplot(variable, bins=15, color=sns.color_palette('deep')[i], alpha=0.7, ax=axes[1, 0])

axes[1, 0].set_title('Histogram of Variables')

# Scatter plot
axes[1, 1].scatter(data[:, 0], data[:, 1], alpha=0.7)
axes[1, 1].set_xlabel('Variable 1')
axes[1, 1].set_ylabel('Variable 2')
axes[1, 1].set_title('Scatter Plot of Variable 1 vs Variable 2')

# Adjust layout and show the plot
plt.tight_layout()
plt.show()
