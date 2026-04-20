from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[2]
OUTPUT_DIR = ROOT / "assets" / "img"


def ensure_output_dir() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def save_bn_example_plot() -> None:
    x = np.array([2.0, 4.0, 6.0, 8.0], dtype=float)
    epsilon = 1e-5
    mu = x.mean()
    var = ((x - mu) ** 2).mean()
    x_hat = (x - mu) / np.sqrt(var + epsilon)
    y = 2.0 * x_hat + 1.0

    positions = np.arange(len(x))

    fig, axes = plt.subplots(1, 3, figsize=(13, 4), sharex=True)
    series = [
        ("Original Activations", x, "#345995"),
        ("Normalized Activations", x_hat, "#03cea4"),
        ("Scaled and Shifted", y, "#fb4d3d"),
    ]

    for ax, (title, values, color) in zip(axes, series):
        ax.bar(positions, values, color=color, width=0.65)
        ax.axhline(0.0, color="#666666", linewidth=0.8)
        ax.set_title(title)
        ax.set_xticks(positions)
        ax.set_xticklabels([f"x{i + 1}" for i in positions])
        ax.grid(axis="y", linestyle="--", alpha=0.35)

    axes[0].set_ylabel("Value")
    fig.suptitle("Batch Normalization Example", fontsize=14)
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "batch-normalization-example.png", dpi=180, bbox_inches="tight")
    plt.close(fig)


def generate_data(batch_size: int, features: int, num_batches: int, seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    means = np.linspace(-1.4, 1.4, num_batches)
    data = []

    for idx, mean in enumerate(means):
        scale = 0.7 + 0.2 * np.sin(idx / 6)
        batch = rng.normal(loc=mean, scale=scale, size=(batch_size, features))
        data.append(batch)

    return np.array(data)


def train_running_stats(data: np.ndarray, dynamic_momentum: bool = False) -> tuple[list[float], list[float]]:
    running_mean = np.zeros(data.shape[-1], dtype=float)
    running_var = np.ones(data.shape[-1], dtype=float)
    running_means: list[float] = []
    running_vars: list[float] = []

    for epoch, batch in enumerate(data):
        momentum = max(0.9 - (epoch / 50), 0.1) if dynamic_momentum else 0.9
        batch_mean = batch.mean(axis=0)
        batch_var = batch.var(axis=0)

        running_mean = (1 - momentum) * running_mean + momentum * batch_mean
        running_var = (1 - momentum) * running_var + momentum * batch_var

        running_means.append(float(running_mean.mean()))
        running_vars.append(float(running_var.mean()))

    return running_means, running_vars


def save_momentum_comparison_plot() -> None:
    data = generate_data(batch_size=16, features=5, num_batches=50, seed=7)
    static_means, static_vars = train_running_stats(data, dynamic_momentum=False)
    dynamic_means, dynamic_vars = train_running_stats(data, dynamic_momentum=True)
    epochs = np.arange(len(static_means))

    fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))

    axes[0].plot(epochs, static_means, label="Static Momentum", linewidth=2, color="#345995")
    axes[0].plot(epochs, dynamic_means, label="Dynamic Momentum", linewidth=2, color="#fb4d3d")
    axes[0].set_title("Running Mean")
    axes[0].set_xlabel("Epoch")
    axes[0].set_ylabel("Mean Value")
    axes[0].grid(True, linestyle="--", alpha=0.35)
    axes[0].legend()

    axes[1].plot(epochs, static_vars, label="Static Momentum", linewidth=2, color="#345995")
    axes[1].plot(epochs, dynamic_vars, label="Dynamic Momentum", linewidth=2, color="#fb4d3d")
    axes[1].set_title("Running Variance")
    axes[1].set_xlabel("Epoch")
    axes[1].set_ylabel("Variance Value")
    axes[1].grid(True, linestyle="--", alpha=0.35)
    axes[1].legend()

    fig.suptitle("Static vs Dynamic Momentum", fontsize=14)
    fig.tight_layout()
    fig.savefig(
        OUTPUT_DIR / "batch-normalization-momentum-comparison.png",
        dpi=180,
        bbox_inches="tight",
    )
    plt.close(fig)


def main() -> None:
    ensure_output_dir()
    save_bn_example_plot()
    save_momentum_comparison_plot()


if __name__ == "__main__":
    main()
