import numpy as np

def main():
	xvalues = np.linspace(0, 2*np.pi, 1000)
	sinvalues = np.sin(xvalues)

	print(f"{'x':>10} {'sin(x)':>10}")
	print("-" * 25)

	for x, sin_x in zip(xvalues, sinvalues):
	    print(f"{x:>10.4f} {sin_x:>10.4f}")

if __name__ == "__main__":
	main()