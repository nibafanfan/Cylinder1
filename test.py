import numpy as np
annotated_data = np.fromfile('/root/Cylinder3D/savefolder/000002.label', dtype=np.uint32).reshape((-1, 1))
annotated_data = annotated_data & 0xFFFF  # delete high 16 digits binary
annotated_data2 = np.fromfile('/root/Cylinder3D/rellisdata/sequences/04/labels/000002.label', dtype=np.uint32).reshape((-1, 1))
annotated_data2 = annotated_data2 & 0xFFFF
# annotated_data = np.vectorize(self.learning_map.__getitem__)(annotated_data)
print(annotated_data.shape)
print(annotated_data2.shape)
print(np.unique(annotated_data, return_counts=True))
print(np.unique(annotated_data2, return_counts=True))
