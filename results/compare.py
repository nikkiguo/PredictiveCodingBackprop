import matplotlib.pyplot as plt

# Define the constant for the x-axis range
N_EPOCHS = 16  

# Load y-axis data from files
def load_data(filename):
    with open(filename, 'r') as file:
        return [float(line.strip()) for line in file]

tanh_pc = load_data('./test_accuracies/tanh_cifar_pc_accuracies.txt')
sigmoid_pc = load_data('./test_accuracies/sigmoid_cifar_pc_accuracies.txt')
linear_pc = load_data('./test_accuracies/linear_cifar_pc_accuracies.txt')
relu_pc = load_data('./test_accuracies/relu_cifar_pc_accuracies.txt')
lrelu_pc = load_data('./test_accuracies/lrelu_cifar_pc_accuracies.txt')

tanh_bp = load_data('./test_accuracies/tanh_cifar_bp_accuracies.txt')
sigmoid_bp = load_data('./test_accuracies/sigmoid_cifar_bp_accuracies.txt')
linear_bp = load_data('./test_accuracies/linear_cifar_bp_accuracies.txt')
relu_bp = load_data('./test_accuracies/relu_cifar_bp_accuracies.txt')
lrelu_bp = load_data('./test_accuracies/lrelu_cifar_bp_accuracies.txt')

x = list(range(0, N_EPOCHS))

plt.figure(figsize=(10, 6))
# Plot each line
plt.plot(x, tanh_pc, label="pc tanh", color="blue", marker="o")
plt.plot(x, sigmoid_pc, label="pc sigmoid", color="green", marker="o")
plt.plot(x, linear_pc, label="pc linear", color="red", marker="o")
plt.plot(x, relu_pc, label="pc relu", color="orange", marker="o")
plt.plot(x, lrelu_pc, label="pc leaky_relu", color="purple", marker="o")

plt.plot(x, tanh_bp, label="bp tanh", color="blue", marker="x")
plt.plot(x, sigmoid_bp, label="bp sigmoid", color="green", marker="x")
plt.plot(x, linear_bp, label="bp linear", color="red", marker="x")
plt.plot(x, relu_bp, label="bp relu", color="orange", marker="x")
plt.plot(x, lrelu_bp, label="bp leaky_relu", color="purple", marker="x")

# Customize the plot
plt.ylim(0.4, 0.7)
plt.xlabel("Epoch")
plt.ylabel("Accuracy (%)")

plt.title("Test Accuracy of BP and PC on CIFAR Dataset", pad=20)
plt.legend(title='Activation Function', loc="center left", bbox_to_anchor=(1, 0.5))
plt.grid(True)
plt.tight_layout()

# save the plot
plt.savefig('./graphs/CIFAR.png')

# Show the plot
plt.show()
