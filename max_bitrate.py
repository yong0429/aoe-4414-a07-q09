# max_bitrate.py
#
# Usage: python3 max_bitrate.py tx_w tx_gain_db freq_hz dist_km rx_gain_db n0_j bw_hz

# Parameters:
#  tx_w: transmitter power in watts
#  tx_gain_db: transmitter gain in dB
#  freq_hz: frequency in Hz
#  dist_km: distance in km
#  rx_gain_db: receiver gain in dB
#  n0_j: noise spectral density in J/Hz
#  bw_hz: bandwidth in Hz

# Output:
#  r_max: Maximum achievable bitrate

# Written by Yonghwa Kim
# Other contributors: None

# import Python modules
import math # math module
import sys  # argv

# constants
c = 2.99792458e8; # speed of light in m/s

# initialize script arguments
tx_w = float('nan')
tx_gain_db = float('nan')
freq_hz = float('nan')
dist_km = float('nan')
rx_gain_db = float('nan')
n0_j = float('nan')
bw_hz = float('nan')

# parse script arguments
if len(sys.argv)==8:
  tx_w = float(sys.argv[1])
  tx_gain_db = float(sys.argv[2])
  freq_hz = float(sys.argv[3])
  dist_km = float(sys.argv[4])
  rx_gain_db = float(sys.argv[5])
  n0_j = float(sys.argv[6])
  bw_hz = float(sys.argv[7])
else:
  print(\
   'Usage: '\
   'python3 max_bitrate.py tx_w tx_gain_db freq_hz dist_km rx_gain_db n0_j bw_hz'\
  )
  exit()

# Convert gains from dB to linear scale
G_t = 10**(tx_gain_db / 10)
G_r = 10**(rx_gain_db / 10)

# Convert db to linear scale
L_l = 10**(-1 / 10)
L_a = 10**(0 / 10)

# Convert distance
dist_m = dist_km * 1000

# Calculate the wavelength
lam = c / freq_hz

# Calculate Received Power
C = tx_w * L_l * G_t * (lam / (4 * math.pi * dist_m))**2 * L_a * G_r

# Calculate Received Noise Power
N = n0_j * bw_hz

# Calculate the maximum achievable bitrate
r_max = bw_hz * math.log2(1 + (C / N))


print(math.floor(r_max))