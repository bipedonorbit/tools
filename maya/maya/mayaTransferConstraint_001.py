import maya.cmds as cmds

def list_constraints(root):
    """List all constraints under a root node."""
    constraints = cmds.listRelatives(root, allDescendents=True, type='constraint') or []
    return constraints

def saveConstraint(old_root):
    """Transfer constraints from old_root to new_root."""
    old_constraints = list_constraints(old_root)

    for old_con in old_constraints:
        constrained_objs = cmds.listConnections(old_con + ".constraintParentInverseMatrix", s=True, d=False) or []
        if not constrained_objs:
            print(f"No constrained object found for {old_con}")
            continue

        target_name = '_'.join(old_con.split('_')[:-1])
        new_target = cmds.ls(f"{namespace}{target_name}", type='transform')
        con_input=cmds.listConnections(f'{old_con}.target[0].targetParentMatrix', source=True, destination=False)

        if not new_target:
            print(f"Target {namespace}{target_name} not found in new geo.")
            continue

        # Get constraint type
        constraint_type = cmds.nodeType(old_con)

        print (f"{con_input[0]} is connectected to {old_con} and this is a {constraint_type}")
        print (f"now i will create a {constraint_type} between {con_input[0]} and {new_target[0]}")
        print ("_")
        if constraint_type=="scaleConstraint":
            cmds.scaleConstraint( con_input[0], new_target[0] ,maintainOffset=1)
        if constraint_type=="parentConstraint":
            cmds.parentConstraint( con_input[0], new_target[0] ,maintainOffset=1)


# Example usage
old_geo = "geo"
saveConstraint(old_geo)


