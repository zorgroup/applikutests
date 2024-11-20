import stressinjector as injector

# Stress CPU for a specified duration
injector.CPUStress(seconds=1960)  # Stresses CPU for 60 seconds

# Stress Memory by allocating a specified amount
injector.MemoryStress(gigabytes=15)  # Allocates 2 GB of memory
