import numpy as np

g = 9.81 # [m/s^2]

def l(vox: np.float64, voz: np.float64, h_hoop: np.float64, h_jump: np.float64, h_srp: np.float64) -> tuple[np.float64, np.float64]:
    voz_over_vox_sq = voz**2 / vox**2
    h_diff = h_hoop - h_jump - h_srp
    lp = (vox*voz + np.sqrt(voz_over_vox_sq - 2.0 * g / vox**2 * h_diff)) / g
    lm = (vox*voz - np.sqrt(voz_over_vox_sq - 2.0 * g / vox**2 * h_diff)) / g
    return (lp, lm) 