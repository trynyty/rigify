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


def create(obj):
    # generated by rigify.utils.write_metarig
    bpy.ops.object.mode_set(mode='EDIT')
    arm = obj.data

    for i in range(28):
        arm.rigify_layers.add()

    arm.rigify_layers[0].name = "Tete"
    arm.rigify_layers[0].row = 1
    arm.rigify_layers[1].name = " "
    arm.rigify_layers[1].row = 1
    arm.rigify_layers[2].name = "Torse"
    arm.rigify_layers[2].row = 2
    arm.rigify_layers[3].name = " "
    arm.rigify_layers[3].row = 1
    arm.rigify_layers[4].name = "Bras Gauche"
    arm.rigify_layers[4].row = 3
    arm.rigify_layers[5].name = ""
    arm.rigify_layers[5].row = 1
    arm.rigify_layers[6].name = "Jambe Gauche"
    arm.rigify_layers[6].row = 4
    arm.rigify_layers[7].name = " "
    arm.rigify_layers[7].row = 1
    arm.rigify_layers[8].name = "Torse"
    arm.rigify_layers[8].row = 5
    arm.rigify_layers[9].name = " "
    arm.rigify_layers[9].row = 1
    arm.rigify_layers[10].name = " "
    arm.rigify_layers[10].row = 1
    arm.rigify_layers[11].name = " "
    arm.rigify_layers[11].row = 1
    arm.rigify_layers[12].name = " "
    arm.rigify_layers[12].row = 1
    arm.rigify_layers[13].name = " "
    arm.rigify_layers[13].row = 1
    arm.rigify_layers[14].name = " "
    arm.rigify_layers[14].row = 1
    arm.rigify_layers[15].name = " "
    arm.rigify_layers[15].row = 1
    arm.rigify_layers[16].name = " "
    arm.rigify_layers[16].row = 1
    arm.rigify_layers[17].name = " "
    arm.rigify_layers[17].row = 1
    arm.rigify_layers[18].name = " "
    arm.rigify_layers[18].row = 1
    arm.rigify_layers[19].name = " "
    arm.rigify_layers[19].row = 1
    arm.rigify_layers[20].name = "Bras Droit"
    arm.rigify_layers[20].row = 3
    arm.rigify_layers[21].name = " "
    arm.rigify_layers[21].row = 1
    arm.rigify_layers[22].name = "Jambe Droite"
    arm.rigify_layers[22].row = 4
    arm.rigify_layers[23].name = " "
    arm.rigify_layers[23].row = 1
    arm.rigify_layers[24].name = " "
    arm.rigify_layers[24].row = 1
    arm.rigify_layers[25].name = " "
    arm.rigify_layers[25].row = 1
    arm.rigify_layers[26].name = " "
    arm.rigify_layers[26].row = 1
    arm.rigify_layers[27].name = " "
    arm.rigify_layers[27].row = 1

    bones = {}

    bone = arm.edit_bones.new('Bassin')
    bone.head[:] = 0.0094, -0.0000, 0.9156
    bone.tail[:] = 0.0112, -0.0000, 1.0197
    bone.roll = -3.1237
    bone.use_connect = False
    bones['Bassin'] = bone.name
    bone = arm.edit_bones.new('Abdomen')
    bone.head[:] = 0.0112, -0.0000, 1.0197
    bone.tail[:] = 0.0131, -0.0000, 1.1238
    bone.roll = -3.1237
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['Bassin']]
    bones['Abdomen'] = bone.name
    bone = arm.edit_bones.new('Jambe haut.L')
    bone.head[:] = 0.0431, 0.0000, 0.8865
    bone.tail[:] = 0.2010, -0.0000, 0.4891
    bone.roll = -0.3784
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['Bassin']]
    bones['Jambe haut.L'] = bone.name
    bone = arm.edit_bones.new('Jambe haut.R')
    bone.head[:] = -0.0157, 0.0000, 0.8890
    bone.tail[:] = -0.0266, -0.0000, 0.4693
    bone.roll = 0.0257
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['Bassin']]
    bones['Jambe haut.R'] = bone.name
    bone = arm.edit_bones.new('Thorax')
    bone.head[:] = 0.0131, -0.0000, 1.1238
    bone.tail[:] = 0.0215, -0.0000, 1.2723
    bone.roll = -3.0849
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['Abdomen']]
    bones['Thorax'] = bone.name
    bone = arm.edit_bones.new('Jambe bas.L')
    bone.head[:] = 0.2010, -0.0000, 0.4891
    bone.tail[:] = 0.1679, 0.0000, 0.0680
    bone.roll = 0.0785
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['Jambe haut.L']]
    bones['Jambe bas.L'] = bone.name
    bone = arm.edit_bones.new('Jambe bas.R')
    bone.head[:] = -0.0266, -0.0000, 0.4693
    bone.tail[:] = -0.0749, -0.0000, 0.0824
    bone.roll = 0.1245
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['Jambe haut.R']]
    bones['Jambe bas.R'] = bone.name
    bone = arm.edit_bones.new('Buste')
    bone.head[:] = 0.0215, -0.0000, 1.2723
    bone.tail[:] = 0.0314, -0.0000, 1.4488
    bone.roll = -3.0859
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['Thorax']]
    bones['Buste'] = bone.name
    bone = arm.edit_bones.new('Pied.L')
    bone.head[:] = 0.1679, 0.0000, 0.0680
    bone.tail[:] = 0.2555, 0.0000, 0.0195
    bone.roll = -1.0650
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['Jambe bas.L']]
    bones['Pied.L'] = bone.name
    bone = arm.edit_bones.new('Talon.L')
    bone.head[:] = 0.1679, 0.0000, 0.0680
    bone.tail[:] = 0.1099, 0.0000, -0.0022
    bone.roll = 0.6906
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['Jambe bas.L']]
    bones['Talon.L'] = bone.name
    bone = arm.edit_bones.new('Pied.R')
    bone.head[:] = -0.0749, -0.0000, 0.0824
    bone.tail[:] = 0.0219, -0.0000, 0.0243
    bone.roll = -1.0306
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['Jambe bas.R']]
    bones['Pied.R'] = bone.name
    bone = arm.edit_bones.new('Talon.R')
    bone.head[:] = -0.0749, -0.0000, 0.0824
    bone.tail[:] = -0.1430, -0.0000, 0.0051
    bone.roll = 0.7216
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['Jambe bas.R']]
    bones['Talon.R'] = bone.name
    bone = arm.edit_bones.new('Cou')
    bone.head[:] = 0.0314, -0.0000, 1.4488
    bone.tail[:] = 0.0703, -0.0000, 1.5159
    bone.roll = -2.6160
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['Buste']]
    bones['Cou'] = bone.name
    bone = arm.edit_bones.new('Bras haut.L')
    bone.head[:] = 0.0439, 0.0000, 1.3920
    bone.tail[:] = 0.0899, -0.0000, 1.1325
    bone.roll = -0.1751
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['Buste']]
    bones['Bras haut.L'] = bone.name
    bone = arm.edit_bones.new('Bras haut.R')
    bone.head[:] = -0.0277, -0.0000, 1.3996
    bone.tail[:] = -0.0432, -0.0000, 1.0917
    bone.roll = 0.0503
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['Buste']]
    bones['Bras haut.R'] = bone.name
    bone = arm.edit_bones.new('Orteil.L')
    bone.head[:] = 0.2555, 0.0000, 0.0195
    bone.tail[:] = 0.3079, -0.0000, 0.0044
    bone.roll = -1.2916
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['Pied.L']]
    bones['Orteil.L'] = bone.name
    bone = arm.edit_bones.new('Orteil.R')
    bone.head[:] = 0.0219, -0.0000, 0.0243
    bone.tail[:] = 0.0887, 0.0000, 0.0000
    bone.roll = -1.2210
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['Pied.R']]
    bones['Orteil.R'] = bone.name
    bone = arm.edit_bones.new('Tete')
    bone.head[:] = 0.0703, -0.0000, 1.5159
    bone.tail[:] = 0.1024, -0.0000, 1.6612
    bone.roll = -2.9242
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['Cou']]
    bones['Tete'] = bone.name
    bone = arm.edit_bones.new('Bras bas.L')
    bone.head[:] = 0.0899, -0.0000, 1.1325
    bone.tail[:] = 0.2565, -0.0000, 0.9915
    bone.roll = -0.8686
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['Bras haut.L']]
    bones['Bras bas.L'] = bone.name
    bone = arm.edit_bones.new('Bras bas.R')
    bone.head[:] = -0.0432, -0.0000, 1.0917
    bone.tail[:] = 0.1264, -0.0000, 0.9515
    bone.roll = -0.8798
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['Bras haut.R']]
    bones['Bras bas.R'] = bone.name
    bone = arm.edit_bones.new('Machoire')
    bone.head[:] = 0.0865, -0.0000, 1.5502
    bone.tail[:] = 0.1543, -0.0000, 1.4757
    bone.roll = -0.7383
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['Tete']]
    bones['Machoire'] = bone.name
    bone = arm.edit_bones.new('Paupiere')
    bone.head[:] = 0.1683, -0.0000, 1.5866
    bone.tail[:] = 0.1881, -0.0000, 1.5750
    bone.roll = -1.0436
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['Tete']]
    bones['Paupiere'] = bone.name
    bone = arm.edit_bones.new('Chapeau')
    bone.head[:] = 0.0841, -0.0000, 1.6888
    bone.tail[:] = 0.0841, -0.0000, 1.8177
    bone.roll = 3.1416
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['Tete']]
    bones['Chapeau'] = bone.name
    bone = arm.edit_bones.new('Main.L')
    bone.head[:] = 0.2565, -0.0000, 0.9915
    bone.tail[:] = 0.3366, -0.0000, 0.8363
    bone.roll = -0.4764
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['Bras bas.L']]
    bones['Main.L'] = bone.name
    bone = arm.edit_bones.new('Main.R')
    bone.head[:] = 0.1264, -0.0000, 0.9515
    bone.tail[:] = 0.1290, -0.0000, 0.7804
    bone.roll = -0.0148
    bone.use_connect = True
    bone.parent = arm.edit_bones[bones['Bras bas.R']]
    bones['Main.R'] = bone.name
    bone = arm.edit_bones.new('Accessoire')
    bone.head[:] = 0.3599, -0.0000, 0.9073
    bone.tail[:] = 0.6984, -0.0000, 1.0624
    bone.roll = -2.0004
    bone.use_connect = False
    bone.parent = arm.edit_bones[bones['Main.L']]
    bones['Accessoire'] = bone.name

    bpy.ops.object.mode_set(mode='OBJECT')
    pbone = obj.pose.bones[bones['Bassin']]
    pbone.rigify_type = 'pantin.torso'
    pbone.lock_location = (False, False, True)
    pbone.lock_rotation = (True, True, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (True, True, True)
    pbone.rotation_mode = 'XZY'
    pbone.bone.layers = [False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    try:
        pbone.rigify_parameters.Z_index = 1.0
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.mutable_order = False
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.root_name = "Racine"
    except AttributeError:
        pass
    pbone = obj.pose.bones[bones['Abdomen']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (True, True, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'XZY'
    pbone.bone.layers = [False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['Jambe haut.L']]
    pbone.rigify_type = 'pantin.leg'
    pbone.lock_location = (False, False, True)
    pbone.lock_rotation = (True, True, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'XZY'
    pbone.bone.layers = [False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    try:
        pbone.rigify_parameters.Z_index = 2.0
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.joint_name = "Genou"
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.right_layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False]
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.pelvis_name = "Bassin"
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.duplicate_lr = False
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.side = ".L"
    except AttributeError:
        pass
    pbone = obj.pose.bones[bones['Jambe haut.R']]
    pbone.rigify_type = 'pantin.leg'
    pbone.lock_location = (False, False, True)
    pbone.lock_rotation = (True, True, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'XZY'
    pbone.bone.layers = [False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    try:
        pbone.rigify_parameters.Z_index = 2.0
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.joint_name = "Genou"
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.right_layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False]
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.pelvis_name = "Bassin"
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.duplicate_lr = False
    except AttributeError:
        pass
    pbone = obj.pose.bones[bones['Thorax']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (True, True, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'XZY'
    pbone.bone.layers = [False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['Jambe bas.L']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, True)
    pbone.lock_rotation = (True, True, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'XZY'
    pbone.bone.layers = [False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['Jambe bas.R']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, True)
    pbone.lock_rotation = (True, True, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'XZY'
    pbone.bone.layers = [False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['Buste']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, False)
    pbone.lock_rotation = (True, True, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'XZY'
    pbone.bone.layers = [False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['Pied.L']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, True)
    pbone.lock_rotation = (True, True, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'XZY'
    pbone.bone.layers = [False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['Talon.L']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, True)
    pbone.lock_rotation = (True, True, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'XZY'
    pbone.bone.layers = [False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['Pied.R']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, True)
    pbone.lock_rotation = (True, True, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'XZY'
    pbone.bone.layers = [False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['Talon.R']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, True)
    pbone.lock_rotation = (True, True, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'XZY'
    pbone.bone.layers = [False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['Cou']]
    pbone.rigify_type = 'pantin.head'
    pbone.lock_location = (True, True, True)
    pbone.lock_rotation = (True, True, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (True, True, True)
    pbone.rotation_mode = 'XZY'
    pbone.bone.layers = [True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    try:
        pbone.rigify_parameters.Z_index = 0.0
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.mutable_order = False
    except AttributeError:
        pass
    pbone = obj.pose.bones[bones['Bras haut.L']]
    pbone.rigify_type = 'pantin.arm'
    pbone.lock_location = (False, False, True)
    pbone.lock_rotation = (True, True, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'XZY'
    pbone.bone.layers = [False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    try:
        pbone.rigify_parameters.right_layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False]
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.joint_name = "Coude"
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.pelvis_name = "Bassin"
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.duplicate_lr = False
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.Z_index = 3.0
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.side = ".L"
    except AttributeError:
        pass
    pbone = obj.pose.bones[bones['Bras haut.R']]
    pbone.rigify_type = 'pantin.arm'
    pbone.lock_location = (False, False, True)
    pbone.lock_rotation = (True, True, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'XZY'
    pbone.bone.layers = [False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    try:
        pbone.rigify_parameters.right_layers = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False]
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.joint_name = "Coude"
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.pelvis_name = "Bassin"
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.duplicate_lr = False
    except AttributeError:
        pass
    try:
        pbone.rigify_parameters.Z_index = 3.0
    except AttributeError:
        pass
    pbone = obj.pose.bones[bones['Orteil.L']]
    pbone.rigify_type = ''
    pbone.lock_location = (True, True, True)
    pbone.lock_rotation = (True, True, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'XZY'
    pbone.bone.layers = [False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['Orteil.R']]
    pbone.rigify_type = ''
    pbone.lock_location = (True, True, True)
    pbone.lock_rotation = (True, True, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'XZY'
    pbone.bone.layers = [False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['Tete']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, True)
    pbone.lock_rotation = (True, True, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (True, True, True)
    pbone.rotation_mode = 'XZY'
    pbone.bone.layers = [True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['Bras bas.L']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, True)
    pbone.lock_rotation = (True, True, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'XZY'
    pbone.bone.layers = [False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['Bras bas.R']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, True)
    pbone.lock_rotation = (True, True, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'XZY'
    pbone.bone.layers = [False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['Machoire']]
    pbone.rigify_type = ''
    pbone.lock_location = (True, True, True)
    pbone.lock_rotation = (True, True, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (True, True, True)
    pbone.rotation_mode = 'XZY'
    pbone.bone.layers = [True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['Paupiere']]
    pbone.rigify_type = ''
    pbone.lock_location = (True, True, True)
    pbone.lock_rotation = (True, True, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'XZY'
    pbone.bone.layers = [True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['Chapeau']]
    pbone.rigify_type = 'pantin.simple'
    pbone.lock_location = (False, False, True)
    pbone.lock_rotation = (True, True, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'XZY'
    pbone.bone.layers = [True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['Main.L']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, True)
    pbone.lock_rotation = (True, True, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'XZY'
    pbone.bone.layers = [False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['Main.R']]
    pbone.rigify_type = ''
    pbone.lock_location = (False, False, True)
    pbone.lock_rotation = (True, True, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'XZY'
    pbone.bone.layers = [False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    pbone = obj.pose.bones[bones['Accessoire']]
    pbone.rigify_type = 'pantin.simple'
    pbone.lock_location = (False, False, True)
    pbone.lock_rotation = (True, True, False)
    pbone.lock_rotation_w = False
    pbone.lock_scale = (False, False, False)
    pbone.rotation_mode = 'XZY'
    pbone.bone.layers = [True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    try:
        pbone.rigify_parameters.object_side = ".R"
    except AttributeError:
        pass

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

    arm.layers = [(x in [0, 2, 4, 6]) for x in range(32)]

    # Select proper UI template
    template_name = 'pantin_template'
    arm_templates = arm.rigify_templates.items()
    template_index = None
    for i, template in enumerate(arm_templates):
        if template[0] == template_name:
            template_index = i
            break
    if template_index is None:
        template_index = 0 # Default to something...
    else:
        arm.rigify_active_template = template_index

if __name__ == "__main__":
    create(bpy.context.active_object)
