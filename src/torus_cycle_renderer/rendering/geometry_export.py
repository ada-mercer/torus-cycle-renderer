from __future__ import annotations

from pathlib import Path
import numpy as np


def export_scene_npz(
    path: str,
    x: np.ndarray,
    y: np.ndarray,
    z: np.ndarray,
    lx: np.ndarray,
    ly: np.ndarray,
    lz: np.ndarray,
) -> None:
    out = Path(path)
    out.parent.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(out, x=x, y=y, z=z, lx=lx, ly=ly, lz=lz)


def export_torus_obj(path: str, x: np.ndarray, y: np.ndarray, z: np.ndarray) -> None:
    """Export torus mesh as OBJ triangle surface.

    Uses periodic wrap in both parametric directions.
    """
    out = Path(path)
    out.parent.mkdir(parents=True, exist_ok=True)

    nv, nu = x.shape
    verts = np.column_stack([x.ravel(), y.ravel(), z.ravel()])

    def vid(i: int, j: int) -> int:
        return i * nu + j + 1  # OBJ is 1-indexed

    with out.open("w", encoding="utf-8") as f:
        f.write("# torus-cycle-renderer mesh export\n")
        for vx, vy, vz in verts:
            f.write(f"v {vx:.9f} {vy:.9f} {vz:.9f}\n")

        for i in range(nv):
            i2 = (i + 1) % nv
            for j in range(nu):
                j2 = (j + 1) % nu
                a = vid(i, j)
                b = vid(i, j2)
                c = vid(i2, j2)
                d = vid(i2, j)
                f.write(f"f {a} {b} {c}\n")
                f.write(f"f {a} {c} {d}\n")


def export_loop_obj(path: str, lx: np.ndarray, ly: np.ndarray, lz: np.ndarray) -> None:
    out = Path(path)
    out.parent.mkdir(parents=True, exist_ok=True)

    with out.open("w", encoding="utf-8") as f:
        f.write("# torus-cycle-renderer loop export\n")
        for vx, vy, vz in zip(lx, ly, lz):
            f.write(f"v {vx:.9f} {vy:.9f} {vz:.9f}\n")
        idx = " ".join(str(i + 1) for i in range(len(lx)))
        f.write(f"l {idx}\n")
