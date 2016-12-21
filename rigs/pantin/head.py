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

import bpy

from ...utils import copy_bone
from ...utils import make_deformer_name, strip_org
from ...utils import create_bone_widget, create_widget, create_cube_widget
from ...utils import connected_children_names, has_connected_children

from . import pantin_utils


class Rig:
    def __init__(self, obj, bone_name, params):
        self.obj = obj
        self.params = params

        self.neck = bone_name
        self.head = connected_children_names(self.obj, bone_name)[0]
        # sort jaw and eyelid based on their height. ok, that's dirty
        head_children = list(self.obj.pose.bones[self.head].children)
        # remove bones which have a type, hence do not belong
        head_children = [c for c in head_children if not c['rigify_type']]
        head_children = sorted(head_children, key=lambda b: b.tail.z)

        self.jaw = head_children[0].name
        self.eyelid = head_children[1].name

        self.org_bones = [self.neck, self.head, self.jaw, self.eyelid]

    def generate(self):
        bpy.ops.object.mode_set(mode='EDIT')

        ctrl_chain = []

        eb = self.obj.data.edit_bones
        for i, b in enumerate(self.org_bones):
            # Control bones
            ctrl_bone = copy_bone(self.obj, b)
            ctrl_bone_e = eb[ctrl_bone]

            # Name
            ctrl_bone_e.name = strip_org(b)

            # Parenting
            if i == 0:
                # First bone: neck
                if eb[b].parent is not None:
                    bone_parent_name = strip_org(eb[b].parent.name)
                    ctrl_bone_e.parent = eb[bone_parent_name]
            elif i >= len(self.org_bones)-1:
                # Parent jaw and eyelid to the head (1)
                ctrl_bone_e.parent = eb[ctrl_chain[1]]
            else:
                # The rest
                ctrl_bone_e.parent = eb[ctrl_chain[-1]]

            # Add to list
            ctrl_chain += [ctrl_bone_e.name]

            # Def bones
            def_bone = pantin_utils.create_deformation(
                self.obj,
                b,
                self.params.flip_switch,
                member_index=self.params.Z_index,
                bone_index=i)
            if b == self.eyelid:
                eyelid_def_bone = def_bone

        bpy.ops.object.mode_set(mode='OBJECT')
        pb = self.obj.pose.bones

        # Widgets
        global_scale = self.obj.dimensions[2]
        member_factor = 0.08
        widget_size = global_scale * member_factor

        neck = ctrl_chain[0]
        head = ctrl_chain[1]
        jaw = ctrl_chain[2]
        eyelid = ctrl_chain[3]

        pantin_utils.create_capsule_widget(
            self.obj, neck, width=widget_size, height=widget_size*0.1)
        pantin_utils.create_aligned_circle_widget(
            self.obj, head, radius=widget_size, head_tail=0.5)
        pantin_utils.create_aligned_circle_widget(
            self.obj, jaw, radius=widget_size * 0.3, head_tail=0.5)

        # Constraints
        for org, ctrl in zip(self.org_bones, ctrl_chain):
            con = pb[org].constraints.new('COPY_TRANSFORMS')
            con.name = "copy_transforms"
            con.target = self.obj
            con.subtarget = ctrl

        con = pb[neck].constraints.new('LIMIT_ROTATION')
        con.name = "limit_rotation"
        con.use_limit_z = True
        con.min_z = -1.14
        con.max_z = 1.5
        con.owner_space = 'LOCAL'

        con = pb[head].constraints.new('LIMIT_ROTATION')
        con.name = "limit_rotation"
        con.use_limit_z = True
        con.min_z = -0.5
        con.max_z = 0.68
        con.owner_space = 'LOCAL'

        # con = pb[jaw].constraints.new('LIMIT_ROTATION')
        # con.name = "limit_rotation"
        # con.use_limit_z = True
        # con.min_z = 0.0
        # con.max_z = 0.39
        # con.owner_space = 'LOCAL'

        con = pb[eyelid].constraints.new('LIMIT_ROTATION')
        con.name = "limit_rotation"
        con.use_limit_z = True
        con.min_z = -0.39
        con.max_z = 0.0
        con.owner_space = 'LOCAL'

        # Driver for hiding the eyelid behind the head, using the extra_offset
        # When the eyelid is open (rotation < 0.25...),
        # the def bone goes behind the head
        driver = self.obj.animation_data.drivers.find(
            'pose.bones["DEF-Paupiere"].location', index=2)
        driver.driver.expression = ('z_index_same(member_index, '
                                    'flip, bone_index, -2 * '
                                    '(eyelid_offset < -0.25))')
        var = driver.driver.variables.new()

        var.type = 'SINGLE_PROP'
        var.name = 'eyelid_offset'
        var.type = 'TRANSFORMS'
        # var.targets[0].id_type = 'OBJECT'
        var.targets[0].id = self.obj
        var.targets[0].bone_target = eyelid
        var.targets[0].transform_type = 'ROT_Z'
        var.targets[0].transform_space = 'TRANSFORM_SPACE'
        # var.targets[0].data_path = 'pose.bones["{}"]'.format(eyelid)


