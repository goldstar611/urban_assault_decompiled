# Static Code Review Report

**File name:** `io_mesh_sklt/export_sklt.py`
**Brief summary:** This script is a Blender add-on function designed to export selected or all mesh objects into the custom SKLT format, supporting polygon and edge primitive definitions, as well as generating an encompassing SEN2 bounding box.

---

### Strengths
*   The code clearly delineates modes for different primitive types (polygon 'p', edge 'e') and SEN2 generation ('a').
*   It correctly uses `bpy.context.scene.objects` to iterate over objects, though the original code had a commented-out selection mode.
*   Basic structure for binary file writing using Python's `struct` module is present.

### Defects
*   **TODO/Unresolved Logic:** Multiple instances of `#TODO` comments indicate incomplete logic paths (e.g., vertex duplication checks, polygon mode vertex re-indexing).
*   **Transformation Inconsistencies:** Coordinate transformations are handled inconsistently. For polygons, the vertex indexing relies on `sklt_vertices.index(tuple(tmatrix*sklt_mesh.vertices[v].co)))` (Line 104), which is slow ($O(N)$ lookup inside loops) and relies on the vertex being exactly equal after transformation, which might not hold if floating-point errors differ slightly from how it was added to `sklt_vertices`.
*   **SEN2 Vertex Representation:** The generated SEN2 vertices use a dictionary format for storage within the loop (Lines 132-139) which is inconsistent with how other vertices are stored as tuples of coordinates. The final writing logic (Lines 183-184) expects tuples `(v[0], v[1], v[2])`.

### Possible Bugs
*   **Indexing Error in Polygons (High):** On Line 104, `sklt_vertices.index(...)` searches the entire accumulated list for a transformed vertex coordinate. If floating-point arithmetic causes the exact tuple representation to differ slightly between when the vertex was added (Line 93) and when it is looked up for an index, this lookup will fail silently (if the vertex was somehow added again) or produce incorrect indices.
*   **SEN2 Writing Error (Medium):** The SEN2 vertices are appended as dictionaries (`sen2_vertices.append({"x": ..., "y": ...})` on Lines 132-139), but the writing loop (Lines 180-184) expects them to be iterated as if they were tuples, leading to a `TypeError` during packing (`struct.pack(">fff", v[0], v[1], v[2])`).
*   **Vertex Transformation (Medium):** In polygon mode (Line 103), the coordinate transformation is mentioned but not explicitly applied to determine the index, relying solely on the transformed coordinates matching an already added vertex. This is coupled with the performance issue above.

### Performance Improvements
*   **Vertex Lookup (High):** The repeated use of `sklt_vertices.index(...)` inside polygon and edge loops (Lines 104, 110) is highly inefficient ($O(N^2)$ complexity overall for primitive generation). A dictionary mapping transformed coordinates (as tuples) to their indices should be used for $O(1)$ lookup.
*   **Duplicate Checking (Medium):** While checking `if tv not in sklt_vertices` works, using a set for tracking added vertices alongside the list would provide $O(1)$ average time complexity for insertion and lookup, improving performance.

### Memory Improvements
*   No critical memory leaks are apparent given the object scope, but optimization of data structures (using sets/dicts instead of list lookups) also improves time complexity, which is generally more critical than immediate memory usage here.

### Blender API Issues
*   **Object Iteration Scope (Medium):** Line 39 uses `bpy.context.scene.objects`, which includes *all* objects in the scene. The original code hinted at using `bpy.context.selected_objects` (Line 37). Using all objects without filtering can lead to massive exports containing irrelevant data, which is a usage/design error rather than an API misuse, but it's important context.

### Maintainability Improvements
*   **Magic Numbers/Constants:** The magic number `3*4` used in calculating lengths (Lines 144, 154) should be defined as a constant for clarity.
*   **Code Clarity:** The block comment `#Handle existing SEN2 RIGHT HERE then skip rest of the loop` (Line 58) suggests complex conditional logic that could benefit from better structure or extraction into helper functions.

### Suggested fixes
*   **Refactor Vertex Mapping (High):** Implement a dictionary mapping transformed vertex coordinates to their SKLT indices immediately after adding them to `sklt_vertices` (e.g., `coord_to_index = {tv: i for i, tv in enumerate(sklt_vertices)}`). Use this map instead of `list.index()`.
*   **Fix SEN2 Data Structure (High):** Ensure the SEN2 vertices added in Line 132-139 are stored as tuples `(x, y, z)` matching the format expected in Line 183.
*   **Implement Pruning/Filtering (Medium):** Decide on and implement the logic for line 56's `TODO`: what to do with non-mesh objects that aren't ignored?
