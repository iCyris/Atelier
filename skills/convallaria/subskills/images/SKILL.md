---
name: images
description: "Image optimization workflow for bitmap compression, conversion, responsive variants, metadata stripping, image manifests, and delivery-ready image assets."
---

# Image Optimization Workflow

Use when: bitmap assets need compression, conversion, responsive variants, metadata stripping, or delivery manifests.
Needs: source image files and any requested formats, size limits, quality targets, or transparency requirements.
Produces: optimized image files plus `image-manifest.json` with dimensions, formats, byte sizes, and savings.
Done when: outputs match real usage, source quality is preserved, and user-facing delivery reports before and after sizes.

Use this reference for bitmap compression, conversion, responsive image generation, metadata removal, and asset delivery manifests.

## Process

1. Inspect source dimensions, format, color mode, transparency, and file size.
2. Choose output formats:
   - PNG for transparency, pixel art, diagrams, or screenshots requiring lossless edges.
   - JPEG for photographs without transparency.
   - WebP for broad modern web delivery.
   - AVIF when the runtime supports it and the user wants maximum compression.
3. Generate size variants only when they map to real usage.
4. Strip metadata unless the user asks to preserve it.
5. Write an image manifest with original size, output size, dimensions, format, quality, and savings.

## Script

Use:

```bash
python3 subskills/images/scripts/optimize_images.py input-a.png input-b.jpg --out images --formats webp jpeg --max-width 1600 --quality 82
```

The script requires Pillow. If Pillow is unavailable, report that dependency and keep the source files unchanged.

## Quality Criteria

- Do not upscale raster images unless explicitly requested.
- Preserve transparency for logos, marks, UI stickers, and cutouts.
- Avoid converting crisp UI screenshots to low-quality JPEG.
- Use descriptive names: `hero-1600.webp`, `logo-mark-512.png`, `avatar-1024.webp`.
- For user-facing delivery, include before/after byte sizes and percent savings.
