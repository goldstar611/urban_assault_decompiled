import os

from compile import Form, Poo2, Pol2, Olpl, Atts, Amsh, Otl2
from io_mesh_3ds.export_3ds import write_3ds


material_dict = {"AIR1TXT.ILBM": "AIR1TXT.png",
                 "BODEN5.ILBM": "BODEN5.png",
                 "FHUBI.ILBM": "FHUBI.png",
                 "HYPE.ILBM": "HYPE.png",
                 "BAGGER.ILBM": "BAGGER.png",
                 "CITY1.ILBM": "CITY1.png",
                 "FHYPE.ILBM": "FHYPE.png",
                 "MACHT.ILBM": "MACHT.png",
                 "BERUD.ILBM": "BERUD.png",
                 "FAERROBO.ILBM": "FAERROBO.png",
                 "FMACHT.ILBM": "FMACHT.png",
                 "MTL.ILBM": "MTL.png",
                 "BODEN1.ILBM": "BODEN1.png",
                 "FBAGGER.ILBM": "FBAGGER.png",
                 "FSCHROTT.ILBM": "FSCHROTT.png",
                 "ROBONEU.ILBM": "ROBONEU.png",
                 "BODEN2.ILBM": "BODEN2.png",
                 "FBERUD.ILBM": "FBERUD.png",
                 "FX1.ILBM": "FX1.png",
                 "SCHROTT.ILBM": "SCHROTT.png",
                 "BODEN3.ILBM": "BODEN3.png",
                 "FCITY1.ILBM": "FCITY1.png",
                 "FX2.ILBM": "FX2.png",
                 "SHRTTWND.ILBM": "SHRTTWND.png",
                 "BODEN4.ILBM": "BODEN4.png",
                 "FHRTTWND.ILBM": "FHRTTWND.png",
                 "HUBI.ILBM": "HUBI.png",
                 "TAERROBO.ILBM": "TAERROBO.png",
                 }


class FakeBlenderMesh:
    def __init__(self, ob_name, vertices, faces, uv_map, material):
        self.ob_name = ob_name
        self.tessface_uv_textures = uv_map
        self.material = material
        self.tessfaces = faces
        self.vertices = vertices


def make_fake_mesh(ob_name, vertices, faces, mesh: Amsh):

    if mesh.has_uv:
        material = mesh.get_single("NAM2").to_class().name
        olpl = mesh.get_single("OLPL").to_class()  # type: Olpl
        olpl.normalize()
        uv_map = olpl.points
    else:
        material = None
        uv_map = None

    atts = mesh.get_single("ATTS").to_class()  # type: Atts
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


def area_to_fake_mesh(ob_name, vertices, faces, area: Form):
    if area.get_single("OTL2"):

        # Material
        nam2 = area.get_single("NAM2")
        material = nam2.to_class().name

        # Poly
        ade = area.get_single("ADE ")  # type: Form
        poly = ade.get_single("STRC").to_class().poly
        faces = [faces[poly]]

        # UV Mapping
        otl2 = area.get_single("OTL2")  # type: Form
        otl2 = otl2.to_class()  # type: Otl2
        olpl = Olpl()
        olpl.points = [otl2.points]
        olpl.normalize()
        uv_map = olpl.points

        return FakeBlenderMesh(ob_name=ob_name,
                               vertices=vertices,
                               faces=faces,
                               uv_map=uv_map,
                               material=material)

    if area.get_single("BANI"):
        # Poly
        ade = area.get_single("ADE ")  # type: Form
        poly = ade.get_single("STRC").to_class().poly
        faces = [faces[poly]]

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

        sklt_file_name = model_form.get_single("SKLC").get_single("NAME").to_class().name[:-1]  # HACK

        sklt_form = Form().from_json_file("./assets/sets/{}/{}.json".format(set_number, sklt_file_name))
        poo2 = sklt_form.get_single("POO2").to_class()  # type: Poo2
        poo2.apply_scaling_factor(150)
        poo2.change_coordinate_system()
        vertices = poo2.points_as_vectors()

        if not sklt_form.get_single("POL2"):
            continue

        pol2 = sklt_form.get_single("POL2").to_class()  # type: Pol2
        faces = pol2.edges

        meshes = [make_fake_mesh(ob_name, vertices.copy(), faces.copy(), m.to_class()) for m in model_form.get_all("AMSH")]
        meshes += [area_to_fake_mesh(ob_name, vertices.copy(), faces.copy(), m.to_class()) for m in model_form.get_all("AREA")]  # TODO FIX HACK
        meshes = [m for m in meshes if m is not None]
        write_3ds("./output/{}.3ds".format(ob_name), meshes, material_dict)


if __name__ == '__main__':
    main()
