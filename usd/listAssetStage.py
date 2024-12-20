from pxr import Usd
stage = Usd.Stage.Open(r"I:\swaChristmas_2407\03_Production\Shots\cnt\s070\Export\_layer_Anim_AnimMaya\v009\cnt-s070__layer_Anim_AnimMaya_v009.usdc")
world = stage.GetPrimAtPath('/world')
prout=world.GetPropertyNames()
print(prout)