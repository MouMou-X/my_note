---
tags: [编程/ClaudeCode]
type: note
status: 🌿
---

# * **NotebookEdit**

Completely replaces the contents of a specific cell in a Jupyter notebook (.ipynb file) with new source. Jupyter notebooks are interactive documents that combine code, text, and visualizations, commonly used for data analysis and scientific computing. The notebook_path parameter must be an absolute path, not a relative path. The cell_number is 0-indexed. Use edit_mode=insert to add a new cell at the index specified by cell_number. Use edit_mode=delete to delete the cell at the index specified by cell_number.

Parameters:

notebook_path [string] (required) - The absolute path to the Jupyter notebook file to edit (must be absolute, not relative)

cell_id [string] - The ID of the cell to edit. When inserting a new cell, the new cell will be inserted after the cell with this ID, or at the beginning if not specified.

new_source [string] (required) - The new source for the cell

cell_type [string] - The type of the cell (code or markdown). If not specified, it defaults to the current cell type. If using edit_mode=insert, this is required.

edit_mode [string] - The type of edit to make (replace, insert, delete). Defaults to replace.
