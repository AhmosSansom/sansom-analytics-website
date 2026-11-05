
from pathlib import Path
from PIL import Image, ImageOps

assets = Path(__file__).resolve().parent / "assets"

images = [
    "trading-floor.png",
    "wind-farm.jpg",
    "solar-farm.jpg",
]

for filename in images:
    source = assets / filename
    destination = source.with_suffix(".webp")

    if not source.exists():
        print(f"Not found: {source}")
        continue

    with Image.open(source) as img:
        img = ImageOps.exif_transpose(img)
        img = img.convert("RGB")

        # Maximum width of 1000 pixels
        if img.width > 1000:
            new_height = round(img.height * 1000 / img.width)
            img = img.resize(
                (1000, new_height),
                Image.Resampling.LANCZOS
            )

        img.save(
            destination,
            "WEBP",
            quality=82,
            method=6
        )

    original_kb = source.stat().st_size / 1024
    optimised_kb = destination.stat().st_size / 1024

    print(
        f"{filename}: {original_kb:.0f} KB "
        f"-> {optimised_kb:.0f} KB"
    )
