# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####


#SKLT export plugin for Blender - very experimental!
#Supports merging multiple objects into single SKLT file
#Does NOT convert complex polygons into triangles/tetragons - do this yourself in Blender
#May change polygon order - texture definitions should be checked if editing existing files!
##Changelog at the end of this file

import bpy
import struct




def writeSklt(filepath, polygon_mode, sen2_mode):
    
    current_scene = bpy.context.scene
    
    #write selected objects only (NOTE: Change this?)
    #objs_list = bpy.context.selected_objects
    ##changed
    objs_list = bpy.context.scene.objects
    
    sklt_vertices = []
    sklt_primitives = []
    sen2_vertices = []
    #Check objects
    for obj in objs_list:
        
        #world transformation matrix - this is used to find the coordinates relative to global origin (0,0,0) - object origin can be elsewhere
        tmatrix = obj.matrix_world.copy()
        
        #skip lamps, cameras etc.
        if obj.type in ("LAMP", "CAMERA", "SPEAKER"):
            continue
        
        #non-mesh things
        elif obj.type != "MESH":
            continue    #TODO: do something?
        
        #Handle existing SEN2 RIGHT HERE then skip rest of the loop
        #TODO: add autogeneration
        elif obj.name == "SEN2_BOX":
            #mode check - putting it here ensures that SEN2 box is not handled as an ordinary mesh
            if sen2_mode != "s":
                continue
            else:
                sen2_mesh = obj.data
            #duplicate object check - TODO
            if sen2_vertices:
                pass    #warn, continue, replace...?
            
            for v in sen2_mesh.vertices:
                tv = tuple(tmatrix*v.co)
                #duplicate vertex check - TODO
                if tv in sen2_vertices:
                    pass
                sen2_vertices.append(tv)
            
            #vertex count check - TODO
            if len(sen2_vertices) != 8:
                pass
            continue
        #Skip rest of the loop
        ############################
        
        #meshes
        else:
            sklt_mesh = obj.data
        
        #pick vertices
        #removes duplicates automatically TODO: is it always beneficial to do it?
        #do coordinate transformation!
        for v in sklt_mesh.vertices:
            tv = tuple(tmatrix*v.co)
            if tv not in sklt_vertices:
                sklt_vertices.append(tv)
                
        
        #polygon mode
        if polygon_mode == "p":
            for p in sklt_mesh.polygons:
                new_polygon = []
                for v in p.vertices:
                    #NOTE: p = index of vertex in current mesh vertex list - find the index in global vertex list
                    #NOTE: Do coordinate transformation here as well!
                    new_polygon.append(sklt_vertices.index(tuple(tmatrix*sklt_mesh.vertices[v].co)))
                sklt_primitives.append(tuple(new_polygon))
        #edge mode
        elif polygon_mode == "e":
            for e in sklt_mesh.edges:
                #all edges should have 2 vertices so no need to loop over e.vertices ##TODO: looping = cleaner code?
                sklt_primitives.append( (sklt_vertices.index(tuple(tmatrix*sklt_mesh.vertices[e.vertices[0]].co)), sklt_vertices.index(tuple(tmatrix*sklt_mesh.vertices[e.vertices[1]].co))) )
        
    
    
    #SEN2 autogenerator
    #Find vertices with biggest/smallest coordinates, then generate a box around the model
    if sen2_mode == "a":
        sen2_min_x, sen2_max_x, sen2_min_y, sen2_max_y, sen2_min_z, sen2_max_z = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
        for v in sklt_vertices:
            if v[0] < sen2_min_x:
                sen2_min_x = v[0]
            elif v[0] > sen2_max_x:
                sen2_max_x = v[0]
            if v[1] < sen2_min_y:
                sen2_min_y = v[1]
            elif v[1] > sen2_max_y:
                sen2_max_y = v[1]
            if v[2] < sen2_min_z:
                sen2_min_z = v[2]
            elif v[2] > sen2_max_z:
                sen2_max_z = v[2]
        #TODO! Vertex order?
        sen2_vertices.append((sen2_min_x, sen2_min_y, sen2_min_z))     
        sen2_vertices.append((sen2_min_x, sen2_min_y, sen2_max_z))
        sen2_vertices.append((sen2_min_x, sen2_max_y, sen2_min_z))
        sen2_vertices.append((sen2_min_x, sen2_max_y, sen2_max_z))
        sen2_vertices.append((sen2_max_x, sen2_min_y, sen2_min_z))
        sen2_vertices.append((sen2_max_x, sen2_min_y, sen2_max_z))
        sen2_vertices.append((sen2_max_x, sen2_max_y, sen2_min_z))
        sen2_vertices.append((sen2_max_x, sen2_max_y, sen2_max_z))
        
    
    #calculate lengths
    #POO2 (vertices) section
    len_poo2 = 3*4*len(sklt_vertices)
    
    #POL2 (primitives) section
    len_pol2 = 0
    for p in sklt_primitives:
        len_pol2 += 2 + 2*len(p)    #length of "command" + length of each definition (=number of vertices)
    if sklt_primitives:
        len_pol2 += 4                #length of polygon number indicator
    
    #SEN2 section    #NOTE: Check SEN2 handling mode when processing SEN2 data - check not done here! Leave sen2_vertices list empty if no SEN2 to be created!
    len_sen2 = 3*4*len(sen2_vertices)
    
    len_total = 4                        #SKLT identifier
    if sklt_vertices:
        len_total += 4+4+len_poo2    #POO2 + length + data
    if sklt_primitives:
        len_total += 4+4+len_pol2    #POL2 + length + data
    if sen2_vertices:
        len_total += 4+4+len_sen2    #SEN2 + length + data
    
    #start writing file
    skltfile = open(filepath, "wb")
    
    #Header
    skltfile.write(b"FORM")
    skltfile.write(struct.pack(">I", len_total))
    skltfile.write(b"SKLT")
    
    #Vertices
    if sklt_vertices:
        skltfile.write(b"POO2")
        skltfile.write(struct.pack(">I", len_poo2))
        for v in sklt_vertices:
            skltfile.write(struct.pack(">fff", v[0], v[1], v[2]))
    
    #SEN2
    if sen2_vertices:
        skltfile.write(b"SEN2")
        skltfile.write(struct.pack(">I", len_sen2))
        for v in sen2_vertices:
            skltfile.write(struct.pack(">fff", v[0], v[1], v[2]))
    
    #primitives
    if sklt_primitives:
        skltfile.write(b"POL2")
        skltfile.write(struct.pack(">I", len_pol2))                    #length
        skltfile.write(struct.pack(">I", len(sklt_primitives)))        #number of polygons!
        for p in sklt_primitives:
            skltfile.write(struct.pack(">H", len(p)))
            for n in p:
                skltfile.write(struct.pack(">H", n))
    
    skltfile.close()
    
    
#30.8.2013: Added polygon/edge mode
##Added basic SEN2 handling