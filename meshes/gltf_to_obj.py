import glob
from pathlib import Path

import trimesh

script_dir = Path(__file__).resolve().parent
gltf_dir = script_dir / "gltf"
obj_dir = script_dir / "obj"

for gltf_path in glob.glob(str(gltf_dir / "*.gltf")):
    mesh = trimesh.load(gltf_path, force="mesh")
    obj_path = obj_dir / Path(gltf_path).name.replace(".gltf", ".obj")
    mesh.export(obj_path)
    print(f"Converted {gltf_path} -> {obj_path}")
