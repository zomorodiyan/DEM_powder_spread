# Given radii for each bin (in micrometers)
radii = [6, 12.5, 21.5, 30]

# Given target volume fractions for each bin
volume_fractions = [0.10, 0.40, 0.40, 0.10]

# Calculate the volume of a single particle in each bin (proportional to r^3)
volumes = [r**3 for r in radii]

# Compute unnormalized number weights: volume_fraction / particle_volume
number_weights = [vf / v for vf, v in zip(volume_fractions, volumes)]

# Normalize to get number fractions
total_weight = sum(number_weights)
number_fractions = [nw / total_weight for nw in number_weights]

# Print result
for i, (r, vf, nf) in enumerate(zip(radii, volume_fractions, number_fractions), 1):
    print(f"Bin {i}: Radius = {r} µm, Volume Fraction = {vf:.2f}, Number Fraction = {nf:.6f}")

