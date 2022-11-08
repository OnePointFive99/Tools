import pymeshlab as ml
from pathlib import Path
from rich.progress import track

root = Path('modelPath')
new_root = Path('savePath')
target_faces = 1024 #simplify mesh faces to this number
shape_list = sorted(list(root.glob('*/*/*/*.obj')))

ms = ml.MeshSet()

for shape_dir in track(shape_list):
    out_dir = new_root / shape_dir.relative_to(root).with_suffix('.obj')

    out_dir.parent.mkdir(parents=True, exist_ok=True)

    ms.clear()
    # load mesh
    ms.load_new_mesh(str(shape_dir))
    mesh = ms.current_mesh()
    print('input mesh has', mesh.vertex_number(), 'vertex and', mesh.face_number(), 'faces')
    if mesh.face_number() > target_faces:
    #simplify Mesh to 500 faces
        ms.apply_filter('simplification_quadric_edge_collapse_decimation', targetfacenum=target_faces, preservenormal=True)
        mesh = ms.current_mesh()
        print('Simplified mesh has', mesh.vertex_number(), 'vertex and', mesh.face_number(), 'faces')
    ms.save_current_mesh(str(out_dir))
