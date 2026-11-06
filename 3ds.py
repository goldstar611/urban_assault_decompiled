import os

from compile import Ades, Area, Form, Poo2, Pol2, Olpl, Atts, Amsh, Nam2, Otl2, Sklc
from io_mesh_3ds.export_3ds import write_3ds


class FakeBlenderMesh:
    def __init__(self, ob_name, vertices, faces, uv_map, material):
        self.ob_name = ob_name
        self.tessface_uv_textures = uv_map
        self.material = material
        self.tessfaces = faces
        self.vertices = vertices


def make_fake_mesh(ob_name, vertices, faces, mesh: Amsh):
    vertices = vertices.copy()
    faces = faces.copy()

    if mesh.has_uv:
        nam2: Nam2 = mesh.get_single("NAM2")
        material = nam2.name
        olpl: Olpl = mesh.get_single("OLPL")
        olpl.normalize()
        uv_map = olpl.points
    else:
        material = None
        uv_map = None

    atts: Atts = mesh.get_single("ATTS")
    pop_faces = [i for i in range(len(faces)) if i not in [x["poly_id"] for x in atts.atts_entries]]
    pop_faces.sort(reverse=True)
    for idx in pop_faces:
        faces.pop(idx)  # Pop face if no UV texture assigned

    return FakeBlenderMesh(ob_name=ob_name,
                           vertices=vertices,
                           faces=faces,
                           uv_map=uv_map,
                           material=material
                           )


def area_to_fake_mesh(ob_name, vertices, faces, area: Area):
    vertices = vertices.copy()
    faces = faces.copy()

    if area.outline:
        material = area.bitmap_name
        faces = [faces[area.polygon_index]]

        # UV Mapping
        olpl = Olpl()
        olpl.points = [area.outline.points]
        olpl.normalize()
        uv_map = olpl.points

        return FakeBlenderMesh(ob_name=ob_name,
                               vertices=vertices,
                               faces=faces,
                               uv_map=uv_map,
                               material=material)

    if area.is_animated:
        faces = [faces[area.polygon_index]]

        return FakeBlenderMesh(ob_name=ob_name,
                               vertices=vertices,
                               faces=faces,
                               uv_map=None,
                               material=None)
    return None


def main():
    import glob
    set_number = "set1"
    for file_name in glob.glob("assets/sets/{}/objects/buildings/*.bas.json".format(set_number)) + \
                     glob.glob("assets/sets/{}/objects/vehicles/*.bas.json".format(set_number)):
        print(file_name)

        model_form = Form().from_json_file(file_name)
        ob_name = os.path.basename(file_name).replace(".bas", "").replace(".json", "")

        sklc: Sklc = model_form.get_single("SKLC")
        sklt_file_name = sklc.skeleton_name[:-1]  # HACK: .sklt resource maps to a .skl.json file

        sklt_form = Form().from_json_file("./assets/sets/{}/{}.json".format(set_number, sklt_file_name))
        poo2: Poo2 = sklt_form.get_single("POO2")
        poo2.scale_down(150)
        poo2.change_coordinate_system()
        vertices = poo2.points_as_vectors()

        if not sklt_form.get_single("POL2"):
            print("Skipping {} because it has no polygons.".format(file_name))
            continue

        pol2: Pol2 = sklt_form.get_single("POL2")
        faces = pol2.edges

        material_dict = {}
        meshes = []
        ades: Ades = model_form.get_single("ADES")
        for objt in ades.objects:
            class_id = objt.get_single("CLID").class_id

            if class_id == "amesh.class":
                mesh = make_fake_mesh(ob_name, vertices, faces, objt.get_single("AMSH"))
                if mesh:
                    meshes.append(mesh)
                if mesh and mesh.material:
                    material_dict[mesh.material] = os.path.splitext(mesh.material)[0] + ".png"
                continue

            if class_id == "area.class":
                mesh = area_to_fake_mesh(ob_name, vertices, faces, objt.get_single("AREA"))
                if mesh:
                    meshes.append(mesh)
                if mesh and mesh.material:
                    material_dict[mesh.material] = os.path.splitext(mesh.material)[0] + ".png"
                continue

            if class_id == "particle.class":
                # print("skipping {} in {}".format(class_id, file_name))
                continue

            raise ValueError(class_id)

        write_3ds("./output/{}.3ds".format(ob_name), meshes, material_dict)
    print("Finished")


if __name__ == '__main__':
    main()