def add_parameters(params):
    params.Z_index = bpy.props.FloatProperty(
        name="Z index", default=0.0, description="Defines member's Z order")
    params.flip_switch = bpy.props.BoolProperty(
        name="Flip Switch", default=False,
        description="This member may change depth when flipped")


def parameters_ui(layout, params):
    """ Create the ui for the rig parameters.
    """
    r = layout.row()
    r.prop(params, "Z_index")
    r = layout.row()
    r.prop(params, "flip_switch")


def create_sample(obj):
    # generated by rigify.utils.write_metarig
    bpy.ops.object.mode_set(mode='EDIT')
    arm = obj.data

    bones = {}

    bone = arm.edit_bones.new('Cou')
    bone.head[:] = 0.0005, 0.0000, 1.4038
    bone.tail[:] = 0.0271, 0.0000, 1.4720
    bone.roll = -2.7688
    bone.use_connect = False
    bones['Cou'] = bone.name
    bone = arm.edit_bones.new('Tete')
    bone.head[:] = 0.0271, 0.0000, 1.4720
    bone.tail[:] = 0.0592, 0.0000, 1.6173
    bone.roll = -2.9241
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['Cou']]
    bones['Tete'] = bone.name
    bone = arm.edit_bones.new('Machoire')
    bone.head[:] = 0.0223, 0.0000, 1.4938
    bone.tail[:] = 0.0964, 0.0000, 1.4450
    bone.roll = -0.9887
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['Tete']]
    bones['Machoire'] = bone.name
    bone = arm.edit_bones.new('Paupiere')
    bone.head[:] = 0.0713, -0.0000, 1.5667
    bone.tail[:] = 0.1014, 0.0000, 1.5618
    bone.roll = -1.4091
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['Tete']]
    bones['Paupiere'] = bone.name

    bpy.ops.object.mode_set(mode='OBJECT')
    pbone = obj.pose.bones[bones['Cou']]
    pbone.rigify_type = 'pantin.head'
    pbone.lock_location = (True, True, True)
    pbone.lock_rotation = (True, True, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (True, True, True)
    pbone.rotation_mode = 'XZY'
    try:
        pbone.rigify_parameters.Z_index = 0.0
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.flip_switch = False
    except AttributeError:
        pass
    pbone = obj.pose.bones[bones['Tete']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, True)
    pbone.lock_rotation = (True, True, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (True, True, True)
    pbone.rotation_mode = 'XZY'
    pbone = obj.pose.bones[bones['Machoire']]
    pbone.rigify_type = ''
    pbone.lock_location = (True, True, True)
    pbone.lock_rotation = (True, True, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (True, True, True)
    pbone.rotation_mode = 'XZY'
    pbone = obj.pose.bones[bones['Paupiere']]
    pbone.rigify_type = ''
    pbone.lock_location = (True, True, True)
    pbone.lock_rotation = (True, True, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'XZY'

    bpy.ops.object.mode_set(mode='EDIT')
    for bone in arm.edit_bones:
        bone.select = False
        bone.select_head = False
        bone.select_tail = False
    for b in bones:
        bone = arm.edit_bones[bones[b]]
        bone.select = True
        bone.select_head = True
        bone.select_tail = True
        arm.edit_bones.active = bone
