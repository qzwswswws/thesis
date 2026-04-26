from __future__ import annotations

from pathlib import Path

import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage


THESIS_ROOT = Path(__file__).resolve().parents[2]
FIG_DIR = THESIS_ROOT / "01_Thesis_LaTeX" / "figures"
CURRENT_FIG = FIG_DIR / "C3-6_Alpha_Validation_20260408.png"
LEGACY_FIG = FIG_DIR / "_backup_before_remote_replacement_20260424" / "C3-6_Alpha_Validation_20260408.png"

# These boxes cover only the colored plotting regions, so the legacy overlay
# adds the old curve without reintroducing labels, axes, or titles.
CURRENT_PANELS = (
    (177, 225, 3180, 1093),
    (177, 1252, 3180, 2120),
)
LEGACY_PANELS = (
    (248, 93, 2073, 671),
    (248, 779, 2073, 1356),
)

LINE_RGB = (148, 148, 148)
MAX_ALPHA = 82


def extract_widest_component(mask: np.ndarray, min_width_ratio: float = 0.7) -> np.ndarray:
    labels, count = ndimage.label(mask)
    if count == 0:
        raise RuntimeError("No connected component found in legacy crop.")

    best_label = None
    best_score = -1
    min_width = int(mask.shape[1] * min_width_ratio)

    for label_id, sl in enumerate(ndimage.find_objects(labels), start=1):
        if sl is None:
            continue
        ys, xs = sl
        width = xs.stop - xs.start
        height = ys.stop - ys.start
        if width < min_width:
            continue

        component = labels[sl] == label_id
        area = int(component.sum())
        score = width * 1000 + area - height
        if score > best_score:
            best_score = score
            best_label = label_id

    if best_label is None:
        raise RuntimeError("Failed to isolate the legacy alpha curve.")

    return labels == best_label


def build_overlay(legacy_rgb: Image.Image, box: tuple[int, int, int, int]) -> Image.Image:
    crop = np.array(legacy_rgb.crop(box), dtype=np.uint8)
    gray = crop.mean(axis=2)

    dark_mask = gray < 120
    dark_mask = ndimage.binary_closing(dark_mask, structure=np.ones((3, 3), dtype=bool))
    component_mask = extract_widest_component(dark_mask)

    darkness = np.clip(200.0 - gray, 0.0, 200.0) / 200.0
    alpha = np.zeros(gray.shape, dtype=np.uint8)
    alpha_values = np.clip(darkness * MAX_ALPHA, 18, MAX_ALPHA).astype(np.uint8)
    alpha[component_mask] = alpha_values[component_mask]

    rgba = np.zeros((crop.shape[0], crop.shape[1], 4), dtype=np.uint8)
    rgba[..., 0] = LINE_RGB[0]
    rgba[..., 1] = LINE_RGB[1]
    rgba[..., 2] = LINE_RGB[2]
    rgba[..., 3] = alpha
    return Image.fromarray(rgba, "RGBA").filter(ImageFilter.GaussianBlur(radius=0.55))


def main() -> None:
    current = Image.open(CURRENT_FIG).convert("RGBA")
    legacy = Image.open(LEGACY_FIG).convert("RGB")

    for current_box, legacy_box in zip(CURRENT_PANELS, LEGACY_PANELS):
        overlay = build_overlay(legacy, legacy_box)
        width = current_box[2] - current_box[0]
        height = current_box[3] - current_box[1]
        overlay = overlay.resize((width, height), Image.Resampling.LANCZOS)
        current.alpha_composite(overlay, dest=(current_box[0], current_box[1]))

    current.save(CURRENT_FIG)
    print(f"WROTE {CURRENT_FIG}")


if __name__ == "__main__":
    main()
