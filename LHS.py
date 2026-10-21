import pandas as pd
from scipy.stats import qmc

# Number of parameters (dimensions)
d = 7
# Rule of thumb: 50 samples per parameter
n_sims = 10

# Parameter bounds based on your previous grid
# Order: [oc, mnu, h, w0, wa, As, ns]
l_bounds = [0.20, 0.00, 61.0, -1.3, -0.6, 1.91e-9, 0.87]
u_bounds = [0.34, 0.15, 73.0, -0.7,  0.6, 2.31e-9, 1.056]

# Generate the Latin Hypercube (seeded for reproducibility)
sampler = qmc.LatinHypercube(d=d, seed=42)
sample = sampler.random(n=n_sims)

# Scale the 0-1 samples to your actual cosmological bounds
scaled = qmc.scale(sample, l_bounds, u_bounds)

df = pd.DataFrame(scaled, columns=["oc", "mnu", "h", "w0", "wa", "As", "ns"])
# Add a run index (1 to 300) to easily track files
df.insert(0, "run_id", range(101, len(df) + 101))

# Save to CSV
df.to_csv("validation_10.csv", index=False)
print(f"Successfully generated lhs_params.csv with {n_sims} simulations.")