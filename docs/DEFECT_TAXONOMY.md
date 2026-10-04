# Steel Defect Taxonomy

This project models common hot-rolled and cold-rolled surface defects including scratches, cracks, pitting, inclusions, scale, rolled-in scale, patches, and crazing. Labels should include bounding boxes, optional segmentation masks, acquisition metadata, line speed, illumination setting, steel grade, and severity.

## Annotation policy
- Preserve ambiguous examples with an `uncertain` flag.
- Record defect size in pixels and physical units when calibration is available.
- Split data by coil/batch to avoid leakage.
- Maintain an expert-reviewed holdout set for final reporting.
