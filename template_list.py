#====================== BEGIN GPL LICENSE BLOCK ======================
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
#======================= END GPL LICENSE BLOCK ========================

import os

from . import utils


def get_template_list():
    """ Searches for template types, and returns a list.
    """
    rigs = []
    MODULE_DIR = os.path.dirname(__file__)
    TTE_DIR_ABS = os.path.join(MODULE_DIR, utils.TEMPLATE_DIR)
    # SEARCH_DIR_ABS = os.path.join(TTE_DIR_ABS, path)
    files = os.listdir(TTE_DIR_ABS)
    files.sort()

    files = [f for f in files if f.endswith(".py")]
    # for f in files:
    #     is_dir = os.path.isdir(os.path.join(SEARCH_DIR_ABS, f))  # Whether the file is a directory

    #     # Stop cases
    #     if f[0] in [".", "_"]:
    #         continue
    #     if f.count(".") >= 2 or (is_dir and "." in f):
    #         print("Warning: %r, filename contains a '.', skipping" % os.path.join(SEARCH_DIR_ABS, f))
    #         continue

    #     if is_dir:
    #         # Check directories
    #         module_name = os.path.join(path, f).replace(os.sep, ".")
    #         rig = utils.get_rig_type(module_name)
    #         # Check if it's a rig itself
    #         if hasattr(rig, "Rig"):
    #             rigs += [f]
    #         else:
    #             # Check for sub-rigs
    #             ls = get_rig_list(os.path.join(path, f, ""))  # "" adds a final slash
    #             rigs.extend(["%s.%s" % (f, l) for l in ls])
    #     elif f.endswith(".py"):
    #         # Check straight-up python files
    #         t = f[:-3]
    #         module_name = os.path.join(path, t).replace(os.sep, ".")
    #         rig = utils.get_rig_type(module_name)
    #         if hasattr(rig, "Rig"):
    #             rigs += [t]
    # rigs.sort()
    return files


# def get_collection_list(rig_list):
#     collection_list = []
#     for r in rig_list:
#         a = r.split(".")
#         if len(a) >= 2 and a[0] not in collection_list:
#             collection_list += [a[0]]
#     return collection_list

def fill_ui_template_list(obj):
    """Fill rig's UI template list
    """
    armature_id_store = obj.data
    for i in range(0, len(armature_id_store.rigify_templates)):
        armature_id_store.rigify_templates.remove(0)

    for t in template_list:
        a = armature_id_store.rigify_templates.add()
        a.name = t[:-3]

# Public variables
template_list = get_template_list()
#collection_list = get_collection_list(rig_list)
#col_enum_list = [("All", "All", ""), ("None", "None", "")] + [(c, c, "") for c in collection_list]
